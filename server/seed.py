#!/usr/bin/env python3

from random import choice as rc
from app import app
from models import db, Bakery, BakedGood
from datetime import datetime

with app.app_context():
    db.drop_all()
    db.create_all()

    bakeries = []
    bakeries.append(Bakery(name='Delightful donuts', created_at=datetime.now()))
    bakeries.append(Bakery(name='Incredible crullers', created_at=datetime.now()))
    db.session.add_all(bakeries)
    db.session.commit()

    baked_goods = []
    baked_goods.append(BakedGood(name='Chocolate dipped donut', price=2.75, bakery=bakeries[0], created_at=datetime.now()))
    baked_goods.append(BakedGood(name='Apple-spice filled donut', price=3.50, bakery=bakeries[0], created_at=datetime.now()))
    baked_goods.append(BakedGood(name='Glazed honey cruller', price=3.25, bakery=bakeries[1], created_at=datetime.now()))
    baked_goods.append(BakedGood(name='Chocolate cruller', price=3.40, bakery=bakeries[1], created_at=datetime.now()))
    db.session.add_all(baked_goods)
    db.session.commit()

