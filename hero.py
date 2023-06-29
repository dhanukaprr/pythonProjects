class Hero:
    def __init__(self, name, attribute, role):
        self. name = "Sven"
        self.attribute = "Strength"
        self.role = "Carry"
    def __str__(self):
        return ("{} is a {} {} hero".format (self.name, self.attribute, self.role))

hero1 = Hero("Sven","Strength","Carry")
print(hero1)

