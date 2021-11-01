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
                if message.author.bot is True :
                        pass
                else :
                        if str(message.channel.id) == "894148486554079232" :
                                extractor = URLExtract()
                                if extractor.has_urls(message.content):
                                        pass
                                else :
                                        await message.channel.send(f"{message.author.mention} only playlist links are allowed in this channel.", delete_after=5)
                                        await message.delete()
					
                        if str(message.content).lower() == "nnn" :
                            nnn_role = message.guild.get_role(904447750970699868)
                            if nnn_role in message.author.roles :
                                try :
                                    await message.author.remove_roles(nnn_role)
                                    await message.add_reaction("\U0000274e")
                                except :
                                    pass

                            else :
                                try :
                                    await message.author.add_roles(nnn_role)
                                    await message.add_reaction("\U00002705")
                                    await message.reply("Congrats comrade, you are a warrior. Gajju welcomes you to the NNN gang. Remember, no jerking off for the whole November, if you do you're a weakling.")
                                except :
                                    pass
                        
                        else :
                            pass
			
			

def setup(bot):
    bot.add_cog(GG(bot))
