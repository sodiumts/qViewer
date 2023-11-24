import discord
import asyncio
from datetime import datetime

class MainClient(discord.Client):
    def __init__(self,intents, session):
        super().__init__(intents=intents)
        self.synced = False
        self.session = session
        self.rooms_message = None
        self.channel = None
        self.command_tree = command_tree
        


    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await self.command_tree.sync() #sync the commands to the server
            self.synced = True

        self.channel = self.get_channel(978241396714639374)
        self.loop.create_task(self.sendRepeatedUpdates())

    async def sendRepeatedUpdates(self):
        old_content = ""
        while True:
            room_data = await self.get_rooms()
            embed_contents = f"{room_data}"

            if old_content != embed_contents:
                message = await self.channel.send(content = "<@567065783499227137>")
                await message.delete()

            old_content = embed_contents

            await self.update_rooms_embed()
            await asyncio.sleep(10*60)

    async def update_rooms_embed(self):
        rooms = self.session.getRooms()
        embedContent = f"{rooms}"

        embed = discord.Embed(title="Rooms", description=embedContent, timestamp=datetime.now())
        if self.rooms_message:
            await self.rooms_message.edit(embed=embed)
        else:
            self.rooms_message = await self.channel.send(embed=embed)

        
        
        
        
