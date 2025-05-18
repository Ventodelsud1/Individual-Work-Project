import json       # For working with JSON format // JSON formatı ilə işləmək üçün
import os         # For file system operations and screen clearing // Fayl sistemi və ekran təmizləməsi üçün
import time       # For adding delays (e.g., showing welcome message) // Gecikmələr üçün (məsələn, qarşılama mesajı)
import platform   # To detect the OS and choose correct clear command // Əməliyyat sistemini təyin etmək üçün

FILENAME = "diary.json"  # File to store diary entries // Gündəlik qeydlərin saxlanacağı fayl


# Clears the terminal screen based on OS // Əməliyyat sistemindən asılı olaraq terminal ekranını təmizləyir
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


# Displays an ASCII welcome message for 3 seconds // 3 saniyəlik ASCII qarşılama mesajı göstərir
def show_ascii_welcome():
    print(r"""
     __          __  _                            _          _   _            _____  _       _ _        _       _ _                                      
     \ \        / / | |                          | |        | | | |          |  __ \(_)     (_) |      | |     | (_)                                     
      \ \  /\  / /__| | ___ ___  _ __ ___   ___  | |_ ___   | |_| |__   ___  | |  | |_  __ _ _| |_ __ _| |   __| |_  __ _ _ __ _   _    __ _ _ __  _ __  
       \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | __| '_ \ / _ \ | |  | | |/ _` | | __/ _` | |  / _` | |/ _` | '__| | | |  / _` | '_ \| '_ \ 
        \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| | | |  __/ | |__| | | (_| | | || (_| | | | (_| | | (_| | |  | |_| | | (_| | |_) | |_) |
         \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \__|_| |_|\___| |_____/|_|\__, |_|\__\__,_|_|  \__,_|_|\__,_|_|   \__, |  \__,_| .__/| .__/ 
                                                                                        __/ |                                   __/ |       | |   | |    
                                                                                       |___/                                   |___/        |_|   |_|    
    """)
    time.sleep(2)
    clear_screen()


# Loads saved diary entries from file // Fayldan gündəlik qeydlərini yükləyir
def load_entries():
    entries = []
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as file:
            data = file.read()
            if data != "":
                entries = json.loads(data)
    return entries


# Saves all diary entries to file // Gündəlik qeydlərini fayla yazır
def save_entries(entries):
    text = json.dumps(entries, indent=4, ensure_ascii=False)
    with open(FILENAME, "w", encoding="utf-8") as file:
        file.write(text)


# Adds a new diary entry // Yeni gündəlik qeydi əlavə edir
def add_entry(entries):
    date = input("Entered (e.g. 29/01/2025): ")
    note = input("What do you want to record? ")
    entries.append({"date": date, "note": note})
    print("Entry added.")


# Displays all diary entries // Bütün qeydləri göstərir
def view_entries(entries):
    if len(entries) == 0:
        print("No entries yet.")
        return

    print("=== All Entries ===")
    for i, entry in enumerate(entries, 1):
        print(f"{i}. {entry['date']} - {entry['note']}")


# Searches for entries by keyword // Açar sözlə qeydləri axtarır
def search_entries(entries):
    keyword = input("Enter a word to search: ").lower()
    found = []

    for entry in entries:
        if keyword in entry["note"].lower():
            found.append(entry)

    if not found:
        print("Nothing found.")
    else:
        print("=== Search Results ===")
        for e in found:
            print(f"{e['date']} - {e['note']}")


# Edits a selected diary entry // Seçilmiş qeydi redaktə edir
def update_entry(entries):
    view_entries(entries)
    user_input = input("Enter the number of the entry to edit: ")
    if user_input.isdigit():
        index = int(user_input) - 1
        if 0 <= index < len(entries):
            new_note = input("Enter the new note: ")
            entries[index]["note"] = new_note
            print("Entry updated.")
        else:
            print("No entry with that number.")
    else:
        print("Please enter a valid number.")


# Deletes a selected entry // Seçilmiş qeydi silir
def delete_entry(entries):
    view_entries(entries)
    user_input = input("Enter the number of the entry to delete: ")
    if user_input.isdigit():
        index = int(user_input) - 1
        if 0 <= index < len(entries):
            removed = entries.pop(index)
            print("Deleted entry from", removed["date"])
        else:
            print("No entry with that number.")
    else:
        print("Please enter a valid number.")


# Deletes all diary entries after confirmation // Təsdiqlədikdən sonra bütün qeydləri silir
def clear_entries(entries):
    confirm = input("Are you sure you want to delete all entries? (y/n): ").lower()
    if confirm == "y":
        entries.clear()
        print("All entries deleted.")


# Displays help instructions // İstifadə qaydalarını göstərir
def show_help():
    print("""
Instructions:
- Add your diary entries with the date
- You can view, edit, search or delete entries
- All entries are saved automatically
""")


# Shows the main menu options // Əsas menyu seçimlərini göstərir
def show_menu():
    print("""
1. Add a post         
2. View all posts     
3. Find a post      
4. Edit a post        
5. Delete a post     
6. Clear all posts    
7. Help              
8. Log out           
""")


# Main function — program loop // Əsas funksiya — proqram dövrü
def main():
    entries = load_entries()
    clear_screen()
    show_ascii_welcome()
    print("Welcome to the Digital Diary app!!\n")

    while True:
        clear_screen()
        show_menu()
        choice = input("Choose an option (1-8): ")
        clear_screen()

        if choice == "1":
            add_entry(entries)
        elif choice == "2":
            view_entries(entries)
        elif choice == "3":
            search_entries(entries)
        elif choice == "4":
            update_entry(entries)
        elif choice == "5":
            delete_entry(entries)
        elif choice == "6":
            clear_entries(entries)
        elif choice == "7":
            show_help()
        elif choice == "8":
            save_entries(entries)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()