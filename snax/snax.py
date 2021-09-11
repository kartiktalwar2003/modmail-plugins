import discord
import discord.ext.commands as commands
from discord.ext import tasks
import asyncio

class Snax(commands.Cog):
        def __init__(self, bot):
                self.bot = bot

        @commands.Cog.listener()
        async def on_member_join(self, member):
            channel = self.bot.get_channel(734735695138258954)

            embed = discord.Embed(title="**Welcome to **{channel.guild.name}**", description=f"Hey {member.mention} hope you enjoy here!!\n\
Check out <#733947076412571680>\n\
Enjoy chatting in <#734735695138258954>\n\
Thank you")
            embed.set_footer(text="Designed by Harshit#0001")
            avatar = member.avatar_url
            embed.set_thumbnail(url=avatar)
            
            msg = await channel.send(content=f"{member.mention}", embed=embed)
            await asyncio.sleep(40)
            await msg.delete()


def setup(bot):
    bot.add_cog(Snax(bot))
