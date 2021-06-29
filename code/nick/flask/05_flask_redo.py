# from flask import Flask
# app = Flask(__name__)

# # localhost:5000
# @app.route('/')
# def path1():
#     return 'you\'re home'

# # localhost:5000/path1/
# @app.route('/path1/')
# def path1():
#     return 'you\'re at path 1'

# # localhost:5000/path2/
# @app.route('/path2/')
# def path2():
#     return 'you\'re at path 2'

# # localhost:5000/path2/path3/
# @app.route('/path2/path3/')#if you enter a url that does not line up with a route, then you will get an error
# def path3():
#     return 'you\'re at path 3'


# from flask import Flask
# app = Flask(__name__)

# # localhost:5000/user/joe/
# # localhost:5000/user/jane/
# @app.route('/user/<string:username>/')#this path will respond to an infinite number of combinations for user/anything
# def show_user_profile(username):
#     return f'Showing profile for {username}'

# # localhost:5000/user/5/
# # localhost:5000/user/656/
# @app.route('/post/<int:post_id>/')#the int post id is more specific. It makes the path more restrictive, by assigning an integer to that path
# def show_post(post_id):
#     return f'Showing post with id {post_id}'
