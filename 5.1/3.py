# Не нажимай красную кнопку!

class RedButton:
    cnt = 0

    def click(self):
        self.cnt += 1
        print("Тревога!")

    def count(self):
        return self.cnt