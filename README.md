# Discord Bot with ChatGPT
## Installation
Before installing, make sure ```Python 3.11``` and ```git``` are installed  

### Windows
Download ```windows.zip``` from last release  
Drop ```setup.bat``` in folder - script will make a folder with project inside the choosen folder  
Drop ```Start.bat``` in project's folder and run it
### Linux
```git clone https://github.com/voidmolly/discord-ChatGPT.git```  
To install requirements use ```$ pip install -r requirements.txt``` in project's directory  

Set up daemon:   
```sudo nano /etc/systemd/system/dchatgpt.service```   
```
[Unit]
Description=Discord ChatGPT
After=syslog.target

[Service]
Type=simple
User=root
Group=sudo
WorkingDirectory=/root/discord-ChatGPT/
ExecStart=/usr/bin/python3.11 main.py

[Install]
WantedBy=multi-user.target
```   

Run: ```sudo systemctl start dchatgpt```  
Stop: ```sudo systemctl stop dchatgpt```  
Restart: ```sudo systemctl restart dchatgpt```  
Check logs: ```sudo systemctl status dchatgpt```  
## Configuring
Open ```config.json``` with any text editor  
Then insert you openai and discord tokens in fields with such names  

_Optional:_  
	1. You may change prefix in field named ```"prefix"```  
	2. You may change ```max_tokens``` and ```temperature``` - ChatGPT's configs, but only if you know what you are doing

## About the bot
### Commands
I use command ```hint``` to send info about commands in chat, because IDK how to make ```help``` command :)  
Commands ```game```, ```stream``` are made at the request of the customer. They are used for changing bot's status.

### Settings
Permissions: ```Read Messages/View Channels``` and ```Send Messages```  
Intents: all

### ChatGPT
I use [```openai``` API](https://platform.openai.com/docs/) to interact with ChatGPT. Actually, I have some problems with it, because sometimes ChatGPT sends a bit unexpected results when you use API.  

In bot you can change the engine of openai Completion:  
	```max_tokens``` is actually max number of symbols in ChatGPT's answer  
	```temperature``` is something that you may change, but you shold read [documentation](https://platform.openai.com/docs/) before  
You may change theese values in ```config.json```  

Also if you run bot in Russia, you should use server located in another country or use proxy, otherwise ChatGPT won't work.
