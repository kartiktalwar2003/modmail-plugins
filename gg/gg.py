import discord
import discord.ext.commands as commands
from discord.ext import tasks

class GG(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
                self.serverstats.start()

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
        
        @commands.command()
        @commands.has_permissions(manage_messages=True)
        async def bots (self, ctx):
                def is_bot(m):
                        return m.author.bot
                deleted = await ctx.channel.purge(limit = 50 , check = is_bot)
                await ctx.message.delete()

def setup(bot):
    bot.add_cog(GG(bot))
