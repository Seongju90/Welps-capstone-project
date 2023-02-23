from app.models import db, restaurant_categories, environment, SCHEMA


def seed_restaurant_categories():
    restaurant1 = [1,1]
    restaurant2 = [2,1]
    restaurant3 = [3,1]
    restaurant4 = [4,1]
    restaurant5 = [5,3]
    restaurant6 = [6,3]
    restaurant7 = [7,3]
    restaurant8 = [8,3]
    restaurant9 = [9,4]
    restaurant10 = [10,4]
    restaurant11 = [11,4]
    restaurant12 = [12,4]
    restaurant13 = [13,5]
    restaurant14 = [14,5]
    restaurant15 = [15,2]
    restaurant16 = [16,2]
    restaurant17 = [17,2]
    restaurant18 = [18,2]
    restaurant19 = [19,6]
    restaurant20 = [20,6]

    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.add(restaurant3)
    db.session.add(restaurant4)
    db.session.add(restaurant5)
    db.session.add(restaurant6)
    db.session.add(restaurant7)
    db.session.add(restaurant8)
    db.session.add(restaurant9)
    db.session.add(restaurant10)
    db.session.add(restaurant11)
    db.session.add(restaurant12)
    db.session.add(restaurant13)
    db.session.add(restaurant14)
    db.session.add(restaurant15)
    db.session.add(restaurant16)
    db.session.add(restaurant17)
    db.session.add(restaurant18)
    db.session.add(restaurant19)
    db.session.add(restaurant20)

    db.session.commit()

def undo_restaurant_categories():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.restaurant_categories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM restaurant_categories")

    db.session.commit()
