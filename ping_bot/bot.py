import discord
from discord.ext import commands, tasks
import asyncio
import subprocess
import config

def run_bot():
    TOKEN = config.token
    bot_intents = discord.Intents.default()
    bot_intents.message_content = True

    bot = commands.Bot(command_prefix = '!', intents = bot_intents)

    @bot.event
    async def on_ready():
        print(f"{bot.user} is now running!")

    @bot.command(name='test')
    async def test(ctx):
         await ctx.send("I'm running!")

    @bot.command(name='ping', arguments={'ip', 'port'}, optional=True)
    async def _status(ctx, ip = '0', port = '0'):
        if ip == '0':
            await ctx.send("Invalid arguments. Should be `!status <ip> <port>`")
        elif port != '0':
            await ctx.send(f"Pinging {ip}:{port}....")
            command = ['ping', ip, port]
            if subprocess.call(command) == 0:
                await ctx.send("Ping successful!")
            else:
                await ctx.send(f"Ping failed! {subprocess.call(command)}")
        else:
            await ctx.send(f"Pinging {ip}")
            command = ['ping', ip]
            if subprocess.call(command) == 0:
                await ctx.send("Ping successful!")
            else:
                await ctx.send("Ping failed!")

    bot.run(TOKEN)