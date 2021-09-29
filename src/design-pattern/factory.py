

class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "worf"


class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "meow"


def get_pet(pet="dog"):

    pet_dict = {
        "dog": Dog("tomy"),
        "cat": Cat("jimmy")
    }
    return pet_dict[pet]


if __name__ == '__main__':
    d = get_pet("dog")
    print(d.speak())

    c = get_pet("cat")
    print(c.speak())






