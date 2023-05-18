import './RestaurantCard.css';
import { Link } from "react-router-dom";


export default function RestaurantCard ({restaurant}) {
    const { id, preview_image, name, reviews, categories, price } = restaurant

    return (
        <div className="restaurant-card-container">
            <Link className="restaurant-img-container" to={`/restaurants/${restaurant.id}`}>
                <img
                    className="restaurant-card-img"
                    src={preview_image}
                    alt="preview-restaurant-img"
                />
            </Link>
            <div className="restaurant-info-container">
                <div className="restaurant-name">{id}. {name}</div>
                <div className="restaurant-total-reviews">{reviews?.length}</div>
                <div className="category-list">
                    {categories?.length ? categories.map(cat => (
                        <div className="restaurant-category" key={cat?.id}>{cat?.type}</div>
                    )) : 'None'}
                    <span className="restaurant-price">{price}</span>
                </div>
                <div className="restaurant-review">{reviews?.length ? reviews[0]?.review : "No Reviews Yet" } </div>
            </div>
        </div>
    )
}
