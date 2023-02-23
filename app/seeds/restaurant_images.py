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
    {
        'restaurant_id': 9,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/2X-lw7TSzGrTkCdhxJWTnw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 9,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/mxPXg8zE-5b7K0nx2ZAwFA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 9,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/C2hYCa_tUA6dwpB5bz3dEA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 9,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/ucE1tVdmGB8ZnuaUY68C0w/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 10,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/8CJ9eOW6bcZ4nSR5ZrV86A/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 10,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/wrcmqEAMW8U_prZpit66GA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 10,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/nqtjGGjPl5YttnVn7k_4rQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 10,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/_Yh3Aag4WbuZrUotPpRXtQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 11,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/hydnbG2KVD-4PgOQiHwg-A/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 11,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/UhwtMBGQyRuNFTDngg0pTw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 11,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/O5BPu_R2JVdA8BveFG6l-A/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 11,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/ZnCmuFVxw7XSS30e_D5zHQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 12,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/58ffh3xxBG30L5X0TFv0Gw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 12,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/QwN2ZpaDfif5JmMvEPosJA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 12,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/yr6dLR4W1eRaO-vblDjDMA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 12,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/wf_zyL-Nuq1M1mTnqZG05Q/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 13,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/r4B-avLXAwe9TU6VQt3rdw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 13,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/SlQm05ElmYybqRlDZNwiRA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 13,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/6FbaGcYQCJD3quwAgIZkxQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 13,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/RviXQFONZ2RVx4ts4F1ZeQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 14,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/P_M3fg4cV3xGJGwnojrPSw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 14,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/EbWxvxBppfyf52ZQkpms0A/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 14,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/9g1xufkJ3jle5uqhFgHa-w/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 14,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/kvy8SEgN9xDq0RLmaLVMtg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 15,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/MpG7_YFViaQSDxYiijVJjw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 15,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/Iu4V17neIsbvRfOGRi0bTw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 15,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/qEx6PQZCR7DwkijvaMDKzg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 15,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/EmKyLC0fuhGSdfVAGRKbIA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 16,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/Gp9aRO0vsjzqTq7PaeQFuA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 16,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/du344wyLFemXBEM7t9lfbg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 16,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/LBrP8SM5mZe8K5TxnqPbIA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 16,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/4A4VkEhtVgWbvLu5ZNylbQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 17,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/dcFagt_wimKNMa_aUn1FIw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 17,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/hbJSI54-_2H1jqnj3RuBcg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 17,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/choKd2mykXiBue7Slqj3gg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 17,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/P4_LPxp-yIFxyHXnmte27Q/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 18,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/vRIRS5J4fz4yx5N06HFkDg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 18,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/OoIQnc17qlmjQOd__jjYyA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 18,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/aQo2SS08pCcnGWcmg0AvvQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 18,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/zVRvwCFhKU5hX5JM_Y-FLw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 19,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/IDQIsRN2NHj0MUb0fwnnMg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 19,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/9mpykOsIcogTAipuFiCUyg/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 19,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/AtWl6TbEu_55EFidFagDmA/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 19,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/cQLTvYqBigtJOE8GhFhB1A/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 20,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/F_MkOtmMc4eI2-s40B9GsQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 20,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/pbvBFdj24TYSEWb05ROJWQ/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 20,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/UukRhfIVpT5aTVwN4ZMvXw/348s.jpg',
        'preview': False
    },
    {
        'restaurant_id': 20,
        'url': 'https://s3-media0.fl.yelpcdn.com/bphoto/RT83L5ZOaZhvWs9vkFafUg/348s.jpg',
        'preview': False
    },
]


def seed_restaurant_images():
    for images in restaurant_images:

        new_image = RestaurantImage(
            restaurant_id = images['restaurant_id'],
            url = images['url'],
            preview = images['preview']
        )

        db.session.add(new_image)
        db.session.commit()


def undo_restaurant_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.restaurant_images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM restaurant_images")

    db.session.commit()
