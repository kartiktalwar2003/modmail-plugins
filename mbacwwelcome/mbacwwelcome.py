import discord
import discord.ext.commands as commands
from PIL import Image, ImageDraw, ImageFont, ImageOps
import aiohttp
from io import BytesIO

class MBACWWelcome(commands.Cog):
        def __init__(self, bot):
                self.bot = bot

        @commands.Cog.listener()
        async def on_member_join(self, member):
            channel = discord.utils.get(member.guild.channels, id=927465465868075028)
            img_url = member.avatar_url_as(format="png")
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{img_url}") as resp:
                    if resp.status != 200:
                        return None
                    data = BytesIO(await resp.read())
                    avatar = Image.open(data)
                    avatar = avatar.convert('RGBA').resize((210,210))
                    mask = Image.new('L', avatar.size, 0)
                    draw = ImageDraw.Draw(mask)
                    draw.ellipse((0, 0) + avatar.size, fill=255)
                    output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
                    output.putalpha(mask)
                    base = Image.open("./Welcome.png")
                    base.paste(output,(408, 50), output)

                    myFont = ImageFont.truetype("welcome.ttf", 80)
                    W, H = (1024,500)
                    welcome = f"WELCOME {member}"
                    msg = f"Now we've {member.guild.member_count} members"
                    draw = ImageDraw.Draw(base)
                    w, h = draw.textsize(welcome, font=myFont)
                    draw.text(((W-w)/2, 300), welcome, fill="hotpink", font=myFont)
                    w, h = draw.textsize(msg, font=myFont)
                    draw.text(((W-w)/2, 390), msg, fill="black", font=myFont)
                    base.save("card.png")
                
                file = discord.File("card.png", filename="card.png")
                await channel.send(file = file)

                        
def setup(bot):
    bot.add_cog(MBACWWelcome(bot))
    print("Welcome Cog Loaded")
