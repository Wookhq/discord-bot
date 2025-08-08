from discord.ext import commands
from modules.shitpost import get_random_shitpost
import discord

class Mods(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ban(self, ctx, member: discord.Member = None, *, reason: str = "No reason provided"):
        if member is None:
            file = discord.File(get_random_shitpost())
            await ctx.send(file=file)
        elif ctx.author.guild_permissions.ban_members:
            try:
                # check bot perms
                if not ctx.guild.me.guild_permissions.ban_members:
                    raise PermissionError("I can't ban, no perms")
                
                await member.ban(reason=reason)
                embed = discord.Embed(title="Banned!",
                        description=f"Banned {member.mention} for {reason}",
                        colour=0x00b0f4)

                await ctx.send(embed=embed)
            except Exception as e:
                    file = discord.File(get_random_shitpost())
                    await ctx.send(file=file)
                    print(e)

        else:
            await ctx.send("You don't have permission to ban members.")

async def setup(bot):
    await bot.add_cog(Mods(bot))
