from design_patterns import builder

def test_end_to_end():
    director = builder.Director(builder.LongSwordBuilder())
    longsword = director.construct()
    director2 = builder.Director(builder.GladiusBuilder())
    gladius = director2.construct()
    assert longsword.type == "Longsword"
    assert gladius.type == "Gladius"
    print(longsword)
    print(gladius)
