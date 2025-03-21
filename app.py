# This is the main entry point of our Flask Application

from flask import Flask , render_template , url_for , redirect

from models.models import db , Admin , User ,  Subject , Quiz , Chapter , Score , Question

from controllers.admin_controller import admin_bp
from controllers.user_controller import user_bp
from controllers.quiz_controller import quiz_bp

def create_app():

    # Create an instance of Flask app now.

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'ABHIST_JAIN'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_master.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint( admin_bp , url_prefix = '/admin')
    app.register_blueprint( user_bp , url_prefix = '/user')
    app.register_blueprint(quiz_bp , url_prefix = '/quiz')

    @app.before_first_request
    def create_tables_and_admin():

        db.create_all()
        # Create all database tables required.

        # Check if Admin user exists or not and if not create it by default.
        existing_admin = Admin.query.first()

        if not existing_admin:
            admin_user = Admin(username = 'admin@gmail.com' , password = 'Admin1234')
            db.session.add(admin_user)
            db.session.commit()

    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app

if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug = True)
