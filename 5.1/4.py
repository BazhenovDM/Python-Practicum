# Работа не волк

class Programmer:
    hours = 0
    money = 0
    post_standarts = {
        "Junior": 10,
        "Middle": 15,
        "Senior": 20,
    }

    def __init__(self, name: str, post: str):
        self.name = name
        self.post = post

    def work(self, time: int):
        self.hours += time
        self.money += self.post_standarts[self.post] * time

    def rise(self):
        match self.post:
            case "Junior":
                self.post = "Middle"
            case "Middle":
                self.post = "Senior"
            case "Senior":
                self.post_standarts["Senior"] += 1

    def info(self):
        return f"{self.name} {self.hours}ч. {self.money}тгр."
