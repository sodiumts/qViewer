import discord
import asyncio
from datetime import datetime

class MainClient(discord.Client):
    def __init__(self,intents, session):
        super().__init__(intents=intents)
        self.synced = False
        self.session = session
        self.rooms_message = None


    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            # await tree.sync() #sync the commands to the server
            self.synced = True

        self.loop.create_task(self.sendRoomMessage())

    async def sendRoomMessage(self):
        channel = self.get_channel(978241396714639374)
        old_content = ""
        while True:
            rooms = self.session.getRooms()
            embedContent = f"{rooms}"
            
            embed = discord.Embed(title="Rooms", description=embedContent, timestamp=datetime.now())

            if old_content != embedContent:
                message = await channel.send(content = "<@567065783499227137>")
                await message.delete()
            

            if self.rooms_message:
                await self.rooms_message.edit(embed=embed)
            else:
                self.rooms_message = await channel.send(embed=embed)
            
            old_content = embedContent

            await asyncio.sleep(30)

