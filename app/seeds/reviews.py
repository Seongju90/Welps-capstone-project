from app.models import db, Review, environment, SCHEMA

review_list = [
    {
        'restaurant_id': 1,
        'user_id': 1,
        'review': 'This place had the best korean food I had in a while!',
        'rating': 4,
    },
    {
        'restaurant_id': 2,
        'user_id': 1,
        'review': 'The food was on the more saltier side, but other than that perfect!',
        'rating': 3,
    },
    {
        'restaurant_id': 3,
        'user_id': 2,
        'review': 'For the price I paid, the food was not worth it, do not come here!',
        'rating': 2,
    },
    {
        'restaurant_id': 4,
        'user_id': 3,
        'review': 'Great food, great drinks, great interior!',
        'rating': 5,
    },
    {
        'restaurant_id': 5,
        'user_id': 4,
        'review': 'Food was great, friends loved it!',
        'rating': 4,
    },
    {
        'restaurant_id': 6,
        'user_id': 4,
        'review': 'For the amount I paid, it was alright, could have been better.',
        'rating': 3,
    },
    {
        'restaurant_id': 7,
        'user_id':5 ,
        'review': 'Why did I even come here, the servers were so rude, the food was okay though.',
        'rating': 2,
    },
    {
        'restaurant_id': 8,
        'user_id': 6,
        'review': 'Love it, coming back again next week!',
        'rating': 4,
    },
    {
        'restaurant_id': 9,
        'user_id': 6,
        'review': 'I wish I knew this place sooner! The best food and service I have received, even though I did not expect much!',
        'rating': 5,
    },
    {
        'restaurant_id': 10,
        'user_id': 5,
        'review': 'You get what you paid for, medium price...medium food.',
        'rating': 3,
    },
]

def seed_reviews():

    for review in review_list:
        new_review = Review(
            restaurant_id = review['restaurant_id'],
            user_id = review['user_id'],
            review = review['review'],
            rating = review['rating']
        )

        db.session.add(new_review)
        db.session.commit()

def undo_reviews():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.reviews RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM reviews")

    db.session.commit()
