import discord.channel
from api.gamemode import AreaType
import yaml, time
from copy import deepcopy

class Area:
    def __init__(self, channel):
        db = yaml.safe_load(open(f"./database/areas/{channel}.yml"))

        self.name = db.get("name")
        self.description = db.get("description")
        self.channel_id = db.get("channel_id")
        self.entitys = db.get("entitys")
        self.battling = db.get("battling")
        self.type = AreaType[db.get("type")]
        self.nearby = db.get("nearby")
        self.area = channel

    def rehydrate(self):
        db = yaml.safe_load(open(f"./database/areas/{self.area}.yml"))

        self.name = db.get("name")
        self.description = db.get("description")
        self.channel_id = db.get("channel_id")
        self.entitys = db.get("entitys")
        self.battling = db.get("battling")
        self.type = AreaType[db.get("type")]
        self.nearby = db.get("nearby")

    def save_to_db(self):
        db = yaml.safe_load(open(f'./database/areas/{self.area}.yml'))

        area_dict = deepcopy(vars(self))

        area_dict['type'] = self.type.name

        db = area_dict

        with open(f"./database/areas/{self.area}.yml", "w") as f:
            yaml.dump(db, f)

    def save_enemy(self, enemy, id):
        if enemy.hp <= 0:
            self.battling.pop(id, None)

            enemy.hp = enemy.max_hp

            enemy.last_death = time.time()

            self.entitys[id] = deepcopy(vars(enemy))


        else:
            self.battling[id] = deepcopy(vars(enemy))
        