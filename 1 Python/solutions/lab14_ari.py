
import requests
import re

def get_books(search):
    # put the search term into our query string / query parameters
    params = {'query': search}
    # send the request to project gutenberg
    response = requests.get('https://www.gutenberg.org/ebooks/search/', params=params)
    # running regex on the html source code that we get in response
    # to get a list of ids of books that match the search term
    text = response.text
    book_ids = re.findall(r'\/ebooks\/(\d+)', text)
    titles = re.findall(r'<span class="title">(.+)<\/span>', text)
    titles = titles[4:]
    print(book_ids)
    print(len(book_ids))
    print(len(titles))
    output = []
    for i in range(len(book_ids)):
        output.append({'title': titles[i], 'id': book_ids[i]})
    return output

    
def get_book_text(book_id):
    url = f'https://www.gutenberg.org/cache/epub/{book_id}/{book_id}.txt'
    response = requests.get(url)
    return response.text




search = input('What book would you like to search for? ') # prompt the user for a search term
books = get_books(search) # list of dictionaries
# [{'title': 'Pygmalion', 'id': '3825'}, {'title': 'Les Fleurs du Mal. English', 'id': '36098'}
for i in range(len(books)):
    print(i, books[i]['title'])

book_index = int(input('What book would you like to see? '))
text = get_book_text(books[book_index]['id'])
print(text)



ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}






