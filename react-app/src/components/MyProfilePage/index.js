import { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { thunkMyRestaurants, thunkDeleteRestaurants } from '../../store/restaurants';
import { thunkDeleteReview, thunkMyReviews } from '../../store/reviews';
import './MyProfilePage.css';
import EditReviewModalButton from '../EditReviewModalButton';
import EditRestaurantModal from '../EditRestaurantModal';
import EditReviewModal from '../EditReviewModal';
import EditRestaurantModalButton from '../EditRestaurantModalButton';

import profile from '../../icons/profile-user.svg';
import deleteIcon from '../../icons/delete.svg';

export default function MyProfilePage () {
    const dispatch = useDispatch()

    // conditional variables to change menu
    const [showMenu, setShowMenu] = useState('restaurants')
    const [selectedOption, setSelectedOption] = useState('restaurants')


    // Selecting state variables
    const currentUser = useSelector(state => state.session?.user)

    const myRestaurantsObj = useSelector(state => state?.restaurants)
    const myRestaurantsArr = Object.values(myRestaurantsObj)

    const myReviewsObj = useSelector(state => state?.reviews)
    const myReviewsArr = Object.values(myReviewsObj)

    // Use Effects for thunks
    useEffect(() => {
        dispatch(thunkMyRestaurants(currentUser.id))
        dispatch(thunkMyReviews(currentUser.id))
    }, [dispatch, currentUser.id])

    // function to call to change options
    const handleOptionClick = (option) => {
        setSelectedOption(option);
    };

    // function to call to change menu
    const handleShowMenu = (menu) => {
        setShowMenu(menu)
    };

    const handleOptionAndShowClick = (option) => {
        handleOptionClick(option);
        handleShowMenu(option);
    }

    const deleteRestaurant = (id) => {
        dispatch(thunkDeleteRestaurants(id))
        window.alert("Restaurant has been deleted!")
    }

    const deleteReview = (id) => {
        dispatch(thunkDeleteReview(id))
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
                    <div
                        className={`switch-option ${selectedOption === 'restaurants' ? 'active' : ''}`}
                        onClick={() => handleOptionAndShowClick('restaurants')}
                    >
                        My Restaurants
                    </div>
                    <div
                        className={`switch-option ${selectedOption === 'reviews' ? 'active' : ''}`}
                        onClick={() => handleOptionAndShowClick('reviews')}
                    >
                        My Reviews
                    </div>
                </div>
                {/* conditional render either restaurant or reviews */}
                {(!myRestaurantsArr.length && showMenu === "restaurants") && <div className="myprofile-no-restaurant-text">You have no restaurants yet create one!</div>}
                {showMenu === 'restaurants' &&
                    <div
                        className="myprofile-restaurant-overall-container"
                    >
                        {myRestaurantsArr?.map(restaurant => (
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
                                        {restaurant.categories?.map(category => (
                                            <div className="myprofile-individual-category">{category.type}</div>
                                        ))}
                                        </div>
                                        <div>{`${restaurant?.address} ${restaurant?.city}, ${restaurant?.state} ${restaurant?.zipcode}`}</div>
                                        <div>Avg Rating: {restaurant?.avgRating ? restaurant?.avgRating : "No Reviews Yet"}</div>
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
                {(!myReviewsArr.length && showMenu === "reviews") && <div className="myprofile-no-reviews-text">You have no reviews yet, go write one!</div>}
                {showMenu === 'reviews' &&
                    <div
                        className="myprofile-restaurant-review-overall-container"
                    >
                        {myReviewsArr?.map(review => (
                            <div className="myprofile-review-main-container" key={review.id}>
                                <div className="myprofile-img-review-container">
                                    <img
                                        height={'64px'}
                                        width={'64px'}
                                        src={profile}
                                        alt={'profile-svg'}
                                    />
                                    <div className="myprofile-rating-review-container">
                                        <div className="myprofile-user-rating">Rating: {review.rating}</div>
                                        <div className="myprofile-user-review">{review.review}</div>
                                    </div>
                                </div>
                                <div className="myprofile-edit-delete-container">
                                    <div className="myprofile-info-container">
                                        <EditReviewModalButton
                                            buttonText="Edit"
                                            modalComponent={<EditReviewModal reviews={review}/>}
                                            buttonName="edit-review-button"
                                        />
                                    </div>
                                    <div className="myprofile-delete-icon">
                                        <img onClick={() => deleteReview(review.id)}
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
            </div>
        </div>
    )
}
