# Lets create all the possible schemas required so far.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    # Admin here is called the Super Master Application.
    # No registration is required in case you are an Admin.

    __tablename__ = 'admins'
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(100) , unique = True , nullable = False)
    password = db.Column(db.String(100) , nullable = False)

    def __repr__(self):
        return f"<Admin {self.username}>"
    

class User(db.Model):

    # User Model for normal user who register and log in
    __tablename__ = 'users'
    id = db.Column(db.Integer , primary_key = True)
    username = db.Column(db.String(100) , unique = True , nullable = False)
    password = db.Column(db.String(100) , nullable = False)
    full_name = db.Column(db.String(100) , nullable = False)
    qualification = db.Column(db.String(100) , nullable = True)
    dob = db.Column(db.String(20) , nullable = True)

    def __repr__(self):
        return f"<User {self.username}>"
    

class Subject(db.Model):
    # Model for Subject representation
    __tablename__ = 'subjects'
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(100) , nullable = False)
    description = db.Column(db.text , nullable = True)

    chapters = db.relationship('Chapter' , backref = 'subject' , cascade = 'all , delete')

    def __repr__(self):
        return f"<Subject {self.name}>"


class Chapter(db.model):
    __tablename__ = 'chapters'
    id = db.column(db.Integer , primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    subject_id = db.column(db.Integer , db.ForeignKey('subjects.id') , nullable = False)

    #Relationship with the Quiz

    quizzes = db.relationship('Quiz' , backref = 'chapter' , cascade = "all , delete")
    def __repr__(self):
        return f"<chapter {self.name}>"
    
class Quiz(db.Model):
   
    __tablename__ = 'quizzes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date_of_quiz = db.Column(db.String(50), nullable=True)
    time_duration = db.Column(db.String(10), nullable=True)
    remarks = db.Column(db.Text, nullable=True)

    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.id'), nullable=False)

    # Relationship with Question
    questions = db.relationship('Question', backref='quiz', cascade="all, delete")

    def __repr__(self):
        return f"<Quiz {self.name}>"


class Question(db.Model):
   
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question_statement = db.Column(db.Text, nullable=False)
    option1 = db.Column(db.String(200), nullable=False)
    option2 = db.Column(db.String(200), nullable=False)
    option3 = db.Column(db.String(200), nullable=False)
    option4 = db.Column(db.String(200), nullable=False)
    correct_option = db.Column(db.String(10), nullable=False)  # '1', '2', '3', or '4'
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)

    def __repr__(self):
        return f"<Question {self.question_statement[:20]}...>"


class Score(db.Model):
 
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizzes.id'), nullable=False)
    time_stamp_of_attempt = db.Column(db.String(50), nullable=True)
    total_scored = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Score user:{self.user_id} quiz:{self.quiz_id} scor

    