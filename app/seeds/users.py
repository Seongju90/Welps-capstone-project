from app.models import db, User, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo',
        email='demo@aa.io',
        password='password',
        first_name='De',
        last_name='Mo',
        )
    marnie = User(
        username='marnie',
        email='marnie@aa.io',
        password='password',
        first_name='Mar',
        last_name='Nie',
        )
    bobbie = User(
        username='bobbie',
        email='bobbie@aa.io',
        password='password',
        first_name='Bob',
        last_name='Bie',
        )
    philip = User(
        username='soju',
        email='philip@gmail.com',
        password='password',
        first_name='Philip',
        last_name='Lee',
        )
    michelle = User(
        username='myoung',
        email='michelle@gmail.com',
        password='password',
        first_name='Michelle',
        last_name='Park',
        )
    lois = User(
        username='lolo',
        email='lois@gmail.com',
        password='password',
        first_name='Lois',
        last_name='Lee',
        )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(philip)
    db.session.add(michelle)
    db.session.add(lois)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.commit()
