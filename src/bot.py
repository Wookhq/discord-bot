# type: ignore
import os
import asyncio
import traceback
import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import app_commands


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
PREFIX = os.getenv("COMMAND_PREFIX", "!")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

bot.remove_command("help")
@bot.event
async def on_ready():
    print(f"logged in as {bot.user} 👀")
    try:
        synced = await bot.tree.sync()
        print(f"✅ synced {len(synced)} slash commands")
    except Exception as e:
        print(f"❌ sync failed: {e}")

@bot.event
async def on_command_error(ctx, error):
    print("===== COMMAND ERROR =====")
    traceback.print_exception(type(error), error, error.__traceback__)
    print("=========================")
    await ctx.send(f"⚠️ oops: `{error}`")

async def load_cogs():
    cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
    for filename in os.listdir(cogs_dir):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-5]}")

@bot.tree.command(name="help", description="Show available commands")
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="Help", description="List of available commands", color=0x00b0f4)
    commands_list = [
        "`/getworkflows` - Fetch workflows information",
        "`/infoworkflow <workflow_id>` - Fetch workflow information",
        "`/themes` - Fetch themes information",
        "`/mods` - Fetch mods information",
        "`/infotheme <themename>` - Fetch theme information",
        "`/infomod <modname>` - Fetch mod information"
    ]
    embed.add_field(name="Commands", value="\n".join(commands_list), inline=False)
    await interaction.response.send_message(embed=embed)


async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())
