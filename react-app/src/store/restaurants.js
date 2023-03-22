/*---------------------- TYPE VARIABLES ----------------------*/
 const  ALL_RESTAURANTS = "restaurants/ALL_RESTAURANTS"


/*---------------------- ACTION CREATORS ----------------------*/
const allRestaurants = (restaurants) => {
    return {
        type: ALL_RESTAURANTS,
        restaurants
    }
}


/*---------------------- THUNK ACTION CREATORS ----------------------*/
export const thunkAllRestaurants = () => async (dispatch) => {
    const response = await fetch(`/api/restaurants/`, {
        headers: { "Content-Type": "application/json"},
    })

    if (response.ok) {
        const data = await response.json();
        dispatch(allRestaurants(data));
        return response
    }
    else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) return data;
    }
    else return { errors: ["An error occurred. Please try again."] }
}


/*---------------------- RESTAURANTS REDUCER ----------------------*/
const initialState = {}
const restaurantsReducer = (state = initialState, action) => {
    let newState = {...state}
}

export default restaurantsReducer


/* ---------- NORMALIZE ARRAY HELPER FUNCTION ----------*/
const normalizeArray = (array) => {
    if (!(array instanceof Array)) throw new Error('Can not normalize data that is not an array')

    // create an empty object to normalize the data array
    const obj = {}
    // for each data we are making setting the id to new in in empty obj to make 0(1) search time.
    array.forEach(data => {
        obj[data.id] = data
    })

    return obj;
}
