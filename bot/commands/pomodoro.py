import discord
from discord.ext import commands, tasks
import asyncio
import time

# Pomodoro 타이머 실행 여부 확인
is_pomodoro_running = False
pomodoro_start_time = None

# /pomodoro 명령어로 Pomodoro 타이머 시작
@commands.command()
async def pomodoro(ctx):
    global is_pomodoro_running, pomodoro_start_time
    
    if is_pomodoro_running:
        await ctx.send("타이머가 이미 실행 중입니다. 강제로 종료하려면 '/stop_pomodoro'를 입력하세요.")
        return
    
    # 사용자에게 타이머 시작 여부 물어보기
    await ctx.send("Pomodoro 타이머를 시작할까요? (yes/no)")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() in ['yes', 'no']

    try:
        msg = await bot.wait_for('message', check=check, timeout=30.0)  # 30초 내로 응답 받기
        if msg.content.lower() == 'yes':
            is_pomodoro_running = True
            pomodoro_start_time = time.time()  # 타이머 시작 시간 기록
            await ctx.send("Pomodoro 타이머 시작! 25분 집중 후 5분 휴식!")

            # 25분 공부
            for i in range(25):
                if not is_pomodoro_running:
                    await ctx.send("Pomodoro 타이머가 강제 종료되었습니다.")
                    break
                await asyncio.sleep(60)  # 1분마다 반복
                await ctx.send(f'{i+1}분 경과...')

            # 5분 휴식
            if is_pomodoro_running:
                await ctx.send("25분 공부 끝! 5분 휴식 시작!")
                for i in range(5):
                    if not is_pomodoro_running:
                        await ctx.send("Pomodoro 타이머가 강제 종료되었습니다.")
                        break
                    await asyncio.sleep(60)  # 1분마다 반복
                    await ctx.send(f'{i+1}분 경과... 휴식 중')

            # 타이머 종료 후 피드백
            if is_pomodoro_running:
                is_pomodoro_running = False
                focus_time = int((time.time() - pomodoro_start_time) / 60)  # 집중 시간 계산 (분 단위)
                if focus_time < 25:
                    await ctx.send(f"{focus_time}분 동안 집중했어요! 다음에는 좀 더 집중해봐요.")
                else:
                    await ctx.send(f"멋져요! {focus_time}분 동안 꾸준히 집중했어요! 계속 이런 식으로 해보세요.")
        else:
            await ctx.send("Pomodoro 타이머가 취소되었습니다.")
    except asyncio.TimeoutError:
        await ctx.send("시간 초과! 명령어에 대한 응답이 없어서 타이머를 시작하지 않습니다.")

# /stop_pomodoro 명령어로 강제 종료
@commands.command()
async def stop_pomodoro(ctx):
    global is_pomodoro_running, pomodoro_start_time
    
    if is_pomodoro_running:
        focus_time = int((time.time() - pomodoro_start_time) / 60)  # 강제 종료 시 집중 시간 계산
        is_pomodoro_running = False
        await ctx.send("Pomodoro 타이머가 강제 종료되었습니다.")
        
        # 강제 종료 후 피드백
        if focus_time < 25:
            await ctx.send(f"{focus_time}분 동안 집중했어요! 다음에는 좀 더 집중해봐요.")
        else:
            await ctx.send(f"멋져요! {focus_time}분 동안 꾸준히 집중했어요! 계속 이런 식으로 해보세요.")
    else:
        await ctx.send("현재 실행 중인 Pomodoro 타이머가 없습니다.")
