import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from 'react-router-dom';
import { useModal } from "../../context/Modal";
import "./AddRestaurantImageForm.css"
import { thunkAddImage } from "../../store/restaurants";

export default function AddRestaurantImageForm({ restaurantId, restaurantName }) {
    const dispatch = useDispatch()
    const history = useHistory()
    const { closeModal } = useModal()

    const [image, setImage] = useState(null)
    const [errors, setErrors] = useState([])

    const restaurant = useSelector(state => state?.restaurants?.singleRestaurant)

    const handleSubmit = async (e) => {
        e.preventDefault()

        const formData = new FormData()
        formData.append("image", image)
        formData.append("preview", false)

        const data = await dispatch(thunkAddImage(restaurant?.id, formData))

        if (data) {
            setErrors(data.errors)
        } else {
            closeModal()
            history.push(`/restaurants/${restaurant?.id}`)
        }
    }

    return (
        <div className="add-image-form-main-container">
            <form className="add-image-form-container" onSubmit={handleSubmit} encType="multipart/form-data">
                <h1 className="add-image-header">Add an Image to {restaurant?.name}</h1>
                <div className="image-label-input-container">
                    <label>Add Image:</label>
                        <input
                            className="input-preview"
                            type="file"
                            accept="image/*"
                            onChange={(e) => setImage(e.target.files[0])}
                        />
                </div>
                <button className="add-image-submit-button" type="submit">Submit</button>
            </form>
        </div>
    )
}
