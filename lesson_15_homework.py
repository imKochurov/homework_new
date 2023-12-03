# TASK 1

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        return f"\nHello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old."
  
user1 = Person("DEN", "BROWN", 48)
user2 = Person("KLAUDIA", "SMITH", 34)

print(user1.talk(), user2.talk(), sep = "\n")


# TASK 2

class Dog:
    def __init__(self, dog_name, dog_age, age_factor=7):
        self.dog_name = dog_name
        self.dog_age = dog_age
        self.age_factor = age_factor

    def human_age(self):
        convert = self.dog_age*self.age_factor
        return f"\n{self.dog_name} has {convert} years in human equivalent"
    
dog1 = Dog("Kokos", 5)
dog2 = Dog("Marty", 3)

print(dog1.human_age(), dog2.human_age(), sep = '\n')


# TASK 3

class TVcontroller:
    channels = ["BBC", "Discovery", "National Geographik", "M1", "Hallmark"]
    def __init__(self, default_channel=0):
        self.default_channel = default_channel

    def first_channel(self):
        self.default_channel = 0
        return self.channels[self.default_channel]

    def last_channel(self):
        self.default_channel = self.channels.index(self.channels[-1]) # змінюємо канал по дефолту
        return self.channels[-1]
    
    def turn_channel(self, N:int):
        if N in range(1, len(self.channels)+1):
            self.default_channel = N-1 # змінюємо канал по дефолту
            return self.channels[N-1]
        else:
            return f"Channel num '{N}' not in list"
    
    def next_channel(self):
        if self.default_channel in range(0, len(self.channels)-1):
            self.default_channel = self.default_channel + 1
            return self.channels[self.default_channel]
        else:
            return f"Channel list is over"
        
    def previous_channel(self):
        if self.default_channel in range(1, len(self.channels)):
            self.default_channel = self.default_channel - 1
            return self.channels[self.default_channel]
        else:
            return f"Channel list is over"
        
    def current_channel(self):
        return self.channels[self.default_channel]
    
    def exists(self, name:str):
        if name in self.channels:
            return "Yes"
        else:
            return "No"
        
pult = TVcontroller() # створюємо ексемпляр - віртуальний пульт


print("\n", pult.channels) # список каналів

print(pult.turn_channel(3)) # вмикаємо 3 канал - National Geographik
print(pult.last_channel()) # перемикаємо на останній канал - Hallmark
print(pult.previous_channel()) # перемикаємо на попередній канал - M1
print(pult.first_channel()) # перемикаємо на перший канал - BBC
print(pult.next_channel()) # вмикаємо наступний канал - Discovery
print(pult.current_channel()) # виводимо назву поточного каналу - Discovery