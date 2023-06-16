import './RestaurantCard.css';
import { useHistory } from "react-router-dom";

import chatBubble from '../../icons/chat-bubble.svg'

export default function RestaurantCard ({restaurant}) {
    const history = useHistory()
    const { id, preview_image, name, reviews, categories, price } = restaurant

    const navigateToSingleRestaurant = () => {
        history.push(`/restaurants/${restaurant.id}`)
    }

    return (
        <>
            <div className="restaurant-card-container" onClick={navigateToSingleRestaurant}>
                <div className="restaurant-img-container" >
                    <img
                        className="restaurant-card-img"
                        src={preview_image}
                        alt="preview-restaurant-img"
                    />
                </div>
                <div className="index-restaurant-info-container">
                    <div className="index-restaurant-name">{id}. {name}</div>
                    <div className="index-restaurant-total-reviews">{reviews?.length} reviews</div>
                    <div className="index-category-list">
                        {categories?.length ? categories.map(cat => (
                            <div className="index-restaurant-category" key={cat?.id}>{cat?.type}</div>
                        )) : 'None'}
                        <span className="index-restaurant-price">{price}</span>
                    </div>
                    <div className="index-restaurant-review">
                        <div>
                            <img height={'20px'} width={'20px'}src={chatBubble} alt={'index-chat-bubble'}/>
                        </div>
                        <span className="index-review-preview">
                            {reviews?.length ? reviews[0]?.review : "No Reviews Yet" }
                        </span>
                    </div>
                </div>
            </div>
        </>
    )
}
