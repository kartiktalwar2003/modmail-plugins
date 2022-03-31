from cgitb import text
import discord
import discord.ext.commands as commands


class Rules(commands.Cog):
        def __init__(self, client):
                self.client = client
        
        @commands.command()
        @commands.is_owner()
        async def verify(self, ctx):
                ask_img = await ctx.send("Send the image.")
                img_msg = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
                if img_msg.attachments:
                        image_msg = await ctx.send(img_msg.attachments[0].url)
                else:
                        image_msg = await ctx.send(img_msg.content)

                ask_footer = await ctx.send("Send the name for footer.")
                footer_msg = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
                embed = discord.Embed()
                embed.color = discord.Color(0x303136)
                embed.set_footer(text=f"{footer_msg.content} © 2022")
                embed.title = "REACT ON THIS MESSAGE TO GET VERIFIED"
                embed.description = "By reactiong you agree to follow all the rules of the server.\n\
You cannot claim that you did'nt know about a rule in any sort of manner.\n\
Warning-this also means that by reacting you are not allowed to pursuit anything of legal matters on the server."
                verify_msg = await ctx.send(embed=embed)
                await ctx.message.delete()
                await img_msg.delete()
                await footer_msg.delete()
                await ask_img.delete()
                await ask_footer.delete()
                await verify_msg.pin()
                await image_msg.pin()



        @commands.command()
        @commands.is_owner()
        async def rules(self, ctx):
                ask_img = await ctx.send("Send the image.")
                img_msg = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
                if img_msg.attachments:
                        rule_img = await ctx.send(img_msg.attachments[0].url)
                else:
                        rule_img = await ctx.send(img_msg.content)

                ask_footer = await ctx.send("Send the name for footer.")
                footer_msg = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)

                rule1_embed = discord.Embed()
                rule1_embed.set_footer(text=f"{footer_msg.content} © 2022")
                rule1_embed.color = discord.Color(0x303136)
                rule1_embed.title = "PAGE 1"
                rule1_embed.description = "\n\
1.1. Follow Discord TOS and Discord Guidelines.\n\
1.2. Treat all members with respect.\n\
1.3. Harassment, abuse, hate speech or any kind of discriminatory speech will not be tolerated.\n\
1.4. Do not in any way intentionally offend any member in the Discord server.\n\
1.5. Racial or offensive slurs will not be tolerated.\n\
1.6. Tagging a member/staff member without reason will result in a warning.\n\
1.7. Revealing private information about any individual; is a zero tolerance rule.\n\
1.8. Do not publicly accuse other users/players of misconduct.\n\
1.9. No backseat modding.\n\
1.10. No talking about topics related to religion or politics.\n\
1.11. Words or small sentences in other languages other than English are allowed only for the purpose of teaching someone, or for clarification, or in specific channels."

                rule2_embed = discord.Embed()
                rule2_embed.set_footer(text=f"{footer_msg.content} © 2022")
                rule2_embed.color = discord.Color(0x303136)
                rule2_embed.title = "PAGE 2"
                rule2_embed.description = "\n\
2.1. Don’t Spam (Emoji , same msg again & again or Dont spam for Level Increase.\n\
2.2. Don’t Promote Yourself or Others + Don’t post any kind of link anywhere in server.\n\
2.3. If any of staff member is asking to Change the Topic of conversation then it needs to be changed, if it gets too offensive to other members. If not followed, there are kick/ban.\n\
2.4. We highly request to our old members to welcome new members & try including them in your conversation. Don’t act creepy or rude towards the new members because they don't know how to behave in server.\n\
2.5. Respect all staff and follow their instruction , Don't Use Abusive/odd Names/ Profile Pictures. If Any mod Found You Guilty they Can Change Your Name Any time.\n\
2.6. Don’t expose anyone. Do not send any private information of anyone without permission. That includes pictures.\n\
2.7. Don't randomly tag staff if unnecessary.\n\
2.8. If you are annoyed by someone: Just block the person and move on.\n\
2.9. Have common sense to understand puns/sarcasm."


                rule3_embed = discord.Embed()
                rule3_embed.set_footer(text=f"{footer_msg.content} © 2022")
                rule3_embed.color = discord.Color(0x303136)
                rule3_embed.title = "PAGE 3"
                rule3_embed.description = "\n\
3.1. Posting any content related to piracy, cheats, cracks, exploits or any kind of copyright breaching materials is forbidden.\n\
3.2. Any malicious activity toward the server or any member is forbidden.\n\
3.3 This server follows all the Discord Guidelines and TermsOfServices. Please do read and follow all them listed.\n\
3.4 Threats such as DDoS, DoX, or generalized threats are strictly prohibited and will result in an immediate removal/ban from the community.\n\
3.5 Any attempts to “ear-rape” other fellow community members is strictly prohibited and will result in an immediate removal/ban from the server.\n\
3.6 Intentional toxic behavior is not allowed.\n\
3.7. Don't Argue With Any Mod/Staff. Their Decision will be last Decision"

                rule1_msg = await ctx.send(embed=rule1_embed)
                rule2_msg = await ctx.send(embed=rule2_embed)
                rule3_msg = await ctx.send(embed=rule3_embed)
                await ctx.message.delete()
                await footer_msg.delete()
                await ask_footer.delete()
                await img_msg.delete()
                await ask_img.delete()
                await rule3_msg.pin()
                await rule2_msg.pin()
                await rule1_msg.pin()
                await rule_img.pin()

        @commands.command()
        @commands.is_owner()
        async def selfrole(self, ctx):
                ask_img = await ctx.send("Send the image.")
                img_msg = await self.client.wait_for('message', check=lambda message: message.author == ctx.author)
                if img_msg.attachments:
                        image_msg = await ctx.send(img_msg.attachments[0].url)
                else:
                        image_msg = await ctx.send(img_msg.content)

                await ctx.message.delete()
                await img_msg.delete()
                await ask_img.delete()
                await image_msg.pin()


def setup(client):
        client.add_cog(Rules(client))
        print("Rules loaded")