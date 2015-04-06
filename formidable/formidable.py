class Formidable:

    def __init__(self, config=None):
        if config:
            self.configure(config)

    def configure(self, config):
        for field in config:
            field_name = field['name']
            setattr(self, field_name, {})
            self.__dict__[field_name]['type'] = field['type']
            self.__dict__[field_name]['must_be_present'] = \
                field['must_be_present']
            self.__dict__[field_name]['rules'] = field['rules']


def value_is_required(field, value, message=None, data=None):
    valid = True
    response = {}
    if field == "":
        valid = False
    elif value == "":
        valid = False

    if message:
        print(message)
        response['message'] = message

    return valid, response
