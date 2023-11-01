import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { thunkEditRestaurants } from "../../store/restaurants";
import { useModal } from "../../context/Modal";


export default function EditRestaurantModal({restaurant}) {
    const dispatch = useDispatch();
    const { closeModal } = useModal();


    const [name, setName] = useState(restaurant.name)
    const [address, setAddress] = useState(restaurant.address)
    const [city, setCity] = useState(restaurant.city)
    const [state, setState] = useState(restaurant.state)
    const [country, setCountry] = useState(restaurant.country)
    const [zipcode, setZipcode] = useState(restaurant.zipcode)
    const [price, setPrice] = useState()
    const [phoneNumber, setPhoneNumber] = useState(restaurant.phone_number)
    const [previewImage, setPreviewImage] = useState(restaurant.preview_image)
    const [startHours, setStartHours] = useState(restaurant.start_hours)
    const [endHours, setEndHours] = useState(restaurant.end_hours)
    const [errors, setErrors] = useState([])


    const handleSubmit = async (e) => {
        e.preventDefault();

        const restaurantData = {
            'name': name,
            'address': address,
            'city': city,
            'state': state,
            'country': country,
            'zipcode': zipcode,
            'price': price,
            'phone_number': phoneNumber,
            'preview_image': previewImage,
            'start_hours': startHours,
            'end_hours': endHours,
        }


        const data = await dispatch(thunkEditRestaurants(restaurant.id, restaurantData))

        if(data) {
            setErrors(data.errors)
        } else {
            // if data is created properly, it returns null which close Modal.
            closeModal()
        }
    }

    return (
        <div className="create-form-main-container">
            <form className="create-restaurant-container" onSubmit={handleSubmit}>
                <h2>Edit your Restaurant Details</h2>
                <div className="restaurant-form-name">
                    <label>Restaurant Name:</label>
                    <input
                        className="input-name"
                        type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                        placeholder="Name"
                    />
                </div>
                {errors.name && <div className="error">{errors.name}</div>}
                <div className="restaurant-form-address">
                    <div className="address-container">
                        <label>Address:</label>
                        <input
                            className="input-address"
                            type="text"
                            value={address}
                            onChange={(e) => setAddress(e.target.value)}
                            placeholder="Address"
                        />
                    </div>
                    {errors.address && <div className="error">{errors.address}</div>}
                    <div className="city-state-container">
                        <input
                            className="input-city"
                            type="text"
                            value={city}
                            onChange={(e) => setCity(e.target.value)}
                            placeholder="City"
                        />
                        <input
                            className="input-state"
                            type="text"
                            value={state}
                            onChange={(e) => setState(e.target.value)}
                            placeholder="State"
                            />
                    </div>
                    <div className="city-state">
                        {errors.city && <div className="error">{errors.city}</div>}
                        {errors.state && <div className="error">{errors.state}</div>}
                    </div>
                    <div className="country-zipcode-container">
                        <input
                            className="input-country"
                            type="text"
                            value={country}
                            onChange={(e) => setCountry(e.target.value)}
                            placeholder="Country"
                        />
                        <input
                            className="input-zipcode"
                            type="text"
                            value={zipcode}
                            onChange={(e) => setZipcode(e.target.value)}
                            placeholder="Zipcode"
                        />
                    </div>
                    <div className="country-zipcode">
                        {errors.country && <div className="error">{errors.country}</div>}
                        {errors.zipcode && <div className="error">{errors.zipcode}</div>}
                    </div>
                </div>
                <div className="restaurant-form-price">
                    <label>Price</label>
                    <select
                        className="input-price"
                        onChange={(e) => setPrice(e.target.value)}
                    >
                        <option value="">--Please choose an option--</option>
                        <option value="$">$</option>
                        <option value="$$">$$</option>
                        <option value="$$$">$$$</option>
                        <option value="$$$$">$$$$</option>
                    </select>
                    {errors.price && <div className="error">{errors.price}</div>}
                </div>
                <div className="restaurant-form-phone">
                    <label>Phone Number:</label>
                        <input
                            className="input-phone"
                            type="text"
                            value={phoneNumber}
                            onChange={(e) => setPhoneNumber(e.target.value)}
                            placeholder="Phone Number"
                        />
                    {errors.phone_number && <div className="error">{errors.phone_number}</div>}
                </div>
                <div className="restaurant-form-preview">
                    <label>Preview Image Url:</label>
                    <input
                        className="input-preview"
                        type="text"
                        value={previewImage}
                        onChange={(e) => setPreviewImage(e.target.value)}
                        placeholder="Preview Image Url"
                    />
                    {errors.preview_image && <div className="error">{errors.preview_image}</div>}
                </div>
                <div className="start-end-hour-container">
                    <div className="restaurant-form-start-hour">
                        <label>Starting Hour:</label>
                        <input
                            className="input-start-hour"
                            type="text"
                            value={startHours}
                            onChange={(e) => setStartHours(e.target.value)}
                            placeholder="00:00 AM"
                        />
                    </div>
                    <div className="restaurant-form-end-hour">
                        <label className="end-label">Ending Hour:</label>
                        <input
                            className="input-end-hour"
                            type="text"
                            value={endHours}
                            onChange={(e) => setEndHours(e.target.value)}
                            placeholder="00:00 PM"
                        />
                    </div>
                </div>
                <div className="start-end-hours">
                    {errors.start_hours && <div className="error">{errors.start_hours}</div>}
                    {errors.end_hours && <div className="error">{errors.end_hours}</div>}
                    {errors.validate_start_hour && <div className="error">{errors.validate_start_hour}</div>}
                </div>
                <button className="create-submit-button" type="submit" id="modal-submit">Submit</button>
            </form>
        </div>
    )
}
