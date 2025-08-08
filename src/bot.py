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
    # print full traceback to terminal
    print("===== COMMAND ERROR =====")
    traceback.print_exception(type(error), error, error.__traceback__)
    print("=========================")

    # optional: send a small error message in discord
    await ctx.send(f"⚠️ oops: `{error}`")

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            print(f"Loaded cog: {filename[:-3]}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())
