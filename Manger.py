import tkinter as tk
from tkinter import ttk   
import csv
import os
from time import sleep
class PasswordManagerGUI:

    def __init__(self, master):
        self.master = master
        master.title("Password Manager")

        # Text to welcome the user to the GUI
        welcome_text = tk.Label(master, text="Welcome to Your Password Manager", font=("Roboto", 16))
        welcome_text.place(relx=0.5, rely=0.2, anchor='center')

        # Create buttons for the different tabs
        self.see_entries_button = ttk.Button(master, text="See Entries", command=self.see_entries)
        self.see_entries_button.place(relx=0.5, rely=0.5, anchor='center', x=-60)

        self.new_entry_button = ttk.Button(master, text="New Entry", command=self.new_entry)
        self.new_entry_button.place(relx=0.5, rely=0.5, anchor='center', x=60)

        # fix for the forget placeholder error
        self.result_label = tk.Label(self.master, text='', font=("Roboto", 12), fg='green')
        self.result_label.place(relx=0.5, rely=0.8, anchor='center')

#Sets up a text field to that will later be used in another function
    def see_entries(self):
        # Add a label underneath the buttons
        self.entry_label = tk.Label(self.master, text="App", font=("Roboto", 12))
        self.entry_label.place(relx=0.5, rely=0.6, anchor='center', x=-60)

        # Forget the tab buttons
        self.see_entries_button.place_forget()
        self.new_entry_button.place_forget()

        # Create the App text field
        self.entry_entry = tk.Entry(self.master, font=("Roboto", 12))
        self.entry_entry.place(relx=0.5, rely=0.6, anchor='center', x=60)

        # Create the search button
        self.search_button = ttk.Button(self.master, text="Search", command=self.search_entries)
        self.search_button.place(relx=0.3, rely=0.7, anchor='center')

        self.clear_button = ttk.Button(self.master, text="Back", command=self.clear_search_entry)
        self.clear_button.place(relx=0.7, rely=0.7, anchor='center')

    def search_entries(self):
        search = self.entry_entry.get().lower()

        # Read the CSV file
        csv_file = 'Password_Safe.csv'

        try:
            # Check if the file exists
            if not os.path.exists(csv_file):
                raise FileNotFoundError("No data available")

            # Search for the app in the CSV file
            with open(csv_file, 'r', newline='') as file:
                reading = csv.DictReader(file)
                found = False
                for row in reading:
                    if row['Apps'].lower() == search:
                        found = True
                        result_text = f"Username: {row['UserName']} || Password: {row['Password']}"
                        break

                if not found:
                    raise ValueError("App not found")

            # Display the result
            self.result_label.place_forget()

            self.result_label = tk.Label(self.master, text=result_text, font=("Roboto", 12), fg='green')
            self.result_label.place(relx=0.5, rely=0.8, anchor='center')

        except FileNotFoundError as e:
            self.result_label = tk.Label(self.master, text="No file found", font=("Roboto", 12), fg='red')
            self.result_label.place(relx=0.5, rely=0.8, anchor='center')
        except ValueError as e:
            self.result_label = tk.Label(self.master, text="No file found", font=("Roboto", 12), fg='red')
            self.result_label.place(relx=0.5, rely=0.8, anchor='center')
        except Exception as e:
            self.result_label = tk.Label(self.master, text="An error occurred", font=("Roboto", 12), fg='red')
            self.result_label.place(relx=0.5, rely=0.8, anchor='center')

            
#Sets up text fields for the user to input a new Username, Password, and App
    def new_entry(self):

        # Clears the tab buttons
        self.see_entries_button.place_forget()
        self.new_entry_button.place_forget()

        # Create labels and text boxes
        self.username_label = tk.Label(self.master, text="Username", font=("Roboto", 12))
        self.username_label.place(relx=0.3, rely=0.6, anchor='w', x=-30)
        
        self.password_label = tk.Label(self.master, text="Password", font=("Roboto", 12))
        self.password_label.place(relx=0.3, rely=0.7, anchor='w', x=-30)

        self.apps_label = tk.Label(self.master, text="Apps", font=("Roboto", 12))
        self.apps_label.place(relx=0.3, rely=0.8, anchor='w', x=-30)
        
        self.username_entry = tk.Entry(self.master, font=("Roboto", 12))
        self.username_entry.place(relx=0.3, rely=0.6, anchor='w', x=80)

        self.password_entry = tk.Entry(self.master, font=("Roboto", 12), show="*")
        self.password_entry.place(relx=0.3, rely=0.7, anchor='w', x=80)

        self.apps_entry = tk.Entry(self.master, font=("Roboto", 12))
        self.apps_entry.place(relx=0.3, rely=0.8, anchor='w', x=80)

        # Create "Add" button
        self.add_button = ttk.Button(self.master, text="Add", command=self.store_entry)
        self.add_button.place(relx=0.5, rely=0.9, anchor='center')



    def store_entry(self):
        # Retrieves the entered username password and app
        username = self.username_entry.get()
        password = self.password_entry.get()
        apps = self.apps_entry.get().lower()
        check_apps = set()
        # Define the CSV file name
        csv_file = 'Password_Safe.csv'

        # Check if the CSV file exists
        if not os.path.exists(csv_file):
            with open(csv_file, 'w', newline='') as file:
                writing = csv.writer(file)
                # Write the header row
                writing.writerow(['UserName', 'Password', 'Apps'])

        # checks if the CSV already is using an app by the same name
        with open(csv_file, 'r', newline='') as file:
            app_check = csv.DictReader(file)
            for row in app_check:
                check_apps.add(row['Apps'])

        # Clear the entire window of the entry field
        self.username_label.place_forget()
        self.password_label.place_forget()
        self.apps_label.place_forget()
        self.username_entry.place_forget()
        self.password_entry.place_forget()
        self.apps_entry.place_forget()
        self.add_button.place_forget()

        # checks if the entire file is empty
        if len(check_apps) == 0:
            with open(csv_file, 'w') as file:
                writing = csv.writer(file)
                writing.writerow(['UserName', 'Password', 'Apps'])

        # checks if the app is ever used
        if apps not in check_apps:
            # append the new entry to the CSV file
            with open(csv_file, 'a', newline='') as file:
                writing = csv.writer(file)
                writing.writerow([username, password, apps])

            #Displays the Success message
            self.result_label = tk.Label(self.master, text="Username and Password Saved", font=("Roboto", 12), fg='green')
            self.result_label.place(relx=0.5, rely=0.4, anchor='center')
            
            #places the tab entry buttons
            self.see_entries_button.place(relx=0.5, rely=0.5, anchor='center', x=-60)
            self.new_entry_button.place(relx=0.5, rely=0.5, anchor='center', x=60)
        else:
            # Displays the Overwrite message
            self.result_label = tk.Label(self.master, text="Would you like to Overwrite the Existing Entry", font=("Roboto", 12), fg='red')
            self.result_label.place(relx=0.5, rely=0.4, anchor='center')

            # Creating a yes or no button to overwrite the existing entry
            self.yes_button = ttk.Button(self.master, text="Yes", command=lambda: self.overwrite(username, password, apps, csv_file))
            self.yes_button.place(relx=0.5, rely=0.7, anchor='center', x=-60)

            self.no_button = ttk.Button(self.master, text="No", command= self.clear_new_entry)
            self.no_button.place(relx=0.5, rely=0.7, anchor='center', x=60)

    # deletes the app for the new entry
    def overwrite(self, username, password, app, csv_file):
    # finding the app to overwrite  
        with open(csv_file, 'r') as file:
            reading = csv.DictReader(file)
            entries_kept = []
            # reads row by row
            for row in reading:
                if app not in row['Apps']:
                    entries_kept.append(row)
        
        with open(csv_file, 'w', newline='') as file:
            # creates a new csv
            writing= csv.writer(file)
            writing.writerow(['UserName', 'Password', 'Apps'])
            for entry in entries_kept:
                writing.writerow(list(entry.values()))  # Write the dictionary values
            writing.writerow([username, password, app])
        self.clear_new_entry()  

#Clears the new entry tab
    def clear_new_entry(self):
        self.yes_button.place_forget()
        self.no_button.place_forget()
        self.result_label.place_forget()

        #places the tab entry buttons
        self.see_entries_button.place(relx=0.5, rely=0.5, anchor='center', x=-60)
        self.new_entry_button.place(relx=0.5, rely=0.5, anchor='center', x=60)

#Clears the search entry tab
    def clear_search_entry(self):
        self.entry_entry.place_forget()
        self.search_button.place_forget()
        self.entry_label.place_forget()
        self.clear_button.place_forget()
        self.result_label.place_forget()

        #places the tab entry buttons
        self.see_entries_button.place(relx=0.5, rely=0.5, anchor='center', x=-60)
        self.new_entry_button.place(relx=0.5, rely=0.5, anchor='center', x=60)

