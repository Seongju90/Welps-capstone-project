import React, { useState } from "react";
import { useDispatch } from "react-redux";



export default function RestaurantFormModal() {
    const dispatch = useDispatch()

    const [name, setName] = useState("")
    const [address, setAddress] = useState("")
    const [city, setCity] = useState("")
    const [state, setState] = useState("")
    const [country, setCountry] = useState("")
    const [zipcode, setZipcode] = useState(0)
    const [price, setPrice] = useState("")
    const [phoneNumber, setPhoneNumber] = useState("")
    const [previewImage, setPreviewImage] = useState("")
    const [startHours, setStartHours] = useState("")
    const [endHours, setEndHours] = useState("")

    return (
        <>
            <form onSubmit={handleSubmit}>
            <   ul>
					{errors.map((error, idx) => (
						<li key={idx}>{error}</li>
					))}
				</ul>
                <label>
			    		Email
			    		<input
			    			type="text"
			    			value={email}
			    			onChange={(e) => setEmail(e.target.value)}
			    			required
			    		/>
			    </label>
                <label>
			    		Email
			    		<input
			    			type="text"
			    			value={email}
			    			onChange={(e) => setEmail(e.target.value)}
			    			required
			    		/>
			    </label>
                <label>
			    		Email
			    		<input
			    			type="text"
			    			value={email}
			    			onChange={(e) => setEmail(e.target.value)}
			    			required
			    		/>
			    </label>
                <label>
			    		Email
			    		<input
			    			type="text"
			    			value={email}
			    			onChange={(e) => setEmail(e.target.value)}
			    			required
			    		/>
			    </label>
                <label>
			    		Email
			    		<input
			    			type="text"
			    			value={email}
			    			onChange={(e) => setEmail(e.target.value)}
			    			required
			    		/>
			    </label>
                <label>
			    		Email
			    		<input
			    			type="text"
			    			value={email}
			    			onChange={(e) => setEmail(e.target.value)}
			    			required
			    		/>
			    </label>
                <label>
			    		Email
			    		<input
			    			type="text"
			    			value={email}
			    			onChange={(e) => setEmail(e.target.value)}
			    			required
			    		/>
			    </label>
                <label>
			    		Email
			    		<input
			    			type="text"
			    			value={email}
			    			onChange={(e) => setEmail(e.target.value)}
			    			required
			    		/>
			    </label>
            </form>
        </>
    )
}
