# -------------------- Kindle Highlight Aggregator --------------------------------
# this program takes your Kindle book highlights from an HTML file, compiles it into a CSV file, and allows you to compile all your book notes in one place
# later versions will take these highlights and allow you to review them in a spaced interval like Anki
# later versions will automate the downloading of the Kindle notes
# later versions will store more metadata such as last time accessed and allow user to set topics to search by
# later versions will automatically email you your highlights for review

from bs4 import BeautifulSoup
from random import randint
import csv
import json
import ast

# create class for each instance of a book that the user wants
class Book:
    def __init__(self):
        self.note_dict = {"Book Title": "", "Author": ""}
        self.notes = ""

# this function opens the book and saves it to a variable. If the file does not exist, it returns an error message.
    def open(self, user_book):
        try:
            with open(user_book) as data:
                self.notes = BeautifulSoup(data, 'html.parser')
                self.dict_converter(self.notes)
                print(f"\x1b[6;30;42m\n\t--- {user_book} has been successfully processed into the system. ---\x1b[0m")
                return True
        except:
            return print("\x1b[6;30;41mSorry, that file could not be found. Please check the file's location and your spelling, then try again.\x1b[0m")

# this function provides the logic for the user's choice: random, how many, search by author, title, or keyword
    def user_pick(self, pick):
        if pick == 'random': return self.rand_highlight(self.note_dict)
        elif pick == ('all' or 'one'): return self.quantity(pick)
        elif pick == 'add': return self.write_db()
        elif pick == 'keyword': return self.key_highlight()
        elif pick == 'exit': return False
        else: print("\x1b[6;30;41mPlease check the spelling of your request and try again. \x1b[0m")
        
# this function lets user run the program again for the same book
    def another(self):
        if input("Would you like to search for something else in this file? Type 'yes' if so, else type any other key to close this file: ").lower() == 'yes': return True
        else: return False

# this functions gives the user options for when they are going through the program a subsequent time
    def options(self):
        return input("How would you like to search now? 'Random', 'keyword', 'all', 'add', or 'exit': ").lower()

# this function builds a dictionary for the book - separating author, title, and quotes with different key:value paris
    def dict_converter(self, notes):
        # next two lines add the book title to the dict
        self.title = self.notes.find_all("div", "bookTitle")
        self.note_dict["Book Title"] = self.title[0].get_text('\n', strip=True)

        # next two lines add the author to the dict
        self.authors = self.notes.find_all("div", "authors")
        self.note_dict["Author"] = self.authors[0].get_text('\n', strip=True)
        
        # next few lines add the quotes to the dict
        self.quotes = self.notes.find_all("div", "noteText")
        for i, item in enumerate(self.quotes):
            self.quotes[i] = item.get_text("\n", strip=True)
            self.note_dict[f"{i}"] = self.quotes[i]

# this function returns a random highlight
    def rand_highlight(self, note_dict):
        print(f"""\x1b[6;30;46m
        {self.note_dict[f"{randint(2, (len(self.note_dict) - 1))}"]} 
                
                \x1b[6;33;46m-{self.note_dict['Author']} from the book '{self.note_dict['Book Title']}'\x1b[0m
        """)

# this function returns highlights by a specified keyword
    def key_highlight(self):
        key = input("\nPlease enter the keyword you are searching for: ")
        for i in self.note_dict:
            if key in self.note_dict[i]:
                print("\x1b[6;30;46m\n" + self.note_dict[i] + "\x1b[0m")
        print(f"\x1b[6;33;46m\n\t\t-{self.note_dict['Author']} from the book '{self.note_dict['Book Title']}\x1b[0m")

# this function allows user to choose one, multiple, or all highlights
    def quantity(self, pick):
        for i in self.note_dict: print("\x1b[6;30;46m\n" + self.note_dict[i] + "\n\x1b[0m")
        print(f"\x1b[6;33;46m\n\t\t-{self.note_dict['Author']} from the book '{self.note_dict['Book Title']}\x1b[0m")

# this function writes the dictionary into the database file
    def write_db(self):
        database = input("Please enter the file name of your existing database or create a new one: ")
        if '.csv' in database:
            with open(database, 'a') as db:
                new_file = csv.writer(db)
                for key, value in self.note_dict.items():
                    new_file.writerow([key, value])
        elif '.json' in database:
            with open(database, 'a') as db:
                db.write(json.dumps(self.note_dict))
        print("\x1b[6;30;42mYour highlights have been successfully added to the database.\x1b[0m\n")

# ------------- End of the Book class ------------------------

# create a class for opening, compiling, and searching in the database
class Database:
    def __init__(self):
        self.dict = ()
        self.file = ""

# this function opens the users database of highlights - IN PROGRESS
    def open(self, db):
        try:
            if '.csv' in db:
                with open(db, 'r') as data:
                    self.file = data.read()
                    self.dict = ast.literal_eval(self.file)
            elif'.json' in db:
                with open(db, 'r') as data:
                    self.file = json.load(data)
            return True
        except:
            print("\x1b[6;30;41mSorry, that file could not be found. Please check the file's location and your spelling, then try again.\x1b[0m")
            return False

# I need this function to be stored into something that I can use to search through and return the user's request: author, title, keyword
    def user_pick(self, pick):
        if pick == 'random': return self.random(self.dict)
        elif pick == 'author': return self.auth(self.dict)
        elif pick == 'keyword': return self.keyword()
        elif pick == 'title': return self.title()
        elif pick == 'exit': return False
        else: print("\x1b[6;30;41mPlease check the spelling of your request and try again. \x1b[0m")

# this function returns a random highlight from amongst the database
    def random(self, dict):
        rand1 = randint(0, (len(self.dict) - 1))
        rand2 = randint(2, (len(self.dict) - 1))
        print(f"""\x1b[6;30;46m
        {self.dict[rand1][str(rand2)]} 
                
                \x1b[6;33;46m-{self.dict[rand1]['Author']} from the book '{self.dict[rand1]['Book Title']}'\x1b[0m
        """)

# # this function returns highlights from the database by a specified author - NOT COMPLETE
    def auth(self, dict):
        print(enumerate(self.dict))
        print("Which author would you like to search for? ")
        author = input("Please make your entry as 'author last name', 'author first name' (e.g. 'Rowling, J.K.') : ")
        for i in enumerate(self.dict):
            print(i)
            if self.dict[i]['Author'] == author:
                print(f"""\x1b[6;30;46m
                {self.dict[i]} 
                
                \x1b[6;33;46m-{self.dict[i]['Author']} from the book '{self.dict[i]['Book Title']}'\x1b[0m
        """)

# # this function returns highlights by specified keyword - NOT COMPLETE
#     def keyword(self):
#         pass

# # this functions returns highlights by a specified title - NOT COMPLETE
#     def title(self):
#         pass

# this function lets user run the program again for the selected database
    def another(self):
        if input("Would you like to search for something else in this file? Type 'yes' if so, else type any other key to close this file: ").lower() == 'yes': return True
        else: return False

# this functions gives the user options for when they are going through the program a subsequent time
    def options(self):
        return input("How would you like to search now? 'Random', 'author', 'keyword', 'title', or 'exit': ").lower()

# ------------- End of the Database class ----------------------

def again():
    again = input("Would you like to try again with another file? Yes or no? ").lower()
    if again == ("yes" or "y"): return True
    else: return False

def pick_book():
    pick = input("""
    What would you like to do with your highlights?

    To search this book, type 'random', 'keyword', or 'all'. 

    To add your highlights from this book to the database, type 'add'.
 
    Enter your choice here: """).lower()
    loc = enter_file()
    return pick, loc 

def pick_db():
    pick = input(""" 
    To search the database, type 'random' to get a random highlight, 'author' to search by author, 'title' to search by title, or 'keyword' to search by keyword.
    """).lower()
    loc = enter_file()
    return pick, loc 

def enter_file():
    return input("\nPlease type in the file from which you'd like to see your highlights: ").lower()

# --------------------- User facing prompts appear here, runs until user stops ---------------------------
# Add instructions so the user is walked through how to:
#   Locate their highlights and notes on kindle
#   export their kindle book to HTML
#   save it in the proper place
#   locate the file so that they can run it through the parser

print("""\x1b[6;30;47m
This program aggregates highlights from your Kindle books and allows you to access them in ways that Kindle does not.
To begin, you'll need to export your Kindle highlights as an HTML file from https://read.amazon.com/notebook or a device with the Kindle app.
Save each of these files to the directory from which this program is running.
In a moment, you'll be prompted to enter the file name for the Kindle book or database you want to start with.
Let's begin!
\x1b[0m""")

while True:
    book = Book()
    database = Database()
    db_or_book = input("Would you like to search your database of highlights or work with a new book?: 'db' for database or 'book': ").lower()
    if db_or_book == 'db':
        pick, user_db = pick_db()
        if database.open(user_db) == True:
            database.user_pick(pick)
            while database.another() == True: 
                database.user_pick(database.options())
    elif db_or_book == 'book': 
        pick, user_book = pick_book()
        if book.open(user_book) == True:
            book.user_pick(pick)
            while book.another() == True: 
                book.user_pick(book.options())
    else:
        print("\x1b[6;30;41mSorry, that didn't work. Valid entries are 'db' for database or 'book' for book.\x1b[0m")
    if again() == False:
        break