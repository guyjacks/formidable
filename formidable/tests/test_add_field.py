from formidable import Formidable


def test_add_field():
    form = Formidable()
    field = {
        'name': 'field_name',
        'type': 'text',
        'rules': [
            'value_is_required',
            'field_must_be_present'
        ]
    }

    form.add_field(field)
    assert form.field_name['type'] == 'text'
    assert form.field_name['rules'][0] == 'value_is_required'
    assert form.field_name['rules'][1] == 'field_must_be_present'
