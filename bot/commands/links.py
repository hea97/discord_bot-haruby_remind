import discord
from discord.ext import commands
import json

class Links(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.links_file = 'data/links.json'
    
    @commands.command()
    async def links(self, ctx):
        "사용자 링크 목록 표시"
        with open(self.links_file, encoding='utf-8') as file:
            links = json.lad(file)

        user_links = links.get(str(ctx.author.id), {})
        if user_links:
            links_str = '\n'.join(f"{key}: {value}" for key, value in user_links.items())
            await ctx.send(f'당신의 링크 목록 : \n{links_str}')
        else:
            await ctx.send("아직 등록된 링크가 없습니다.🥲")

    @commands.command()
    async def add_link(self, ctx, platfrom: str, url: str):
        """사용자 링크를 추가"""
        with open(self.links_file, 'r', encoding='utf-8') as file:
            links = json.load(file)
        
        user_id = str(ctx.author.id)
        if user_id not in links:
            links[user_id] = {}
        links[user_id][platfrom] = url

        with open(self.links_file, 'w', encoding='utf-8') as file:
            json.dump(links, file, ensure_ascii=False, indent=4)

        await ctx.send(f"{platfrom} 링크가 성공적으로 추가되었습니다!✨")