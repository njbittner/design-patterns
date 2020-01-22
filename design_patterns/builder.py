from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class Pommel(object):
    weight: float
    shape: str

    def __str__(self):
        return f"a {self.shape} pommel"


@dataclass
class Quillion(object):
    weight: float
    style: str

    def __str__(self):
        return f"a {self.style}-style crossguard"


@dataclass
class Blade(object):
    length: int
    weight: float
    ridge_style: str

    def __str__(self):
        return f"a {self.length} cm {self.ridge_style} blade"


class Sword(object):
    pommel: Pommel
    quillion: Quillion
    blade: Blade
    type: str

    @property
    def weight(self):
        return sum([x.weight for x in [self.pommel, self.quillion, self.blade]])

    def __str__(self):
        return f"A {self.type} sword weighing {self.weight} kg with {self.blade}, {self.quillion} and {self.pommel}"


class AbstractSwordBuilder:
    ___metaclass__ = ABCMeta
    sword: Sword

    @abstractmethod
    def build_pommel(self) -> None: pass

    @abstractmethod
    def build_quillion(self) -> None: pass

    @abstractmethod
    def build_blade(self) -> None: pass

    @abstractmethod
    def get_result(self) -> Sword: pass


class LongSwordBuilder(AbstractSwordBuilder):
    def __init__(self):
        self.sword = Sword()
        self.sword.type = "Longsword"

    def build_blade(self) -> None:
        self.sword.blade = Blade(length=98, weight=1.5, ridge_style="beveled")

    def build_pommel(self) -> None:
        self.sword.pommel = Pommel(weight=0.7, shape="perfume-cap")

    def build_quillion(self) -> None:
        self.sword.quillion = Quillion(weight=0.3, style="straight")

    def get_result(self) -> Sword:
        return self.sword


class GladiusBuilder(AbstractSwordBuilder):
    def __init__(self):
        self.sword = Sword()
        self.sword.type = "Gladius"

    def build_blade(self) -> None:
        self.sword.blade = Blade(length=80, weight=0.7, ridge_style="beveled")

    def build_pommel(self) -> None:
        self.sword.pommel = Pommel(weight=0.2, shape="round")

    def build_quillion(self) -> None:
        self.sword.quillion = Quillion(weight=0.1, style="stub")

    def get_result(self) -> Sword:
        return self.sword


class Director(object):
    def __init__(self, builder: AbstractSwordBuilder):
        self._builder = builder

    def construct(self) -> Sword:
        self._builder.build_pommel()
        self._builder.build_quillion()
        self._builder.build_blade()
        return self._builder.get_result()
