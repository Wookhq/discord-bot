from discord.ext import commands
from modules.shitpost import get_next_shitpost
import discord

class Mods(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vaild_emoji = "<:valid:1403596136039579750>"

    @commands.command()
    async def ban(self, ctx, member: discord.Member = None, *, reason: str = "No reason provided"):
        if member is None:
            file = discord.File(get_next_shitpost())
            await ctx.send(file=file)
        elif ctx.author.guild_permissions.ban_members:
            try:
                # check bot perms
                if not ctx.guild.me.guild_permissions.ban_members:
                    raise PermissionError("I can't ban, no perms")
                
                await member.ban(reason=reason)
                embed = discord.Embed(title="Banned!",
                        description=f"{self.vaild_emoji} Banned {member.mention} for {reason}",
                        colour=0x00b0f4)

                await ctx.send(embed=embed)
            except Exception as e:
                    file = discord.File(get_next_shitpost())
                    await ctx.send(file=file)
                    print(e)

        else:
            await ctx.send("You don't have permission to ban members.")
            await ctx.send(file=discord.File(get_next_shitpost()))
    @commands.command()
    async def unban(self, ctx, *, member: str = None):
        if member is None:
            file = discord.File(get_random_shitpost())
            await ctx.send(file=file)
        elif ctx.author.guild_permissions.ban_members:
            try:
                # check bot perms
                if not ctx.guild.me.guild_permissions.ban_members:
                    raise PermissionError("I can't unban, no perms")
                
                banned_users = await ctx.guild.bans()
                member_name, member_discriminator = member.split("#")

                for ban_entry in banned_users:
                    user = ban_entry.user
                    if (user.name, user.discriminator) == (member_name, member_discriminator):
                        await ctx.guild.unban(user)
                        embed = discord.Embed(title="Unbanned!",
                                description=f"{self.vaild_emoji} Unbanned {user.mention}",
                                colour=0x00b0f4)

                        await ctx.send(embed=embed)
                        return

                await ctx.send(f"{member} not found in the ban list.")
            except Exception as e:
                file = discord.File(get_next_shitpost())
                await ctx.send(file=file)
                print(e)
        else:
            await ctx.send("You don't have permission to unban members.")
            await ctx.send(file=discord.File(get_next_shitpost()))

    @commands.command()
    async def kick(self, ctx, member: discord.Member = None, *, reason: str = "No reason provided"):
        if member is None:
            file = discord.File(get_next_shitpost())
            await ctx.send(file=file)
        elif ctx.author.guild_permissions.kick_members:
            try:
                # check bot perms  
                if not ctx.guild.me.guild_permissions.kick_members:
                    raise PermissionError("I can't kick, no perms")
                await member.kick(reason=reason)
                embed = discord.Embed(title="Kicked!",
                        description=f"{self.vaild_emoji} Kicked {member.mention} for {reason}",
                        colour=0x00b0f4)

                await ctx.send(embed=embed)
            except Exception as e:
                file = discord.File(get_next_shitpost())
                await ctx.send(file=file)
                print(e)
        else:
            await ctx.send("You don't have permission to kick members.")
            await ctx.send(file=discord.File(get_next_shitpost()))


async def setup(bot):
    await bot.add_cog(Mods(bot))
