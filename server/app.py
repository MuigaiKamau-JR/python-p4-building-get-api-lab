#!/usr/bin/env python3

from flask import Flask, make_response, jsonify, abort
from flask_migrate import Migrate
from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json_encoder.compact = False  # Corrected from `app.json.compact`

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    all_bakeries = Bakery.query.all()
    serialized_bakeries = [bakery.to_dict(nested=True) for bakery in all_bakeries]
    return jsonify(serialized_bakeries), 200

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.get(id)
    if bakery is None:
        abort(404)
    serialized_bakery = bakery.to_dict(nested=True)
    return jsonify(serialized_bakery), 200

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    sorted_baked_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
    serialized_baked_goods = [baked_good.to_dict() for baked_good in sorted_baked_goods]
    return jsonify(serialized_baked_goods), 200

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    most_expensive = BakedGood.query.order_by(BakedGood.price.desc()).first()
    if most_expensive is None:
        abort(404)
    serialized_most_expensive = most_expensive.to_dict()
    return jsonify(serialized_most_expensive), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
