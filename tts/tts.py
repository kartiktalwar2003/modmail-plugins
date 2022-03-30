import discord
import discord.ext.commands as commands
from gtts import gTTS


def create_audio(text, lang, speed, guild: discord.Guild):
    speech = gTTS(text=text, lang=lang, slow=speed)
    speech.save(f"{str(guild)+'tts.mp3'}")
    return

class TTS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="tts", usage="tts message", help="tts Hi this is a tts message", description="Speak's a text message in a voice channel")
    async def tts(self, ctx, *, text):
        try:
            author_channel = ctx.message.author.voice
            connected_voice = ctx.guild.voice_client
            print(author_channel)
            print(connected_voice)
            
            if connected_voice is None:
                speak_perms = author_channel.channel.permissions_for(ctx.guild.me).speak
                connect_perms = author_channel.channel.permissions_for(ctx.guild.me).connect
                print("First IF")
                
                if connect_perms and speak_perms is True:
                    await author_channel.channel.connect()
                    print("Second IF")
                    await ctx.reply(f"Joined {author_channel.channel.mention}", mention_author=False)
                    
                if connect_perms or speak_perms is False:
                    print("Third IF")
                    return await ctx.reply(f"Make sure I've enough permissions in the {author_channel.channel.mention} to connect and speak.", mention_author=False)
                    
                else :
                    print("First ELSE")

            else:
                print("Second ELSE")

        except:
            pass

        lang = "hi"
        create_audio(text=text, lang=lang, speed=False, guild=ctx.guild.id)
        file = str(str(ctx.guild.id) + "tts.mp3")
        audio = f"{file}"
        print(audio)
        vc = ctx.voice_client
        print(vc)
        vc.play(discord.FFmpegPCMAudio(executable=r"ffmpeg", source=audio))

def setup(bot):
    bot.add_cog(TTS(bot))
    print("TTS loaded")