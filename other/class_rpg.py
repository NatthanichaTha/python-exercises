from random import randint

class NPC:
    def __init__(self, type, gender, name):
        self.type = type
        self.gender = gender
        self.name = name
    
    def talk(self):
        if self.type == "human":
            print(self.name.upper()+":"+" Hello!")
        elif self.type == "orc":
            print(self.name.upper()+":"+" Waaaaah!")

TYPES = ["human", "orc"]
GENDERS = ["m", "f"]
NAMES = ["pepo", "pasasa", "maria", "anna"]

npc_list = []

for i in range(10):
    type_idx = randint(0, len(TYPES)-1)
    gender_idx = randint(0, len(GENDERS)-1)
    name_idx = randint(0, len(NAMES)-1)

    npc_list.append(NPC(TYPES[type_idx], GENDERS[gender_idx], NAMES[name_idx]))
    npc_list[i].talk()
