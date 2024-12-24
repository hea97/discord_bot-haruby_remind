import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler # type: ignore

class Pomodoro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.scheduler = AsyncIOScheduler()
        self.timer_duration= 25 * 60 # 25분 타이머
    
    @commands.command
    async def pomodoro(self, ctx):
        """Pomodore 타이머를 시작합니다"""
        await ctx.send("Pomodore 타이머가 시작되었습니다. 25분 후 알람이 전송됩니다.🍇")

        # 타이머 시작
        self.scheduler.add_job(
            lambda: ctx.send("Pomodore 타이머가 종료되었습니다. 5분간 휴식을 취하세요!🍇"),
            'date',
            run_date='now() + timedelta(minutes=25)'
        )
        self.scheduler.start()
    
    @commands.command
    async def stop_pomodoro(self, ctx):
        """Pomodore 타이머를 중지합니다"""
        self.scheduler.shutdown()
        await ctx.send("Pomodore 타이머가 중지되었습니다.🍇")