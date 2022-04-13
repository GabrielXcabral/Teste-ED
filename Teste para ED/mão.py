class Mão:
    def __init__(self, x):
        self.x = x
    
    def __str__(self):
        return "Contains {} cards".format(len(self.x))
    
    def remove(self):
        return self.x.pop()

    def adicionar_carta(self, add):
        return self.x.extend(add)
