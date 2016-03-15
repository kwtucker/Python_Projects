from app import db


# class DevPost(db.Model):
#     __tablename__ = "posts"

#     id      = db.Column(db.Integer, primary_key=True)
#     title   = db.Column(db.String(120), nullable=False)
#     author  = db.Column(db.String(120), nullable=False)
#     content = db.Column(db.Text, nullable=False)

#     def __init__(self, title, author, content):
#         self.title   = title
#         self.author  = author
#         self.content = content

#     def __repr__(self):
#         return '{}'.format(self.title)


# class Users(db.Model):
#     __tablename__ = "users"

#     id            = db.Column(db.Integer, primary_key=True)
#     user_name     = db.Column(db.String(120), nullable=True)
#     user_email    = db.Column(db.String(120), nullable=True)
#     user_password = db.Column(db.String(120), nullable=True)
#     github_access_token   = db.Column(db.String(255), nullable=True)

#     def __init__(self, user_name, user_email, user_password, github_access_token):
#         self.user_name     = user_name
#         self.user_email    = user_email
#         self.user_password = user_password
#         self.github_access_token   = github_access_token

#     def __repr__(self):
#         return '{}'.format(self.user_name)

class Users(db.Model):
    __tablename__ = "Users"

    id                    = db.Column(db.Integer, primary_key=True)
    the_user_id           = db.relationship('UserSettings', backref='Users', lazy='dynamic')
    github_access_token   = db.Column(db.String(255), nullable=True)


    def __init__(self, github_access_token):
        # self.user_id               = the_user_id
        self.github_access_token   = github_access_token

    def __repr__(self):
        return '{}'.format(self.github_access_token)


class Settings(db.Model):
    __tablename__ = "Settings"

    id                    = db.Column(db.Integer, primary_key=True)
    set_id                = db.relationship('UserSettings', backref='Settings', lazy='dynamic')
    name                  = db.Column(db.String(120))


    def __init__(self, name):
        # self.set_id = set_id
        self.name   = name

    def __repr__(self):
        return '{}'.format(self.name)

class UserSettings(db.Model):
    __tablename__ = "UserSettings"
    id                    = db.Column(db.Integer, primary_key=True)
    user_id               = db.Column(db.Integer,db.ForeignKey('Users.id'), primary_key=True)
    setting_id            = db.Column(db.Integer,db.ForeignKey('Settings.id'), primary_key=True)
    value                 = db.Column(db.String(120))


    def __init__(self, user_id, setting_id, value):
        self.user_id          = user_id
        self.setting_id       = setting_id
        self.value            = value

    def __repr__(self):
        return '{}'.format(self.setting_id)


