from app.models import db, Review, environment, SCHEMA

review_list = [
    {
        'restaurant_id': 1,
        'user_id': 1,
        'review': 'This place had the best korean food I had in a while!',
        'rating': 4,
    },
    {
        'restaurant_id': 1,
        'user_id': 3,
        'review': 'This place has korean food comparable to the food in Korea itself!',
        'rating': 4,
    },
        {
        'restaurant_id': 1,
        'user_id': 2,
        'review': 'The ambiance here is fantastic, and the food is top-notch.',
        'rating': 5,
    },
    {
        'restaurant_id': 2,
        'user_id': 1,
        'review': 'The food was on the more saltier side, but other than that perfect!',
        'rating': 3,
    },
    {
        'restaurant_id': 2,
        'user_id': 5,
        'review': 'I loved the variety of dishes available at this restaurant.',
        'rating': 4,
    },
    {
        'restaurant_id': 2,
        'user_id': 2,
        'review': 'The staff was very friendly and provided excellent service.',
        'rating': 5,
    },
    {
        'restaurant_id': 3,
        'user_id': 2,
        'review': 'For the price I paid, the food was not worth it, do not come here!',
        'rating': 2,
    },
    {
        'restaurant_id': 3,
        'user_id': 3,
        'review': 'The flavors in the food were absolutely incredible!',
        'rating': 5,
    },
    {
        'restaurant_id': 3,
        'user_id': 4,
        'review': 'I had a great dining experience and will definitely be back.',
        'rating': 4,
    },
    {
        'restaurant_id': 4,
        'user_id': 3,
        'review': 'Great food, great drinks, great interior!',
        'rating': 5,
    },
    {
        'restaurant_id': 4,
        'user_id': 1,
        'review': 'The portion sizes here are quite generous and satisfying.',
        'rating': 4,
    },
        {
        'restaurant_id': 4,
        'user_id': 4,
        'review': 'The presentation of the dishes was visually stunning!',
        'rating': 5,
    },
    {
        'restaurant_id': 5,
        'user_id': 4,
        'review': 'Food was great, friends loved it!',
        'rating': 4,
    },
    {
        'restaurant_id': 5,
        'user_id': 5,
        'review': 'I highly recommend trying their signature dish. It was delightful!',
        'rating': 5,
    },
    {
        'restaurant_id': 5,
        'user_id': 6,
        'review': 'The food here surpassed my expectations. I was pleasantly surprised.',
        'rating': 4,
    },
    {
        'restaurant_id': 6,
        'user_id': 4,
        'review': 'For the amount I paid, it was alright, could have been better.',
        'rating': 3,
    },
    {
        'restaurant_id': 6,
        'user_id': 5,
        'review': 'The atmosphere of this restaurant is cozy and inviting.',
        'rating': 4,
    },
    {
        'restaurant_id': 6,
        'user_id': 6,
        'review': 'I had an amazing culinary experience. The flavors were remarkable!',
        'rating': 5,
    },
    {
        'restaurant_id': 7,
        'user_id':5 ,
        'review': 'Why did I even come here, the servers were so rude, the food was okay though.',
        'rating': 2,
    },
    {
        'restaurant_id': 7,
        'user_id': 1,
        'review': 'The quality of ingredients used in the dishes is commendable.',
        'rating': 4,
    },
    {
        'restaurant_id': 7,
        'user_id': 2,
        'review': 'The service here was prompt and attentive. Thumbs up!',
        'rating': 5,
    },
    {
        'restaurant_id': 8,
        'user_id': 6,
        'review': 'Love it, coming back again next week!',
        'rating': 4,
    },
    {
        'restaurant_id': 8,
        'user_id': 3,
        'review': 'I enjoyed the unique fusion of flavors in their cuisine.',
        'rating': 4,
    },
    {
        'restaurant_id': 8,
        'user_id': 4,
        'review': 'The food here is consistently delicious. I am a regular customer.',
        'rating': 5,
    },
    {
        'restaurant_id': 9,
        'user_id': 6,
        'review': 'I wish I knew this place sooner! The best food and service I have received, even though I did not expect much!',
        'rating': 5,
    },
    {
        'restaurant_id': 9,
        'user_id': 5,
        'review': 'The menu offers a great variety of vegetarian options.',
        'rating': 4,
    },
    {
        'restaurant_id': 9,
        'user_id': 2,
        'review': 'The desserts at this place are to die for. Absolutely heavenly!',
        'rating': 5,
    },
    {
        'restaurant_id': 10,
        'user_id': 5,
        'review': 'You get what you paid for, medium price...medium food.',
        'rating': 3,
    },
    {
        'restaurant_id': 10,
        'user_id': 1,
        'review': 'I had a delightful dining experience. The staff was friendly and helpful.',
        'rating': 4,
    },
    {
        'restaurant_id': 10,
        'user_id': 2,
        'review': 'The food here exceeded my expectations. I can not wait to go back!',
        'rating': 5,
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
