import { normalizeArray } from "./restaurants"

/*---------------------- TYPE VARIABLES ----------------------*/
const ALL_REVIEWS = "reviews/ALL_REVIEWS"
const MY_REVIEWS = "reviews/MY_REVIEWS"
const CREATE_REVIEWS = "reviews/CREATE_REVIEWS"
const UPDATE_REVIEWS = "reviews/UPDATE_REVIEWS"
const DELETE_REVIEWS = "reviews/DELETE_REVIEWS"


/*---------------------- ACTION CREATORS ----------------------*/

const actionLoadALLReviews = (payload) => {
    return {
        type: ALL_REVIEWS,
        payload
    }
}

const actionLoadMyReviews = (payload) => {
    return {
        type: MY_REVIEWS,
        payload
    }
}

const actionCreateReview = (payload, user) => {
    return {
        type: CREATE_REVIEWS,
        payload,
        user
    }
}

const actionEditReview = (payload) => {
    return {
        type: UPDATE_REVIEWS,
        payload
    }
}

const actionDeleteReview = (payload) => {
    return {
        type: DELETE_REVIEWS,
        payload
    }
}

/*---------------------- THUNK ACTION CREATORS ----------------------*/

export const thunkAllReviews = (id) => async(dispatch) => {
    const response = await fetch(`/api/restaurants/${id}/reviews`)

    if (response.ok) {
        const data = await response.json();
        dispatch(actionLoadALLReviews(data));
        return response
    }

    else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) return data;
    }

    else return { errors: ["An error occurred. Please try again."] }
}

export const thunkMyReviews = (id) => async (dispatch) => {
    const response = await fetch(`/api/users/${id}/reviews`)

    if (response.ok) {
        const data = await response.json();
        dispatch(actionLoadMyReviews(data))
        return response
    }

    else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) return data;
    }

    else return { errors: ["An error occurred. Please try again."] }
}

export const thunkCreateReview = (review, user, restaurant) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/${restaurant.id}/reviews`, {
        method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify(review)
    })

    if(response.ok) {
        const data = await response.json();
        dispatch(actionCreateReview(data, user))
        return null
    }

    else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) return data;
    }
    else return { errors: ["An error occurred. Please try again."] }
}

export const thunkEditReview = (review, id) => async (dispatch) => {
    const response = await fetch(`/api/reviews/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
		body: JSON.stringify(review)
    })

    if (response.ok) {
        const data = await response.json()
        dispatch(actionEditReview(data))
        return null;
    }

    else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) return data;
    }

    else return { errors: ["An error occurred. Please try again."] }
}

export const thunkDeleteReview = (id) => async (dispatch) => {
    const response = await fetch(`/api/reviews/${id}`, {
        method: 'DELETE',
    })

    if (response.ok) {
        dispatch(actionDeleteReview(id))
        return null
    }

    else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) return data;
    }

    else return { errors: ["An error occurred. Please try again."] }
}
/*---------------------- REVIEWS REDUCER ----------------------*/
const initialState = {}
const reviewsReducer = (state = initialState, action) => {
    let newState = {...state}
    switch(action.type) {
        case ALL_REVIEWS:
            newState = normalizeArray(action.payload.Reviews)
            return newState;
        case CREATE_REVIEWS:
            newState[action.payload.id] = action.payload
            return newState;
        case MY_REVIEWS:
            newState = normalizeArray(action.payload.Reviews)
            return newState;
        case UPDATE_REVIEWS:
            newState[action.payload.id] = action.payload
            return newState;
        case DELETE_REVIEWS:
            delete newState[action.payload]
            return newState;
        default:
            return state;
    }
}

export default reviewsReducer
