from dotenv import dotenv_values
from discord_client import MainClient
import discord

from DataScraper import DataScraper

config = dotenv_values(".env")

dataSession = DataScraper(providedCookie=config['COOKIE'], providedSessionToken=config["SESSION_TOKEN"])

intents = discord.Intents.default()

client = MainClient(intents=intents, session=dataSession)

client.run(config["BOT_TOKEN"])
