import discord
import discord.ext.commands as commands

class Jishaku(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
                bot.load_extension('jishaku')

                        
def setup(bot):
    bot.add_cog(Jishaku(bot))
    print("Jishaku Cog Loaded")
