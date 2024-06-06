from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
# Define the Person table for the additional task
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    citta = db.Column(db.String(20))

    def __repr__(self):
        return f"Person('{self.first_name}', '{self.last_name}', '{self.age}', '{self.gender}', '{self.citta}')"

'''
with app.app_context():
    db.create_all()

    # Add a new column "citta" to the "Person" table if it doesn't exist
    try:
        db.session.execute("ALTER TABLE person ADD COLUMN citta VARCHAR(20)")
    except Exception as e:
        print(e)  # Column might already exist, so we can ignore the exception

    # Adding a new column "gender" to the "Person" table if it doesn't exist
    try:
        db.session.execute("ALTER TABLE person ADD COLUMN gender VARCHAR(10)")
    except Exception as e:
        print(e)  # Column might already exist, so we can ignore the exception

    db.session.commit()
'''


with app.app_context():
    db.create_all()


    # Add a new column "citta" to the "Person" table if it doesn't exist
    try:
        db.session.execute("ALTER TABLE person ADD COLUMN Fre String(20)")
        #db.session.execute("ALTER TABLE person ADD COLUMN new TEXT")
        #db.session.execute("ALTER TABLE person ADD COLUMN tryApp VARCHAR(20)")
    except Exception as e:
        print(e)  # Column might already exist, so we can ignore the exception

    # Adding a new column "gender" to the "Person" table if it doesn't exist
    db.session.commit()

    # Update existing records to set a default value for the new column "gender"
persons = Person.query.all()
print(persons)