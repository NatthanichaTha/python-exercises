from input_utils import input_menu, input_int

def add_contact():
    contact_name = input("Please insert contact name: ")
    phone_no = input("Please insert phone number: ")
    phonebook = open("./phonebook.txt", "a")
    phonebook.write(contact_name + ";" + phone_no + "\n")

def show_contact():
    phonebook = open("./phonebook.txt", "r")
    content = phonebook.readlines()
    for i, line in enumerate(content):
        contact_info = line.split(";")
        contact_name = contact_info[0]
        phone_no = contact_info[1].replace("\n", "")
        print("-----------------------")
        print(i+1, ")")
        print(contact_name)
        print(phone_no)
    print("-----------------------")               
    
def delete_contact():
    phonebook = open("./phonebook.txt", "r")
    content = phonebook.readlines()
    to_delete = -1
    while to_delete > len(content) or to_delete < 1:
        to_delete = int(input("Plese insert the number: "))

    print("Contact deleted.")
    content.pop(to_delete-1)

    phonebook = open("./phonebook.txt", "w")
    phonebook.write("".join(content))


print("Menu")
print("Please select the menu:")
user_choice = None
while user_choice != "3":
    user_choice = input_menu(["Add contact", "Show contact list", "Delete contact", "Exit"])
    if user_choice == 0:
        add_contact()
    elif user_choice == 1:
        show_contact()
    elif user_choice == 2:
        delete_contact()
    elif user_choice == 3:
        break