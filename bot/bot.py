import discord
import config
from discord.ext import commands
from discord.ext import tasks
import datetime
import random
import os
from random import choice
from itertools import cycle
from discord.utils import get
import asyncio
import youtube_dl
import shutil
import json
from pydub import AudioSegment

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    stratus.start()
    print('We have logged in as {0.user}'.format(bot))

@tasks.loop(seconds = 30)
async def stratus():
    await bot.change_presence(activity=discord.Game(next(config.status)))

@bot.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


#command for telling in console to check the member list
@bot.command(aliases = ['PING', 'Ping'])
async def ping(ctx):
    print(f'{ctx.message.author} used comand "ping" at {datetime.datetime.now()}')
    await ctx.send(f'Pong! {round(bot.latency * 1000)}ms')

@bot.command(aliases = ['ванга', 'ВАНГА', 'вАНГА'])
async def Ванга(ctx, *, question):
    await ctx.send(f'Твой вопрос: {question}\nВанга говорит: {random.choice(config.responses)}')
    print(f'{ctx.message.author} used comand "VANGA" at {datetime.datetime.now()}')
@bot.command(aliases = ['Сlear', 'CLEAR'])
async def clear(ctx, ammount=100):
    await ctx.channel.purge(limit=ammount)
    print(f'{ctx.message.author} used comand "clear" at {datetime.datetime.now()}')
@bot.command()
async def clearext(ctx, ammount=100000):
    await ctx.channel.purge(limit=ammount)
    print(f'{ctx.message.author} used comand "clearext" at {datetime.datetime.now()}')
@bot.command()
async def who(ctx):
    await ctx.send(config.kamenshik)
    print(f'{ctx.message.author} used comand "kamenshick" at {datetime.datetime.now()}')

@bot.command(pass_context=True)
async def clown(ctx):
    clown = choice(ctx.message.channel.guild.members)
    await ctx.send(f'{clown.mention} - клоун 🤡')
    print(f'{ctx.message.author} used comand "clown" at {datetime.datetime.now()}')
@bot.command(pass_context=True)
async def hug(ctx):
    user313 = choice(ctx.message.channel.guild.members)
    await ctx.send(f'{ctx.message.author.mention} обнял {user313.mention}')
    print(f'{ctx.message.author} used comand "hug" at {datetime.datetime.now()}')

@bot.command()
async def info(ctx):
    await ctx.send(config.info)
    print(f'{ctx.message.author} used comand "info" at {datetime.datetime.now()}')

@bot.command(aliases = ['PP', 'Pp'])
async def pp(ctx):
    pp = choice(range(30))
    await ctx.send(f'Длина pipi {ctx.message.author.mention} = {pp}' )
    print(f'{ctx.message.author} used comand "pp" at {datetime.datetime.now()}')

@bot.command(aliases = ['Box', 'BOX'])
async def box(ctx):
    list = ['Легендарка', 'Cинька', 'Эпик', 'Гавно']
    box1 = choice(list)
    box2 = choice(list)
    box3 = choice(list)
    box4 = choice(list)
    await ctx.send(f'В контейнере {box1}, {box2}, {box3}, {box4}')
    print(f'{ctx.message.author} used comand "box" at {datetime.datetime.now()}')

@bot.command(aliases = ['WeeWee', 'Weewee','WEEWEE'])
async def weewee(ctx):
    user312 = choice(ctx.message.channel.guild.members)
    await ctx.send(f'У {user312.mention} большой WeeWee')
    print(f'{ctx.message.author} used comand "weewee" at {datetime.datetime.now()}')

    """
    @commands.command(aliases = ['KOT', 'Kot'])
    async def kot(ctx):
        num = choice(range(43))
        await ctx.send(file=discord.File(f'{num}.png'))
    """

@bot.command(aliases = ['Winx','WINX'])
async def winx(ctx):
    await ctx.send(f'{ctx.message.author.mention} - ты {choice(config.winx)}')
    print(f'{ctx.message.author} used comand "winx" at {datetime.datetime.now()}')

###############################################


#music part

@bot.command(pass_context=True)
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send(f'Lucio has arrived at {channel}!')

@bot.command(pass_context=True)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.sent(f'Ran out of {channel}')
@bot.command(pass_context=True, aliases=['p', 'pl'])
async def play(ctx, url: str):

    def check_queue():
        Queue_infile = os.path.isdir('./Queue')
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_q = length - 1
            try:
                first_file = os.listdir(DIR)[0]
            except:
                print('No more queued song(s)\n')
                queues.clear()
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath('Queue') + '\\' + first_file)
            if length != 0:
                print("Song done, next queued\n")
                print(f'Songs still in queue: {still_q}')
                song_there = os.path.isfile('song.mp3')
                if song_there:
                    os.remove('song.mp3')
                shutil.move(song_path, main_location)
                for file in os.listdir('./'):
                    if file.endswith('.mp3'):
                        os.rename(file, 'song.mp3')
                voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: check_queue())
                voice.source = discord.PCMVolumeTransformer(voice.source)
                voice.source.volume = 0.07

            else:
                queues.clear()
                return
        else:
            queues.clear()
            print("No songs were queued before the ending of the last song\n")

    song_there = os.path.isfile('song.mp3')

    try:
        if song_there:
            os.remove('song.mp3')
            queues.clear()
            print('Removed old song file')
    except PermissionError:
        print('Trying to delete song file, but its being played')
        await ctx.send('ERROR: Music playing ')
        return

    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = './Queue'
        if Queue_infile is True:
            print('Removed old Queue Folder')
            shutil.rmtree(Queue_folder)
    except:
        print('No old Queue folder')
    await ctx.send('Dropping the beat')
    voice = get(bot.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessor': [{
            'key': 'FFmpegExtractAudio',
            'preferedcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('Downloading audio now\n')
        ydl.download([url])

    for file in os.listdir("C:\\Users\\forps\\Desktop\\lucio_bot\\Queues"):
        print(file)
        AudioSegment.from_file(f"C:\\Users\\forps\\Desktop\\lucio_bot\\downloads\\{file}").export(
            f"C:\\Users\\forps\\Desktop\\lucio_bot\\Queues\\song.mp3", format="mp3")
        print('converting')

    voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: check_queue())
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit('-', 2)
    await ctx.send(f' Playing: {name[0]}')
    print('playing\n')


@bot.command(pass_context=True, aliases=['pa', 'pau'])
async def pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_playing():
        print('Music paused')
        voice.pause()
        await ctx.send('Music paused')
    else:
        print('Music not playing failed to pause')
        await ctx.send('Music not playing failed to pause')


@bot.command(pass_context=True, aliases=['r', 'res'])
async def resume(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_paused():
        print('Resumed music')
        voice.resume()
        await ctx.send('Resumed music')
    else:
        print('Music isn\'t paused')
        await ctx.send('Music isn\'t paused')


@bot.command(pass_context=True, aliases=['s', 'sk'])
async def skip(ctx):

    voice = get(bot.voice_clients, guild=ctx.guild)

    queues.clear()

    if voice and voice.is_playing():
        print('Music skipped')
        voice.stop()
        await ctx.send('Music skipped')
    else:
        print('Music isn\'t playing')
        await ctx.send('Music isn\'t playing')

queues = {}

@bot.command(pass_context=True, aliases=['q'])
async def queue(ctx, url: str):
    Queue_infile = os.path.isdir('./Queue')
    if Queue_infile is False:
        os.mkdir("Queue")
    DIR = os.path.abspath(os.path.realpath('Queue'))
    q_num = len(os.listdir(DIR))
    q_num += 1
    add_queue = True
    while add_queue:
        if q_num in queues:
            q_num += 1
        else:
            add_queue = False
            queues[q_num] = q_num
    queue_path = os.path.abspath(os.path.realpath("Queue") + f'./song{q_num}.%(ext)s')

    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'postprocessor': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

        
    for file in os.listdir("C:\\Users\\forps\\Desktop\\lucio_bot\\Queues"):
        print(file)
        AudioSegment.from_file(f"C:\\Users\\forps\\Desktop\\lucio_bot\\downloads\\{file}").export(
            f"C:\\Users\\forps\\Desktop\\lucio_bot\\Queues\\song.mp3", format="mp3")
        print('now converting')
        await ctx.send('Adding song' + str(q_num) + 'to the queue')
        print('Song was added to queue')
bot.run(config.TOKEN)
