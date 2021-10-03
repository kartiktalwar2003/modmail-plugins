import discord
import discord.ext.commands as commands
from discord.ext import tasks
from urlextract import URLExtract

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
                
        @commands.Cog.listener()
        async def on_message(self, message):
                if str(message.channel.id) == "894148486554079232" :
                        extractor = URLExtract()
                        if extractor.has_urls(message.content):
                                pass
                        else :
                                await message.reply("Only links are allowed in this channel.", delete_after=5)
                                await message.delete()

                else :
                        pass
                
                

def setup(bot):
    bot.add_cog(GG(bot))
