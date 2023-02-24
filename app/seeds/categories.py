from app.models import db, Category, environment, SCHEMA


categories = ['Korean', 'Chinese', 'Japanese', 'American', 'Fast Food', 'Drinks']


def seed_categories():

    for category in categories:
        new_type = Category(
            type = category
        )

        db.session.add(new_type)
        db.session.commit()


def undo_categories():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.categories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM categories")

    db.session.commit()
