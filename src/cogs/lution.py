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
        
        thememes = await ctx.send("`Loading themes...`")
        
        if not themes:
            await thememes.edit("No themes found.")
            return
        
        embed = discord.Embed(title="Available Themes", description="These are available Themes", color=0x00b0f4)
        for theme in themes:
            embed.add_field(name=theme, value=marketplace.get_theme_description(theme) or "No description available", inline=False)
        await thememes.edit(embed=embed)


async def setup(bot):
    await bot.add_cog(LutionMarketplace(bot))
