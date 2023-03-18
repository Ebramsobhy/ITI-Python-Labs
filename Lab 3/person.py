class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.mood = 'sad'
        self.health_rate = '100%'

    def sleep(self, hours):
        if hours == 7:
            self.mood = 'happy'
        elif hours < 7:
            self.mood = 'tired'
        else:
            self.mood = 'lazy'

    def eat(self, meals):
        if meals == 3:
            self.health_rate = '100%'
        elif meals == 2:
            self.health_rate = '75%'
        elif meals == 1:
            self.health_rate = '50%'
        else:
            self.health_rate = '0%, You should visit the doctor!'

    def buy(self, items):
        self.money -= 10 * items

    def get_mood(self):
        return self.mood

    def get_health_rate(self):
        return self.health_rate
