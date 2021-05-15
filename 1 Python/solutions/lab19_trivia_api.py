
import requests
import html
import random


# dictionaries for the parameters containing the parameter and name

categories = [
    { 'parameter': '', 'name': 'Any Category' },
    { 'parameter': '9', 'name': 'General Knowledge' },
    { 'parameter': '10', 'name': 'Entertainment: Books' },
    { 'parameter': '11', 'name': 'Entertainment: Film' },
    { 'parameter': '12', 'name': 'Entertainment: Music' },
    { 'parameter': '13', 'name': 'Entertainment: Musicals &amp; Theatres' },
    { 'parameter': '14', 'name': 'Entertainment: Television' },
    { 'parameter': '15', 'name': 'Entertainment: Video Games' },
    { 'parameter': '16', 'name': 'Entertainment: Board Games' },
    { 'parameter': '17', 'name': 'Science &amp; Nature' },
    { 'parameter': '18', 'name': 'Science: Computers' },
    { 'parameter': '19', 'name': 'Science: Mathematics' },
    { 'parameter': '20', 'name': 'Mythology' },
    { 'parameter': '21', 'name': 'Sports' },
    { 'parameter': '22', 'name': 'Geography' },
    { 'parameter': '23', 'name': 'History' },
    { 'parameter': '24', 'name': 'Politics' },
    { 'parameter': '25', 'name': 'Art' },
    { 'parameter': '26', 'name': 'Celebrities' },
    { 'parameter': '27', 'name': 'Animals' },
    { 'parameter': '28', 'name': 'Vehicles' },
    { 'parameter': '29', 'name': 'Entertainment: Comics' },
    { 'parameter': '30', 'name': 'Science: Gadgets' },
    { 'parameter': '31', 'name': 'Entertainment: Japanese Anime &amp; Manga' },
    { 'parameter': '32', 'name': 'Entertainment: Cartoon &amp; Animations' }
]

difficulties = [
    { 'parameter': '', 'name': 'Any Difficulty'},
    { 'parameter': 'easy', 'name': 'Easy' },
    { 'parameter': 'medium', 'name': 'Medium' },
    { 'parameter': 'hard', 'name': 'Hard' }
]

types = [
    { 'parameter': '', 'name': 'Any Type'},
    { 'parameter': 'multiple', 'name': 'Multiple Choice' },
    { 'parameter': 'boolean', 'name': 'True / False' }
]


# given a name and list of dictionaries representing the options
# get a parameter from the user
def get_parameter(name, options):
    # show all the options
    for i in range(len(options)):
        print(i+1, options[i]['name'])
    # prompt the user for a value
    choice_index = int(input(f'What {name} do you pick? '))
    # return the parameter
    return options[choice_index-1]['parameter']

# given the parameters, get a list of questions
def get_questions(param_amount, param_category, param_difficulty, param_type):
    url = f'https://opentdb.com/api.php'
    params = {
        'amount': param_amount,
        'category': param_category,
        'difficulty': param_difficulty,
        'type': param_type
    }
    response = requests.get(url, params=params)
    print(response.url)
    data = response.json()

    questions = data['results']
    return questions



# get the parameters for the quiz from the user ================================

param_amount = int(input('How many questions? '))
param_category = get_parameter('category', categories)
param_difficulty = get_parameter('diffficulty', difficulties)
param_type = get_parameter('type', types)

questions = get_questions(param_amount, param_category, param_difficulty, param_type)

# iterate over our questions and ask them one at a time

num_correct = 0
for question in questions:
    question_text = html.unescape(question['question'])
    print(question_text)
    if question['type'] == 'boolean':
        answer = input('True or False? ').title()
        if answer == question['correct_answer']:
            num_correct += 1
            print('Correct!')
        else:
            print('Incorrect, the correct answer was "' + question['correct_answer'] + '\"')
    elif question['type'] == 'multiple':
        answers = question['incorrect_answers'] + [question['correct_answer']]
        # answers = question['incorrect_answers'].copy()
        # answers.append(question['correct_answer'])
        random.shuffle(answers)
        for i in range(len(answers)):
            answer_text = html.unescape(answers[i])
            print(i+1, answer_text)
        answer = int(input('What is your answer (1-4)? '))
        if answers[answer-1] == question['correct_answer']:
            num_correct += 1
            print('Correct!')
        else:
            print('Incorrect, the correct answer was "' + question['correct_answer'] + '\"')

print(f'Correct answers: {num_correct}/{len(questions)}')



