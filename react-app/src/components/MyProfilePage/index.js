import { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { thunkMyRestaurants } from '../../store/restaurants';
import './MyProfilePage.css';
import OpenModalButton from '../OpenModalButton';
import EditRestaurantModal from '../EditRestaurantModal';

export default function MyProfilePage () {
    const dispatch = useDispatch()
    const currentUser = useSelector(state => state.session?.user)

    const myRestaurantsObj = useSelector(state => state.restaurants)
    const myResaurantsArr = Object.values(myRestaurantsObj)


    useEffect(() => {
        dispatch(thunkMyRestaurants(currentUser.id))
    }, [dispatch])

    return (
        <div className="my-profile-main-container">
            {myResaurantsArr.map(restaurant => (
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
                        <div>Delete</div>
                    </div>
                </div>
            ))}
        </div>
    )
}
