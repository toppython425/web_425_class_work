class Hero:
    available_classes = ["рейнджер", "воин", "маг"]
    ranger_skill_list = ['быстрая стрельба', 'скрытность']
    warrior_skill_list = ['сокрушительный удар', 'вой']
    mage_skill_list = ['огненный шар', 'барьер']
    party_list = []

    def __init__(self, name, hero_class):
        self.name = name
        if hero_class in self.available_classes:
            self.hero_class = hero_class
        else:
            self.hero_class = 'воин'
        self.level = 0
        self.exp = 0
        self.available_skills = []
        self.skill_list = []

    def add_available_skills(self):
        if self.hero_class == "рейнджер":
            self.available_skills = self.ranger_skill_list.copy()
        elif self.hero_class == "воин":
            self.available_skills = list(self.warrior_skill_list)
        else:
            self.available_skills = self.mage_skill_list[:]

    def add_exp(self, exp):
        self.exp += exp
        if self.exp >= 1000:
            self.level = 3
        elif self.exp >= 500:
            self.level = 2
            self.add_skill()
        elif self.exp >= 200:
            self.level = 1
            self.add_skill()
        return f"Герой {self.name} получил {exp} очков опыта!\nЕго уровень теперь {self.level}\nНавыки {', '.join(self.skill_list)}"

    def add_skill(self):
        skill = input(f'Вы повысили свой уровень, выберете навык {', '.join(self.available_skills)}: ')
        while skill not in self.available_skills:
            print("Неподходящий навык")
            skill = input(f'Вы повысили свой уровень, выберете навык {', '.join(self.available_skills)}: ')
        self.skill_list.append(skill)
        self.available_skills.remove(skill)
        return f'Герой {self.name} получает навык {skill}'

    def add_to_party(self):
        self.party_list.append(self)
        return f"{self.name} добавлен в команду"

    def remove_from_party(self):
        self.party_list.remove(self)
        return f"{self.name} исключен из команду"

    @classmethod
    def get_party_list(cls):
        return cls.party_list


ranger = Hero("Леголас", "рейнджер")
ranger.add_available_skills()
print(ranger.add_exp(250))
print(ranger.add_exp(250))
print(ranger.add_to_party())

ranger1 = Hero("Арагорн", "рейнджер")
ranger1.add_available_skills()
print(ranger1.add_exp(250))
print(ranger1.add_exp(250))
print(ranger1.add_to_party())

warrior = Hero("Гимли", "воин")
warrior.add_available_skills()
print(warrior.add_exp(250))
print(warrior.add_exp(250))
print(warrior.add_to_party())

print(Hero.party_list)
print(warrior.remove_from_party())
print(Hero.party_list)
