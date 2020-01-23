import factory


def test_duck_factory():
    duck_factory = factory.DuckFactory()
    teen_duck = duck_factory.make_duck("teen")
    rubber_duck = duck_factory.make_duck("rubber")
    for duck in [teen_duck, rubber_duck]:
        duck.quack()
        duck.fly()
        duck.smile()
        duck.stop_smiling()


