from dotenv import dotenv_values
from discord_client import MainClient
import discord
from DataScraper import DataScraper

config = dotenv_values(".env")

dataSession = DataScraper(providedCookie=config['COOKIE'], providedSessionToken=config["SESSION_TOKEN"])

intents = discord.Intents.default()


client = MainClient(intents=intents, session=dataSession)


@client.command_tree.command(name="force_refresh", description = "Forces the bot to refresh the queue")
async def force_refresh(interaction:discord.Interaction):
    await client.update_rooms_embed()
    await interaction.response.send_message("Queue has been refreshed!", ephemeral = True)


@client.command_tree.command(name="auth")
async def update_tokens(interaction:discord.Interaction, cookie:str, token:str):
    result = await client.session.setTokenCookie(cookie, token)
    if result:
        await interaction.response.send_message("Tokens have been updated", ephemeral = True)
    else:
        await interaction.response.send_message("Invalid tokens", ephemeral = True)


client.run(config["BOT_TOKEN"])
