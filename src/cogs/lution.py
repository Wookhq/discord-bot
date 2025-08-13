import discord
from discord import app_commands
from discord.ext import commands
from modules.lutionmarketplace import LutionMarketplace as MarketplaceFetcher

class LutionMarketplace(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.loading_emoji = "<a:loading:1403596623732277338>"
        self.invalid_emoji = "<:invalid:1403596167547195502>"
        self.vaild_emoji = "<:valid:1403596136039579750>"
        self.info_emoji = "<:info:1403627652132245504>"

    @app_commands.command(name="themes", description="List all available themes from the marketplace")
    async def themes(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=f"{self.loading_emoji} Lution Marketplace",
            description="Fetching themes...",
            color=0x00b0f4
        )
        await interaction.response.send_message(embed=embed)
        msg = await interaction.original_response()

        marketplace = MarketplaceFetcher()
        themes = marketplace.get_themes()

        if not themes:
            await msg.edit(content=f"{self.invalid_emoji} No themes found.")
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
        await msg.edit(embed=embed)

    @app_commands.command(name="mods", description="List all available mods from the marketplace")
    async def mods(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title=f"{self.loading_emoji} Lution Marketplace",
            description="Fetching mods...",
            color=0x00b0f4
        )
        await interaction.response.send_message(embed=embed)
        msg = await interaction.original_response()

        marketplace = MarketplaceFetcher()
        mods = marketplace.get_mods()

        if not mods:
            await msg.edit(content=f"{self.invalid_emoji} No mods found.")
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
        await msg.edit(embed=embed)

    # autocomplete for themes
    async def theme_autocomplete(self, interaction: discord.Interaction, current: str):
        marketplace = MarketplaceFetcher()
        themes = marketplace.get_themes()
        return [
            app_commands.Choice(name=theme, value=theme)
            for theme in themes if current.lower() in theme.lower()
        ][:25]  # max 25 choices

    @app_commands.command(name="infotheme", description="Get detailed info about a theme")
    @app_commands.autocomplete(title=theme_autocomplete)
    async def infotheme(self, interaction: discord.Interaction, title: str):
        embed = discord.Embed(
            title=f"{self.loading_emoji} Lution Marketplace",
            description="Fetching theme...",
            color=0x00b0f4
        )
        await interaction.response.send_message(embed=embed)
        msg = await interaction.original_response()

        marketplace = MarketplaceFetcher()
        description = marketplace.get_theme_description(title)
        sb = marketplace.get_theme_sb(title)
        image = marketplace.get_theme_image(title)
        link = marketplace.get_theme_download(title)

        if not description:
            await msg.edit(embed=discord.Embed(
                title=f"{self.invalid_emoji} Lution Marketplace",
                description="Not found",
                color=0x00b0f4
            ))
            return

        embed = discord.Embed(title=f"{self.info_emoji} {title}", description=description, color=0x00b0f4)
        if sb:
            embed.add_field(name="Status", value=sb, inline=False)
        if image:
            embed.set_image(url=image)
        if link:
            embed.add_field(name="Download", value=f"[Click here]({link})", inline=False)

        await msg.edit(embed=embed)

    # autocomplete for mods
    async def mod_autocomplete(self, interaction: discord.Interaction, current: str):
        marketplace = MarketplaceFetcher()
        mods = marketplace.get_mods()
        return [
            app_commands.Choice(name=mod, value=mod)
            for mod in mods if current.lower() in mod.lower()
        ][:25]

    @app_commands.command(name="infomod", description="Get detailed info about a mod")
    @app_commands.autocomplete(mod=mod_autocomplete)
    async def infomod(self, interaction: discord.Interaction, mod: str):
        embed = discord.Embed(
            title=f"{self.loading_emoji} Lution Marketplace",
            description="Fetching mod...",
            color=0x00b0f4
        )
        await interaction.response.send_message(embed=embed)
        msg = await interaction.original_response()

        marketplace = MarketplaceFetcher()
        description = marketplace.get_mod_description(mod)
        sb = marketplace.get_mod_sb(mod)
        image = marketplace.get_mod_image(mod)
        link = marketplace.get_mod_download(mod)

        if not description:
            await msg.edit(embed=discord.Embed(
                title=f"{self.invalid_emoji} Lution Marketplace",
                description="Not found",
                color=0x00b0f4
            ))
            return

        embed = discord.Embed(title=f"{self.info_emoji} {mod}", description=description, color=0x00b0f4)
        if sb:
            embed.add_field(name="Status", value=sb, inline=False)
        if image:
            embed.set_image(url=image)
        if link:
            embed.add_field(name="Download", value=f"[Click here]({link})", inline=False)

        await msg.edit(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(LutionMarketplace(bot))
