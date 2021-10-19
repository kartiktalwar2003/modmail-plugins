import discord
import discord.ext.commands as commands
from discord.ext import tasks
import random

class GGcolor(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
                self.change_color.start()

        @tasks.loop(seconds=3600)
        async def change_color(self):
            try :
                guild = self.bot.get_guild(477929808022601739)
                channel = await guild.get_role(900013276799307807)
                await role.edit(color=discord.Color(random.randint(0x000000, 0xFFFFFF)))

            except Exception as error :
                raise(error)


        @change_color.before_loop
        async def before_change_color(self):
            await self.bot.wait_until_ready()


def setup(bot):
    bot.add_cog(GGcolor(bot))
