class Warrior():

    def __init__(self,name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep (self):
        print(f"{self.name} лег спать")
        self.endurance += 2


    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1


    def hit(self):
        print(f"{self.name} бьет кого-то")
        self.endurance -= 1


    def wolk (self):
        print(f"{self.name} гуляет")


    def info(self):
        print(f"имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_color}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")

war1 = Warrior (name='Марк',power=30,endurance=10,hair_color='Красные')
war2 = Warrior (name='Степашка',power=76, endurance=77,hair_color='Белые')
war2.info()

war2.sleep()
war2.wolk()
war2.eat()

war2.info()
