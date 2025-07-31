# Ломать — не строить 2

class Error:
    def __repr__(self):
        raise Exception


func(Error())
