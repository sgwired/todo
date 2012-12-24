
def create_todo(todos, title, description, level):
	todo = {'title' : title,
	        'description' : description,
	        'level' : level,
	}
	todos.append(todo)

def get_input(fields):
	user_input = {}
	for field in fields:
		user_input[field] = raw_input(field + " > ")
	return user_input


commands = {
	'new' : [create_todo, ['title', 'description', 'level']],

}

def get_function(command_name):
	return commands[command_name][0]	


def get_fields(command_name):
	return commands[command_name][1]


def main_loop():
	user_input = ""
	while 1:
		print run_cammand(user_input)
		user_input = raw_input("> ")

		if user_input.lower().startswith("quit"):
			print "Exiting"
			break

	if __name__ == '__main__':
		main_loop()
