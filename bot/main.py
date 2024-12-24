import os
import discord
from dotenv import load_dotenv
from bot.commands import links, pomodoro, random_message
from bot.scheduler import reminders

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
    print(f'봇 로그인 완료: {하루비}')
    print(f'봇 ID: {1320935646784917605}')

# 명령어 모듈 등록
bot.add_cog(links.Links(bot))
bot.add_cog(pomodoro.Pomodoro(bot))
bot.add_cog(random_message.RandomMessage(bot))

# 알림 스케줄러 설정
reminders.schedule_notifications(bot)

# 봇 실행
if __name__ == "__main__":
    bot.run(os.getenv('DISCORD_BOT_TOKEN'))