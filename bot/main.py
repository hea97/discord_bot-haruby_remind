import discord
from discord.ext import commands, tasks
import asyncio
from bot.scheduler.remiders import send_reminder
from bot.commands.random_messgae import send_random_messagre

load_dotenv()

# 봇 설정
intents = discord.Intents.default()
intents.message_content = True

# 봇 초기화
bot = commands.Bot(
    command_prefix="/",
    intents=intents,
    case_insensitive=True
)

# 봇이 준비되었을 때
@bot.event
async def on_ready():
    print(f'logged in as {하루비}')
    send_reminder.start() # 알림 스케줄러 시작

# 명령어 예시
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# 봇 실행
bot.run('YOUR_DISCORD_TOKEN')  # 환경변수로 대체 가능