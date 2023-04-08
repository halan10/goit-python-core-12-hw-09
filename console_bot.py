users =  { 'petro':  '0862807641', 
           'ivan': '0349634663',
           'alla': '0758541633'}


def input_error(func):
        def wrapper(*args):
                try:
                        return func(*args)
                except IndexError:
                        return "Not enough params."
                except KeyError:
                        return "Enter user name."
                except ValueError:
                        return "Give me name please."
        return wrapper

def hello(*args):
        return "Hello. How can I help You?"

@input_error
def add(*args):
        list_of_param = args[0].split()
        name = list_of_param[0]
        phone = list_of_param[1]
        new_user = {name : phone}
        users.update(new_user)
        if not name:
                raise KeyError()
        return f"name: {name}, phone: {phone}"

def show_all(*args):
        result = '\n'.join([f'{k}:{v}' for k, v in users.items()])
        return result

@input_error
def get_phone(*args):
        name = args[0]
        phone = users.get(name)
        if not name:
                raise ValueError()
        return f"name: {name}, phone: {phone}"

@input_error
def change(*args):
        list_of_param = args[0].split()
        name = list_of_param[0]
        phone = list_of_param[1]
        update_user = {name : phone}
        users.update(update_user)
        if not name:
                raise KeyError()
        return f"User {name} has changed thhe phone to {phone}"

def no_command(*args):
        return "Unknown command, please try again."

COMMANDS = {hello: 'hello',
            add: 'add',
            show_all: 'show all',
            get_phone: 'phone',
            change: 'change'
        }

def command_handler(text):
        for command, kword in COMMANDS.items():
                if text.startswith(kword):
                        return command, text.replace(kword, '').strip()
        return no_command, None
def main():
        
        while True:
                user_input = input(">>>>")
                exit_commands = ['good buy', 'exit', 'close', '.']

                if user_input.lower() in exit_commands:
                        print ("Good bye!")
                        break

                command,data = command_handler(user_input.lower())
                print(command(data))



if __name__ == '__main__':
        main()