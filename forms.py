from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional, URL, EqualTo

class LoginForm(FlaskForm):
    username_email = StringField('Usuário ou Email', validators=[
        DataRequired(message='Digite seu usuário ou email para iniciar a missão')
    ])
    password = PasswordField('Senha', validators=[
        DataRequired(message='A senha é necessária para acessar a nave')
    ])
    remember_me = BooleanField('Lembrar-me nesta estação')
    submit = SubmitField('Iniciar Missão 🚀')

class RegisterForm(FlaskForm):
    username = StringField('Nome de Usuário', validators=[
        DataRequired(message='Escolha um nome de astronauta'),
        Length(min=4, max=25, message='Nome deve ter entre 4 e 25 caracteres')
    ])
    
    email = StringField('Email', validators=[
        DataRequired(message='Email é necessário para comunicação espacial'),
        Email(message='Formato de email inválido')
    ])
    
    password = PasswordField('Senha', validators=[
        DataRequired(message='Crie uma senha para proteger sua nave'),
        Length(min=6, message='Senha deve ter pelo menos 6 caracteres')
    ])
    
    password_confirm = PasswordField('Confirmar Senha', validators=[
        DataRequired(message='Confirme sua senha'),
        EqualTo('password', message='As senhas devem ser iguais')
    ])
    
    submit = SubmitField('Entrar na Tripulação 🚀')

class ProjectForm(FlaskForm):
    name = StringField('Nome do Projeto', validators=[
        DataRequired(message='O projeto precisa de um nome'),
        Length(min=2, max=100, message='Nome deve ter entre 2 e 100 caracteres')
    ])
    
    description = TextAreaField('Descrição', validators=[
        DataRequired(message='Descreva seu projeto'),
        Length(min=10, message='Descrição deve ter pelo menos 10 caracteres')
    ])
    
    technologies = StringField('Tecnologias', validators=[
        DataRequired(message='Informe as tecnologias utilizadas')
    ], description='Separe as tecnologias por vírgula (ex: Python, Flask, JavaScript)')
    
    image = FileField('Imagem do Projeto', validators=[
        FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'webp'], 'Apenas imagens são permitidas')
    ])
    
    demo_link = StringField('Link da Demonstração', validators=[
        Optional(),
        URL(message='Insira um URL válido')
    ])
    
    github_link = StringField('Link do GitHub', validators=[
        Optional(),
        URL(message='Insira um URL válido')
    ])
    
    status = SelectField('Status', choices=[
        ('draft', 'Rascunho'),
        ('published', 'Publicado')
    ], default='draft')
    
    submit = SubmitField('Salvar Projeto')

class TechnologyForm(FlaskForm):
    name = StringField('Nome da Tecnologia', validators=[
        DataRequired(message='Nome é obrigatório'),
        Length(min=2, max=50, message='Nome deve ter entre 2 e 50 caracteres')
    ])
    
    icon = StringField('Classe do Ícone', validators=[
        Optional(),
        Length(max=100, message='Classe do ícone muito longa')
    ], description='Ex: fab fa-python, fas fa-code')
    
    category = StringField('Categoria', validators=[
        Optional(),
        Length(max=50, message='Categoria muito longa')
    ])
    
    order = SelectField('Ordem', coerce=int, choices=[
        (i, str(i)) for i in range(1, 21)
    ], default=10)
    
    submit = SubmitField('Salvar Tecnologia')
