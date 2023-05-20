import { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { thunkMyRestaurants, thunkDeleteRestaurants } from '../../store/restaurants';
import { useHistory } from "react-router-dom"
import { thunkDeleteReview, thunkMyReviews } from '../../store/reviews';
import './MyProfilePage.css';
import OpenModalButton from '../OpenModalButton';
import EditRestaurantModal from '../EditRestaurantModal';
import EditReviewModal from '../EditReviewModal';

export default function MyProfilePage () {
    const dispatch = useDispatch()
    const history = useHistory()
    const currentUser = useSelector(state => state.session?.user)

    const myRestaurantsObj = useSelector(state => state?.restaurants)
    const myResaurantsArr = Object.values(myRestaurantsObj)

    const myReviewsObj = useSelector(state => state?.reviews)
    const myReviewsArr = Object.values(myReviewsObj)

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
        <div className="my-profile-main-container">
            {myResaurantsArr?.map(restaurant => (
                <div className="restaurant-info-main-container" key={restaurant.id}>
                    <img
                    className="restaurant-card-img"
                    src={restaurant.preview_image}
                    alt="preview-restaurant-img"
                    />
                    <div className="info-container">
                        <div>{restaurant.name}</div>
                        <OpenModalButton
                            buttonText="Edit"
                            modalComponent={<EditRestaurantModal restaurant={restaurant}/>}
                            buttonName="edit-restaurant-button"
                        />
                        <div onClick={() => deleteRestaurant(restaurant.id)}>Delete</div>
                    </div>
                </div>
            ))}
            {myReviewsArr?.map(review => (
                <div className="review-info-main-container" key={review.id}>
                    {review.review}
                    <OpenModalButton
                        buttonText="Edit"
                        modalComponent={<EditReviewModal reviews={review}/>}
                        buttonName="edit-review-button"
                    />
                    <div onClick={() => deleteReview(review.id)}>Delete</div>
                </div>
            ))}
        </div>
    )
}
