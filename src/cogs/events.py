from discord.ext import commands
import discord

class JoinEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        total_members = member.guild.member_count
        if channel:
            embed = discord.Embed(title='yo', description=f'{member.metion}, thank you for showing up, check out the server. Member number {total_members}')
            embed.set_thumbnail(url=member.display_avatar.url)
            await channel.send(embed=embed)
    
    @commands.Cog.listener()
    async def on_member_leave(self, member):
        channel = member.guild.system_channel
        if channel:
            embed = discord.Embed(title=f'bye {member.mention}', description='thank you for joinning the server, youre welcome')
            embed.set_thumbnail(url=member.display_avatar.url)
            await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(JoinEvent(bot))
