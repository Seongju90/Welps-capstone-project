from app.models import db, favorites, User, Restaurant, environment, SCHEMA
import random

def seed_favorites():
    # query all the users
    all_users = User.query.all()

    for user in all_users:
        favorite1 = Restaurant.query.get(random.randint(1,7))
        favorite2 = Restaurant.query.get(random.randint(9,13))
        favorite3 = Restaurant.query.get(random.randint(14,20))

        user.favorite.append(favorite1)
        user.favorite.append(favorite2)
        user.favorite.append(favorite3)

    db.session.commit()


def undo_favorites():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.favorites RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM favorites")

    db.session.commit()
