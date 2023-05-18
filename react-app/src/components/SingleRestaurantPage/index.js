import './SingleRestaurantPage.css'
import { useParams, useHistory } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux";
import { useEffect } from 'react';
import { thunkOneRestaurant } from '../../store/restaurants';


export default function SingleRestaurantPage () {
    const dispatch = useDispatch()
    const history = useHistory()
    // extracting the restaurant id from the url parameter
    const { restaurantId } = useParams()
    const restaurant = useSelector(state => state?.restaurants.singleRestaurant)


    // Manipulating the images array for the banner
    let imagesArr = restaurant?.images

    while (imagesArr?.length < 3) {
        imagesArr.push({url: 'https://www.thermaxglobal.com/wp-content/uploads/2020/05/image-not-found-300x169.jpg'})
    }

    if (imagesArr?.length >= 3) {
        imagesArr = imagesArr.slice(0,3)
    }


    useEffect(() => {
        dispatch(thunkOneRestaurant(restaurantId))
    }, [dispatch])


    return (
        <div className="single-card-main-container">
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
                Hello!
            </div>
        </div>
    )
}
