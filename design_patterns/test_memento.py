import pytest
from design_patterns import memento

FIELD1 = 42
FIELD2 = "mu"


@pytest.fixture
def caretaker_originator_pair():
    originator = memento.Originator(FIELD1, FIELD2)
    caretaker = memento.Caretaker(originator)
    return originator, caretaker


def test_basic(caretaker_originator_pair):
    originator, caretaker = caretaker_originator_pair
    caretaker.save_snapshot()
    originator.field2 = "asdf"
    originator.field1 = 35
    caretaker.restore_snapshot()
    assert originator.field1 == FIELD1
    assert originator.field2 == FIELD2





