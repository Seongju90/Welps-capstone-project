import './SplashPage.css'
import { useDispatch, useSelector } from 'react-redux'
import { useEffect } from 'react'
import { thunkSplashReview } from '../../store/reviews'
import SplashReviewCard from '../SplashReviewCard'

import koreanFoodBanner from "../../assets/DSCF7368.jpg"
import githubIcon from "../../icons/github-com.svg"
import linkedInIcon from "../../icons/linkedin-svgrepo-com.svg"

function SplashPage() {
    const dispatch = useDispatch()

    // already pulling six random reviews from backend
    const splashReviews = useSelector(state => state?.reviews)
    const splashReviewsArray = Object.values(splashReviews)

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
            <footer className="footer-main-container">
                <div className="footer-about-container">
                    <div className="footer-about-text">About</div>
                    <a className="footer-about-link-text" href="https://github.com/Seongju90/Welps-capstone-project" target="_blank" rel="noreferrer">About Welp</a>
                </div>
                <div className="footer-developer-container">
                    <div className="developer-text">Developer</div>
                    <div className="developer-info-sub-container">
                        <a className="github-icon" href="https://github.com/Seongju90" target="_blank" rel="noreferrer">
                            <img
                                src={githubIcon}
                                alt="github-icon"
                                width="14px"
                                height="14px"
                            />
                        </a>
                        {/* target="_blank" target attribute on a element, tells browser to open in new tab */}
                        {/* rel="noreferrer" instructs browser to not send HTTP header when opening new page, "security reasons" */}
                        <a className="linkedin-icon" href="https://www.linkedin.com/in/lee-philip-31902124a/" target="_blank" rel="noreferrer">
                            <img
                                src={linkedInIcon}
                                alt="linkedin-icon"
                                width="14px"
                                height="14px"
                                style={{paddingLeft:'5px'}}
                            />
                        </a>
                        <div className="developer-name">Philip Lee</div>
                    </div>
                </div>
            </footer>
        </>
    )
}


export default SplashPage
