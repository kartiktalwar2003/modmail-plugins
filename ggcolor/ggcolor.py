import discord
import discord.ext.commands as commands
from discord.ext import tasks

class GGcolor(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
                self.change_color.start()

        @tasks.loop(seconds=3600)
        async def change_color():
            try :
                guild = self.bot.get_guild(704217816940675072)
                channel = guild.get_role(900013276799307807)
                await role.edit(color=discord.Color(random.randint(0x000000, 0xFFFFFF)))

            except Exception as error :
                raise(error)


        @change_color.before_loop
        async def before_change_color():
            await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(GGcolor(bot))
