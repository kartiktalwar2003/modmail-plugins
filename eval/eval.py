import discord
import discord.ext.commands as commands
import json
import io
import textwrap
import traceback
from contextlib import redirect_stdout

class eval(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
                self._last_result = None
                self.bot.owner_ids = [451707918320926733]

        def cleanup_code(self, content):
                if content.startswith('```') and content.endswith('```'):
                        return '\n'.join(content.split('\n')[1:-1])

                return content.strip('` \n')


        @commands.command(name='eval' , usage = "eval code" , help = "eval print('Cute')" , description = "Evaluates a Code")
        @commands.is_owner()
        async def _eval(self, ctx, *, body: str):
                """Evaluates a code"""

                env = {
                    'bot': self.bot,
                    'client': self.bot,
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


                        
def setup(bot):
    bot.add_cog(eval(bot))
