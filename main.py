from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10), default='M')
    citta = db.Column(db.String(20))

    def __repr__(self):
        print("line 20" ,self.first_name)
        return f"Person('{self.first_name}', '{self.last_name}', '{self.age}', '{self.gender}')"

with app.app_context():
    db.create_all()


@app.route('/add_person', methods=['POST'])
def add_person():
    data = request.json
    print("line 30",data['first_name'])
    new_person = Person(
        first_name=data['first_name'],
        last_name=data['last_name'],
        age=data['age'],
        gender=data.get('gender', 'M'),  # Default to 'M' if not provided
        citta=data.get('citta', '')      # Default to empty string if not provided
    )
    db.session.add(new_person)
    db.session.commit()
    return jsonify({"message": "Person added successfully"}), 201


@app.route('/search_person', methods=['GET'])
def search_person():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    print(f"first_name  ",first_name )

    query = Person.query
    if first_name:
        query = query.filter(Person.first_name.like(f'%{first_name}%'))
    if last_name:
        query = query.filter(Person.last_name.like(f'%{last_name}%'))

    persons = query.all()
    results = [
        {
            "first_name": person.first_name,
            "last_name": person.last_name,
            "age": person.age,
            "gender": person.gender,
            "citta": person.citta
        } for person in persons
    ]
    return jsonify(results), 200


@app.route('/update_person/<int:id>', methods=['PUT'])
def update_person(id):
    data = request.json
    person = Person.query.get(id)
    if not person:
        return jsonify({"message": "Person not found"}), 404

    person.first_name = data.get('first_name', person.first_name)
    person.last_name = data.get('last_name', person.last_name)
    person.age = data.get('age', person.age)
    person.gender = data.get('gender', person.gender)
    person.citta = data.get('citta', person.citta)

    db.session.commit()
    return jsonify({"message": "Person updated successfully"}), 200


@app.route('/delete_person/<int:id>', methods=['DELETE'])
def delete_person(id):
    person = Person.query.get(id)
    if not person:
        return jsonify({"message": "Person not found"}), 404

    db.session.delete(person)
    db.session.commit()
    return jsonify({"message": "Person deleted successfully"}), 200
if __name__ == '__main__':
    app.run(debug=True)
