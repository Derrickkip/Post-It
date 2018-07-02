import datetime

from models import Users, users, Comments, comments

session = {}

def register():
    """
    Register into account
    """
    print('Register below: ')
    username = input('Enter your username: ')
    email = input('Enter your email: ')
    password = input('Enter your password: ')

    if email not in users:
        new_user = Users(username, email, password)
        users[email] = new_user.__dict__
        print('Signup successful...')
    else:
        print('That email already exists')

def login():
    """
    Login into account
    """
    print('Enter your login details: ')
    email = input('Enter your email: ')
    password = input('Enter your password: ')

    if not email in users:
        print('You are not registered!!')

    session['logged_in'] = email
    print('login successful')

def add_comments():
    """
    add comments
    """
    comment = input("What's on your mind? ")
    timestamp = datetime.time()
    user = session['logged_in']
    new_comment = Comments(comment, timestamp, user)
    if len(comments) == 0:
        comments[1] = new_comment.__dict__
    else:
        comments[len(comments)+1] = new_comment.__dict__

def see_comments():
    """
    get comments
    """
    for key in comments:
        print(comments[key])

def edit_comments(comment_id):
    """
    update comment
    """
    pass
    
register()
login()
add_comments()
see_comments()
