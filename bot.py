import discord
import json


class subscritions():

    with open('bot_names_list.json', encoding = 'utf-8') as f:
        data = json.load(f)

    def __init__(self, username):
        self.username = username
    
    def subscribe(self):
        if self.username not in self.data["names"]:
            self.data["names"].append(self.username)
            with open('bot_names_list.json', 'w', encoding = 'utf-8') as json_file:
                json.dump(self.data, json_file)
            return("Your username is now subscribed to BotG services! :star_struck: :partying_face:")
        else:
            return("Your username is already subscribed. :upside_down:")
            
    def unsubscribe(self):
        if self.username in self.data["names"]:
            self.data["names"].remove(self.username)
            with open('bot_names_list.json', 'w', encoding = 'utf-8') as json_file:
                json.dump(self.data, json_file)
            return("Your username is no longer subscribed to BotG services. :pleading_face:")
        else:
            return("Your username is not subscribed to BotG services, consider doing with command !subscribe :smiling_face_with_3_hearts:")







with open('bot_names_list.json', encoding = 'utf-8') as f:
    json_data = json.load(f)

active_members_list = json_data["names"]



def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
    

token = read_token()

client = discord.Client()


my_files = [discord.File('img\\cool.png')]

@client.event
async def on_message(message):
    id = client.get_guild(143361209591136256)
    members = id.members

    if message.content == "!":
        await message.channel.send(f"Number of Members {id.member_count}")
        await message.author.send("DM")

        for member in members:
            if member.name in active_members_list:
                await member.send("Parabens, estás na lista de testes Hentai do BotG!")

    elif message.content == "!subscribe":
        user = subscritions(message.author.name)
        await message.author.send(user.subscribe())

    elif message.content == "!unsubscribe":
        user = subscritions(message.author.name)
        await message.author.send(user.unsubscribe())
        





            

    





    # OTHER USEFULL EXAMPLES


    # channels = ["420blazeit"]

    # if str(message.channel) in channels:
    #     if message.content == "!users":
    #         # print(message.author)
    #         await message.channel.send(f"Number of Members {id.member_count}")


    # print(message.content)
    # if message.content.find("!hello") != -1:
    #     await message.channel.send("Hi bitch")
    
    # if message.content.find("!jimmy") != -1:
    #     await message.channel.send('Here is Jimmy:', files=my_files)


    
client.run(token)


