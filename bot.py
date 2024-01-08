from discord.ext import commands, tasks
import discord
from dataclasses import dataclass
from math_operations import *
from translator import *
from chem import getElementProperties


BOT_TOKEN = 'TOKEN' # this should be your own token
CHANNEL_ID = 1111111111 # this should be your own channel ID

# reminder sessional info
@dataclass
class Session:
   is_active: bool = False
   start_time: int = 0
   note: str = ''

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
session = Session()


# introduction message
@bot.event
async def on_ready():
   print('Cracked Bot is ready')
   channel = bot.get_channel(CHANNEL_ID)
   await channel.send("Hi, I'm Cracked Bot! Type !helpcommands for a list of commands.")


# commands
@bot.command()
async def remind(ctx, minutes, *activity):
   MAX_SESSION_TIME_MINUTES = int(minutes)

   global reminder

   @tasks.loop(minutes=MAX_SESSION_TIME_MINUTES, count=2)
   async def reminder():
      if reminder.current_loop == 0:
         return

      await ctx.send(f'This is your reminder for: [{session.note}]' )
      session.note = ''


   if session.is_active:
      await ctx.send("You already have a reminder set")
      return

   session.is_active = True

   current_note = ''
   for i in range(len(activity)):
      if i != len(activity) - 1:
         current_note = current_note + activity[i] + ' '
      else:
         current_note = current_note + activity[i]

   session.note = current_note
   reminder.start()
   await ctx.send(f'I will remind you about [{session.note}] in {minutes} minute(s)')


@bot.command()
async def end(ctx):
   if not session.is_active:
      await ctx.send("No reminders have been set")
      return

   session.is_active = False
   reminder.stop()
   await ctx.send(f'Reminder for: [{session.note}] cancelled.')
   session.note = ''


@bot.command()
async def helpcommands(ctx):
   await ctx.send(""" Here are the following commands available with Cracked Bot:

!helpcommands - list of commands

!remind [minutes] [text] - set a reminder for [text] after [minutes] minutes

!end - cancel current reminder

!add [x1] [x2] [x3] ... - add all numbers x1 +  x2 + x3...

!multiply [x1] [x2] [x3] ... - multiply all numbers x1 *  x2 * x3...

!divide [x1] [x2] [x3] ... - divide all numbers x1 / x2 / x3...

!subtract [x1] [x2] [x3] ... - subtract all numbers x1-x2-x3...

!french [text] - translates english [text] into french

!english [text] - translates french [text] into english

!chem [Hg] - gives a list of properties of the given element, e.g. Hg - mercury""")


@bot.command()
async def multiply(ctx, *arr):
   await ctx.send(str(mult(arr)))


@bot.command()
async def divide(ctx, *arr):
   await ctx.send(str(div(arr)))


@bot.command()
async def add(ctx, *arr):
   await ctx.send(str(ad(arr)))


@bot.command()
async def subtract(ctx, *arr):
   await ctx.send(str(sub(arr)))


@bot.command()
async def french(ctx, *arr):
   await ctx.send(eng_to_fr(arr))


@bot.command()
async def english(ctx, *arr):
   await ctx.send(fr_to_eng(arr))


@bot.command()
async def chem(ctx, symbol):
   await ctx.send(getElementProperties(symbol))


bot.run(BOT_TOKEN)
