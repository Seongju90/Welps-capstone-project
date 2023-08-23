import { useSelector, useDispatch } from "react-redux";
import './PhotoModal.css'
import OpenAddImageButton from "../OpenAddImageButton";
import AddRestaurantImageForm from "../AddRestaurantImageForm";

import deleteIcon from '../../icons/delete.svg';


function PhotoModal() {
    const dispatch = useDispatch()

    const all_photos_array = useSelector(state => state?.restaurants?.singleRestaurant?.images)
    const restaurant = useSelector(state => state?.restaurants?.singleRestaurant)

    const userId = useSelector(state => state?.session?.user?.id)
    const ownerId = useSelector(state => state?.restaurants?.singleRestaurant?.owner_id)


    const deletePhoto = (imageId) => {
        dispatch()
        window.alert(`Photo has been deleted from ${restaurant?.name}`)
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
                    <div>
                        <img
                            src={image.url}
                            alt="restaurant-images"
                            key={image.id}
                        />
                        {ownerId === userId &&
                            <img onClick={() => deletePhoto(image.id)}
                                className="photo-delete-icon"
                                src={deleteIcon}
                                height={'16x'}
                                width={'16px'}
                                alt={'photo-delete'}
                            />
                        }
                    </div>
                ))}
            </div>
        </div>
    )
}


export default PhotoModal;
