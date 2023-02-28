# Discord Bot with ChatGPT
## Installation
Before installing, make sure ```Python 3.6``` is installed  
To install requirements use ```$ pip install -r requirements.txt``` in project's directory  

But if you use *Windows*, you can just run ```setup.bat``` to install libraries, then ```Start.bat``` to run the bot  
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

### ChatGPT
I use [```openai``` API](https://platform.openai.com/docs/) to interact with ChatGPT. Actually, I have some problems with it, because sometimes ChatGPT sends a bit unexpected resaults when you use API.  

In bot you can change the engine of openai Completion:  
	```max_tokens``` is actually max number of symbols in ChatGPT's answer  
	```temperature``` is something that you may change, but you shold read [documentation](https://platform.openai.com/docs/) before  
You may change theese values in ```config.json```
	