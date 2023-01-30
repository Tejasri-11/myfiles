#abstract class
#handling info by hiding informal or unnecessary info of the user.
class fruits:
    def taste(self):
        raise NotImplementedError()
    def rich(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()
class mango(fruits):
    def taste(self):
        return "sweet"
    def rich(self):
        return "vitamin A"
    def color(self):
        return "yellow"
class orange(fruits):
    def taste(self):
        return "sweet"
    def rich(self):
        return "vitamin c"
    def color(self):
        return "orange"
Alphanso= mango()
print(Alphanso.taste(),Alphanso.rich(),Alphanso.color())
orange=orange()
print(orange.taste(),orange.rich(),orange.color())

