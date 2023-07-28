import { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { useParams } from 'react-router-dom';
import { thunkAllRestaurants } from '../../store/restaurants';
import RestaurantCard from '../RestaurantCard';
import './RestaurantIndex.css';

import map from '../../icons/google-map.png'
import { thunkSearchRestaurants } from '../../store/search';

export default function RestaurantsIndex() {
    const dispatch = useDispatch()
    const restaurantsObj = useSelector(state => state?.restaurants)
    const restaurantsArray = Object.values(restaurantsObj)

    const { query } = useParams()
    const searchArray = useSelector(state => state?.search)

    useEffect(() => {
        dispatch(thunkAllRestaurants())
        // added this thunk so on hard refresh the query data persists
        dispatch(thunkSearchRestaurants(query))
    }, [dispatch])


    return (
        <div className="main-container">
            <div className="restaurant-main-container">
                {!searchArray.length ? restaurantsArray?.map(restaurant => (
                     <div className="restaurant-card-main-container" key={restaurant.id}>
                        <RestaurantCard restaurant={restaurant}/>
                    </div>
                )) :
                searchArray?.map(restaurant => (
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
