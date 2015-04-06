from formidable import value_is_required


def test_value_is_required():
    field = "field"
    value = ""
    message = "test"
    valid, resp = value_is_required(field, value, message)
    assert valid == False
    assert resp['message'] == 'test'
