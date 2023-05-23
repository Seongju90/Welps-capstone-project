import { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { thunkMyRestaurants, thunkDeleteRestaurants } from '../../store/restaurants';
import { useHistory } from "react-router-dom"
import { thunkDeleteReview, thunkMyReviews } from '../../store/reviews';
import './MyProfilePage.css';
import OpenModalButton from '../OpenModalButton';
import EditRestaurantModal from '../EditRestaurantModal';
import EditReviewModal from '../EditReviewModal';
import EditRestaurantModalButton from '../EditRestaurantModalButton';

import profile from '../../icons/profile-user.svg';
import deleteIcon from '../../icons/delete.svg';

export default function MyProfilePage () {
    const dispatch = useDispatch()
    const history = useHistory()

    // conditional variables to change menu
    const [showMyRestaurant, setShowMyRestuarant] = useState(true)
    const [showMyReview, setShowMyReview] = useState(false)

    // Selecting state variables
    const currentUser = useSelector(state => state.session?.user)

    const myRestaurantsObj = useSelector(state => state?.restaurants)
    const myResaurantsArr = Object.values(myRestaurantsObj)

    const myReviewsObj = useSelector(state => state?.reviews)
    const myReviewsArr = Object.values(myReviewsObj)



    // Use Effects for thunks
    useEffect(() => {
        dispatch(thunkMyRestaurants(currentUser.id))
        dispatch(thunkMyReviews(currentUser.id))
    }, [dispatch, currentUser.id])


    const deleteRestaurant = (id) => {
        dispatch(thunkDeleteRestaurants(id))
        dispatch(thunkMyRestaurants(currentUser.id))
        window.alert("Restaurant has been deleted!")
    }

    const deleteReview = (id) => {
        dispatch(thunkDeleteReview(id))
        dispatch(thunkMyReviews)
        window.alert("Review has been deleted!")
    }

    return (
        <div className="myprofile-main-container">
            <div className="myprofile-user-main-container">
                <img
                    className="myprofile-user-icon"
                    width={'190px'}
                    height={'190px'}
                    src={profile}
                    alt={"profile-user-icon"}
                />
                <div className="myprofile-user-info-container">
                    <div>{`${currentUser.first_name} ${currentUser.last_name}`}</div>
                    <div>{myReviewsArr?.length} reviews</div>
                </div>
            </div>
            <div className="myprofile-options-values-container">
                <div className="options-container">
                    <div>My Restaurants</div>
                    <div>My Reviews</div>
                </div>
                {/* conditional render either restaurant or reviews */}
                {showMyRestaurant &&
                    <div className="myprofile-restaurant-overall-container">
                        {myResaurantsArr?.map(restaurant => (
                            <div className="myprofile-restaurant-info-main-container" key={restaurant.id}>
                                <div className="myprofile-img-info-container">
                                    <img
                                        width={'150px'}
                                        height={'150px'}
                                        className="myprofile-restaurant-card-img"
                                        src={restaurant.preview_image}
                                        alt="preview-restaurant-img"
                                    />
                                    <div className="myprofile-restaurant-info-container">
                                        <div>{restaurant.name}</div>
                                        <div className="myprofile-categories">
                                        {restaurant.categories.map(category => (
                                            <div>{category.type}</div>
                                        ))}
                                        </div>
                                        <div>{`${restaurant?.address} ${restaurant?.city}, ${restaurant?.state} ${restaurant?.zipcode}`}</div>
                                        <div>Avg Rating: {restaurant?.avgRating}</div>
                                    </div>
                                </div>
                                <div className="myprofile-edit-delete-container">
                                    <div className="myprofile-info-container">
                                        <EditRestaurantModalButton
                                            buttonText="Edit"
                                            modalComponent={<EditRestaurantModal restaurant={restaurant}/>}
                                            buttonName="edit-restaurant-button"
                                        />
                                    </div>
                                    <div className="myprofile-delete-icon">
                                        <img onClick={() => deleteRestaurant(restaurant.id)}
                                            height={'16px'}
                                            width={'16px'}
                                            src={deleteIcon}
                                            alt={'myprofile-delete'}
                                        />
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                }
                {showMyReview &&
                    <div className="myprofile-restaurant-review-overall-container">
                        {myReviewsArr?.map(review => (
                            <div className="myprofile-review-main-container" key={review.id}>
                                {review.review}
                                <OpenModalButton
                                    buttonText="Edit"
                                    modalComponent={<EditReviewModal reviews={review}/>}
                                    buttonName="edit-review-button"
                                />
                                <div onClick={() => deleteReview(review.id)}>{deleteIcon}</div>
                            </div>
                        ))}
                    </div>
                }
            </div>
        </div>
    )
}
