from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))

    citta = db.Column(db.String(20))

    def __repr__(self):
        return f"Person('{self.first_name}', '{self.last_name}', '{self.age}', '{self.gender}')"

with app.app_context():
    # Aggiungi la colonna "gender" alla tabella "person"
    db.session.execute("ALTER TABLE person ADD COLUMN citta VARCHAR(20)")
    #db.session.execute("ALTER TABLE person ADD COLUMN gender VARCHAR(10)")
    db.session.commit()

    # Crea un oggetto Person con i dati esistenti
    persons = Person.query.all()

    # Aggiorna i dati esistenti con un valore predefinito per la colonna "gender"
    for person in persons:
        person.gender = "M"  # Imposta un valore predefinito, ad esempio "M" per maschio
        db.session.add(person)
    db.session.commit()