# type: ignore
import os
import asyncio
import traceback
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("COMMAND_PREFIX", "!")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"logged in as {bot.user} 👀")

@bot.event
async def on_command_error(ctx, error):
    print("===== COMMAND ERROR =====")
    traceback.print_exception(type(error), error, error.__traceback__)
    print("=========================")
    await ctx.send(f"⚠️ oops: `{error}`")

async def load_cogs():
    cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
    for filename in os.listdir(cogs_dir):
        if filename.endswith(".py") and not filename.startswith("lution"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())
