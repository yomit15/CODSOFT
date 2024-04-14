class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if self.contacts:
            print("Contact List:")
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {contact.name}, Phone: {contact.phone_number}")
        else:
            print("Contact list is empty.")

    def search_contact(self, keyword):
        found_contacts = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, index, new_contact):
        if 0 < index <= len(self.contacts):
            self.contacts[index - 1] = new_contact
            print("Contact updated successfully.")
        else:
            print("Invalid index.")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            del self.contacts[index - 1]
            print("Contact deleted successfully.")
        else:
            print("Invalid index.")

def create_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return Contact(name, phone_number, email, address)

def main():
    contact_manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            contact_manager.add_contact(create_contact())
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            found_contacts = contact_manager.search_contact(keyword)
            if found_contacts:
                print("Search results:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            index = int(input("Enter the index of the contact to update: "))
            new_contact = create_contact()
            contact_manager.update_contact(index, new_contact)
        elif choice == '5':
            index = int(input("Enter the index of the contact to delete: "))
            contact_manager.delete_contact(index)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
