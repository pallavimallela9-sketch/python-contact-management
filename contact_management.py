print("==========================================")
print("        CONTACT MANAGEMENT SYSTEM")
print("==========================================")

contacts = {}

while True:
    print("\n============== MENU ==============")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Contact Summary")
    print("7. Exit")
    print("==================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ").strip()

        if name in contacts:
            print("Contact already exists.")
        else:
            phone = input("Enter phone number: ").strip()
            email = input("Enter email address: ").strip()
            city = input("Enter city: ").strip()

            contacts[name] = {
                "phone": phone,
                "email": email,
                "city": city
            }

            print("Contact added successfully.")

    elif choice == "2":
        if not contacts:
            print("No contacts available.")
        else:
            print("\n========== CONTACT LIST ==========")

            for name, details in contacts.items():
                print("\nName  :", name)
                print("Phone :", details["phone"])
                print("Email :", details["email"])
                print("City  :", details["city"])

    elif choice == "3":
        search_name = input("Enter contact name to search: ").strip()

        if search_name in contacts:
            details = contacts[search_name]

            print("\n========== CONTACT FOUND ==========")
            print("Name  :", search_name)
            print("Phone :", details["phone"])
            print("Email :", details["email"])
            print("City  :", details["city"])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to update: ").strip()

        if name in contacts:
            print("\nCurrent Contact Details:")
            print("Phone :", contacts[name]["phone"])
            print("Email :", contacts[name]["email"])
            print("City  :", contacts[name]["city"])

            phone = input("Enter new phone number: ").strip()
            email = input("Enter new email address: ").strip()
            city = input("Enter new city: ").strip()

            contacts[name]["phone"] = phone
            contacts[name]["email"] = email
            contacts[name]["city"] = city

            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter contact name to delete: ").strip()

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("\n========== CONTACT SUMMARY ==========")
        print("Total Contacts:", len(contacts))

        if contacts:
            print("\nContact Names:")

            for name in contacts:
                print("-", name)
        else:
            print("No contacts stored.")

    elif choice == "7":
        print("\nThank you for using Contact Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
