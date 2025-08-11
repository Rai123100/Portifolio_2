from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.utils import secure_filename
from app import app, db
from models import User, Project, Technology, Certificate
from forms import LoginForm, RegisterForm, ProjectForm
from utils import allowed_file, save_uploaded_file
import os

@app.route('/')
def index():
    """Homepage with portfolio sections"""
    # Get published projects
    projects = Project.query.filter_by(status='published').order_by(Project.created_at.desc()).all()
    
    # Get technologies for carousel
    technologies = Technology.query.order_by(Technology.order, Technology.name).all()
    
    # Get certificates
    certificates = Certificate.query.order_by(Certificate.date_issued.desc()).all()
    
    return render_template('index.html', 
                         projects=projects, 
                         technologies=technologies,
                         certificates=certificates)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Astronaut-themed login page"""
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard') if current_user.is_admin else url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(
            (User.username == form.username_email.data) | 
            (User.email == form.username_email.data)
        ).first()
        
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash(f'Bem-vindo ao espaço, {user.username}! 🚀', 'success')
            
            next_page = request.args.get('next')
            if not next_page or not next_page.startswith('/'):
                next_page = url_for('admin_dashboard') if user.is_admin else url_for('index')
            return redirect(next_page)
        else:
            flash('Coordenadas de acesso inválidas. Verifique suas credenciais. 🛸', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration page"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        # Check if username already exists
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            flash('Este nome de astronauta já está em uso. Escolha outro! 🚀', 'danger')
            return render_template('register.html', form=form)
        
        # Check if email already exists
        existing_email = User.query.filter_by(email=form.email.data).first()
        if existing_email:
            flash('Este email já está registrado na estação espacial! 📡', 'danger')
            return render_template('register.html', form=form)
        
        # Create new user
        user = User(
            username=form.username.data,
            email=form.email.data,
            is_admin=False  # New users are not admin by default
        )
        user.set_password(form.password.data)
        
        db.session.add(user)
        db.session.commit()
        
        flash('Conta criada com sucesso! Bem-vindo à tripulação! 🌌', 'success')
        login_user(user)
        return redirect(url_for('index'))
    
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    """Logout user"""
    logout_user()
    flash('Desconectado com sucesso. Até a próxima missão! 🌌', 'info')
    return redirect(url_for('index'))

@app.route('/admin')
@login_required
def admin_dashboard():
    """Admin dashboard - only accessible by admin users"""
    if not current_user.is_admin:
        flash('Acesso negado. Área restrita para comandantes da estação! 🛰️', 'danger')
        return redirect(url_for('index'))
    
    projects = Project.query.order_by(Project.created_at.desc()).all()
    technologies = Technology.query.order_by(Technology.order, Technology.name).all()
    certificates = Certificate.query.order_by(Certificate.date_issued.desc()).all()
    
    return render_template('admin_dashboard.html', 
                         projects=projects,
                         technologies=technologies,
                         certificates=certificates)

@app.route('/admin/project/new', methods=['GET', 'POST'])
@login_required
def new_project():
    """Create new project"""
    if not current_user.is_admin:
        flash('Acesso negado. Área restrita para comandantes da estação! 🛰️', 'danger')
        return redirect(url_for('index'))
    
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project()
        form.populate_obj(project)
        
        # Handle file upload
        if form.image.data:
            filename = save_uploaded_file(form.image.data, 'projects')
            if filename:
                project.image = filename
        
        db.session.add(project)
        db.session.commit()
        
        flash(f'Projeto "{project.name}" criado com sucesso! 🚀', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('project_form.html', form=form, title='Novo Projeto')

@app.route('/admin/project/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_project(id):
    """Edit existing project"""
    if not current_user.is_admin:
        flash('Acesso negado. Área restrita para comandantes da estação! 🛰️', 'danger')
        return redirect(url_for('index'))
    
    project = Project.query.get_or_404(id)
    form = ProjectForm(obj=project)
    
    if form.validate_on_submit():
        form.populate_obj(project)
        
        # Handle file upload
        if form.image.data:
            filename = save_uploaded_file(form.image.data, 'projects')
            if filename:
                project.image = filename
        
        db.session.commit()
        
        flash(f'Projeto "{project.name}" atualizado com sucesso! 🛸', 'success')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('project_form.html', form=form, title='Editar Projeto', project=project)

@app.route('/admin/project/<int:id>/delete', methods=['POST'])
@login_required
def delete_project(id):
    """Delete project"""
    if not current_user.is_admin:
        flash('Acesso negado. Área restrita para comandantes da estação! 🛰️', 'danger')
        return redirect(url_for('index'))
    
    project = Project.query.get_or_404(id)
    
    # Delete associated image file
    if project.image:
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], 'projects', project.image))
        except OSError:
            pass
    
    db.session.delete(project)
    db.session.commit()
    
    flash(f'Projeto "{project.name}" removido da galáxia! 🌌', 'success')
    return redirect(url_for('admin_dashboard'))

@app.route('/project/<int:id>')
def project_detail(id):
    """View single project details"""
    project = Project.query.filter_by(id=id, status='published').first_or_404()
    return render_template('project_detail.html', project=project)

@app.errorhandler(404)
def not_found(error):
    """404 error handler"""
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """500 error handler"""
    db.session.rollback()
    return render_template('errors/500.html'), 500
