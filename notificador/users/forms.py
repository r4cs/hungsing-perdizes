from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from notificador.models import User
from flask import request


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Entre')


class RegistrationForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])

    enrollment = IntegerField('Matrícula', validators=[DataRequired()], render_kw={"placeholder":
    "Seu número de matrícula Hung Sing"})

    username = StringField('Nome', validators=[DataRequired()])

    last_name = StringField('Sobrenome', validators=[DataRequired()])

    franchise = SelectField(u'Unidade', choices=[
        ('perdizes', 'Perdizes'),
        ('pacaembu', 'Pacaembu')
    ],
                      validators=[DataRequired()]
                      )

    # beginer = BooleanField(u'Iniciante')
    #
    # interm = BooleanField(u"Intermediário")
    #
    # adv = BooleanField(u"Avançado")
    #
    # t_kids = BooleanField(u"Kids")
    #
    # t_tigres = BooleanField(u"Tigres")
    #
    # t_sanda = BooleanField(u"Sanda")
    #
    # t_manha = BooleanField(u"Aulas matutina")
    #
    # t_vesp = BooleanField(u"Aulas vespertinas")
    #
    # t_noite = BooleanField(u"Aulas noturnas")
    #
    # t_sabado = BooleanField(u"Aulas aos sábado")

    cellphone = StringField('Celular com DDD', validators=[DataRequired()], render_kw={"placeholder":
    "ex: 11912345678"})

    password = PasswordField('Senha', validators=[
        DataRequired(),
        EqualTo('pass_confirm', message='As senhas devem coincidir!')
    ]
                             )

    pass_confirm = PasswordField('Confirmar senha', validators=[DataRequired()])

    submit = SubmitField('Confirmar!')

    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Seu email já está registrado.')

    def check_enrollment(self, field):
        # Check if not None for that username!
        if User.query.filter_by(enrollment=field.data).first():
            raise ValidationError('Desculpe, matrícula já cadastrsada. Contate a adminstradora.')


class UpdateUserForm(FlaskForm):
    # username = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])

    cellphone = StringField('Celular', validators=[DataRequired()], render_kw={"placeholder":
    "com DDD - ex: 11912345678"})

    franchise = SelectField(u'Unidade', choices=[
        ('perdizes', 'Perdizes'),
        ('pacaembu', 'Pacaembu')
    ],
                      validators=[DataRequired()]
                      )


    submit = SubmitField('Atualizar')

    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Este email já está registrado')
    #
    # def check_username(self, field):
    #     # Check if not None for that username!
    #     if User.query.filter_by(username=field.data).first():
    #         raise ValidationError('Sorry, that username is taken!')


class DeleteUserForm(FlaskForm):
    submit = SubmitField('Apagar usuário !')
