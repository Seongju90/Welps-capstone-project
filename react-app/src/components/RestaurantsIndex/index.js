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

    // Variable to hold true or false depending on if the search results went over the threshold in backend,
    // since the result is "pushed" at the end we extract from the end without modifying it.
    const searchResult = searchArray[searchArray.length - 1]
    console.log("frontend search result", searchResult)

    useEffect(() => {
        dispatch(thunkAllRestaurants())
        // added this thunk so on hard refresh the query data persists
        dispatch(thunkSearchRestaurants(query))
    }, [dispatch, query])


    return (
        <div className="main-container">
            <div className="restaurant-main-container">
                {!searchResult &&
                    <div className="no-result-found-container">
                        <div className="no-results-header">Sorry there were no results found for {query}</div>
                        <div className="suggestions-no-result">Suggestions for improving your results:</div>
                        <ul className="list-of-no-result-text">
                            <li>Try a larger search area</li>
                            <li>Try searching a different location</li>
                            <li>Check the spelling or try alternate spellings</li>
                            <li>Although there are no results matching your search, here are some places you can check out!</li>
                        </ul>
                    </div>
                }
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
