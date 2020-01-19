"""
The memento design pattern is made up of three components:
1) the originator, which has state that changes over time and may be reset back to a state at a previous point in time.
2) the memento(s), which are data encoding the state the object should return to
3) the caretaker, which holds onto memento on behalf of the originator.

Memento could be as simple as an integer value representing an enum state. Or they could be as complicated as a full
copy of the object itself. They could be anything, so long as the memento can return the original object back to the
state of the object when the memento was created. In this way, a memento is just a time snapshot of the object.
"""


class Memento(object):
    """
    A memento is the information needed ot return an object back to its previous state.
    """
    def __init__(self, field1: int, field2: str):
        self.field1 = field1
        self.field2 = field2


class Originator(object):
    """
    The Originator is the object whose state changes and is (possibly) later reset at the request of the caretaker
    """
    def __init__(self, field1: int, field2: str):
        self.field1 = field1
        self.field2 = field2

    def produce_memento(self) -> Memento:
        return Memento(self.field1, self.field2)

    def ingest_memento(self, memento: Memento):
        self.field1 = memento.field1
        self.field2 = memento.field2


class Caretaker(object):
    """
    The Caretaker object requests and stores mementos from the originator. Eventually it may give the memento back
    to the originator and request that the originator return to its previous state.
    """
    def __init__(self, originator: Originator):
        self.originator = originator
        self.snapshots = []

    def save_snapshot(self):
        self.snapshots.append(self.originator.produce_memento())

    def restore_snapshot(self):
        self.originator.ingest_memento(self.snapshots.pop(-1))
