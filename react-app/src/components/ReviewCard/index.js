import './ReviewCard.css'

import profile from '../../icons/profile-user.svg'

export default function ReviewCard ({review}) {
    const userInfo = review?.user_info

    return (
        <div className='review-card-main-container'>
            <div className="user-main-container">
                <img
                    height={'64px'}
                    width={'64px'}
                    src={profile}
                    alt={'profile-svg'}
                />
                <div>
                    {`${userInfo?.first_name} ${userInfo?.last_name}`}
                </div>
            </div>
            <div className="user-review-container">
                {review.review}
            </div>
        </div>
    )
}
