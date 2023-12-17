class Animal:

    def __init__(self, name, age, sex, date_of_birth):
        self.name = name
        self.age = age
        self.sex = sex
        self.date_of_birth = date_of_birth

    def run(self):
        print("I can run faster, than you!")

    def scratch(self):
        print('scratching')

    def voice(self):
        print("there is some voice of animal here")

    def jump(self):
        return 'Jump!'

    def get_info(self):
        FEMALE = 'женский', 'Женский'

        if self.sex == FEMALE:
            print(f"Привет!\n"
                  f"Моя кличка: {self.name}!\n"
                  f"Мой пол: {self.sex}\n"
                  f"Мне {self.age} лет.\n" 
                  f"Я родилась {self.date_of_birth}г.\n")
        else:
            print(f"Привет!\n"
                  f"Моя кличка: {self.name}!\n"
                  f"Мой пол: {self.sex}\n"
                  f"Мне {self.age} лет.\n"
                  f"Я родился {self.date_of_birth}г.\n")



barsik = Animal('Барсик', 10, 'мужской', "01.01.1998")
barsik.get_info()

murzik = Animal('Мурзик', 11, 'мужской', '02.03.1997')
murzik.get_info()

animal_snezhok = Animal('Снежок', 7, 'мужской', '03.05.2001')
animal_snezhok.get_info()

animal_snezhana = Animal('Снежана', 6, 'женский', '04.06.2002')
animal_snezhana.get_info()
