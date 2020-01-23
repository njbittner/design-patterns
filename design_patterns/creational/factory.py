from abc import ABCMeta, abstractmethod


class Duck(object):
    __metaclass__ = ABCMeta
    state = "not smiling"

    @abstractmethod
    def quack(self): pass

    @abstractmethod
    def fly(self): pass

    def smile(self):
        self.state = "smiling"

    def stop_smiling(self):
        self.state = "not smiling"


class TeenageDuck(Duck):
    def quack(self):
        return "you can't make me"

    def fly(self):
        return "ugh."


class RubberDuck(Duck):
    def quack(self):
        return "squeak"

    def fly(self):
        return "..."



class DuckFactory(object):
    duck_types = {
        "rubber": RubberDuck,
        "teen": TeenageDuck
    }
    @staticmethod
    def make_duck(duck_type):
        return DuckFactory.duck_types[duck_type]()
