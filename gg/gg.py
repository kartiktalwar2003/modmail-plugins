import discord
import discord.ext.commands as commands
from discord.ext import tasks

class GG(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
        
        @commands.command(aliases = ["bota","bot"])
        @commands.has_permissions(manage_messages=True)
        async def bots (self, ctx):
                def is_bot(m):
                        return m.author.bot
                deleted = await ctx.channel.purge(limit = 50 , check = is_bot)
                await ctx.message.delete()

def setup(bot):
    bot.add_cog(GG(bot))
