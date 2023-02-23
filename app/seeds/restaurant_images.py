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
        'restaurant_id': ,
        'url': '',
        'preview': False
    },
    {
        'restaurant_id': ,
        'url': '',
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
