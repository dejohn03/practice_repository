# Initialize a global list to store all tickets
tickets_list = []

def main_menu():
    print("\n" + "=" * 30)
    print("     CAMPUSFLOW MANAGEMENT     ")
    print("=" * 30)
    print("1. Create a ticket")
    print("2. Show all tickets")
    print("3. Show all open tickets")
    print("4. Assign tickets")
    print("5. Show reports")
    print("6. Exit")
    print("=" * 30)

def add_ticket():
    title = input("Enter ticket description: ")
    # Added "assigned_to" key to track ownership
    tickets_list.append({"title": title, "done": False, "assigned_to": "Unassigned"})
    print(f"Ticket '{title}' added successfully!")

def show_ticket():
    if not tickets_list:
        print("\nNo tickets found.")
        return False
    
    print("\n--- ALL TICKETS ---")                
    for x, t in enumerate(tickets_list, start=1): 
        status = "✅ Done" if t["done"] else "❌ Open" 
        print(f"{x}. [{status}] {t['title']} (Assigned to: {t['assigned_to']})")
    return True

def show_open_tickets():
    # Filter out only the tickets where "done" is False
    open_tickets = [t for t in tickets_list if not t["done"]]
    
    if not open_tickets:
        print("\nNo open tickets! Everything is completed.")
        return False

    print("\n--- OPEN TICKETS ---")
    for x, t in enumerate(open_tickets, start=1):
        print(f"{x}. [❌ Open] {t['title']} (Assigned to: {t['assigned_to']})")
    
    # Let the user close an open ticket directly from here if they want
    try:
        choice = input("\nEnter a ticket number to mark as done (or press Enter to skip): ")
        if choice.strip() == "":
            return
            
        idx = int(choice) - 1
        if 0 <= idx < len(open_tickets):
            # Find the original ticket in the main list and mark it done
            open_tickets[idx]["done"] = True
            print("Ticket marked as done!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def assign_ticket():
    if not show_ticket():
        return
        
    try:
        x = int(input("\nEnter the ticket number you want to assign: ")) - 1
        if 0 <= x < len(tickets_list):
            name = input("Enter the name of the person to assign this ticket to: ")
            if name.strip() == "":
                name = "Unassigned"
            tickets_list[x]["assigned_to"] = name
            print(f"Ticket successfully assigned to {name}!")
        else:
            print("Invalid ticket number.")
    except ValueError:
        print("Please enter a valid number.")

def show_reports():
    if not tickets_list:
        print("\nNo data available to generate reports.")
        return

    total = len(tickets_list)
    # Count completed vs open tickets
    done_count = sum(1 for t in tickets_list if t["done"])
    open_count = total - done_count
    
    print("\n" + "=" * 20)
    print("   CAMPUSFLOW REPORT   ")
    print("=" * 20)
    print(f"Total Tickets Created : {total}")
    print(f"Open Tickets Remaining: {open_count} ❌")
    print(f"Completed Tickets     : {done_count} ✅")
    
    # Calculate simple progress percentage
    progress = (done_count / total) * 100
    print(f"Completion Rate       : {progress:.1f}%")
    print("=" * 20)

# Main program loop to run the menu system
while True:
    main_menu()
    choice = input("Choose an option (1-6): ")
    
    if choice == "1":
        add_ticket()
    elif choice == "2":
        show_ticket()
    elif choice == "3":
        show_open_tickets()
    elif choice == "4":
        assign_ticket()
    elif choice == "5":
        show_reports()
    elif choice == "6":
        print("Exiting CampusFlow Management. Goodbye!")
        break
    else:
        print("Invalid choice, please select a number between 1 and 6.")
