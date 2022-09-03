person_count = 1
class person:
    count = 1

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.count += 1

taro = person('taro',20)
print(person_count)
#yamada = person_count('yamada',30)
print(taro.count)
class Charcter:
    race = "基本クラス"
    def __init__(self,name):
        self.name = name

    def show_profile(self):
        print(f'名前:{self.name}種族:{self.race}')
class Fencor(Charcter):
    race ="剣士"
class Fighter(Charcter):
    race ="戦士"
taro = Fighter("taro")
taro.show_profile()
jiro = Fencor("jiro")
jiro.show_profile()