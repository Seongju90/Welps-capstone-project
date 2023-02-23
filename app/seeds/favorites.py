from app.models import db, favorites, environment, SCHEMA


def seed_favorites():
    favorite1 = [1,1]
    favorite2 = [2,1]
    favorite3 = [3,1]
    favorite4 = [4,2]
    favorite5 = [5,2]
    favorite6 = [6,2]
    favorite7 = [7,3]
    favorite8 = [8,3]
    favorite9 = [9,3]
    favorite10 = [10,4]
    favorite11 = [1,4]
    favorite12 = [2,4]
    favorite13 = [3,5]
    favorite14 = [4,5]
    favorite15 = [11,5]
    favorite16 = [12,6]
    favorite17 = [13,6]
    favorite18 = [18,6]

    db.session.add(favorite1)
    db.session.add(favorite2)
    db.session.add(favorite3)
    db.session.add(favorite4)
    db.session.add(favorite5)
    db.session.add(favorite6)
    db.session.add(favorite7)
    db.session.add(favorite8)
    db.session.add(favorite9)
    db.session.add(favorite10)
    db.session.add(favorite11)
    db.session.add(favorite12)
    db.session.add(favorite13)
    db.session.add(favorite14)
    db.session.add(favorite15)
    db.session.add(favorite16)
    db.session.add(favorite17)
    db.session.add(favorite18)


def undo_favorites():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.favorites RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM favorites")

    db.session.commit()
