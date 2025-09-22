import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("🤖 Bot {bot.user} está online!")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

@bot.command()
async def ola(ctx):
    await ctx.send("Olá, {ctx.author.mention}! 👋")

@bot.command()
async def ajuda(ctx):
    ajuda_texto = """
**Lista de comandos disponíveis:**
- `!ping` → Responde com Pong!
- `!ola` → O bot cumprimenta você
- `!ajuda` → Mostra esta mensagem
"""
    await ctx.send(ajuda_texto)

if __name__ == "__main__":
    TOKEN = "MTQxOTc5NTc1NTg5MTQyNTMzMg.G0DwEk.ukCZc1vYzOIiJT9mze6ZPDjoyn7Uj2s_US90q8"  
    bot.run(TOKEN)
