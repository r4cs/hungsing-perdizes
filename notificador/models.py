from notificador import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime

# By inheriting the UserMixin we get access to a lot of built-in attributes
# which we will be able to call in our views!
# is_authenticated()
# is_active()
# is_anonymous()
# get_id()

# The user_loader decorator allows flask-login to load the current user
# and grab their id.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    # Create a table in the db
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), index=True)
    enrollment = db.Column(db.Integer)
    username = db.Column(db.String(64))
    last_name = db.Column(db.String())

    beginer = db.Column(db.Boolean)
    interm = db.Column(db.Boolean)
    adv = db.Column(db.Boolean)
    t_kids = db.Column(db.Boolean)
    t_tigres = db.Column(db.Boolean)
    t_sanda = db.Column(db.Boolean)
    t_mat = db.Column(db.Boolean)
    t_vesp = db.Column(db.Boolean)
    t_not = db.Column(db.Boolean)
    t_sab = db.Column(db.Boolean)

    franchise = db.Column(db.String())
    cellphone = db.Column(db.String)
    password = db.Column(db.String(20))
    password_hash = db.Column(db.String(252))
    registered_on = db.Column(db.DateTime, nullable=False)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, enrollment, username, last_name, beginer, interm, adv, t_kids,t_tigres, t_sanda, t_mat, t_vesp, t_not, t_sab, franchise, cellphone, password, confirmed):
        self.email = email
        self.enrollment = enrollment
        self.username = username
        self.last_name = last_name

        self.beginer = beginer
        self.interm = interm
        self.adv = adv
        self.t_kids = t_kids
        self.t_tigres = t_tigres
        self.t_sanda = t_sanda
        self.t_mat = t_mat
        self.t_vesp = t_vesp
        self.t_not = t_not
        self.t_sab = t_sab

        self.franchise = franchise
        self.cellphone = cellphone
        self.password = password
        self.password_hash = generate_password_hash(password)
        self.registered_on = datetime.datetime.now()
        self.confirmed = confirmed

    def check_password(self, password):
        # https://stackoverflow.com/questions/23432478/flask-generate-password-hash-not-constant-output
        return check_password_hash(self.password_hash, password)

    def json(self):
        return {'name': self.username, 'Last name': self.last_name, 'email': self.email,
                'age': self.age, 'nível': self.level}

    def __repr__(self):
        return f"UserName: {self.username}"

    def __str__(self):
        return f'User ID: {self.id}'


class DelUser(db.Model, UserMixin):

    __tablename__ = 'deleted_users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    enrollment = db.Column(db.Integer)
    username = db.Column(db.String(64))
    last_name = db.Column(db.String())

    beginer = db.Column(db.Boolean)
    interm = db.Column(db.Boolean)
    adv = db.Column(db.Boolean)
    t_kids = db.Column(db.Boolean)
    t_tigres = db.Column(db.Boolean)
    t_sanda = db.Column(db.Boolean)
    t_mat = db.Column(db.Boolean)
    t_vesp = db.Column(db.Boolean)
    t_not = db.Column(db.Boolean)
    t_sab = db.Column(db.Boolean)

    franchise = db.Column(db.String())
    cellphone = db.Column(db.String(), unique=True)
    deleted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, email, enrollment, username, last_name, franchise, beginer, interm, adv, t_kids, t_tigres, t_sanda, t_mat, t_vesp, t_not, t_sab, cellphone): # level
        self.email = email
        self.enrollment = enrollment
        self.username = username
        self.last_name = last_name

        self.beginer = beginer
        self.interm = interm
        self.adv = adv
        self.t_kids = t_kids
        self.t_tigres = t_tigres
        self.t_sanda = t_sanda
        self.t_mat = t_mat
        self.t_vesp = t_vesp
        self.t_not = t_not
        self.t_sab = t_sab

        self.franchise = franchise
        self.cellphone = cellphone
        self.deleted_on = datetime.datetime.now()

    def __repr__(self):
        return f"UserName: {self.username}"

    def __str__(self):
        return f'User ID: {self.id}'
