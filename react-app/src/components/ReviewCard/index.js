import './ReviewCard.css'


export default function ReviewCard ({review}) {

    return (
        <div className='review-main-container'>
            {review.review}
        </div>
    )
}
