class animal(object):
    def speak(self):
        print("动物的叫声")

class cat(animal):
    def speak(self):
        print("喵喵")

class dog(animal):
    def speak(self):
        print("汪汪")

def speak(object):
    object.speak()

kitty = cat()
kitty.speak()
speak(kitty)



