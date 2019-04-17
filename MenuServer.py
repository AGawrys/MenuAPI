from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'MenuServer.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name

class MenuSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name', 'id')

menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)

@app.route("/menu", methods=["POST"])
def add_menu():
    name = request.json['name']
    
    new_menu = Menu(name)

    db.session.add(new_menu)
    db.session.commit()

    return menu_schema.jsonify(new_menu)
        
# show all menu
@app.route("/menu", methods=["GET"])
def get_menu():
    all_menus = Menu.query.all()
    result = menus_schema.dump(all_menus)
    return jsonify(result.data)

# get menu by id
@app.route("/menu/<id>", methods=["GET"])
def menu_detail(id):
    menu = Menu.query.get(id)
    return menu_schema.jsonify(menu)

# update menu
@app.route("/menu/<id>", methods=["PUT"])
def menu_update(id):
    menu = Menu.query.get(id)
    name = request.json['name']

    menu.name = name

    db.session.commit()
    return menu_schema.jsonify(menu)

# to delete menu
@app.route("/menu/<id>", methods=["DELETE"])
def menu_delete(id):
    menu = Menu.query.get(id)
    db.session.delete(menu)
    db.session.commit()

    return menu_schema.jsonify(menu)


if __name__ == '__main__':
    app.run(debug=True)