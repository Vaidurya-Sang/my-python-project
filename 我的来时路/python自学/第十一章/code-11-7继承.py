class Role(object):
    number = 1
    all_role_ATK = []

    def __init__(self,HP,ATK,DEF,SP,name):
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.SP = SP
        self.name = name
        self.level = 1
        self.UID = Role.number
        Role.number += 1
        Role.all_role_ATK.append(self.ATK)

    def promote(self):
        self.HP = self.HP + 200
        self.ATK = self.ATK + 200
        self.DEF = self.DEF + 200
        print("已晋级")

    def level_up(self):
        try:
            if self.level <20:
                if self.level %10 != 0:
                    self.level += 1
                    self.HP += 100
                    self.ATK += 100
                    self.DEF += 100
                else:
                    Role.promote(self)
                    self.level += 1
            else:
                raise Exception("已满级")
        except Exception as e:
            print(e)


    def show(self):
        print(self.__dict__)

class _special(Role):
    def __init__(self,HP,ATK,DEF,SP,name,status):
        super().__init__(HP,ATK,DEF,SP,name)
        self.status = status
    def show(self):
        print(self.__dict__)

Acheron = _special(1125,698,436,101,"Acheron","emanator")
Acheron.show()

