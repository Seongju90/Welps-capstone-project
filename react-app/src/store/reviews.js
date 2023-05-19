import { normalizeArray } from "./restaurants"

/*---------------------- TYPE VARIABLES ----------------------*/
const ALL_REVIEWS = "reviews/ALL_REVIEWS"
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

/*---------------------- REVIEWS REDUCER ----------------------*/
const initialState = {}
const reviewsReducer = (state = initialState, action) => {
    let newState = {...state}
    switch(action.type) {
        case ALL_REVIEWS:
            newState = normalizeArray(action.payload.Reviews)
            return newState;
        default:
            return state;
    }
}

export default reviewsReducer
