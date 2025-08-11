# Overview

This is a complete Flask-based astronaut-themed portfolio website for developer Raí. The application includes user authentication, admin dashboard for project management, technology carousel display, and modern space-themed UI design. All requested features have been implemented including the admin user (Rai123100), social media links, and technologies carousel with HTML, CSS, Bootstrap, Git, GitHub, Node.js, JavaScript, SQL Server, Python, SASS, Figma, Google Cloud, and AWS.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Web Framework
- **Flask**: Core web framework providing routing, templating, and request handling
- **Flask-SQLAlchemy**: Database ORM for model definitions and queries
- **Flask-Login**: User session management and authentication
- **Flask-WTF**: Form handling with CSRF protection and validation
- **WTForms**: Form field definitions and server-side validation

## Frontend Architecture
- **Jinja2 Templates**: Server-side rendered HTML with template inheritance
- **Bootstrap 5**: Responsive CSS framework for layout and components
- **Custom CSS**: Space-themed styling with glassmorphism effects and animations
- **Font Awesome**: Icon library for UI elements
- **JavaScript**: Client-side interactivity for carousels, animations, and smooth scrolling

## Database Design
- **SQLite**: Default development database (configurable via DATABASE_URL)
- **User Model**: Authentication with username, email, password hash, and admin privileges
- **Project Model**: Portfolio projects with name, description, technologies, images, and status
- **Technology Model**: Tech stack items with icons, categories, and display order
- **Certificate Model**: Professional certifications (structure defined but implementation incomplete)

## Authentication & Authorization
- **Password Hashing**: Werkzeug security for password storage
- **Session Management**: Flask-Login for user sessions with remember-me functionality
- **Role-based Access**: Admin flag on User model for dashboard access
- **Login Protection**: Route decorators for protected admin areas

## File Management
- **File Uploads**: Image upload system for project portfolios
- **File Validation**: Extension and size restrictions for security
- **UUID Naming**: Unique filenames to prevent conflicts
- **Static File Serving**: Flask static file handling for uploaded images

## Application Structure
- **MVC Pattern**: Clear separation between models, views (templates), and controllers (routes)
- **Form Classes**: Dedicated form classes for validation and rendering
- **Utility Functions**: Helper functions for file handling and data formatting
- **Error Handling**: Custom 404 and 500 error pages with space theme
- **Configuration**: Environment-based configuration for database and secret keys

# External Dependencies

## Core Framework Dependencies
- **Flask**: Web framework
- **Flask-SQLAlchemy**: Database ORM
- **Flask-Login**: Authentication management
- **Flask-WTF**: Form handling
- **WTForms**: Form validation
- **Werkzeug**: WSGI utilities and security functions

## Frontend Libraries
- **Bootstrap 5.3.0**: CSS framework (CDN)
- **Font Awesome 6.4.0**: Icon library (CDN)
- **Google Fonts**: Orbitron and Exo 2 fonts (CDN)

## Database
- **SQLite**: Default database (development)
- **Database URL**: Configurable for production databases via environment variable

## File Storage
- **Local File System**: Image uploads stored in uploads/ directory
- **File Size Limits**: 16MB maximum upload size configured

## Deployment Configuration
- **ProxyFix**: Werkzeug middleware for reverse proxy headers
- **Environment Variables**: DATABASE_URL and SESSION_SECRET for configuration
- **Debug Mode**: Configurable Flask debug setting