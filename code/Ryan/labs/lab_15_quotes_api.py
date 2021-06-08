
#from numpy.core.numeric import tensordot

breakflag = False
while True:
    import requests
    response = requests.get('https://favqs.com/api/qotd', headers = {'accept': 'application/json'})
    data = response.json()
    quote = data["quote"]["body"]
    #print("Quote:", quote)
    #print(data)
    #print(quote)

    author = data["quote"]["author"]
    #print("Author:", author)
    #print(data)
    #print(author)
    qotd = {}
    qotd.update({author: quote})
    #print(str(qotd))
    print("Quote:", quote)
    print("Author:", author)

    keyword = input("Enter a keyword or done: ")
    if keyword == "done":
        exit()
    page = 1
    #print(keyword)
    # list quotes
    response2 = requests.get(f'https://favqs.com/api/quotes/?page={page}&filter={keyword}', headers = {'accept': 'application/json', 'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    data2 = response2.json()
    quote2 = data2["quotes"]

    #print(quote2)
    #print(response2[0])
    quote3_body = []
    quote3_author = []
    for item in quote2:
        print(item["body"])
        print(item["author"])
        quote3_body.append(item["body"])
        quote3_author.append(item["author"])
        #print(item[0])
        #print("~~~~~~~~")
        #print("Quote:", item["quote"])
        #print("Author:", item["author"])
    # Show next page
    # enter new keyword
    #print({quote3_body[0]}, {quote3_author[0]})

    # for each in quote3_body:
    #     print(each)
    #     for each in quote3_author:
    #         print(each)
    #         break

    breakflag2 = True
    while breakflag2 == True:
        page = 1
        user_input = input("Enter next page or done: ")
        if user_input == "done":
            breakflag2 = False
        else:
            page = page + 1
            response2 = requests.get(f'https://favqs.com/api/quotes/?page={page}&filter={keyword}', headers = {'accept': 'application/json', 'Authorization':'Token token="855df50978dc9afd6bf86579913c9f8b"'})
            data2 = response2.json()
            quote2 = data2["quotes"]

            #print(quote2)
            #print(response2[0])
            quote3_body = []
            quote3_author = []
            for item in quote2:
                print(item["body"])
                print(item["author"])
                quote3_body.append(item["body"])
                quote3_author.append(item["author"])


    
"""
[
        {'id': 1265, 

        'dialogue': False, 

        'private': False, 

        'tags': ['age', 'funny'], 

        'url': 'https://favqs.com/quotes/rowan-atkinson/1265-no-no-i-was-on-', 

        'favorites_count': 1, 

        'upvotes_count': 0, 

        'downvotes_count': 0, 

        'author': 'Rowan Atkinson', 

        'author_permalink': 'rowan-atkinson', 

        'body': 'No, no, I was only funny on stage, really. I, I, think I was funny as a person toward my classmates when I was very young. You know, when I was a child, up to about the age of 12.'}, 

        {'id': 2759, 
'dialogue': False, 
'private': False, 
'tags': ['funny'], 
'url': 
'https://favqs.com/quotes/mitch-hedberg/2759-why-is-cloud-9-', 
'favorites_count': 1, 
'upvotes_count': 2, 
'downvotes_count': 0, 
'author': 'Mitch Hedberg', 
'author_permalink': 'mitch-hedberg', 
'body': "Why is Cloud 9 so amazing? What is wrong with Cloud 8? That joke came off the top of my head, 
and the top of my 
head ain't funny!"}, 
{'id': 2917, 
'dialogue': False, 
'private': False, 
'tags': ['amazing', 
'funny'], 
'url': 'https://favqs.com/quotes/beth-ditto/2917-my-size-has-he-', 
'favorites_count': 1, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Beth Ditto', 
'author_permalink': 'beth-ditto', 
'body': "My size has helped make me an amazing performer too. The cliche of the Funny Fat Friend: I 
absolutely was that character - I am that character... It's a complicated bag 
of tools I acquired, 
and I've put them all to work onstage."}, 
{'id': 3329, 
'dialogue': False, 
'private': False, 
'tags': ['amazing'], 
'url': 'https://favqs.com/quotes/linda-hamilton/3329-my-heart-is-so-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Linda Hamilton', 
'author_permalink': 'linda-hamilton', 
'body': "My heart is so light that it's amazing. I get 
to play all this grief, 
all this loss, 
all this disaster and chaos. It's hysterically funny. I am very light."}, 
{'id': 3561, 
'dialogue': False, 
'private': 
False, 
'tags': ['amazing'], 
'url': 'https://favqs.com/quotes/majel-barrett/3561-you-go-through-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Majel Barrett', 
'author_permalink': 'majel-barrett', 
'body': 
'You go through at least the first two years of Star Trek and you find some amazing stuff. Everything that was going on Gene put into the series. He just put strange costumes on the actors and painted them funny colours and left the same situation in.'}, 
{'id': 25003, 
'dialogue': False, 
'private': False, 
'tags': ['funny'], 
'url': 'https://favqs.com/quotes/chris-rock/25003-hollywood-s-j-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Chris Rock', 
'author_permalink': 'chris-rock', 
'body': "Hollywood's just not funny."}, 
{'id': 25357, 
'dialogue': False, 
'private': False, 
'tags': ['funny'], 

'url': 'https://favqs.com/quotes/ridley-scott/25357-i-knew-exactl-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Ridley Scott', 
'author_permalink': 'ridley-scott', 
'body': 'I knew exactly what to do on Alien, 
it was funny.'}, 
{'id': 25356, 
'dialogue': False, 
'private': False, 
'tags': ['funny'], 
'url': 'https://favqs.com/quotes/sophie-ellis-bextor/25356-it-s-funny-ho-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Sophie Ellis-Bextor', 
'author_permalink': 'sophie-ellis-bextor', 
'body': "It's funny how intimate it feels to get a text."}, 
{'id': 5249, 
'dialogue': False, 
'private': False, 
'tags': ['art', 
'funny'], 
'url': 'https://favqs.com/quotes/jonathan-safran-foer/5249-literature-has-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Jonathan Safran Foer', 
'author_permalink': 'jonathan-safran-foer', 
'body': "Literature has drawn a funny 
perimeter that other art forms haven't."}, 
{'id': 5350, 
'dialogue': False, 
'private': False, 
'tags': ['attitude', 
'funny'], 
'url': 'https://favqs.com/quotes/flip-wilson/5350-funny-is-an-at-', 
'favorites_count': 0, 
'upvotes_count': 0, 

'downvotes_count': 0, 
'author': 'Flip Wilson', 
'author_permalink': 'flip-wilson', 
'body': 'Funny is an attitude.'}, 
{'id': 5553, 
'dialogue': False, 
'private': False, 
'tags': ['attitude', 
'funny'], 
'url': 'https://favqs.com/quotes/don-rickles/5553-you-know-what--', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Don Rickles', 
'author_permalink': 'don-rickles', 
'body': "You know what's funny to me? Attitude."}, 
{'id': 5722, 
'dialogue': False, 
'private': False, 
'tags': ['attitude'], 
'url': 'https://favqs.com/quotes/james-welch/5722-the-townspeopl-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'James Welch', 
'author_permalink': 'james-welch', 
'body': "The townspeople outside the reservations had a very superior attitude toward Indians, 
which was kind of funny, 
because they weren't very wealthy 
they were on the fringes of society themselves."}, 
{'id': 6425, 
'dialogue': False, 
'private': False, 
'tags': ['beauty', 
'funny'], 
'url': 'https://favqs.com/quotes/lauren-graham/6425-i-didn-t-grow--', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Lauren Graham', 
'author_permalink': 'lauren-graham', 
'body': "I didn't grow up identifying with beauty. I grew up thinking I could be smart and funny - those are the things I got feedback on."}, 
{'id': 6731, 
'dialogue': False, 
'private': False, 
'tags': ['best', 
'funny', 

'life'], 
'url': 'https://favqs.com/quotes/w-somerset-maugham/6731-it-s-a-funny-t-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'W. Somerset Maugham', 
'author_permalink': 'w-somerset-maugham', 
'body': "It's a funny thing about life if you refuse to accept anything but the best, 
you very often get it."}, 
{'id': 7160, 
'dialogue': False, 
'private': False, 
'tags': ['best', 
'funny'], 
'url': 'https://favqs.com/quotes/david-ogilvy/7160-the-best-ideas-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'David Ogilvy', 
'author_permalink': 'david-ogilvy', 
'body': 'The best ideas come as jokes. Make your thinking as funny as possible.'}, 
{'id': 7354, 
'dialogue': False, 
'private': False, 
'tags': ['best', 
'funny'], 
'url': 'https://favqs.com/quotes/steve-martin/7354-i-ve-always-be-', 
'favorites_count': 0, 

'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Steve Martin', 
'author_permalink': 'steve-martin', 
'body': "I've always believed that there are funny people everywhere, 
but they're just not comedians. In fact, 
some of my best comedic inspirations were not professional entertainers."}, 
{'id': 7434, 
'dialogue': False, 
'private': False, 
'tags': ['best', 
'funny'], 
'url': 'https://favqs.com/quotes/j-k-rowling/7434-the-middle-cla-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'J. K. Rowling', 
'author_permalink': 'j-k-rowling', 
'body': "The middle class is so funny, 
it's the class I know best, 
and it's the class where you find the most pretension, 
so that's what makes the middle classes so funny."}, 
{'id': 7573, 
'dialogue': False, 
'private': 
False, 
'tags': ['best', 
'funny'], 
'url': 'https://favqs.com/quotes/tom-hiddleston/7573-if-you-play-it-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Tom Hiddleston', 
'author_permalink': 'tom-hiddleston', 
'body': "If you play it straight it's funny - the best comedy is always played straight down the middle. The adjustment is understanding from the screenplay that a moment is hilarious."}, 
{'id': 9133, 
'dialogue': False, 
'private': False, 
'tags': ['car', 
'funny', 
'mom'], 
'url': 'https://favqs.com/quotes/criss-angel/9133-it-s-so-funny--', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Criss Angel', 
'author_permalink': 'criss-angel', 
'body': "It's so funny looking back, 
but my so-called overnight success actually took 15 years. I remember when I didn't have any money, 
and my only car was mom's Hyundai."}, 
{'id': 9487, 
'dialogue': False, 
'private': False, 
'tags': ['car', 
'sports'], 
'url': 'https://favqs.com/quotes/corey-stoll/9487-it-s-funny-i-m-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 
'Corey Stoll', 
'author_permalink': 'corey-stoll', 
'body': "It's funny I'm in some ways hopelessly masculine, 
but I don't fish, 
I don't hunt, 
I'm not that into sports. I can't fix a car. I think it's my point of view and the way I see 
the world."}, 
{'id': 25045, 
'dialogue': False, 
'private': False, 
'tags': ['funny'], 
'url': 'https://favqs.com/quotes/maynard-james-keenan/25045-actually-i-ne-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Maynard James Keenan', 
'author_permalink': 'maynard-james-keenan', 
'body': "Actually I never did stand up. I'm not that funny."}, 
{'id': 11461, 
'dialogue': False, 
'private': False, 
'tags': ['cool', 
'funny'], 
'url': 'https://favqs.com/quotes/james-denton/11461-the-promos-wi-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'James Denton', 
'author_permalink': 'james-denton', 
'body': "The promos with all of the beautiful women probably attracted some men, 
but the mystery story line is pretty cool. It's got that dark edge, 
and people will watch anything funny."}, 
{'id': 11523, 
'dialogue': False, 
'private': False, 
'tags': ['cool'], 
'url': 'https://favqs.com/quotes/martin-short/11523-david-lynch-a-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Martin Short', 
'author_permalink': 'martin-short', 
'body': "David Lynch and I almost made a movie together in the late '80s. We 
had lots of dinners and lunches. He's a very cool, 
hip guy. This film, 
let's face it, 
is like an homage to him, 
I would imagine he'd find it funny."}, 
{'id': 11529, 
'dialogue': False, 
'private': False, 
'tags': ['cool'], 
'url': 'https://favqs.com/quotes/matthew-vaughn/11529-i-think-movie-', 
'favorites_count': 0, 
'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Matthew Vaughn', 
'author_permalink': 'matthew-vaughn', 
'body': "I think movies glamorize violence, 
in 
the sense that they make it in a way that it's either cool or funny."}, 
{'id': 11589, 
'dialogue': False, 
'private': False, 
'tags': ['cool'], 
'url': 'https://favqs.com/quotes/dakota-fanning/11589-courtney-love-', 
'favorites_count': 0, 

'upvotes_count': 0, 
'downvotes_count': 0, 
'author': 'Dakota Fanning', 
'author_permalink': 'dakota-fanning', 
'body': 'Courtney Love is really cool and funny. I would like to meet Julia Roberts and Cameron Diaz. I think I could play their daughters.'}]
"""