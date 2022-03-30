import discord
import discord.ext.commands as commands
from gtts import gTTS 

def create_audio(text , lang, speed , guild:discord.Guild):        
        speech = gTTS(text = text, lang = lang , slow = speed)
        return speech.save(f"tts/{str(guild)+'tts.mp3'}")


class TTS(commands.Cog):
        def __init__(self, client):
                self.client = client

        @commands.command(name = "tts" , usage = "tts message" , help = "tts Hi this is a tts message", description = "Speak's a text message in a voice channel")
        async def tts(self, ctx, *,text):
                try :
                        author_channel = ctx.message.author.voice
                        connected_voice = ctx.guild.voice_client

                        if connected_voice is None :
                                speak_perms = author_channel.channel.permissions_for(ctx.guild.me).speak
                                connect_perms = author_channel.channel.permissions_for(ctx.guild.me).connect

                                if connect_perms and speak_perms is True :
                                        await author_channel.channel.connect()
                                        await ctx.reply(f"Joined {author_channel.channel.mention}", mention_author = False)

                                elif connect_perms or speak_perms is False :
                                        return await ctx.reply(f"Make sure I've enough permissions in the {author_channel.channel.mention} to connect and speak.", mention_author = False)
                                

                except :
                        pass
                
                guild = ctx.guild        
                lang = "hi"
                speed = False
                        
                create_audio(text=text , lang=lang, speed = eval(speed) , guild = ctx.guild.id )
                file = str(str(ctx.guild.id) + "tts.mp3")
                audio = f"tts/{file}"
                vc = ctx.voice_client
                vc.play(discord.FFmpegPCMAudio(executable=r"ffmpeg" , source=audio))
                        

        @commands.command(name = "join" , usage = "join" , help = "join", description = "Join's the voice channel in which user is.", aliases=['j', 'summon'])
        async def join(self, ctx):
                author_channel = ctx.message.author.voice
                connected_voice = ctx.guild.voice_client

                if connected_voice is None :
                        speak_perms = author_channel.channel.permissions_for(ctx.guild.me).speak
                        connect_perms = author_channel.channel.permissions_for(ctx.guild.me).connect

                        if connect_perms and speak_perms is True :
                                await author_channel.channel.connect()
                                await ctx.reply(f"Joined {author_channel.channel.mention}", mention_author = False)

                        elif connect_perms or speak_perms is False :
                                return await ctx.reply(f"Make sure I've enough permissions in the {author_channel.channel.mention} to connect and speak.", mention_author = False)
                                

                elif connected_voice.channel == author_channel.channel :
                        await ctx.reply("I'm in your voice channel only.", mention_author = False)

                else :
                        await ctx.reply(f"I'm connected to {connected_voice.channel.mention} currently. Can't join {author_channel.channel.mention}.", mention_author = False)

        @commands.command(name = "disconnect" , usage = "disconnect" , help = "disconnect", description = "Disconnect's from voice channel", aliases=['dc', 'l','leave'])
        async def disconnect(self,ctx):
                author_channel = ctx.message.author.voice
                voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
                connected_voice = ctx.guild.voice_client

                if connected_voice is None :
                        await ctx.reply(f"I'm not in a voice channel, How can I leave ?", mention_author = False)

                elif author_channel.channel == connected_voice.channel :
                        try :
                                await connected_voice.disconnect()
                        except Exception as e :
                                raise e
                        await ctx.reply(f"Left {author_channel.channel.mention}", mention_author = False)

                elif author_channel != connected_voice.channel :
                        try :
                                if len(connected_voice.channel.members) <= 1 :
                                        await voice.disconnect()
                                        await ctx.reply(f"Left {connected_voice.channel.mention}", mention_author = False)
                                        
                        except :
                                await ctx.reply(f"I'm in {connected_voice.channel.mention}, join this channel to disconnect me.", mention_author = False)

                else :
                        await ctx.reply(f"Error while disconnecting. Please contact my support server for help.", mention_author = False)
                        
                        

        @commands.command(aliases=['skip','s','n', 'next'])
        async def stop(self, ctx):
                voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
                if voice and voice.is_playing():
                        voice.stop()
                        await ctx.reply("Stopped!", mention_author = False)
                else:
                        await ctx.reply("No audio playing", mention_author = False)
                


def setup(client):
    client.add_cog(TTS(client))
    print("TTS loaded")
