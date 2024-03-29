import { useSelector, useDispatch } from "react-redux";
import './PhotoModal.css'
import OpenAddImageButton from "../OpenAddImageButton";
import AddRestaurantImageForm from "../AddRestaurantImageForm";
import { useModal } from "../../context/Modal";
import { thunkRemoveImage } from "../../store/restaurants";

import deleteIcon from '../../icons/delete.svg';


function PhotoModal() {
    const dispatch = useDispatch()
    const { closeModal } = useModal();

    const all_photos_array = useSelector(state => state?.restaurants?.singleRestaurant?.images)
    const restaurant = useSelector(state => state?.restaurants?.singleRestaurant)

    const userId = useSelector(state => state?.session?.user?.id)
    const ownerId = useSelector(state => state?.restaurants?.singleRestaurant?.owner_id)


    const deletePhoto = (imageId) => {
        dispatch(thunkRemoveImage(imageId))
        window.alert(`Photo has been deleted from ${restaurant?.name}`)
        closeModal()
    }

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
                    <div className="image-delete-container">
                        <img
                            className="photos-for-restaurant"
                            src={image.url}
                            alt="restaurant-sub"
                            key={image.id}
                        />
                        {ownerId === userId &&
                            <img onClick={() => deletePhoto(image.id)}
                                className="photo-delete-icon"
                                src={deleteIcon}
                                height={'16x'}
                                width={'16px'}
                                alt='icon-delete'
                            />
                        }
                    </div>
                ))}
            </div>
        </div>
    )
}


export default PhotoModal;
