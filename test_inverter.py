from inverter import invert

def test_invert():
    assert invert('ameer') == 'reema'
    assert invert(None) == ''
    assert invert('') == ''
    assert invert(' ') == ' '
    assert invert('h') == 'h'
    assert invert(5) == 'Your input is not a string type!'
    assert invert(['1','2','3']) == 'Your input is not a string type!'
