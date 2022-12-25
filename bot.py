#!/usr/bin/env python3
import discord
import requests
import json
import asyncio
import string

client = discord.Client(intents=discord.Intents.default())
alpha = string.ascii_uppercase
def get_question():
    qs = ''
    id = 1
    answer = 0
    response = requests.get("http://103.167.132.178:8000/api/random/")
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]['title'] + "\n"

    for item in json_data[0]['answer']:
        ans =  alpha[id-1]
        qs += ans + ". " + item['answer'] + "\n"

        if item['is_correct']:
            answer = ans
        
        id += 1 
    
    return(qs, answer)

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    if message.content.startswith('!question'):
        qs, answer = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isupper()

        try: 
            guess = await client.wait_for('message', check=check, timeout=30.0)
        except asyncio.TimeoutError:
            return await message.channel.send('Sorry, you took too long time')

        if guess.content == answer:
            await message.channel.send('Correct!')
        else:
            await message.channel.send('Wrong Answer, try again')
    
    elif message.content.startswith('!help'):
        await message.channel.send('Usage: To use quiz bot \n!help : show help information \n!question: give you a question \nto answer just type the alphabet order: A')
    
    
client.run('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
