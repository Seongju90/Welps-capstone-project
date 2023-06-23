import './SplashReviewCard.css'
import { useHistory } from "react-router-dom"

import profileImg from "../../icons/profile-user2.svg"
import brokenImg from "../../icons/broken-image.svg"

function SplashReviewCard({reviews}) {
    const history = useHistory()
    const userInfo = reviews?.user_info;
    const reviewImageArr = reviews?.review_images;
    const restaurantInfo = reviews?.restaurant_info;

    // if review has no img, put broken img icon otherwise, choose one from the array
    let reviewImg;

    if (!reviewImageArr.length) {
        reviewImg = brokenImg
    } else {
        // math.random * array length scale the random decimal number to the length of the array
        // inclusive of 0 and exclusive the length of array, this ensures will fall in valid range of array
        // math.floor to round it to a whole number
        const randomIndex = Math.floor(Math.random() * reviewImageArr.length)
        reviewImg = reviewImageArr[randomIndex].url
    }

    const navigateToSingleRestaurant = () => {
        history.push(`/restaurants/${restaurantInfo?.id}`)
    }

    return (
        <div className="splash-individual-card-container">
            <div className="splash-page-user-info-container">
                <img
                    src={profileImg}
                    alt='profile-img-splash-page'
                    width="40px"
                    height="40px"
                />
                <div className="splash-user-name-comment">
                    <div className="splash-first-last-name">
                        {`${userInfo?.first_name} ${userInfo?.last_name}`}
                    </div>
                    <div className="splash-comment">
                        Wrote a Review
                    </div>
                </div>
            </div>
            <img
                className="splash-review-image"
                src={reviewImg}
                alt="splash-review-image"
            />
            <div className="splash-restaurant-info-rating-review-container">
                <div className="splash-restaurant-name" onClick={navigateToSingleRestaurant}>
                    {restaurantInfo?.name}
                </div>
                <div className="splash-review-rating">
                    Rating: {reviews?.rating}
                </div>
                <div className="splash-actual-review">
                    {reviews?.review}
                </div>
            </div>
        </div>
    )
}

export default SplashReviewCard
