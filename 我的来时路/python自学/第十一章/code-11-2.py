class Player(object):
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city

MBS = Player("MBS",20,'南京')
print(MBS.name,MBS.age,MBS.city)
print(MBS.__dict__)

class Role(object):
    def __init__(self,HP,ATK,DEF,SP,name):
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SP = SP
        self.name = name
Acheron = Role(1125,698,436,101,"Acheron")
Castorice = Role(1630,524,485,95,"Castorice")
print(Acheron.__dict__)
print(Castorice.__dict__)







