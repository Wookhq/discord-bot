import os
import asyncio
import traceback
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from typing import Optional

load_dotenv()
TOKEN: Optional[str] = os.getenv("DISCORD_TOKEN")
PREFIX: str = os.getenv("COMMAND_PREFIX", "!")


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
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("⚠️ You don't have permission to use this command!")
    else:
        await ctx.send(f"⚠️ oops: `{error}`")

async def load_cogs():
    cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
    if not os.path.exists(cogs_dir):
        print(f"❌ Cogs directory '{cogs_dir}' not found")
        return
    for filename in os.listdir(cogs_dir):
        if filename.endswith(".py") and filename not in ["__init__.py", "__pycache__"]:
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")  # Use :-3 to remove .py
                print(f"✅ Loaded cog: {filename[:-3]}")
            except Exception as e:
                print(f"❌ Failed to load cog {filename[:-3]}: {e}")

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

@bot.check
async def onlycommands(ctx):
    allowed_channels = [int(ch.strip()) for ch in os.getenv("COMMAND_CHANNELS", "").split(",")]
    return ctx.channel.id in allowed_channels

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())