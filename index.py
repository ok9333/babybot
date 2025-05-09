from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext import commands
import discord
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
scheduler = AsyncIOScheduler()

@bot.event
async def on_ready():
    print(f"✅ 봇 온라인: {bot.user}")
    print(f"시스템 준비완료: {bot.user}")
    
    scheduler.start()

    scheduler.add_job(send_alert, 'cron', hour=5, minute=55, args=["⏰ 결계 5분 전입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=6, minute=00, args=["⏰ 결계 출현 중입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=8, minute=55, args=["⏰ 결계 5분 전입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=9, minute=00, args=["⏰ 결계 출현 중입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=11, minute=55, args=["⏰ 결계 5분 전입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=12, minute=00, args=["⏰ 결계 출현 중입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=14, minute=55, args=["⏰ 결계 5분 전입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=15, minute=00, args=["⏰ 결계 출현 중입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=17, minute=55, args=["⏰ 결계 5분 전입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=18, minute=00, args=["⏰ 결계 출현 중입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=20, minute=55, args=["⏰ 결계 5분 전입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=21, minute=00, args=["⏰ 결계 출현 중입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=23, minute=55, args=["⏰ 결계 5분 전입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=00, minute=00, args=["⏰ 결계 출현 중입니다!"], timezone='Asia/Seoul')

   
    scheduler.add_job(send_alert, 'cron', hour=11, minute=55, args=["⚔️ 필드보스 5분 전입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=12, minute=00, args=["⚔️ 필드보스 출현 중입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=17, minute=55, args=["⚔️ 필드보스 5분 전입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=18, minute=00, args=["⚔️ 필드보스 출현 중입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=19, minute=55, args=["⚔️ 필드보스 5분 전입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=20, minute=00, args=["⚔️ 필드보스 출현 중입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=21, minute=55, args=["⚔️ 필드보스 5분 전입니다!"], timezone='Asia/Seoul')
    scheduler.add_job(send_alert, 'cron', hour=22, minute=00, args=["⚔️ 필드보스 출현 중입니다!"], timezone='Asia/Seoul')

@bot.command()
async def 테스트(ctx):
    await ctx.send("✅ 시스템 정상가동 준비완료")

async def send_alert(message):
    channel = bot.get_channel(1370382522990723226)  # 채널 ID
    if channel and channel.guild.id == 1358037717023326269:  # 서버 ID
        await channel.send(message)

access_token = os.environ["BOT_TOKEN"]
bot.run("access_token")
