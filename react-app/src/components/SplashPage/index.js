import './SplashPage.css'

import koreanFoodBanner from "../../assets/DSCF7368.jpg"

function SplashPage() {

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
