# For Sullivan 2019 Pycon "FUN CODE" contest
from abc import abstractmethod, ABC
from dataclasses import dataclass

# Sorry, I don't know Korean language
# I'm pretty sure that the metaprogramming example is useless  and people shouldn't write like this
# The example can run normally without runtime example

_ = type('', (), dict(__getattr__=lambda s, _: s))()
_.d = dataclass
_.a = abstractmethod


@_._._._._.d
class Coordinates:
    x: float
    y: float


class Connection(ABC):
    @_._._.a
    def open(self):
        ...

    @_._._.a
    def close(self):
        ...
