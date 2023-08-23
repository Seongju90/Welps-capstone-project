import { useModal } from "../../context/Modal";
import { useSelector } from "react-redux";
import './PhotoModal.css'
import OpenAddImageButton from "../OpenAddImageButton";
import AddRestaurantImageForm from "../AddRestaurantImageForm";

function PhotoModal() {
    const all_photos_array = useSelector(state => state?.restaurants?.singleRestaurant?.images)
    const restaurant = useSelector(state => state?.restaurants?.singleRestaurant)
    const { closeModal } = useModal();


    return (
        <div className="photos-main-container">
            <div className="header-and-add-button">
                <h1>Photos for {restaurant?.name}</h1>
                <OpenAddImageButton
                    buttonText="Add Photo"
                    modalComponent={<AddRestaurantImageForm/>}
                    buttonName="add-photo-restaurant-button"
                    restaurantId = {restaurant?.id}
                    restaurantName = {restaurant?.name}
                />
            </div>
            <div className="photo-grid">
                {all_photos_array.map(image => (
                    <img
                        src={image.url}
                        alt="restaurant-images"
                        key={image.id}
                    />
                ))}
            </div>
        </div>
    )
}


export default PhotoModal;
