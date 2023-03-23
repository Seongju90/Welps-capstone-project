import { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { thunkAllRestaurants } from '../../store/restaurants'
import RestaurantCard from '../RestaurantCard'


export default function RestaurantsIndex() {
    const dispatch = useDispatch()
    const restaurantsObj = useSelector(state => state.restaurants)
    const restaurantsArray = Object.values(restaurantsObj)


    useEffect(() => {
        dispatch(thunkAllRestaurants())
    }, [dispatch])


    return (
        <div className="main-container">
            <div className="restaurant-main-container">
                {restaurantsArray.map(restaurant => (
                    <div>
                        <RestaurantCard key={restaurant.id} restaurant={restaurant}/>
                    </div>
                ))}
            </div>
            <div className="google-map-container">
                Google Map
            </div>
        </div>
    )
}
