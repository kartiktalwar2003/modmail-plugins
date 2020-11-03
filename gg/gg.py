import discord
import discord.ext.commands as commands
from discord.ext import tasks

class GG(commands.Cog):
        def __init__(self, bot):
                self.bot = bot

        @tasks.loop(seconds=300)
        async def serverstats(self):
            try :
                guild = self.bot.get_guild(477929808022601739)
                channel = self.bot.get_channel(773068370400641044)
                mc = guild.member_count
                await channel.edit(name=f"𝙂𝙖𝙣𝙜 : {mc}")

            except Exception as error :
                raise error
                
                
        @serverstats.before_loop
        async def before_serverstats(self):
            await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(GG(bot))
