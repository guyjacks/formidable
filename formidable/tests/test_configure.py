from formidable import Formidable


def test_config_from_python_dict():
    config = [
        {
            'name': 'field_name',
            'type': 'text',
            'must_be_present': True,
            'rules': [
                'value_is_required'
            ]
        }
    ]

    form = Formidable()
    form.configure(config)
    assert form.field_name['type'] == 'text'
    assert form.field_name['must_be_present'] == True
    assert form.field_name['rules'][0] == 'value_is_required'
