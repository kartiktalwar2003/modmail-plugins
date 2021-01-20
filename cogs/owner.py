import discord
import discord.ext.commands as commands
import json
import io
import textwrap
import traceback
import gtts
from contextlib import redirect_stdout
from PIL import Image, ImageDraw, ImageFont , ImageFilter , ImageGrab , ImageOps

class Owner(commands.Cog):
        def __init__(self, client):
                self.client = client
                self._last_result = None
                self.client.owner_ids = [451707918320926733 , 456456900414799873]

        def cleanup_code(self, content):
                if content.startswith('```') and content.endswith('```'):
                        return '\n'.join(content.split('\n')[1:-1])

                return content.strip('` \n')


        @commands.command(name = "console" , usage = "console" , help = "console" , description = "Send's a screenshot of console")
        @commands.is_owner()
        async def console(self , ctx):
                img = ImageGrab.grab()
                img.save("console.png")
                await ctx.author.send(file=discord.File("console.png"))

        @commands.command(name = "details" , usage = "details serverId" , help = "details 1234567891234" , description = "Send's the details from database")
        @commands.is_owner()
        async def details(self , ctx , guild):
                with open(r'C:\Users\Acer\Desktop\Bots\Recolt\cogs\settings.json', 'r') as f:
                        data = json.load(f)
                        server = data[str(guild)]
                guild = self.client.get_guild(int(guild))
                await ctx.send(f"```Details for {guild}\nMember count: {guild.member_count}\n{server}```")
                

        @commands.command(name = "load" , usage = "load cog_name" , help = "load help" , description = "Load's a Cog" , hidden = True)
        @commands.is_owner()
        async def load (self , ctx , *, extension):
                self.client.load_extension(f"cogs.{extension}")
                print(f"{extension} cog loaded by {ctx.author}")

        @commands.command(name = "unload" , usage = "unload cog_name" , help = "unload help" , description = "Unload's a Cog")
        @commands.is_owner()
        async def unload (self , ctx , *, extension):
                self.client.unload_extension(f"cogs.{extension}")
                print(f"{extension} cog unloaded by {ctx.author}")

        @commands.command(name = "reload" , usage = "reload cog_name" , help = "reload help" , description = "Reload's a Cog" )
        @commands.is_owner()
        async def reload (self , ctx , *, extension):
                self.client.unload_extension(f"cogs.{extension}")
                self.client.load_extension(f"cogs.{extension}")
                print(f"{extension} cog reloaded by {ctx.author}")

        @commands.command(name = "act", aliases=["activity" , "presence"], usage = "activity type text" , help = "activity Playing help" , description = "Set's an activity")
        @commands.is_owner()
        async def act(self, ctx, TYPE, *, presence:str):
                if TYPE == "Watching":
                        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"{presence}"))
                        await ctx.channel.send(f'Activity changed to: Watching {presence}')
                        
                if TYPE == "Listening":
                        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=f"{presence}"))
                        await ctx.channel.send(f'Activity changed to: Listening to {presence}')
                        
                if TYPE == "Playing":
                        await self.client.change_presence(activity=discord.Game(name=f"{presence}"))
                        await ctx.channel.send(f'Activity changed to: Playing {presence}')
                        
                if TYPE == "Streaming":
                        await self.client.change_presence(activity=discord.Streaming(name=f"{presence}",url="https://pornhub.com/"))
                        await ctx.channel.send(f'Activity changed to: Streaming {presence}')
                        
                else :
                        pass


        @commands.command(name='eval' , usage = "eval code" , help = "eval print('Cute mc')" , description = "Evaluates a Code")
        @commands.is_owner()
        async def _eval(self, ctx, *, body: str):
                """Evaluates a code"""

                env = {
                    'bot': self.client,
                    'ctx': ctx,
                    'channel': ctx.channel,
                    'author': ctx.author,
                    'guild': ctx.guild,
                    'message': ctx.message,
                    '_': self._last_result
                    }

                env.update(globals())

                body = self.cleanup_code(body)
                stdout = io.StringIO()

                to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

                try:
                    exec(to_compile, env)
                except Exception as e:
                    return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

                func = env['func']
                try:
                    with redirect_stdout(stdout):
                        ret = await func()
                except Exception as e:
                    value = stdout.getvalue()
                    await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
                else:
                    value = stdout.getvalue()
                    try:
                        await ctx.message.add_reaction('\u2705')
                    except:
                        pass

                    if ret is None:
                        if value:
                            await ctx.send(f'```py\n{value}\n```')
                    else:
                        self._last_result = ret
                        await ctx.send(f'```py\n{value}{ret}\n```')


                        
def setup(client):
    client.add_cog(Owner(client))
    print("Owner's Cog Loaded")
