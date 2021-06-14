
import random
from flask import Flask, render_template
app = Flask('my app')



@app.route('/')
def index():
    # return '<html><head></head><body><h1>Hello world!</h1></body></html'
    temperature = random.randint(50,100)
    return render_template('index.html', name='bob', favorite_fruit='apples', temperature=temperature, nums=[1, 2, 3])


@app.route('/emoticon/')
def emoticon():
    eyes = random.choice([':', ';', '='])
    nose = random.choice(['', '-', 'o'])
    mouth = random.choice([')', '(', ']', 'D'])
    emoticon = eyes + nose + mouth
    return render_template('emoticon.html', emoticon=emoticon)


@app.route('/blog/')
def blog():

    posts = [{
        'title': 'My First Post',
        'image': 'https://picsum.photos/500/',
        'preview': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tempor nisi nec hendrerit gravida. Morbi laoreet libero ipsum, nec vestibulum nulla sollicitudin condimentum. Suspendisse potenti. Etiam commodo neque ac purus hendrerit, vitae lacinia mi efficitur. Nulla purus neque, consectetur sed felis et, sodales mollis sem. Nam et blandit urna. Integer at nisl et purus vulputate volutpat.'
    },{
        'title': 'My Second Post',
        'image': 'https://picsum.photos/499/',
        'preview': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tempor nisi nec hendrerit gravida. Morbi laoreet libero ipsum, nec vestibulum nulla sollicitudin condimentum. Suspendisse potenti. Etiam commodo neque ac purus hendrerit, vitae lacinia mi efficitur. Nulla purus neque, consectetur sed felis et, sodales mollis sem. Nam et blandit urna. Integer at nisl et purus vulputate volutpat.'
    },{
        'title': 'My Third Post',
        'image': 'https://picsum.photos/501/',
        'preview': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tempor nisi nec hendrerit gravida. Morbi laoreet libero ipsum, nec vestibulum nulla sollicitudin condimentum. Suspendisse potenti. Etiam commodo neque ac purus hendrerit, vitae lacinia mi efficitur. Nulla purus neque, consectetur sed felis et, sodales mollis sem. Nam et blandit urna. Integer at nisl et purus vulputate volutpat.'
    },{
        'title': 'My Fourth Post',
        'image': 'https://picsum.photos/502/',
        'preview': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tempor nisi nec hendrerit gravida. Morbi laoreet libero ipsum, nec vestibulum nulla sollicitudin condimentum. Suspendisse potenti. Etiam commodo neque ac purus hendrerit, vitae lacinia mi efficitur. Nulla purus neque, consectetur sed felis et, sodales mollis sem. Nam et blandit urna. Integer at nisl et purus vulputate volutpat.'
    },{
        'title': 'My Fifth Post',
        'image': 'https://picsum.photos/503/',
        'preview': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus tempor nisi nec hendrerit gravida. Morbi laoreet libero ipsum, nec vestibulum nulla sollicitudin condimentum. Suspendisse potenti. Etiam commodo neque ac purus hendrerit, vitae lacinia mi efficitur. Nulla purus neque, consectetur sed felis et, sodales mollis sem. Nam et blandit urna. Integer at nisl et purus vulputate volutpat.'
    }]

    return render_template('blog.html', posts=posts)

@app.route('/about/')
def about():
    return 'About View'

@app.route('/about/contact/')
def about_contact():
    return 'About-Contact View'

@app.route('/post/<int:post_id>/')
def post_detail(post_id):
    print(post_id)
    # look up the record in the database with id 78
    # display it to the user
    return f'Looking at post with id {post_id}'



app.run(debug=True)
