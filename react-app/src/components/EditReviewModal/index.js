import './EditReviewModal.css';
import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkEditReview } from '../../store/reviews';


export default function EditReviewModal ({reviews}) {
    const dispatch = useDispatch()
    const { closeModal } = useModal()

    const [review, setReview] = useState(reviews.review)
    const [rating, setRating] = useState(reviews.rating)
    const [errors, setErrors] = useState([])


    const handleSubmit = async (e) => {
        e.preventDefault()

        const reviewData = {
            'review': review,
            'rating': rating
        }

        const data = await dispatch(thunkEditReview(reviewData, reviews?.id))

        if(data) {
            setErrors(data.errors)
        } else {
            closeModal()
        }
    }


    return (
        <div className="review-form-main-container">
            <form className="review-form-container" onSubmit={handleSubmit}>
                <h1>Write a Review</h1>
                <div className="review-form-input-container">
                    <label>
                        <input
                            className="review-input-form"
                            type="text"
                            value={review}
                            onChange={(e) => setReview(e.target.value)}
                            placeholder='Write your review!'
                        />
                    </label>
                    {errors.review && <div className="errors">{errors.review}</div>}
                </div>
                <div className="review-rating-container">
                    <div style={{marginTop: "1vw"}}>Rating</div>
                    <label>
                        <input
                            className="review-rating-input-form"
                            type="number"
                            value={rating}
                            onChange={(e) => setRating(e.target.value)}
                            placeholder='Give your rating!'
                        />
                    </label>
                    {errors.rating && <div className="errors">{errors.rating}</div>}
                </div>
                <label>
                    <button className="review-create-submit-button"type="submit" id="modal-submit">Submit</button>
                </label>
            </form>
        </div>
    )
}
