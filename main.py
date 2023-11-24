from dotenv import dotenv_values
from discord_client import MainClient
import discord
from discord import app_commands
from DataScraper import DataScraper

config = dotenv_values(".env")

dataSession = DataScraper(providedCookie=config['COOKIE'], providedSessionToken=config["SESSION_TOKEN"])

intents = discord.Intents.default()


client = MainClient(intents=intents, session=dataSession)

command_tree = app_commands(client)

@command_tree.command(name="force_refresh", description = "Forces the bot to refresh the queue")
async def force_refresh(interaction):
    await client.update_rooms_embed()
    await interaction.response.send_message("Queue has been refreshed!", ephemeral = True)


client.run(config["BOT_TOKEN"])
