
def parse_input(user_input):
    cmd, *args = user_input.strip().split()
    cmd = cmd.strip().lower()
    return cmd.lower(), args

def add_contact(args, contacts):
    if len(args) != 2: 
         return "Invalid input. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
         return "Invalid input. Usage: change [name] [new phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"No contact found with name '{name}'."
    

    def show_phone(args, contacts):
        if len(args) != 1:
             return "Invalid input. Usage: phone [name]"
        name = args[0]
        if name in contacts:
             return contacts[name]
        else:
             return f"No contact found with name '{name}'."
        
        def show_all(contacts):
            if not contacts:
                return "No contacts found."
            return "\n".join([f"{name}:{phone}"for name, phone in contacts.items()])
        
        
            def main():
                contacts = {}
                print("Welcome to the assistant bot!")
                while True:
                    user_input = input("Enter a command: ")
                    command, args = parse_input(user_input)
                    if commad in ["close", "exit"]:
                            print("Good bye!")
                            break
                    elif command == "hello":
                            print("How can I help you?")
                        
                    elif commad == "add":
                            print(add_contact(args, contacts))
                    elif command == "change":
                            print(change_contact(args, contacts))
                    elif command == "phone":
                            print(show_phone(args, contacts))
                    elif commad == "all":
                            print(show_all(contacts))
                    else:
                            print("Invalid commad.")

    if __name__ == "__main__":
        main()

