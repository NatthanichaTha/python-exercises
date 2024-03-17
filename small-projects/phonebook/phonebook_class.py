class Contact:
    def __init__(self, full_name: str, phone_number: str):
        self.full_name = full_name
        self.phone_number = phone_number
        
    def __repr__(self):
        return self.full_name + "," + self.phone_number + "\n"
    
class Phonebook:
    def __init__(self):
        self.phonebook_file = open("phonebook.txt", "r")
        self.phonebook_file_lines = self.phonebook_file.readlines()
        self.contact_list = []
        for line in self.phonebook_file_lines:
            self.contact_list.append(self.parse_contact(line))
    
    def __repr__(self) -> str:
        contact_list_line = ""
        for contact in self.contact_list:
            contact_list_line += "--------------------" + "\n"
            contact_list_line += str(contact.full_name) + "\n"
            contact_list_line += str(contact.phone_number) +"\n"
        contact_list_line += "--------------------"
        return contact_list_line
    
    def parse_contact(self, contact_string: str) -> Contact:
        contact_name = contact_string.split(",")[0]
        phone_number = contact_string.split(",")[1].replace("\n", "")
        contact = Contact(contact_name, phone_number)
        return contact

    def is_duplicate(self, new_contact: Contact):
        for contact in self.contact_list:
            if new_contact.full_name == contact.full_name or new_contact.phone_number == contact.phone_number:
                return True
        return False


    def add_contact(self, contact: Contact):
        self.phonebook_file = open("phonebook.txt", "r+")
        if self.is_duplicate(contact) == True:
            print("The contact is already existed.")
        else:
            self.contact_list.append(contact)
            for contact in self.contact_list:
                self.phonebook_file.write(str(contact))
    
if __name__ == "__main__":
    phonebook = Phonebook()

    #phonebook.add_contact(Contact("Giuseppe", "3463166601"))
    print(phonebook) 