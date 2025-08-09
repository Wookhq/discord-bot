# cogs/lution_marketplace.py
from discord.ext import commands
import discord
from modules.lutionmarketplace import LutionMarketplace as MarketplaceFetcher

class LutionMarketplace(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.loading_emoji = "<a:loading:1403596623732277338>"
        self.invalid_emoji = "<:invalid:1403596167547195502>"
        self.vaild_emoji = "<:valid:1403596136039579750>"
        self.info_emoji = "<:info:1403627652132245504>"

    @commands.command()
    async def themes(self, ctx):
        embed = discord.Embed(
            title=f"{self.loading_emoji} Lution Marketplace",
            description="Fetching themes...",
            color=0x00b0f4
        )
        thememes = await ctx.send(embed=embed)

        marketplace = MarketplaceFetcher()
        themes = marketplace.get_themes()

        if not themes:
            await thememes.edit(content=f"{self.invalid_emoji} No themes found.")
            return

        embed = discord.Embed(
            title="Available Themes",
            description="These are available Themes",
            color=0x00b0f4
        )
        for theme in themes:
            embed.add_field(
                name=f"{self.info_emoji} {theme}",
                value=marketplace.get_theme_description(theme) or "No description available",
                inline=False
            )
        await thememes.edit(embed=embed)

    @commands.command()
    async def mods(self, ctx):
        embed = discord.Embed(
            title=f"{self.loading_emoji} Lution Marketplace",
            description="Fetching mods...",
            color=0x00b0f4
        )
        modmes = await ctx.send(embed=embed)

        marketplace = MarketplaceFetcher()
        mods = marketplace.get_mods()

        if not mods:
            await modmes.edit(content=f"{self.invalid_emoji} No mods found.")
            return

        embed = discord.Embed(
            title="Available Mods",
            description="These are available Mods",
            color=0x00b0f4
        )
        for mod in mods:
            embed.add_field(
                name=f"{self.info_emoji}  {mod}",
                value=marketplace.get_mod_description(mod) or "No description available",
                inline=False
            )
        await modmes.edit(embed=embed)

    @commands.command()
    async def infotheme(self, ctx, *, title: str):
        embed = discord.Embed(
            title=f"{self.loading_emoji} Lution Marketplace",
            description="Fetching theme...",
            color=0x00b0f4
        )
        thememes = await ctx.send(embed=embed)

        marketplace = MarketplaceFetcher()
        description = marketplace.get_theme_description(title)
        sb = marketplace.get_theme_sb(title)
        image = marketplace.get_theme_image(title)
        link = marketplace.get_theme_download(title)

        if not description:
            embed = discord.Embed(
                title=f"{self.invalid_emoji} Lution Marketplace",
                description="Not found",
                color=0x00b0f4
            )
            await thememes.edit(embed=embed)
            return

        embed = discord.Embed(title=f"{self.info_emoji} {title}", description=description, color=0x00b0f4)
        if sb:
            embed.add_field(name="Status", value=sb, inline=False)
        if image:
            embed.set_image(url=image)
        if link:
            embed.add_field(name="Download", value=f"[Click here]({link})", inline=False)

        await thememes.edit(embed=embed)

    @commands.command()
    async def infomod(self, ctx, *, mod: str):
        embed = discord.Embed(
            title=f"{self.loading_emoji} Lution Marketplace",
            description="Fetching mod...",
            color=0x00b0f4
        )
        modmes = await ctx.send(embed=embed)

        marketplace = MarketplaceFetcher()
        description = marketplace.get_mod_description(mod)
        sb = marketplace.get_mod_sb(mod)
        image = marketplace.get_mod_image(mod)
        link = marketplace.get_mod_download(mod)

        if not description:
            embed = discord.Embed(
                title=f"{self.invalid_emoji} Lution Marketplace",
                description="Not found",
                color=0x00b0f4
            )
            await modmes.edit(embed=embed)
            return

        embed = discord.Embed(title=f"{self.info_emoji} {mod}", description=description, color=0x00b0f4)
        if sb:
            embed.add_field(name="Status", value=sb, inline=False)
        if image:
            embed.set_image(url=image)
        if link:
            embed.add_field(name="Download", value=f"[Click here]({link})", inline=False)

        await modmes.edit(embed=embed)

async def setup(bot):
    await bot.add_cog(LutionMarketplace(bot))
