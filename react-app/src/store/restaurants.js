/*---------------------- TYPE VARIABLES ----------------------*/
const ALL_RESTAURANTS = "restaurants/ALL_RESTAURANTS"
const ONE_RESTAURANTS = "restaurants/ONE_RESTAURANTS"
const CREATE_RESTAURANTS = "restaurants/CREATE_RESTAURANTS"
const MY_RESTAURANTS = 'restaurants/MY_RESTAURANTS'
const EDIT_RESTAURANTS = "restaurants/EDIT_RESTAURANTS"
const DELETE_RESTAURANTS = "restaurants/DELETE_RESTAURANTS"

/*---------------------- ACTION CREATORS ----------------------*/
const actionLoadAllRestaurants = (payload) => {
    return {
        type: ALL_RESTAURANTS,
        payload
    }
}

const actionLoadOneRestaurant = (payload) => {
    return {
        type: ONE_RESTAURANTS,
        payload
    }
}

const actionCreateRestaurants = (payload) => {
    return {
        type: CREATE_RESTAURANTS,
        payload
    }
}

const actionMyRestaurants = (payload) => {
    return {
        type: MY_RESTAURANTS,
        payload
    }
}

const actionEditRestaurants = (payload) => {
    return {
        type: EDIT_RESTAURANTS,
        payload
    }
}

const actionDeleteRestaurants = (payload) => {
    return {
        type: DELETE_RESTAURANTS,
        payload
    }
}

/*---------------------- THUNK ACTION CREATORS ----------------------*/
export const thunkAllRestaurants = () => async (dispatch) => {
    const response = await fetch(`/api/restaurants`)

    if (response.ok) {
        const data = await response.json();
        dispatch(actionLoadAllRestaurants(data));
        return response
    }

    else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) return data;
    }

    else return { errors: ["An error occurred. Please try again."] }
}

export const thunkOneRestaurant = (id) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/${id}`, {
        headers: {"Content-Type": "application/json"},
    })

    if (response.ok) {
        const data = await response.json()
        dispatch(actionLoadOneRestaurant(data))
        return null
    }

    else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) return data;
    }

    else return { errors: ["An error occurred. Please try again."] }
}

export const thunkCreateRestaurant = (form) => async (dispatch) => {
    const response = await fetch(`/api/restaurants`, {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify(form)
    })

    if(response.ok) {
        const newRes = await response.json();
        dispatch(actionCreateRestaurants(newRes))
        return newRes
    }

    else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) return data;
    }

    else return { errors: ["An error occurred. Please try again."] }
}

export const thunkMyRestaurants = (id) =>  async (dispatch) => {
    const response = await fetch(`/api/users/${id}/restaurants`)

    if (response.ok) {
        const data = await response.json();
        dispatch(actionMyRestaurants(data))
        return response
    }

    else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) return data;
    }

    else return { errors: ["An error occurred. Please try again."] }
}

export const thunkEditRestaurants = (id, form) => async (dispatch) => {
    // this fetch hits the backend route, no link to the actual URL
    const response = await fetch(`/api/restaurants/${id}`,{
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(form)
    })

    if (response.ok) {
        const data = await response.json()
        dispatch(actionEditRestaurants(data))
        return null;
    }

    else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) return data;
    }

    else return { errors: ["An error occurred. Please try again."] }
}

export const thunkDeleteRestaurants = (id) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/${id}`, {
        method: 'DELETE',
    })

    if (response.ok) {
        dispatch(actionDeleteRestaurants(id))
        return null
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
    switch (action.type) {
        case ALL_RESTAURANTS:
            newState = normalizeArray(action.payload.Restaurants)
            return newState;
        case ONE_RESTAURANTS:
            // clear old data and state
            newState = {}
            newState.singleRestaurant = action.payload.Single_Restaurant
            return newState;
        case CREATE_RESTAURANTS:
            newState[action.payload.id] = action.payload
            return newState;
        case MY_RESTAURANTS:
            newState = normalizeArray(action.payload.Restaurants)
            return newState;
        case EDIT_RESTAURANTS:
            newState[action.payload.id] = action.payload
            return newState;
        case DELETE_RESTAURANTS:
            delete newState[action.payload]
            return newState;
        default:
            return state;
    }
}

export default restaurantsReducer


/* ---------- NORMALIZE ARRAY HELPER FUNCTION ----------*/
export const normalizeArray = (array) => {
    if (!(array instanceof Array)) throw new Error('Can not normalize data that is not an array')

    // create an empty object to normalize the data array
    const obj = {}
    // for each data we are making setting the id to new in in empty obj to make 0(1) search time.
    array.forEach(data => {
        obj[data.id] = data
    })

    return obj;
}
