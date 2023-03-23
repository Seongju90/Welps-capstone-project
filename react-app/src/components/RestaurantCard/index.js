

export default function RestaurantCard ({restaurant}) {
    console.log("%%%%%%%%", restaurant)
    const { preview_image, name, reviews, categories, price } = restaurant

    return (
        <div className="restaurant-card-main-container">
            <img
                className="restaurant-card-img"
                src={preview_image}
                alt="preview-restaurant-img"
            />
            <div className="restaurant-info-container">
                <div className="restaurant-name">{name}</div>
                <div className="restaurant-total-reviews">{reviews.length}</div>
                <div className="category-list">
                    {categories.map(cat => (
                        <div className="restaurant-category">{cat.type}</div>
                    ))}
                </div>
                <div className="restaurant-price">{price}</div>
                <div className="restaurant-review">{reviews.length ? reviews[0]?.review : "No Reviews Yet" } </div>
            </div>
        </div>
    )
}
