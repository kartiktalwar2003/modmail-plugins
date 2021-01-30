import discord
import discord.ext.commands as commands
from datetime import datetime


class PogChamp(commands.Cog):
        def __init__(self, bot):
                self.bot = bot


        @commands.Cog.listener()
        async def on_member_remove(self, member):
                try :
                        guild = self.bot.get_guild(477929808022601739)
                        print(guild)
                        pog_champ = guild.get_role(786300688866082886)
                        print(pog_champ)

                        mod_chat = guild.get_channel(746335357079126046)
                        print(mod_chat)

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
    bot.add_cog(PogChamp(bot))
    print("PogChamp's Cog Loaded")
