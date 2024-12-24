import discord
from discord.ext import commands
import json

# /links 명령어로 유용한 사이트 보고, 추가/삭제 할 수 있게 처리리
@commands.command()
async def links(ctx):
    try:
        with open('data/links.json', 'r') as f:
            links = json.load(f)
        await ctx.send("\n", join([f"{platform}: {url}"for platform, url in links.items()]))
    except FileNotFoundError:
        await ctx.send("추가되지 않은 링크 입니다. 링크를 추가해 주세요!")

# /add_link 명령어로 유용한 사이트를 추가가
@commands.command()
async def add_link(ctx, platform: str, url: str):
    try:
        with open('data/links.json', 'r') as f:
            links = json.load(f)
    except FileNotFoundError:
        links = {}

    links[platform] = url
    with open('data/links.json', 'w') as f:
        json.dump(links, f, indent=4)
    
    await ctx.send(f"{platform}에 대한 링크가 추가되었습니다: {url}")

# /remove_link 명령어로 유용한 사이트를 삭제
@commands.command()
async def remove_link(ctx, platform: str):
    try:
        with open('data/links.json', 'r') as f:
            links = json.load(f)
        if platform in links:
            del links[platform]
            with open('data/links.json', 'w') as f:
                json.dump(links, f, indent=4)
            await ctx.send(f"{platform}에 대한 링크가 삭제되었습니다.")
        else:
            await ctx.send(f"{platform} 링크가 존재하지 않습니다.")
    except FileNotFoundError:
        await ctx.send("링크 데이터가 없습니다. 링크를 추가해 주세요!")