import discord
import openai
# from asyncio import sleep
import json
from discord.ext import commands

# Токены
with open("config.json", "r", encoding="utf-8") as config:
    tokens = json.loads(config.read())
    DISCORD_TOKEN = tokens['discord_token']
    OPENAI_TOKEN = tokens['openai_token']

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents) # создаем экземпляр командного бота

openai.api_key = OPENAI_TOKEN # устанавливаем API ключ OpenAI

@bot.event
async def on_ready():
    print(f'{bot.user} подключился к Discord!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Людские жизни"))


@bot.event
async def on_message(message):
    if message.author == bot.user:  # игнорируем сообщения, отправленные ботом
        return
    print(message.content)
    # Обрабатываем команды
    if message.content.startswith('!'):  # проверяем, начинается ли сообщение с префикса "!"
        print("jdfds")
        # Изменяем статус
        if message.content.startswith('!game'):  # реагируем на команду "!game"
            print("обработал")
            name = message.content.replace('!game ', '')
            await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=name))
            await message.reply(f"Успешно изменил активность на {name}")
            return  # завершаем функцию, чтобы не выполнять другие проверки
        if message.content.startswith('!stream'):
            name = message.content.replace('!stream ', '').split(", ")[0]
            url = message.content.replace('!stream ', '').split(", ")[1]
            await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name=name, url=url))
            await message.reply(f"Успешно изменил активность на {name}")
            return
        if message.content.startswith('!activ'):
            name = message.content.replace('!activ ', '')
            await bot.change_presence(status=discord.Status.online, activity=discord.Activity(name=name))
            await message.reply(f"Успешно изменил активность на {name}")
            return

        if message.content == '!help':  # даем помощь по взаимодействию с ботом
            await message.reply(
                'Чтобы поговорить с ChatGPT, отправьте сообщение с запросом и упомянанием бота\n\n' +
                'Администратор может изменять статус бота, используя команды:\n' +
                '"!game <name>"\n' +
                '"!stream <name> <url>"\n' +
                '"!activ <name>"\n'
                )
            return

    if bot.user in message.mentions:    # проверяем, был ли упомянут бот
        prompt = message.content.replace(f'{bot.user.mention} ', '') # получаем текст запроса без упоминания бота
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=0.5
        )   # используем OpenAI API для создания ответа с помощью GPT модели

        await message.reply(response.choices[0].text)   # отправляем ответ в канал, где было задано сообщение


bot.run(DISCORD_TOKEN)  # запускаем бота с токеном
