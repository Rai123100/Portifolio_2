import os
import uuid
from werkzeug.utils import secure_filename
from app import app

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg'}

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_file(file, folder):
    """Save uploaded file and return filename"""
    if file and allowed_file(file.filename):
        # Create unique filename to avoid conflicts
        filename = str(uuid.uuid4()) + '.' + file.filename.rsplit('.', 1)[1].lower()
        
        # Create upload directory if it doesn't exist
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], folder)
        os.makedirs(upload_path, exist_ok=True)
        
        # Save file
        file_path = os.path.join(upload_path, filename)
        file.save(file_path)
        
        return filename
    return None

def format_technologies(tech_string):
    """Format comma-separated technologies into a list"""
    if not tech_string:
        return []
    return [tech.strip() for tech in tech_string.split(',') if tech.strip()]
