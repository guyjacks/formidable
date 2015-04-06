from formidable import Formidable


def test_add_validator():
    form = Formidable()
    form.add_validator('validator', validator)
    assert form.validators['validator'] == validator
    valid, resp = form.validators['validator']('field', 'value')
    assert valid is False
    assert resp['test'] == 'test'


def validator(field, value):
    return False, {'test': 'test'}
