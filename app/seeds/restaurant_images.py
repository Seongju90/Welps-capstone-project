from app.models import db, RestaurantImage, environment, SCHEMA


restaurant_images = [
    {
        'restaurant_id': 1,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/lg4B19Wrv6YX2m_2ydzzWQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 1,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/Rv2NW1HUoHAxCuyVeZRuzg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 1,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/2ce6UOYBfi3jD4BYpXAVKA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 1,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/oHv2vvfo4QkHMLax6VowiA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 1,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/oJbM01d4abPHMvDYiJ5qIg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 2,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/Net3aAui3voR5e5BXmsSgg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 2,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/Q6c-munP4AU73rEyJqQQLQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 2,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/gBM8z271992OKoyPZzUtoA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 2,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/Nvu2OERrSxCB6rXfvA9Yeg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 2,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/yJVW9K2N_FXQlX480HMuSQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 3,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/ZvIAUxNhxcmc_xuTXeRJMg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 3,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/Uli1eQ_iuD8-5lTybO36HA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 3,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/Z4wBWAIyd2xdaBYie3yhMw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 3,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/-ngpZOG46kIWvjABY-ARxA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 3,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/9rSAKTSb49-OMcc9QbXjxA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 4,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/OOeMaed2Dqu6qMS6XpHB4g/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 4,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/zuCuHodvu9q3OYsznqO8JQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 4,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/b3SJgqH-YIHokuts0-h3Xw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 4,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/G7h00dsI34KtBTQKhkVzNw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 4,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/apghWAHqvrgkEpuyjuZlvw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 5,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/BR8Wkm_XTB9iVnbq92sdhA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 5,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/oHyzfNwEQ20UljExmQrbww/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 5,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/dUhQd2W2wLp-PQOvAvilDQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 5,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/5w50SqIfArLefcZaCnB9Cg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 6,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/fSFlsSYVmjJsIryM-D3jdA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 6,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/PmfT0CR9XhVPOb69CKojig/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 6,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/RZ23FxmXuRH3s4BaUXqLEw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 6,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/F97kUE5HQN_mqv3Tvk_m9Q/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 7,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/1AussqtbyeeSYSFzYLwMsA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 7,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/PB0IYRIgCtjR4_08nrYxyA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 7,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/pS44AuffGJ12fNB0PQHtTg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 7,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/XPzpeRmpACO3mgeO1GBZoA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 8,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/r2GXyUlICiNrfkINd3creA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 8,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/M4WyXT3ytSvDN9rT2k8cbw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 8,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/hCcpJR8VfxsdLKbISu9eVQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 8,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/-SxaJ38SVYxPW5eR_iZxHA/348s.jpg',
        'preview': False
    },
]


def seed_restaurants():
    pass
def undo_restaurants():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.restaurant_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM restaurant_images")

    db.session.commit()
