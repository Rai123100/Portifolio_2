from app import db
from models import User, Technology

def init_admin_user():
    """Initialize admin user and default technologies"""
    # Check if admin user exists
    admin = User.query.filter_by(email='raicarvalho343@gmail.com').first()
    
    if not admin:
        admin = User(
            username='Rai123100',
            email='raicarvalho343@gmail.com',
            is_admin=True
        )
        admin.set_password('rai123100')
        db.session.add(admin)
        print("Administrador criado: Rai123100")
    
    # Initialize default technologies if none exist
    if Technology.query.count() == 0:
        technologies = [
            {'name': 'HTML', 'icon': 'fab fa-html5', 'category': 'Frontend', 'order': 1},
            {'name': 'CSS', 'icon': 'fab fa-css3-alt', 'category': 'Frontend', 'order': 2},
            {'name': 'Bootstrap', 'icon': 'fab fa-bootstrap', 'category': 'Frontend', 'order': 3},
            {'name': 'JavaScript', 'icon': 'fab fa-js-square', 'category': 'Frontend', 'order': 4},
            {'name': 'Node.js', 'icon': 'fab fa-node-js', 'category': 'Backend', 'order': 5},
            {'name': 'Python', 'icon': 'fab fa-python', 'category': 'Backend', 'order': 6},
            {'name': 'Git', 'icon': 'fab fa-git-alt', 'category': 'Tools', 'order': 7},
            {'name': 'GitHub', 'icon': 'fab fa-github', 'category': 'Tools', 'order': 8},
            {'name': 'SQL Server', 'icon': 'fas fa-database', 'category': 'Database', 'order': 9},
            {'name': 'SASS', 'icon': 'fab fa-sass', 'category': 'Frontend', 'order': 10},
            {'name': 'Figma', 'icon': 'fab fa-figma', 'category': 'Design', 'order': 11},
            {'name': 'Google Cloud', 'icon': 'fab fa-google', 'category': 'Cloud', 'order': 12},
            {'name': 'AWS', 'icon': 'fab fa-aws', 'category': 'Cloud', 'order': 13}
        ]
        
        for tech_data in technologies:
            tech = Technology(**tech_data)
            db.session.add(tech)
        
        print("Tecnologias padrão adicionadas")
    
    db.session.commit()
