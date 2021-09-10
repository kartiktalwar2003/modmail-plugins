import discord
import discord.ext.commands as commands
from discord.ext import tasks
import asyncio

class Snax(commands.Cog):
        def __init__(self, bot):
                self.bot = bot

        @commands.listener()
        async def on_member_join(self, member):
            channel = self.bot.get_channel(734735695138258954)

            embed = discord.Embed(title="**Welcome to **{channel.guild.name}**", description=f"Hey {member.mention} hope you enjoy here!!")
            embed.add_field(title="Check out <#733947076412571680>")
            embed.add_field(title="Enjoy chatting in <#734735695138258954>")
            embed.add_field(title="Thank you")
            embed.set_footer(text="Designed by Harshit#0001")
            avatar = member.avatar_url
            embed.set_image(url=avatar)
            
            msg = await channel.send(content=f"{member.mention}", embed=embed)
            asyncio.sleep(40)
            await msg.delete()


def setup(bot):
    bot.add_cog(Snax(bot))
