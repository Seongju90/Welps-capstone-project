/*---------------------- TYPE VARIABLES ----------------------*/
const SEARCH_RESTAURANTS = "restaurants/SEARCH_RESTAURANTS"


/*---------------------- ACTION CREATORS ----------------------*/

const actionSearchRestaurants = (payload) => {
    return {
        type: SEARCH_RESTAURANTS,
        payload
    }
}


/*---------------------- THUNK ACTION CREATORS ----------------------*/

export const thunkSearchRestaurants = (query) => async(dispatch) => {
    const response = await fetch(`/api/search?query=${query}`)

    if (response.ok) {
        const data = await response.json()
        dispatch(actionSearchRestaurants(data))
        return response
    }

    else if (response.status < 500) {
        const data = await response.json()
        if (data.errors) return data;
    }

    else return { errors: ["An error occured. Please try again"]}
}


/*---------------------- SEARCH REDUCER ----------------------*/
const initialState = {}
const searchReducer = (state = initialState, action) => {
    let newState = {...state}
    switch(action.type) {
        case SEARCH_RESTAURANTS:
            newState = action.payload.Search
            newState.push(action.payload.Results)
            return newState;
        default:
            return state;
    }
}


export default searchReducer
