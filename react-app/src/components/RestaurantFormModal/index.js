import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { thunkCreateRestaurant } from "../../store/restaurants";
import { useModal } from "../../context/Modal";
import "./RestaurantForm.css"
import { ReactComponent as Cityscape } from '../../assets/cityscape_300x233_v2.yji-deccc3d10e15b4494be1.svg';


export default function RestaurantFormModal() {
    const dispatch = useDispatch();
    const { closeModal } = useModal();


    const [name, setName] = useState("")
    const [address, setAddress] = useState("")
    const [city, setCity] = useState("")
    const [state, setState] = useState("")
    const [country, setCountry] = useState("")
    const [zipcode, setZipcode] = useState()
    const [price, setPrice] = useState("")
    const [phoneNumber, setPhoneNumber] = useState("")
    const [previewImage, setPreviewImage] = useState("")
    const [startHours, setStartHours] = useState("")
    const [endHours, setEndHours] = useState("")
    const [errors, setErrors] = useState([])


    const handleSubmit = async (e) => {
        e.preventDefault();

        const data = await dispatch(thunkCreateRestaurant({
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
            'end_hours': endHours
        }))

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
                <h2>List a Restaurant</h2>
                <ul>
                    {errors.map((error, idx) => (
                        <li key={idx}>{error}</li>
                    ))}
                </ul>
                <label>
                        <input
                            type="text"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                            placeholder="Name"
                        />
                </label>
                <label>
                        <input
                            type="text"
                            value={address}
                            onChange={(e) => setAddress(e.target.value)}
                            placeholder="Address"
                        />
                </label>
                <label>
                        <input
                            type="text"
                            value={city}
                            onChange={(e) => setCity(e.target.value)}
                            placeholder="City"
                        />
                </label>
                <label>
                        <input
                            type="text"
                            value={state}
                            onChange={(e) => setState(e.target.value)}
                            placeholder="State"
                        />
                </label>
                <label>
                        <input
                            type="text"
                            value={country}
                            onChange={(e) => setCountry(e.target.value)}
                            placeholder="Country"
                        />
                </label>
                <label>
                        <input
                            type="number"
                            value={zipcode}
                            onChange={(e) => setZipcode(e.target.value)}
                            placeholder="Zipcode"
                        />
                </label>
                <label>
                        <input
                            type="text"
                            value={price}
                            onChange={(e) => setPrice(e.target.value)}
                            placeholder="Price"
                        />
                </label>
                <label>
                        <input
                            type="text"
                            value={phoneNumber}
                            onChange={(e) => setPhoneNumber(e.target.value)}
                            placeholder="Phone Number"
                        />
                </label>
                <label>
                        <input
                            type="text"
                            value={previewImage}
                            onChange={(e) => setPreviewImage(e.target.value)}
                            placeholder="Preview Image Url"
                        />
                </label>
                <label>
                        <input
                            type="text"
                            value={startHours}
                            onChange={(e) => setStartHours(e.target.value)}
                            placeholder="Starting Hours"
                        />
                </label>
                <label>
                        <input
                            type="text"
                            value={endHours}
                            onChange={(e) => setEndHours(e.target.value)}
                            placeholder="Ending Hours"
                        />
                </label>
                <label>
                    <button type="submit" id="modal-submit">Create</button>
                </label>
            </form>
            <div className="form-picture-container">
                <Cityscape/>
            </div>
        </div>
    )
}
