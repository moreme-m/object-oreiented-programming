class Dogs:
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed

    def introduce(self):
        print("The name of my dog is ", self.name)

    def read(self):
        print("The color of my dog is ", self.color)


dog1 = Dogs("Bingo", "brown", "poodle")
dog2 = Dogs("Bluey", "white", "German shephard")

print("My best dog is ", dog2.name)