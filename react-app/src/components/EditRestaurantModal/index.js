import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { thunkEditRestaurants } from "../../store/restaurants";
import { useModal } from "../../context/Modal";
import { ReactComponent as Cityscape } from '../../assets/cityscape_300x233_v2.yji-deccc3d10e15b4494be1.svg';


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
        console.log('frontend', restaurant.id)

        const data = await dispatch(thunkEditRestaurants(restaurant.id, restaurantData))

        if(data) {
            console.log(data)
            setErrors(data.errors)
        } else {
            // if data is created properly, it returns null which close Modal.
            closeModal()
        }
    }


    return (
        <div className="create-form-main-container">
            <form className="create-restaurant-container" onSubmit={handleSubmit}>
                <h2>Edit a Restaurant</h2>
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
                            type="text"
                            value={zipcode}
                            onChange={(e) => setZipcode(e.target.value)}
                            placeholder="Zipcode"
                        />
                </label>
                <label>
                    <select
                        onChange={(e) => setPrice(e.target.value)}
                    >
                        <option value="">--Please choose an option--</option>
                        <option value="$">$</option>
                        <option value="$$">$$</option>
                        <option value="$$$">$$$</option>
                        <option value="$$$$">$$$$</option>
                    </select>
                </label>
                <label>
                        <input
                            type="text"
                            value={phoneNumber}
                            onChange={(e) => setPhoneNumber(e.target.value)}
                            placeholder="Phone Number"
                        />
                </label>
                { errors.phone_number && <div>{errors.phone_number}</div>}
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
                    <button type="submit" id="modal-submit">Edit</button>
                </label>
            </form>
            <div className="form-picture-container">
                <Cityscape/>
            </div>
        </div>
    )
}
