import discord
from discord.ext import commands
from bot.commands.links import links, add_link, remove_link
from bot.commands.pomodoro import pomodoro
from bot.commands.random_message import random_message
from bot.commands.routine import routine

# 봇 인텐트 설정
intents = discord.Intents.default()
intents.message_content = True  # 메시지 내용 읽기 권한 활성화

# 봇 초기화
bot = commands.Bot(
    command_prefix="/",  # 명령어 접두사
    intents=intents,  # 인텐트 설정
    case_insensitive=True  # 대소문자 구분 없이 명령어 처리
)

# 명령어 등록
bot.add_command(links)
bot.add_command(add_link)
bot.add_command(remove_link)
bot.add_command(pomodoro)
bot.add_command(random_message)
bot.add_command(routine)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# 봇 실행
bot.run('YOUR_DISCORD_TOKEN')  # 환경변수로 대체 가능