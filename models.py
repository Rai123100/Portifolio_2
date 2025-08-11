from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        """Set password hash"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check password against hash"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    technologies = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(200))
    demo_link = db.Column(db.String(200))
    github_link = db.Column(db.String(200))
    status = db.Column(db.String(20), default='draft')  # 'published' or 'draft'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Project {self.name}>'

class Technology(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(100))  # Font Awesome icon class
    category = db.Column(db.String(50))
    order = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Technology {self.name}>'

class Certificate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    issuer = db.Column(db.String(100), nullable=False)
    date_issued = db.Column(db.Date, nullable=False)
    certificate_url = db.Column(db.String(200))
    image = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Certificate {self.name}>'
