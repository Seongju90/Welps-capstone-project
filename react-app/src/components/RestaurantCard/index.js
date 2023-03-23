import './RestaurantCard.css';

export default function RestaurantCard ({restaurant}) {
    const { id, preview_image, name, reviews, categories, price } = restaurant

    return (
        <div className="restaurant-card-container">
            <div className="restaurant-img-container">
                <img
                    className="restaurant-card-img"
                    src={preview_image}
                    alt="preview-restaurant-img"
                />
            </div>
            <div className="restaurant-info-container">
                <div className="restaurant-name">{id}. {name}</div>
                <div className="restaurant-total-reviews">{reviews.length}</div>
                <div className="category-list">
                    {categories.map(cat => (
                        <div className="restaurant-category" key={cat.id}>{cat.type}</div>
                    ))}
                    <span className="restaurant-price">{price}</span>
                </div>
                {/* <div className="restaurant-price">{price}</div> */}
                <div className="restaurant-review">{reviews.length ? reviews[0]?.review : "No Reviews Yet" } </div>
            </div>
        </div>
    )
}
