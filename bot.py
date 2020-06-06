#Discord Bot
import discord
import json
import time
import asyncio
#WebScraping
import bs4 as bs
from urllib.request import Request, urlopen
import pickle
import os
import sys




#Discord Bot


class subscritions():

    with open('data_json\\bot_names_list.json', encoding = 'utf-8') as f:
        data = json.load(f)

    def __init__(self, username):
        self.username = username
    
    def subscribe(self):
        if self.username not in self.data["names"]:
            self.data["names"].append(self.username)
            with open('data_json\\bot_names_list.json', 'w', encoding = 'utf-8') as json_file:
                json.dump(self.data, json_file)
            return("Your username is now subscribed to BotG services! :star_struck: :partying_face:")
        else:
            return("Your username is already subscribed. :upside_down:")
            
    def unsubscribe(self):
        if self.username in self.data["names"]:
            self.data["names"].remove(self.username)
            with open('data_json\\bot_names_list.json', 'w', encoding = 'utf-8') as json_file:
                json.dump(self.data, json_file)
            return("Your username is no longer subscribed to BotG services. :pleading_face:")
        else:
            return("Your username is not subscribed to BotG services, consider doing with command !subscribe :smiling_face_with_3_hearts:")





with open('data_json\\bot_names_list.json', encoding = 'utf-8') as f:
    json_data = json.load(f)

active_members_list = json_data["names"]



def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
    

token = read_token()

client = discord.Client()


async def update_free_games_stats():
    await client.wait_until_ready()
    id = client.get_guild(143361209591136256)
    members = id.members

    while not client.is_closed():
        try:
            req = Request('https://www.indiegamebundles.com/category/free/', headers={'User-Agent': 'XYZ/3.0'})
            sauce = urlopen(req, timeout=10).read()
            soup = bs.BeautifulSoup(sauce,'lxml')

            with open('data_json\\last_free_games.json', encoding = 'utf-8') as f:
                last_games_dic = json.load(f)

            div = soup.find_all("div", {"class": "td-ss-main-content"})

            for element in div:
                row = element.find_all("div", {"class": "td_module_10 td_module_wrap td-animation-stack"})
                for h3 in row:
                    row_info = h3.find("h3", {"class": "entry-title td-module-title"}).find('a')
                    title = row_info.text.strip()
                    href_tag = row_info.get("href") 

                    if title not in last_games_dic:

                        if len(last_games_dic) > 10:
                            oldest_title = list(last_games_dic.keys())[0]
                            last_games_dic.pop(oldest_title)

                        last_games_dic.update([(title,href_tag)])

                        with open('data_json\\last_free_games.json', 'w', encoding = 'utf-8') as json_file:
                            json.dump(last_games_dic, json_file)
                        
                        for member in members:
                            if member.name in active_members_list:
                                embed = discord.Embed(title="New Free Game Available! :tada:", description=f"{title}")
                                # embed.add_field(name="More info at:", value=f"{href_tag}")
                                await member.send(content=None, embed=embed)
                                await member.send(f"{href_tag}")
                                # await member.send(f"""New Free Game Available! :tada: \n {title} \n More info at: \n {href_tag}""")

            await asyncio.sleep(21600)
        except Exception as e:
            print(e)




# my_files = [discord.File('img\\cool.png')]

@client.event
async def on_message(message):
    id = client.get_guild(143361209591136256)
    members = id.members

    if message.content == "!teste":
        await message.channel.send(f"Number of Members {id.member_count}")
        await message.author.send("DM")

        for member in members:
            if member.name in active_members_list:
                await member.send("Parabens, estás na lista de testes Hentai do BotG!")
    
    elif message.content == "!help":
        embed = discord.Embed(title="Help info BotG", description="BotG commands")
        embed.add_field(name="!subscribe", value="Subscribe to BotG Services")
        embed.add_field(name="!unsubscribe", value="Unsubscribe to BotG Services")
        await message.author.send(content=None, embed=embed)


    elif message.content == "!subscribe":
        user = subscritions(message.author.name)
        await message.author.send(user.subscribe())

    elif message.content == "!unsubscribe":
        user = subscritions(message.author.name)
        await message.author.send(user.unsubscribe())
        



client.loop.create_task(update_free_games_stats())

            

    





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


