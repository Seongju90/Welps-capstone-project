from app.models import db, Restaurant, environment, SCHEMA

# type [korean, japanese, american, chinese, fastfood, drinks]


restaurants = [
    {
        'owner_id': 1,
        'name': 'Kunjip',
        'address': '1006 Kiely Blvd',
        'city': 'Santa Clara',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95051',
        'price': '$$',
        'phone_number': '408-246-0025',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/lgK3XsiykZ6MhOSCH6Jsog/348s.jpg',
        'start_hours': '10:00 AM',
        'end_hours': '9:00 PM',
    },
    {
        'owner_id': 2,
        'name': 'Chungdam',
        'address': '3180 EL Camino Real',
        'city': 'Santa Clara',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95051',
        'price': '$$$',
        'phone_number': '669-306-4642',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/939DUnel5bqTx1ttIyco2A/348s.jpg',
        'start_hours': '11:30 AM',
        'end_hours': '2:30 PM',
    },
    {
        'owner_id': 3,
        'name': 'Daeho Kalbi Jjim & Beef Soup',
        'address': '217 W Calaveras Blvd',
        'city': 'Milpitas',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95035',
        'price': '$$$',
        'phone_number': '408-770-3778',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/bbbaXkwRLl-BFEd3LNBC5A/348s.jpg',
        'start_hours': '11:00 AM',
        'end_hours': '2:30 PM',
    },
    {
        'owner_id': 4,
        'name': '10 Butchers Korean BBQ',
        'address': '595 E El Camino Real',
        'city': 'Sunnyvale',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '94087',
        'price': '$$$$',
        'phone_number': '408-720-8889',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/-4u6nWQ9rUUsAjsUBBP-sA/348s.jpg',
        'start_hours': '11:30 AM',
        'end_hours': '2:30 PM',
    },
    {
        'owner_id': 5,
        'name': 'Sumiya',
        'address': '2634 Homestead Rd',
        'city': 'Santa Clara',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95051',
        'price': '$$',
        'phone_number': '408-973-0604',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/N-242Y3RF8sEfNBSErwImQ/348s.jpg',
        'start_hours': '11:30AM',
        'end_hours': '1:30 PM',
    },
    {
        'owner_id': 6,
        'name': 'Rantei Japanese Cuisine',
        'address': '1271 Franklin Mall',
        'city': 'Santa Clara',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95050',
        'price': '$$$',
        'phone_number': '408-352-5683',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/EC7xvgMkhxmDCSSk4oXiFw/348s.jpg',
        'start_hours': '4:30 PM',
        'end_hours': '9:00 PM',
    },
    {
        'owner_id': 4,
        'name': 'Izakaya Restaurant',
        'address': '1335 N 1st St',
        'city': 'San Jose',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95112',
        'price': '$$',
        'phone_number': '408-452-8751',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/KXh4HODT6W4DkbQ254QcCQ/348s.jpg',
        'start_hours': '5:30 PM',
        'end_hours': '11:30 PM',
    },
    {
        'owner_id': 3,
        'name': 'Amami Shima Sushi',
        'address': '19068 Stevens Creek Blvd',
        'city': 'Cupertino',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95014',
        'price': '$$',
        'phone_number': '408-996-8815',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/pxcpMMFRhd9xqlo3s5aP4A/348s.jpg',
        'start_hours': '4:30 PM',
        'end_hours': '9:00 PM',
    },
    {
        'owner_id': 1,
        'name': 'The Table',
        'address': '1110 Willow St',
        'city': 'San Jose',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95125',
        'price': '$$',
        'phone_number': '408-638-7911',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/KMiVsvM886v1DpX7Ic9oxg/348s.jpg',
        'start_hours': '9:00 AM',
        'end_hours': '9:00 PM',
    },
    {
        'owner_id': 2,
        'name': 'Lazy Dog Restaurant and Bar',
        'address': '19359 Stevens Creek Blvd',
        'city': 'Cupertino',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95014',
        'price': '$$',
        'phone_number': '408-359-4690',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/vZaj9IYaFuauxOiEkE64cQ/348s.jpg',
        'start_hours': '11:00 AM',
        'end_hours': '12:00 AM',
    },
        {
        'owner_id': 3,
        'name': 'Eureka! Cupertino',
        'address': '19369 Stevens Creek Blvd',
        'city': 'Cupertino',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95014',
        'price': '$$',
        'phone_number': '669-266-6752',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/_nDD5moQaafuKVd-0gwXrg/348s.jpg',
        'start_hours': '11:00 AM',
        'end_hours': '11:00 PM',
    },
    {
        'owner_id': 4,
        'name': "St. John's Bar & Grill",
        'address': '510 Lawrence Expy',
        'city': 'Sunnyvale',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '94085',
        'price': '$$',
        'phone_number': '408-822-9358',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/APhEFFIlFVTiqzOioMdH8w/348s.jpg',
        'start_hours': '11:00 AM',
        'end_hours': '9:00 PM',
    },
        {
        'owner_id': 1,
        'name': "McDonald's",
        'address': '2850 Augustine Dr',
        'city': 'Santa Clara',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95054',
        'price': '$',
        'phone_number': '408-727-9726',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/lKEoDOzrVsg-1Fcbqer4ig/348s.jpg',
        #24 hours
        'start_hours': 'Open 24 hours',
        'end_hours': 'Open 24 hours',
    },
    {
        'owner_id': 2,
        'name': 'Chick-fil-A',
        'address': '53 Headquarters Dr',
        'city': 'San Jose',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95134',
        'price': '$',
        'phone_number': '408-526-0600',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/D-8Y6pZZZ9kBj-qpnGHdFw/348s.jpg',
        'start_hours': '7:00 AM',
        'end_hours': '9:00 PM',
    },
    {
        'owner_id': 4,
        'name': 'Tong Soon Garden',
        'address': 'Buttitta Plaza 3240 El Camino Real',
        'city': 'Santa Clara',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95051',
        'price': '$$',
        'phone_number': '(408) 615-9988',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/Kf_jka6dxdHKpY54AQ8gnw/348s.jpg',
        'start_hours': '11:00 AM',
        'end_hours': '9:30 PM',
    },
    {
        'owner_id': 5,
        'name': 'Lock Chun',
        'address': '4495 Stevens Creek Blvd',
        'city': 'Santa Clara',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95051',
        'price': '$$',
        'phone_number': '(408) 249-2784',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/fLt5K4RwRQSQBNk5VUAVcA/348s.jpg',
        'start_hours': '11:30 AM',
        'end_hours': '8:30 PM',
    },
    {
        'owner_id': 6,
        'name': 'Sifu Wong Kitchen',
        'address': '1219 Wildwood Ave',
        'city': 'Sunnyvale',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '94089',
        'price': '$$',
        'phone_number': '669-454-9022',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/z1MZmJ0GphRxaQg3OX8PCA/348s.jpg',
        'start_hours': '11:30 AM',
        'end_hours': '2:30 PM',
    },
    {
        'owner_id': 4,
        'name': "Hong Kong Banjum Paik's Noodle",
        'address': '1520 Kiely Blvd',
        'city': 'Santa Clara',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95051',
        'price': '$',
        'phone_number': '408-244-0410',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/CaZSnW41uaeve--WSLXy-g/348s.jpg',
        'start_hours': '11:00 AM',
        'end_hours': '8:30 PM',
    },
    {
        'owner_id': 5,
        'name': 'Sunright Tea Studio',
        'address': '795 E El Camino Real',
        'city': 'Sunnyvale',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '94087',
        'price': '$$',
        'phone_number': '510-999-7777',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/uf2kyCTjGWoxeyDksbhC4g/348s.jpg',
        'start_hours': '12:00 PM',
        'end_hours': '9:00 PM',
    },
    {
        'owner_id': 6,
        'name': 'Jiaren Cafe',
        'address': '1171 Homestead Rd',
        'city': 'Santa Clara',
        'state': 'CA',
        'country': 'USA',
        'zipcode': '95050',
        'price': '$',
        'phone_number': '408-780-5199',
        'preview_image': 'https://s3-media0.fl.yelpcdn.com/bphoto/3QvBSQ6s2lfxa9ExxDFa-g/348s.jpg',
        'start_hours': '8:30 AM',
        'end_hours': '10:00 PM',
    },
]


def seed_restaurants():
    # loop through the list of restaurants
    for restaurant in restaurants:
        # create a new restaurant for each in the array, assigning the value to corresponding key
        new_restaurant = Restaurant(
            owner_id = restaurant['owner_id'],
            name = restaurant['name'],
            address = restaurant['address'],
            city = restaurant['city'],
            state = restaurant['state'],
            country = restaurant['country'],
            zipcode = restaurant['zipcode'],
            price = restaurant['price'],
            phone_number = restaurant['phone_number'],
            preview_image = restaurant['preview_image'],
            start_hours = restaurant['start_hours'],
            end_hours = restaurant['end_hours'],
        )

        # add and commit inside the loop for each restaurant
        db.session.add(new_restaurant)
        db.session.commit()

def undo_restaurants():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.restaurants RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM restaurants")

    db.session.commit()
