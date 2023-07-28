import { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { thunkAllRestaurants } from '../../store/restaurants';
import RestaurantCard from '../RestaurantCard';
import './RestaurantIndex.css';

import map from '../../icons/google-map.png'

export default function RestaurantsIndex() {
    const dispatch = useDispatch()
    const restaurantsObj = useSelector(state => state?.restaurants)
    const restaurantsArray = Object.values(restaurantsObj)

    const searchArray = useSelector(state => state?.search)

    useEffect(() => {
        dispatch(thunkAllRestaurants())
    }, [dispatch])


    return (
        <div className="main-container">
            <div className="restaurant-main-container">
                {searchArray ? searchArray?.map(restaurant => (
                     <div className="restaurant-card-main-container" key={restaurant.id}>
                        <RestaurantCard restaurant={restaurant}/>
                    </div>
                )) :
                restaurantsArray?.map(restaurant => (
                    <div className="restaurant-card-main-container" key={restaurant.id}>
                        <RestaurantCard restaurant={restaurant}/>
                    </div>
                ))
                }
            </div>
            <div className="google-map-container">
                <img className="index-map-img" src={map} alt={"restaurant-index-map"}/>
            </div>
        </div>
    )
}
