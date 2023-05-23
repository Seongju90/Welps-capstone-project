import './SingleRestaurantPage.css'
import { useParams } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from 'react';
import { thunkOneRestaurant } from '../../store/restaurants';
import { thunkAllReviews } from '../../store/reviews';
import ReviewCard from '../ReviewCard'
import ReviewFormModal from "../ReviewFormModal";
import OpenReviewModalButton from '../OpenReviewModalButton';

import phone from '../../icons/phone-call.svg'
import directions from '../../icons/directions-svgrepo-com.svg'
import map from '../../icons/google-map.png'


export default function SingleRestaurantPage () {
    const dispatch = useDispatch();

    // const [onButtonClick, setOnButtonClick] = useState(false)

    // extracting the restaurant id from the url parameter
    const { restaurantId } = useParams()
    const restaurant = useSelector(state => state?.restaurants.singleRestaurant)
    const user = useSelector(state => state?.session?.user)
    const all_reviews_dict = useSelector(state => state?.reviews)
    const all_reviews_array = Object.values(all_reviews_dict)
    const categoryArr = restaurant?.categories

    // if there is only one category then just put on category on banner
    let category = null;
    if (categoryArr?.length <= 1) {
        category = categoryArr[0].type
    } else if (categoryArr?.length > 1) {
        // extract all the categorys, then join it with a comma, so no trailing comma at the end
        category = categoryArr?.map((cat) => cat.type).join(', ');
    }

    // Manipulating the images array for the banner
    let imagesArr = restaurant?.images

    while (imagesArr?.length < 3) {
        imagesArr.push({'url': restaurant.preview_image})
    }

    if (imagesArr?.length >= 3) {
        imagesArr = imagesArr.slice(0,3)
    }

    // Creating the address string
    const address = `${restaurant?.address} ${restaurant?.city}, ${restaurant?.state} ${restaurant?.zipcode}`

    // Creating phone number string
    // replace function will search for all non-digits and replace with empty string \D = nondigit
    const digitsOnly = restaurant?.phone_number.replace(/\D/g,"")
    const formatNumber = `(${digitsOnly?.slice(0, 3)}) ${digitsOnly?.slice(3, 6)}-${digitsOnly?.slice(6)}`

    // Creating hour string
    const hourString = `${restaurant?.start_hours} - ${restaurant?.end_hours}`

    useEffect(() => {
        dispatch(thunkOneRestaurant(restaurantId))
        dispatch(thunkAllReviews(restaurantId))
    }, [dispatch, restaurantId])


    return (
        <div className="single-card-main-container">
            <div className="banner-container">
                <div className="single-img-banner">
                    {imagesArr?.map(images => (
                        <img
                            src={images.url}
                            alt="extra-images-for-restaurant"
                            key={images.id}
                        />
                    ))}
                </div>
                <div className="info-overlay">
                    <div className="restaurant-details-container">
                        <div className="restaurant-details">
                            <div className="single-restaurant-name">{restaurant?.name}</div>
                            <div className="single-restaurant-ratings">{restaurant?.avgRating}{" • "}{all_reviews_array.length} (reviews)</div>
                            <div className="single-restaurant-price-categories">{restaurant?.price}{" • "}{category}</div>
                            <div className="single-restaurant-hours">{restaurant?.start_hours}{" - "}{restaurant?.end_hours}</div>
                        </div>
                    </div>
                    <div className="see-photo-button">See more photos</div>
                </div>
            </div>
            <div className="bottom-info-main-container">
                <div className="bottom-left-main-container">
                    <div className="create-review-container">
                        {/* conditional render the review button for owner */}
                        {restaurant?.owner_id !== user.id &&
                            <div className="star-review-button">
                                {/* Used a custom modal for this button so clicking star will open modal */}
					            <OpenReviewModalButton
					                buttonText="Write a Review"
					                modalComponent={<ReviewFormModal/>}
					                buttonName="single-index-create-review-button"
					            />
                            </div>
                        }
					</div>
                    <div className="location-hour-container">
                        <div className="location-map">
                            <div style={{fontWeight: 'bold'}}>Location & Hours</div>
                            <img
                                height={'150'}
                                width={'315'}
                                src={map}
                                alt={'google-map'}
                            />
                            <div>
                                {address}
                            </div>
                        </div>
                        <div className="hours-container">
                            <div className="sub-hours-container">
                                <div>Sun</div>
                                <div>{hourString}</div>
                            </div>
                            <div className="sub-hours-container">
                                <div>Mon</div>
                                <div>{hourString}</div>
                            </div>
                            <div className="sub-hours-container">
                                <div>Tues</div>
                                <div>{hourString}</div>
                            </div>
                            <div className="sub-hours-container">
                                <div>Wed</div>
                                <div>{hourString}</div>
                            </div>
                            <div className="sub-hours-container">
                                <div>Thurs</div>
                                <div>{hourString}</div>
                            </div>
                            <div className="sub-hours-container">
                                <div>Fri</div>
                                <div>{hourString}</div>
                            </div>
                            <div className="sub-hours-container">
                                <div>Sat</div>
                                <div>{hourString}</div>
                            </div>
                        </div>
                    </div>
                    <div className="review-main-container">
                        {all_reviews_array?.map(review => (
                            <ReviewCard review={review} />
                        ))}
                    </div>
                    {/* <div className="review-main-container">
                        {all_reviews_array.map(review => (
                            <ReviewCard review={review} />
                        ))}
                    </div>
                    <div className="review-main-container">
                        {all_reviews_array.map(review => (
                            <ReviewCard review={review} />
                        ))}
                    </div>
                    <div className="review-main-container">
                        {all_reviews_array.map(review => (
                            <ReviewCard review={review} />
                        ))}
                    </div>
                    <div className="review-main-container">
                        {all_reviews_array.map(review => (
                            <ReviewCard review={review} />
                        ))}
                    </div> */}
                </div>
                <div className="bottom-right-main-container">
                    <div className="phone-address-box">
                        <div className="phone-box">
                            <div className="number">{formatNumber}</div>
                            <img height={"18"} src={phone} alt={"phone-svg"}/>
                        </div>
                        <div className="address-box">
                            <div className="address">{address}</div>
                            <img height={"20"} src={directions} alt={"direction-svg"}/>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}
