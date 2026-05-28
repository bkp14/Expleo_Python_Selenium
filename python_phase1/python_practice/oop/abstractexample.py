from abc import ABC,abstractmethod
class base(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class dog(base):
    def make_sound(self):
        return "woof"
class cat(base):
    def make_sound(self):
        return "meow"
c=cat()
d=dog()
print(c.make_sound())
print(d.make_sound())    
