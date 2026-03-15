class Role(object):
    number = 0
    def __init__(self,HP,ATK,DEF,SP,name):
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SP = SP
        self.name = name
        Role.number += 1

Acheron = Role(1125,698,436,101,"Acheron")
print(Acheron.__dict__,"您的UID是%d号" % Acheron.number)
Castorice = Role(1630,524,485,95,"Castorice")
print(Castorice.__dict__,"您的UID是%d号" % Castorice.number)


