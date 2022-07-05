# user registration

username_schema = {
	'name': {
		'type': 'string',
		'minlength': 3,
		'maxlength': 150
	}
}

password_schema = {
	'password': {
		'type': 'string',
		'minlength': 8,
		'maxlength': 200
	}
}

# config file

config_schema = {
	'lives': {
		'type': 'integer', 
		'min': 3, 
		'max': 15
	}, 
	'db': { 'type': 'string' }
}