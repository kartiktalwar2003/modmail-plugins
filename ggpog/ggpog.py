import discord
import discord.ext.commands as commands
from datetime import datetime


class ggpog(commands.Cog):
        def __init__(self, bot):
                self.bot = bot


        @commands.Cog.listener()
        async def on_member_remove(self, member):
                try :
                        guild = self.bot.get_guild(477929808022601739)
                        pog_champ = guild.get_role(786300688866082886)

                        mod_chat = guild.get_channel(746335357079126046)

                        embed = discord.Embed(title = "Pog Champ has left the server!")
                        embed.description = f"{member.mention} {member} has left the server."
                        embed.timestamp = datetime.utcnow()

                        if pog_champ in member.roles :
                                await mod_chat.send(embed = embed)

                        else :
                                pass


                except Exception as error :
                        raise error
                        
                        

def setup(bot):
    bot.add_cog(ggpog(bot))
