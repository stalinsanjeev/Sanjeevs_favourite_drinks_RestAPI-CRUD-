from flask import Flask, request
import os
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)










base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, "data.db")}'
db = SQLAlchemy(app)



class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))


    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return 'hello welcome to sanjeev page please use /drinks for all drinks /drinks/<id> for specific /drinks[POST] with name and description to update the list'


@app.route('/drinks')
def getdrinks():
    drinks = Drink.query.all()
    print(drinks)
    output = []
    for drink in drinks:
        drink_data = {'Rank':drink.id,'name':drink.name, 'description':drink.description}

        output.append(drink_data)

    return {'drinks': output }

@app.route('/drinks/<id>')
def getdrink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name , "description": drink.description}


@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return { 'id':drink.id}


@app.route('/drinks/<id>', methods=['DELETE'])
def deletedrink(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error":"not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message":"deleted lol"}


# Ensure the table is created when the app is run
with app.app_context():
    db.create_all()

# Required to run the app on Hugging Face Spaces
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)