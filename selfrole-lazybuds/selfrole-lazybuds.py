import discord
import discord.ext.commands as commands


class SelfroleLazyBuds(commands.Cog):
        def __init__(self, bot):
                self.bot = bot

        @commands.Cog.listener()
        async def on_raw_reaction_add(self, payload):
                if payload.message_id == 826422797956939786 :
                        guild = self.bot.get_guild(payload.guild_id)
                        member = payload.member
                        if guild is None :
                                print(guild)
                                return
                        
                        if str(payload.emoji.name) == "<:helpers:826419456401342494>" :
                                helper_role = guild.get_role(741821329245995070)

                                await member.add_roles(helper_role)
                                channel = guild.get_channel(payload.channel_id)
                                await channel.send(f"<:helpers:826419456401342494> Gave you {helper_role.name} role.", delete_after = 3)

                        if str(payload.emoji.name) == "<:karuta:826418982969278514>" :
                                karuta_role = guild.get_role(826429583543762954)

                                await member.add_roles(karuta_role)
                                channel = guild.get_channel(payload.channel_id)
                                await channel.send(f"<:karuta:826418982969278514> Gave you {karuta_role.name} role.", delete_after = 3)

                        if str(payload.emoji.name) == "<:shoob:826417788540944394>" :
                                shoob_role = guild.get_role(826430267572748308)

                                await member.add_roles(shoob_role)
                                channel = guild.get_channel(payload.channel_id)
                                await channel.send(f"<:shoob:826417788540944394> Gave you {shoob_role.name} role.", delete_after = 3)


        @commands.Cog.listener()
        async def on_raw_reaction_remove(self, payload):
                print(payload.member)
                if payload.message_id == 826422797956939786 :
                        guild = self.bot.get_guild(payload.guild_id)
                        member = payload.member
                        if guild is None :
                                return
                        
                        if str(payload.emoji.name) == "<:helpers:826419456401342494>" :
                                helper_role = guild.get_role(741821329245995070)

                                await member.remove_roles(helper_role)
                                channel = guild.get_channel(payload.channel_id)
                                await channel.send(f"<:helpers:826419456401342494> Removed you're {helper_role.name} role {member.mention}.", delete_after = 3)

                        if str(payload.emoji.name) == "<:karuta:826418982969278514>" :
                                karuta_role = guild.get_role(826429583543762954)

                                await member.remove_roles(karuta_role)
                                channel = guild.get_channel(payload.channel_id)
                                await channel.send(f"<:karuta:826418982969278514> Removed you're {karuta_role.name} role {member.mention}.", delete_after = 3)

                        if str(payload.emoji.name) == "<:shoob:826417788540944394>" :
                                shoob_role = guild.get_role(826430267572748308)

                                await member.remove_roles(shoob_role)
                                channel = guild.get_channel(payload.channel_id)
                                await channel.send(f"<:shoob:826417788540944394> Removed you're {shoob_role.name} role {member.mention}.", delete_after = 3)

                            
                    
                        
def setup(bot):
    bot.add_cog(SelfroleLazyBuds(bot))
