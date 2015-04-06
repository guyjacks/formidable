from formidable import Formidable


def test_load_data():
    config = [
        {
            'name': 'field_name',
            'type': 'text'
        }
    ]
    form = Formidable(config=config)
    data = [
        {'field_name': 'user input'}
    ]
    form.load_data(data)
    assert form.field_name['data'] == 'user input'
