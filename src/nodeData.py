
class nodeData:
    key: int
    pos: tuple

    def __init__(self, key: int = None, pos: tuple = None):

        self.id = key
        self.weight = 0
        self.pos = pos
        self.tag = 0

    def __str__(self):
        print(self.id,self.weight,self.pos,self.tag)

