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
        <div className="edit-review-main-container">
            <form className="edit-review-form-container" onSubmit={handleSubmit}>
                <h1>Edit your Review</h1>
                <label>
                    <input
                        type="text"
                        value={review}
                        onChange={(e) => setReview(e.target.value)}
                        placeholder='Write your review!'
                    />
                </label>
                <label>
                    <input
                        type="number"
                        value={rating}
                        onChange={(e) => setRating(e.target.value)}
                        placeholder='Give your rating!'
                    />
                </label>
                <label>
                    <button type="submit" id="modal-submit">Submit</button>
                </label>
            </form>
        </div>
    )
}
