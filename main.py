import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import openai
import json


# Tokens
with open("config.json", "r", encoding="utf-8") as file:
    config = json.loads(file.read())
    DISCORD_TOKEN = config['discord_token']
    OPENAI_TOKEN = config['openai_token']
    PREFIX = config['prefix']

intents = discord.Intents.all()
# intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)    # Create an instance of bot with the command prefix '!'

openai.api_key = OPENAI_TOKEN   # set OpenAI API key

# Power On
@bot.event
async def on_ready():
    print(f'{bot.user} connected to Discord!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("людские жизни"))

# Change status
@bot.command()
async def hello(ctx):
    await ctx.reply("Hi")

@bot.command()
@has_permissions(administrator=True)
async def game(ctx, name):
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=name))
    await ctx.reply(f"Изменил активность на {name}")

@bot.command()
@has_permissions(administrator=True)
async def stream(ctx, name, url):
    # name, url = name_url.split(", ")
    await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name=name, url=url))
    await ctx.reply(f"Изменил активность на {name}")

# Idk how to make help
@bot.command()
async def hint(ctx):
    await ctx.reply(
        'Чтобы поговорить с ChatGPT, отправьте сообщение с запросом и упомянанием бота\n\n' +
        'Администратор может изменять статус бота, используя команды:\n' +
        '!game <name>\n' +
        '!stream <name> <url>\n'
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)    # let commands work

    if bot.user in message.mentions:
        prompt = message.content.replace(f'{bot.user.mention} ', '')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=2000,
            n=1,
            stop=None,
            temperature=0.5
        )
        await message.reply(response.choices[0].text)

bot.run(DISCORD_TOKEN)
