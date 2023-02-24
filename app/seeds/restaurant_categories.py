from app.models import db, restaurant_categories, Category, Restaurant, environment, SCHEMA


def seed_restaurant_categories():

    kunjip = Restaurant.query.get(1)
    chungdam = Restaurant.query.get(2)
    daeho = Restaurant.query.get(3)
    tenbutchers = Restaurant.query.get(4)
    sumiya = Restaurant.query.get(5)
    rantei = Restaurant.query.get(6)
    izakaya = Restaurant.query.get(7)
    amami = Restaurant.query.get(8)
    thetable = Restaurant.query.get(9)
    lazydog = Restaurant.query.get(10)
    eureka = Restaurant.query.get(11)
    stjohn = Restaurant.query.get(12)
    mcdonalds = Restaurant.query.get(13)
    chickfila = Restaurant.query.get(14)
    tongsoon = Restaurant.query.get(15)
    lockchun = Restaurant.query.get(16)
    sifu = Restaurant.query.get(17)
    paiknoodle = Restaurant.query.get(18)
    sunright = Restaurant.query.get(19)
    jiaren = Restaurant.query.get(20)

    korean = Category.query.get(1)
    chinese = Category.query.get(2)
    japanese = Category.query.get(3)
    american = Category.query.get(4)
    fastfood = Category.query.get(5)
    drinks = Category.query.get(6)

    # able to use appened, or any list method because property types is a list
    kunjip.types.append(korean)
    chungdam.types.append(korean)
    daeho.types.append(korean)
    tenbutchers.types.append(korean)
    sumiya.types.append(japanese)
    rantei.types.append(japanese)
    izakaya.types.append(japanese)
    amami.types.append(japanese)
    thetable.types.append(american)
    lazydog.types.append(american)
    eureka.types.append(american)
    stjohn.types.append(american)
    mcdonalds.types.extend([fastfood, drinks])
    chickfila.types.extend([fastfood, drinks])
    sifu.types.append(chinese)
    tongsoon.types.append(chinese)
    lockchun.types.append(chinese)
    paiknoodle.types.append(chinese)
    sunright.types.append(drinks)
    jiaren.types.append(drinks)

    db.session.commit()

def undo_restaurant_categories():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.restaurant_categories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM restaurant_categories")

    db.session.commit()
