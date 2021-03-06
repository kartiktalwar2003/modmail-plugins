import discord
import discord.ext.commands as commands
from discord.ext import tasks
import asyncio

async def check_profile(member , guild):
        
        # Badge Roles
        hypesquad_brilliance = discord.utils.get(guild.roles , name = "Discord Hypesquad Brilliance")
        hypesquad_bravery = discord.utils.get(guild.roles , name = "Discord Hypesquad Bravery")
        hypesquad_balance = discord.utils.get(guild.roles , name = "Discord Hypesquad Balance")
        staff = discord.utils.get(guild.roles , name = "Discord Employee")
        partner = discord.utils.get(guild.roles , name = "Discord Partner")
        bug_hunter = discord.utils.get(guild.roles , name = "Discord Bug Hunter")
        bug_hunter_level_2 = discord.utils.get(guild.roles , name = "Discord Bug Hunter Experts")
        hypesquad = discord.utils.get(guild.roles , name = "Discord Hypesquad Events")
        early_supporter = discord.utils.get(guild.roles , name = "Discord Early Supporter")
        verified_bot_developer = discord.utils.get(guild.roles , name = "Discord Verified Developers")

        # Bot Roles

        verified_bot = discord.utils.get(guild.roles , name = "Discord Verified Bots")
        unverified_bot = discord.utils.get(guild.roles , name = "Discord Unverified Bots")

        # Nitro Role
        nitro = discord.utils.get(guild.roles , name = "Discord Nitro")
        
        if member.public_flags.hypesquad_brilliance :
                await member.add_roles(hypesquad_brilliance)

        if member.public_flags.hypesquad_brilliance is False and hypesquad_brilliance in member.roles :
                await member.remove_roles(hypesquad_brilliance)

        if member.public_flags.hypesquad_bravery :
                await member.add_roles(hypesquad_bravery)

        if member.public_flags.hypesquad_bravery is False and hypesquad_bravery in member.roles :
                await member.remove_roles(hypesquad_bravery)

        if member.public_flags.hypesquad_balance :
                await member.add_roles(hypesquad_balance)

        if member.public_flags.hypesquad_balance is False and hypesquad_balance in member.roles :
                await member.remove_roles(hypesquad_balance)

        if member.public_flags.staff :
                await member.add_roles(staff)

        if member.public_flags.staff is False and staff in member.roles :
                await member.remove_roles(staff)

        if member.public_flags.partner :
                await member.add_roles(partner)

        if member.public_flags.partner is False and partner in member.roles :
                await member.remove_roles(partner)

        if member.public_flags.bug_hunter :
                await member.add_roles(bug_hunter)

        if member.public_flags.bug_hunter is False and bug_hunter in member.roles :
                await member.remove_roles(bug_hunter)

        if member.public_flags.bug_hunter_level_2 :
                await member.add_roles(bug_hunter_level_2)

        if member.public_flags.bug_hunter_level_2 is False and bug_hunter_level_2 in member.roles :
                await member.remove_roles(bug_hunter_level_2)

        if member.public_flags.hypesquad :
                await member.add_roles(hypesquad)

        if member.public_flags.hypesquad is False and hypesquad in member.roles :
                await member.remove_roles(hypesquad)

        if member.public_flags.early_supporter :
                await member.add_roles(early_supporter)

        if member.public_flags.early_supporter is False and early_supporter in member.roles :
                await member.remove_roles(early_supporter)

        if member.public_flags.verified_bot_developer :
                await member.add_roles(verified_bot_developer)

        if member.public_flags.verified_bot_developer is False and verified_bot_developer in member.roles :
                await member.remove_roles(verified_bot_developer)

        if member.public_flags.verified_bot :
                await member.add_roles(verified_bot)

        if member.public_flags.verified_bot is False and verified_bot in member.roles :
                await member.remove_roles(verified_bot)

        if member.public_flags.verified_bot is False and member.bot is True :
                await member.add_roles(unverified_bot)

        if member.public_flags.verified_bot is True and member.bot is True and unverified_bot in member.roles :
                await member.remove_roles(unverified_bot)

        if member.is_avatar_animated() is True:
                await member.add_roles(nitro)

        if member.is_avatar_animated() is False and member.premium_since is not None :
                await member.add_roles(nitro)

        if member.is_avatar_animated() is False and member.premium_since is None and nitro in member.roles :
                await member.remove_roles(nitro)

        else :
                pass


class badgeroles(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
                self.give_role.start()

        @tasks.loop(seconds = 60)
        async def give_role(self):
                guild = self.bot.get_guild(int(545956933170102283))
                for member in guild.members :
                        await check_profile(member , guild)

        @give_role.before_loop
        async def before_give_role(self):
                await self.bot.wait_until_ready()
                

        @commands.Cog.listener()
        async def on_member_join(self, member):
                await check_profile(member , member.guild)

                

def setup(bot):
    bot.add_cog(badgeroles(bot))
