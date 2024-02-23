class Animal:
    def __init__(self, type_of_animal=None) -> None:
        home_address = "9 Knoll Road"
        
        if type_of_animal is not None:
            self.type_of_animal = type_of_animal
        else:
            self.type_of_animal = "cat"
        self.name = "tommy"
        self.color = "white"

    def display_name(self):
        MY_NAME = self.name
        MY_COLOR = self.color
        MY_TYPE_OF_ANIMAL = self.type_of_animal

        print(MY_NAME + ": " + MY_COLOR + " " + MY_TYPE_OF_ANIMAL)

        return None


a = Animal()
a.display_name()

b = Animal("dog")
b.display_name()
