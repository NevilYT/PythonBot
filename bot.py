import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Позволяет боту читать сообщения

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot logged in as {bot.user}')

@bot.command()
async def clean_logs(ctx):
    phrases_to_keep = ["LOG", "@outlook.com"]
    
    async for message in ctx.channel.history(limit=None):
        if not any(phrase in message.content for phrase in phrases_to_keep):
            await message.delete()

    await ctx.send("Cleaning completed!")

bot.run('YOUR_BOT_TOKEN')
