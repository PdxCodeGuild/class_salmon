# this program takes your Kindle book highlights from an HTML file, compiles it into a CSV file, and allows you to compile all your book notes in one place
# a further program would take these highlights and allow you to review them in a spaced interval like Anki
# later versions could automate the downloading of the Kindle notes

from bs4 import BeautifulSoup
import random

# create class for each instance of a book that the user wants
class Book:
    def __init__(self):
        self.note_dict = {"Book Title": "", "Author": ""}
        self.notes = ""

# this function opens the book and saves it to a variable - invent and wander.html
    def open(self, user_book):
        try:
            with open(user_book) as data:
                # print(data)
                self.notes = BeautifulSoup(data, 'html.parser')
                self.dict_converter(self.notes)
                print(f"\n\t--- {user_book} has been successfully processed into the system. ---")
                return True
        except:
            return print("Sorry, that file could not be found. Please check the file's location and your spelling, then try again.")

# this function provides the logic for the user's choice: random, how many, search by author, title, or keyword
    def user_pick(self, pick):
        # print("user pick: " + user_pick)
        # print(self.note_dict)
        if pick == 'random':
            return self.rand_highlight(self.note_dict)
        elif pick == 'add':
            return self.write_file()


# this function that builds a dictionary for the book - separates author and the quote
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

# this function that returns a random highlight
    def rand_highlight(self, note_dict):
        print(f"""
        {self.note_dict[f"{random.randint(2, len(self.note_dict) - 1)}"]} 
                
                -{self.note_dict['Author']} from the book '{self.note_dict['Book Title']}'
        """)

# create a function that writes this dictionary into a new file
    def write_file(self):
        database = input("Please enter the name of your database: ")
        database = open(database, 'a')
        database.write(str(self.note_dict) + "\n\n")
        print("Your highlights have been successfully added to the database.")



# Add instructions so the user is walked through how to:
#   Locate their highlights and notes on kindle
#   export their kindle book to HTML
#   save it in the proper place
#   locate the file so that they can run it through the parser
"""
This program aggregates highlights and notes from your Kindle books and allows you to choose how to see them.
To begin, you'll need to export your Kindle notes and highlights from https://read.amazon.com/notebook.
Be sure to save each of these files to the directory from which this program is running.
In a moment, you'll be prompted to enter the file name for the Kindle book you want to start with.
Are you ready?
"""

def again():
    again = input("Would you like to try again with another file? Yes or no? ").lower()
    if again == "yes" or again == "y":
        return True
    else:
        return False

# User facing prompts appear here, runs until user stops
while True:
    book = Book()
    user_book = input("Please type in the file from which you'd like to see your notes and highlights: ")
    if book.open(user_book) == True:
        pick = input("""
        What would you like to do with your highlights?

        To search, type 'random', 'author', or 'keyword'. 
        
        To add you highlights to the database, type 'add'. 
        """).lower()
        book.user_pick(pick)
    if again() == False:
        break