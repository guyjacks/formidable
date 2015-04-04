# formidable
A fully featured web form handler for json data

```
import Formidable from formidable

config = {...} // json string, dict object, json-schema.json, or file.json

# config_file can be specified instead of config
form = Formidable(config=config)
form.register_callback('is_unique', is_unique)
form.register_filter('to_lower_case', to_lower_case)

data = {...}
# apply filters
form.process_before_validation(data)

if form.validates(): # pass data if no processing is required
	# process valid data
else
	# process invalid data

# apply filters
form.process_after_validation(data)

def is_unique(data, param1, parame2):
	return true or errors as json string or dict obj

def to_lower_case(data, param1, param2):
	return filtered
```
