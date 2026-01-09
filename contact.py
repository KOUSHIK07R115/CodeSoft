import sys

def main_menu():
    print("\n" + "="*30)
    print("      CONTACT BOOK")
    print("="*30)
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("="*30)

def add_contact(contacts):
    name = input("Enter Name: ").strip()
    if name in contacts:
        print("Contact already exists!")
        return
    
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"\nContact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("\nYour contact book is empty.")
        return
    
    print("\n--- CONTACT LIST ---")
    print(f"{'Name':<20} | {'Phone Number':<15}")
    print("-" * 40)
    for name, details in contacts.items():
        print(f"{name:<20} | {details['phone']:<15}")

def search_contact(contacts):
    query = input("Search by Name or Phone Number: ").strip().lower()
    found = False
    
    for name, details in contacts.items():
        if query in name.lower() or query in details['phone']:
            print(f"\n--- Result for '{name}' ---")
            print(f"Phone:   {details['phone']}")
            print(f"Email:   {details['email']}")
            print(f"Address: {details['address']}")
            found = True
    
    if not found:
        print("No contact found matching that criteria.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        print("Leave blank to keep current information.")
        
        new_phone = input(f"New Phone [{contacts[name]['phone']}]: ")
        new_email = input(f"New Email [{contacts[name]['email']}]: ")
        new_address = input(f"New Address [{contacts[name]['address']}]: ")
        
        if new_phone: contacts[name]['phone'] = new_phone
        if new_email: contacts[name]['email'] = new_email
        if new_address: contacts[name]['address'] = new_address
        
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        confirm = input(f"Are you sure you want to delete {name}? (y/n): ").lower()
        if confirm == 'y':
            del contacts[name]
            print("Contact deleted.")
    else:
        print("Contact not found.")

def run_app():
    contacts = {} # In-memory database
    while True:
        main_menu()
        choice = input("Select an option (1-6): ")
        
        if choice == '1': add_contact(contacts)
        elif choice == '2': view_contacts(contacts)
        elif choice == '3': search_contact(contacts)
        elif choice == '4': update_contact(contacts)
        elif choice == '5': delete_contact(contacts)
        elif choice == '6':
            print("Closing Contact Book. Goodbye!")
            sys.exit()
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    run_app()
