class Formidable:

    def __init__(self, config=None):
        self.validators = {}
        if config:
            self.configure(config)

    def configure(self, config):
        for field in config:
            self.add_field(field)

    def add_field(self, field):
        field_name = field['name']
        setattr(self, field_name, {})
        self.__dict__[field_name]['type'] = field['type']
        if 'rules' in field:
            self.__dict__[field_name]['rules'] = field['rules']

    def add_validator(self, name, func):
        self.validators[name] = func

    def load_data(self, data):
        for field in data:
            keys = field.keys()
            for name in keys:
                field_name = name
                value = field[name]
            self.__dict__[field_name]['data'] = value


def field_must_be_present(field, value=None, message=None, data=None):
    pass


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
