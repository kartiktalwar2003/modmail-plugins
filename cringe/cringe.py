import discord
import discord.ext.commands as commands
from discord.ext import tasks

class cringe(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
                
        
        @commands.command(aliases=["hehe","joy","hqhq","lol"])
        async def haha(self, ctx ,*,msg_id = None):
                await ctx.message.delete()
                emote1 = "🔥" 
                emote2 = "<:hehe:825292396334022688>"
                emote3 = "😂"
                emote4 = "💯"
                emote5 = "🤞"
                emote6 = "😹"
                emote7 = "<:hahaprateek:786330205865639967>"
                emote8 = "💀"
                emote9 = "<:CoolChamp:826402171112390667>"
                emote10 = "🤣"
                emote11 = "<:chupmadarchod:701780539195261008>"
                emote12 = "<:heheh:798443439128576000>"
                emote13 = "<:hahakomedi:792417780154368020>"
                emote14 = "<:ruineverything:831588564629192745>"
                emote15 = "<:LafdaPopcorn:794542953086451732>"
                emote16 = "<:comedy:769871182773092362>"
                emote17 = "<:bruh:816252917748465695>"
                emote18 = "🤷"
                emote19 = "<:terimaarandi:806603231114821693>"
                emote20 = "<:roflxd:895596018446516284>"
                
                if msg_id is None :
                        command_msg = ctx.message
                        message = await ctx.channel.fetch_message(command_msg.reference.message_id)
                else :
                        message = await ctx.channel.fetch_message(msg_id)
                await message.add_reaction(emote1)
                await message.add_reaction(emote2)
                await message.add_reaction(emote3)
                await message.add_reaction(emote4)
                await message.add_reaction(emote5)
                await message.add_reaction(emote6)
                await message.add_reaction(emote7)
                await message.add_reaction(emote8)
                await message.add_reaction(emote9)
                await message.add_reaction(emote10)
                await message.add_reaction(emote11)
                await message.add_reaction(emote12)
                await message.add_reaction(emote13)
                await message.add_reaction(emote14)
                await message.add_reaction(emote15)
                await message.add_reaction(emote16)
                await message.add_reaction(emote17)
                await message.add_reaction(emote18)
                await message.add_reaction(emote19)
                await message.add_reaction(emote20)
                
        @commands.command()
        async def cringe(self, ctx ,*,msg_id = None):
                await ctx.message.delete()                
                cringe1 = "<:cringe1:771304364911755284>" 
                cringe2 = "<:cringe2:771304385535410176>" 
                cringe3 = "<:cringe3:771304401121443850>" 
                cringe4 = "<:cringe4:771304424849014785>" 
                cringe5 = "<:cringe5:771304439608377355>" 
                cringe6 = "<:cringe6:771304458985406475>" 
                cringe7 =  "<:cringe7:771304482888876072>" 
                cringe8 = "<:cringe8:771304514165800980>" 
                cringe9 = "<:cringe9:771304499218087946>"
                cringe10 = "<a:cringe10:771304537037209600>"
                cringe11 = "<a:cringe11:771304549197545472>"
                cringe12 = "<a:cringe12:771304559381315605>"
                cringe13 = "<a:cringe13:771304601378357248>"
                cringe14 = "<a:cringe14:771304638834016287>"
                cringe15 = "<a:cringe15:771304662657662986>"
                cringe16 = "<a:cringe16:771304677802639381>"
                cringe17 = "<a:cringe17:771304691534921758>"
                cringe18 = "<a:cringe18:771304706471362590>"
                cringe19 = "<a:cringe19:771304759156015127>"
                cringe20 = "<a:cringe20:771304777115762698>"
                if msg_id is None :
                        command_msg = ctx.message
                        message = await ctx.channel.fetch_message(command_msg.reference.message_id)
                else :
                        message = await ctx.channel.fetch_message(msg_id)
                await message.add_reaction(cringe1)
                await message.add_reaction(cringe2)
                await message.add_reaction(cringe3)
                await message.add_reaction(cringe4)
                await message.add_reaction(cringe5)
                await message.add_reaction(cringe6)
                await message.add_reaction(cringe7)
                await message.add_reaction(cringe8)
                await message.add_reaction(cringe9)
                await message.add_reaction(cringe10)
                await message.add_reaction(cringe11)
                await message.add_reaction(cringe12)
                await message.add_reaction(cringe13)
                await message.add_reaction(cringe14)
                await message.add_reaction(cringe15)
                await message.add_reaction(cringe16)
                await message.add_reaction(cringe17)
                await message.add_reaction(cringe18)
                await message.add_reaction(cringe19)
                await message.add_reaction(cringe20)
                

def setup(bot):
    bot.add_cog(cringe(bot))
