import './ReviewCard.css'


export default function ReviewCard ({review}) {
    console.log(review)
    return (
        <div className='review-main-container'>
            {review.review}
        </div>
    )
}
