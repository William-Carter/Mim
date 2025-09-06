import interactions
import interactions.ext.prefixed_commands as pc
import os
import json
import re

dirPath = os.path.dirname(os.path.realpath(__file__))

bot = interactions.Client(intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MEMBERS | interactions.Intents.MESSAGE_CONTENT, send_command_tracebacks=False, fetch_members=False)


@interactions.listen()
async def on_startup():
    print("Bot is ready!")
    print("Bot is in:")
    for guild in bot.guilds:
        print(guild.name, guild.id)


@interactions.listen()
async def on_command_error(event: interactions.events.CommandError):
    await event.ctx.send("Encountered an error!")

pc.setup(bot, default_prefix = "!!") 
names = []

for item in os.scandir(dirPath+"/answers/"):
    if os.path.isfile(f"answers/{item.name}"):
        with open(f"answers/{item.name}", "r", encoding="utf-8") as f:
            first_line = f.readline()
            second_line = f.readline()
            # Extract the name from the HTML comment on the first line
            match = re.match(r"\s*<!--\s*(.*?)\s*-->\s*", first_line)
            name = match.group(1) if match else ""
            match = re.match(r"\s*<!--\s*(.*?)\s*-->\s*", second_line)
            description = match.group(1) if match else ""
            names.append({"name": name, "description": description})
            content = f.read()
            command = f"""
@pc.prefixed_command(name="{name}")
async def {name}(ctx: pc.PrefixedContext):
    await ctx.send(\"\"\"{content}\"\"\")
            """
            exec(command, globals())

        
@pc.prefixed_command(name="list")
async def list_commands(ctx: pc.PrefixedContext):
    response = "Available commands:\n"
    for item in names:
        response += f"**!!{item['name']}** - {item['description']}\n"
    await ctx.send(response)
        



# Load bot token from config file
with open(dirPath+"/config.json", "r") as f:
    data = json.load(f)
    token = data["token"]

bot.start(token)