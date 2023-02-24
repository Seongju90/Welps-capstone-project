from app.models import db, ReviewImage, environment, SCHEMA

review_image_list = [
    {
        'review_id': 1,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/QkcGDPppUrXaLeI-eBAliQ/348s.jpg',
    },
    {
        'review_id': 2,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/wKX3AozjBIlprjkZj1jKZw/348s.jpg',
    },
    {
        'review_id': 3,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/cWRSqtqyQMumN9TDA2Z1Fg/348s.jpg',
    },
    {
        'review_id': 4,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/DmwY_1Sno6fnsctzPiKCFg/348s.jpg',
    },
    {
        'review_id': 5,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/F7t8yqMO5m1ErzA5qyuKsw/348s.jpg',
    },
    {
        'review_id': 6,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/oZUq6LjQJ8nDtbTBwvjs2A/348s.jpg',
    },
    {
        'review_id': 7,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/1YN7Fl6kiUdRVoqTsPwGXA/348s.jpg',
    },
    {
        'review_id': 8,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/7fQvtxK7dF8VEQUgjE9z5w/348s.jpg',
    },
    {
        'review_id': 9,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/5om13kgNSeM0-5oLZzPWNQ/348s.jpg',
    },
    {
        'review_id': 10,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/tRhKiQ4ZVXG5J_9SE99YHA/348s.jpg',
    },
]

def seed_review_images():

    for images in review_image_list:
        new_review_image = ReviewImage(
            review_id = images['review_id'],
            url = images['url'],
        )

        db.session.add(new_review_image)
        db.session.commit()


def undo_review_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.review_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM review_images")

    db.session.commit()
