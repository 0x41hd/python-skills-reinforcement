from collections import defaultdict


class ContactBook:
    """
    A class used to represent a Contact Book.
    """

    def __init__(self):
        self.contacts = defaultdict(dict)

    def add_contact(self, name: str, phone: str, email: str = None):
        if name in self.contacts:
            print("Contact Already Exist!")
            return

        self.contacts[name]["phone"] = phone
        self.contacts[name]["email"] = email

    def view_contact(self):
        for name, info in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info["phone"]}")
            print(f"Email: {info["email"]}")
            print("-" * 60)

    def delete_contact(self, name: str):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} information deleted successfully !")
        else:
            print(f"{name} not found in contacts list !")

    def update_contact(self, name: str, phone: str = None, email: str = None):
        if name in self.contacts:
            if phone or "":
                self.contacts[name]["phone"] = phone
            if email or "":
                self.contacts[name]["email"] = email

            print("Contact update successfuly !")
            return

        print(f"{name} not found in contact list !")


if __name__ == "__main__":
    book = ContactBook()

    while True:
        print("\nWelcom to contact book application!")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. View Contact")
        print("4. Delete Contact")
        print("5. Quit")

        user_choice = input("\nPlease choose an option: ")

        if user_choice == "5":
            break
        elif user_choice == "4":
            name_deleted = input("\nEnter name of person you want to delete: ")
            book.delete_contact(name_deleted)
        elif user_choice == "3":
            print("\n")
            book.view_contact()
        elif user_choice == "2":
            user_name = input("\nEnter contat name you want edit it: ")
            phone = input(
                "Enter contact phone (for clear fild hit one space / Not change just hit enter): ")
            email = input(
                "Enter contact email (for clear fild hit one space / Not change just hit enter): ")

            book.update_contact(name=name, phone=phone, email=email)

        elif user_choice == "1":
            name = input("\nEnter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")

            book.add_contact(name=name, phone=phone, email=email)
