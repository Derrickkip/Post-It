users = {}
comments = {}

class Users:
    """Class contains users cases"""
    def __init__(self, username, email, password, is_moderator=False, is_admin=False):
        self.username = username
        self.email = email
        self.password = password
        self.is_moderator = is_moderator
        self.is_admin = is_admin
        


class Comments:
    """class contains comments cases"""
    def __init__(self, comment, timestamp, user):
        self.comment = comment
        self.timestamp = timestamp
        self.user = user
