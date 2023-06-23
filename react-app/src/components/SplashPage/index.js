import './SplashPage.css'
import { useDispatch, useSelector } from 'react-redux'
import { useEffect } from 'react'
import { thunkSplashReview } from '../../store/reviews'
import SplashReviewCard from '../SplashReviewCard'

import koreanFoodBanner from "../../assets/DSCF7368.jpg"

function SplashPage() {
    const dispatch = useDispatch()

    // already pulling six random reviews from backend
    const splashReviews = useSelector(state => state?.reviews)
    const splashReviewsArray = Object.values(splashReviews)

    console.log(splashReviewsArray)
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
            <div className="splash-review-main-container">
                <div className="splash-review-header">Your Next Review Awaits</div>
                <div className="splash-review-sub-container">
                    {splashReviewsArray?.map(reviews => (
                        <div className="splash-review-card-container" key={reviews.id}>
                            <SplashReviewCard reviews={reviews}/>
                        </div>
                    ))}
                </div>
            </div>
        </>
    )
}


export default SplashPage
