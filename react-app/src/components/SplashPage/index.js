import './SplashPage.css'
import { useDispatch, useSelector } from 'react-redux'
import { useEffect } from 'react'
import { thunkSplashReview } from '../../store/reviews'

import koreanFoodBanner from "../../assets/DSCF7368.jpg"

function SplashPage() {
    const dispatch = useDispatch()

    const splash_reviews = useSelector(state => console.log('front', state))

    useEffect(() => {
        dispatch(thunkSplashReview())
    },[dispatch])

    return (
        <>
            <div className="home-banner-container">
                <img
                    className="banner-img"
                    src={koreanFoodBanner}
                    alt="korean-food-banner-img"
                />
            </div>
            {/* <div className="splash-review-container">
                <div>Reviews</div>
            </div>
            <div className="splash-categories-container">
                <div>Categories</div>
            </div> */}
        </>
    )
}


export default SplashPage
