from discord.ext import commands
from modules.shitpost import get_random_shitpost
import discord

class LutionMarketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def themes(self, ctx):
        from modules.lutionmarketplace import LutionMarketplace
        marketplace = LutionMarketplace()
        themes = marketplace.get_themes()
        
        if not themes:
            await ctx.send("No themes found.")
            return
        
        embed = discord.Embed(title="Available Themes", description="\n".join(themes), color=0x00b0f4)
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(LutionMarketplace(bot))
