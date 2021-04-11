import discord
import discord.ext.commands as commands
from discord.ext import tasks
import asyncio

class activityroles(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
                self.playing_role.start()
                self.coding_role.start()
                self.spotify_role.start()
                self.streaming_role.start()

        @tasks.loop(seconds = 2)
        async def playing_role(self):
                guild = self.bot.get_guild(int(545956933170102283))
                playing = discord.utils.get(guild.roles , name = "Playing Game")
                coding = discord.utils.get(guild.roles , name = "Currently Coding")
                
                for member in guild.members :
                        try :
                                if member is not None :
                                        if member.activity is not None :
                                                for activity in member.activities :
                                                        if len(activity.type) >= 2 and activity.type == discord.ActivityType.playing and member.bot is False :
                                                                await member.add_roles(playing)

                                                        elif len(activity.type) >= 1 and activity.type != discord.ActivityType.playing and playing in member.roles and member.bot is False :
                                                                await member.remove_roles(playing)

                                        if member.activity is None :
                                                if playing in member.roles :
                                                        await member.remove_roles(playing)

                                                

                                        else :
                                                pass


                                else :
                                        pass

                                        
                        except :
                        	return


        @playing_role.before_loop
        async def before_playing_role(self):
                await self.bot.wait_until_ready()

        

        @tasks.loop(seconds = 2)
        async def coding_role(self):
                guild = self.bot.get_guild(int(545956933170102283))
                coding = discord.utils.get(guild.roles , name = "Currently Coding")
                
                for member in guild.members :
                        try :
                                if member is not None :
                                        if member.activity is not None :
                                                for activity in member.activities :
                                                        if len(activity.type) >= 2 and activity.type == discord.ActivityType.playing and member.bot is False :
                                                                if str(activity.name).startswith("Visual") or str(activity.name).startswith("Sublime") or str(activity.name).startswith("Atom") or str(activity.name).startswith("Py") :
                                                                        await member.add_roles(coding)

                                                                else :
                                                                        await member.remove_roles(coding)
                                                                        

                                                        elif len(activity.type) >= 1 and activity.type != discord.ActivityType.playing and coding in member.roles and member.bot is False :
                                                                await member.remove_roles(coding)


                                        if member.activity is None :
                                                if coding in member.roles :
                                                        await member.remove_roles(coding)

                                                

                                        else :
                                                pass


                                else :
                                        pass

                                        
                        except :
                        	return


        @coding_role.before_loop
        async def before_coding_role(self):
                await self.bot.wait_until_ready()



        @tasks.loop(seconds = 2)
        async def spotify_role(self):
                guild = self.bot.get_guild(int(545956933170102283))
                spotify = discord.utils.get(guild.roles , name = "Listening To Spotify")
                
                for member in guild.members :
                        try :
                                if member is not None :
                                        if member.activity is not None :
                                                for activity in member.activities :
                                                        if len(activity.type) >= 2 and activity.type == discord.ActivityType.listening and member.bot is False :
                                                                await member.add_roles(spotify)

                                                        elif len(activity.type) >= 1 and activity.type != discord.ActivityType.listening and spotify in member.roles and member.bot is False :
                                                                await member.remove_roles(spotify)


                                        if member.activity is None :
                                                if spotify in member.roles :
                                                        await member.remove_roles(spotify)
                                                

                                        else :
                                                pass


                                else :
                                        pass

                                        
                        except :
                        	return


        @spotify_role.before_loop
        async def before_spotify_role(self):
                await self.bot.wait_until_ready()



        @tasks.loop(seconds = 2)
        async def streaming_role(self):
                guild = self.bot.get_guild(int(545956933170102283))
                streaming = discord.utils.get(guild.roles , name = "Now Live")
                
                for member in guild.members :
                        try :
                                if member is not None :
                                        if member.activity is not None :
                                                for activity in member.activities :
                                                        if len(activity.type) >= 2 and activity.type == discord.ActivityType.streaming and member.bot is False :
                                                                await member.add_roles(streaming)

                                                        elif len(activity.type) >= 1 and activity.type != discord.ActivityType.streaming and streaming in member.roles and member.bot is False :
                                                                await member.remove_roles(streaming)

                                        if member.activity is None :
                                                if streaming in member.roles :
                                                        await member.remove_roles(streaming)
                                                        

                                        else :
                                                pass


                                else :
                                        pass

                                        
                        except :
                        	return


        @streaming_role.before_loop
        async def before_streaming_role(self):
                await self.bot.wait_until_ready()

                

def setup(bot):
    bot.add_cog(activityroles(bot))
