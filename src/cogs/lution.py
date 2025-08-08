from discord.ext import commands
from modules.shitpost import get_random_shitpost
import discord

class LutionMarketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def themes(self, ctx):
        embed = discord.Embed(title="Lution Marketplace", description="Fetching themes...", color=0x00b0f4)
        thememes = await ctx.send(embed=embed)

        from modules.lutionmarketplace import LutionMarketplace
        marketplace = LutionMarketplace()
        themes = marketplace.get_themes()
        
        
        if not themes:
            await thememes.edit("No themes found.")
            return
        
        embed = discord.Embed(title="Available Themes", description="These are available Themes", color=0x00b0f4)
        for theme in themes:
            embed.add_field(name=theme, value=marketplace.get_theme_description(theme) or "No description available", inline=False)
        await thememes.edit(embed=embed)
    
    @commands.command()
    async def mods(self, ctx):
        embed = discord.Embed(title="Lution Marketplace", description="Fetching mods...", color=0x00b0f4)
        modmes = await ctx.send(embed=embed)

        from modules.lutionmarketplace import LutionMarketplace
        marketplace = LutionMarketplace()
        mods = marketplace.get_mods()
        
        if not mods:
            await modmes.edit("No mods found.")
            return
        
        embed = discord.Embed(title="Available Mods", description="These are available Mods", color=0x00b0f4)
        for mod in mods:
            embed.add_field(name=mod, value=marketplace.get_mod_description(mod) or "No description available", inline=False)
        await modmes.edit(embed=embed)
    
    @commands.command()
    async def infotheme(self, ctx, *, title: str):
        embed = discord.Embed(title="Lution Marketplace", description="Fetching theme...", color=0x00b0f4)
        thememes = await ctx.send(embed=embed)

        from modules.lutionmarketplace import LutionMarketplace
        marketplace = LutionMarketplace()
        description = marketplace.get_theme_description(title)
        sb = marketplace.get_theme_sb(title)
        image = marketplace.get_theme_image(title)

        if not description:
            embed = discord.Embed(title="Lution Marketplace", description="Not found", color=0x00b0f4)
            await thememes.edit(embed=embed)
            return
        
        embed = discord.Embed(title=title, description=description, color=0x00b0f4)
        if sb:
            embed.add_field(name="Status", value=sb, inline=False)
        if image:
            embed.set_image(url=image)
        
        await thememes.edit(embed=embed)
    
    @commands.command()
    async def infomod(self, ctx, *, mod: str):
        embed = discord.Embed(title="Lution Marketplace", description="Fetching mod...", color=0x00b0f4)
        modmes = await ctx.send(embed=embed)

        from modules.lutionmarketplace import LutionMarketplace
        marketplace = LutionMarketplace()
        description = marketplace.get_mod_description(mod)
        sb = marketplace.get_mod_sb(mod)
        image = marketplace.get_mod_image(mod)

        if not description:
            embed = discord.Embed(title="Lution Marketplace", description="Not found", color=0x00b0f4)
            await modmes.edit(embed=embed)
            return
        
        embed = discord.Embed(title=mod, description=description, color=0x00b0f4)
        if sb:
            embed.add_field(name="Status", value=sb, inline=False)
        if image:
            embed.set_image(url=image)
        
        await modmes.edit(embed=embed)

async def setup(bot):
    await bot.add_cog(LutionMarketplace(bot))
