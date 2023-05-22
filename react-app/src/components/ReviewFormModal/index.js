import './ReviewFormModal.css'
import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkCreateReview } from '../../store/reviews';


export default function ReviewFormModal () {
    const dispatch = useDispatch()
    const { closeModal } = useModal()

    const [review, setReview] = useState("")
    const [rating, setRating] = useState(0)
    const [errors, setErrors] = useState([])

    const user = useSelector(state => state?.session.user)
    // for now conditionally render the write a review button when you navigate to single restaurant page
    const restaurant = useSelector(state => state?.restaurants.singleRestaurant)

    const handleSubmit = async (e) => {
        e.preventDefault()

        const newReview = {
            'review': review,
            'rating': rating
        }

        const data = await dispatch(thunkCreateReview(newReview, user, restaurant))

        if(data) {
            setErrors(data.errors)
        } else {
            closeModal()
        }
        console.log(errors)
    }


    return (
        <div className="review-main-container">
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
