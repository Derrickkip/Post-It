import click

from models import Users, users

@click.command()
def register():
    """
    Register into account
    """
    click.echo('Register below: ')
    username = input('Enter your username: ')
    email = input('Enter your email: ')
    password = input('Enter your password: ')

    if email not in users:
        new_user = Users(username, email, password)
        users[email] = new_user.__dict__
        click.echo('Login successful...')
    else:
        click.echo('That email already exists')

@click.command()
def login():
    """
    Login into account
    """
    click.echo('Enter your login details: ')
    email = input('Enter your email: ')
    password = input('Enter your password: ')

    if not email in users:
        click.echo('You are not registered!!')
        register()

    click.echo('login successful')


if __name__ == '__main__':
    register()
    #login()
