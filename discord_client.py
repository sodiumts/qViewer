import discord
import asyncio
from datetime import datetime
from discord import app_commands

class MainClient(discord.Client):
    def __init__(self,intents, session):
        super().__init__(intents=intents)
        self.synced = False
        self.session = session
        self.rooms_message = None
        self.channel = None
        self.command_tree = app_commands.CommandTree(self)

        


    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            self.command_tree.sync()
            self.synced = True

        self.channel = self.get_channel(978241396714639374)
        self.loop.create_task(self.sendRepeatedUpdates())

    async def sendRepeatedUpdates(self):
        old_content = ""
        while True:
            room_data = self.session.getRooms()
            print(room_data)
            embed_contents = f"{room_data}"

            if old_content != embed_contents:
                message = await self.channel.send(content = "<@567065783499227137>")
                await message.delete()

            old_content = embed_contents

            await self.update_rooms_embed()
            await asyncio.sleep(10*60)

    async def update_rooms_embed(self):
        room_data = self.session.getRooms()
        embedContent = f"{room_data}"

        embed = discord.Embed(title="Rooms", description=embedContent, timestamp=datetime.now())
        if self.rooms_message:
            await self.rooms_message.edit(embed=embed)
        else:
            self.rooms_message = await self.channel.send(embed=embed)

        
        
        
        
