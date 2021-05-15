


import requests


# Part 1 =======================================================================

# Get Latest Post User
# an example function for getting the user of the most recent post
def get_latest_post_user():
    response = requests.get('http://localhost:5000/posts/')
    posts = response.json()['posts']
    return posts[-1]['user']

# print(get_latest_post_user()) # situation5839



# Count User Post Upvotes
# returns a dictionary where the keys are the usernames
# and the values are the total number of upvotes they received from posts
def count_user_post_upvotes():
    response = requests.get('http://localhost:5000/users/')
    users = response.json()['users']

    response = requests.get('http://localhost:5000/posts/')
    posts = response.json()['posts']

    user_post_counts = {}
    for user in users:
        user_post_counts[user] = 0
    for post in posts:
        user_post_counts[post['user']] += post['upvotes']
    return user_post_counts

# print(count_user_post_upvotes()) # {'partner5084': 806, 'space9330': 430, 'green1898': 560, 'whom5856': 89, ...}



# Find Most Upvoted Post
# finds and returns the most upvoted post
def find_most_upvoted_post():
    response = requests.get('http://localhost:5000/posts/')
    posts = response.json()['posts']
    max_post = posts[0]
    for post in posts:
        if post['upvotes'] > max_post['upvotes']:
            max_post = post
    return max_post

# print(find_most_upvoted_post()) # {'id': 44, 'text': '...', 'upvotes': 199, 'user': 'whom5856'}



# Part 2 =======================================================================


def print_comments(post_id):
    response = requests.get(f'http://localhost:5000/posts/{post_id}/')
    post = response.json()
    print(post['user'] + ': ' + post['text'][:40])
    for comment in post['comments']:
        print_comments_recursive(comment, 1)

def print_comments_recursive(comment, depth):
    print('\t'*depth + comment['user'] + ': ' + comment['text'][:40])
    for comment in comment['comments']:
        print_comments_recursive(comment, depth+1)

# print_comments(0)



def count_comment_upvotes(post_id):

    # build up our dictionary of users and upvote counts
    # {'agreement8606': 0, 'laugh1923': 0, 'opportunity7319': 0, 'soldier4928': 0, ...}
    response = requests.get('http://localhost:5000/users/')
    users = response.json()['users']
    user_comment_upvotes = {}
    for user in users:
        user_comment_upvotes[user] = 0
    
    # get the data for a single post
    response = requests.get(f'http://localhost:5000/posts/{post_id}/')
    post = response.json()
    
    count_comment_upvotes_recursive(post['comments'], user_comment_upvotes)

    return user_comment_upvotes
    
def count_comment_upvotes_recursive(comments, user_comment_upvotes):
    for comment in comments:
        user_comment_upvotes[comment['user']] += comment['upvotes']
        count_comment_upvotes_recursive(comment['comments'], user_comment_upvotes)

print(count_comment_upvotes(0))
# {'agreement8606': 517, 'laugh1923': 493, 'opportunity7319': 441, 'soldier4928': 297, 'wall4627': 339, ...}


def find_most_upvoted_comment(post_id):
    ...

