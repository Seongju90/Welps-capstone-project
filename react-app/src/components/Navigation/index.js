import React from "react";
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import OpenModalButton from '../OpenModalButton';
import RestaurantFormModal from '../RestaurantFormModal';
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import ReviewFormModal from "../ReviewFormModal";


function Navigation(){
	const sessionUser = useSelector(state => state.session.user);
	const history = useHistory()


	const clickListRestaurants = (e) => {
		e.preventDefault();
		history.push(`/restaurants`)
	}


	return (
		<div className="nav-bar-main-container">
			<div className="home-button-container">
				<NavLink exact to="/">Home</NavLink>
			</div>
			<div className="right-nav-container">
				<div className="create-main-container">
					<div className="list-all-restaurants" onClick={clickListRestaurants}>
						Browse the Restaurants
					</div>
					<div className="create-restaurant-container">
						<OpenModalButton
							buttonText="List a Restaurant"
							modalComponent={<RestaurantFormModal/>}
							buttonName="create-restaurant-button"
						/>
					</div>
					<div className="create-review-container">
						<OpenModalButton
							buttonText="Write a Review"
							modalComponent={<ReviewFormModal/>}
							buttonName="create-review-button"
						/>
					</div>
			</div>
			{!sessionUser ?
				<div className="login-signup-container">
					<div>
					<OpenModalButton
					buttonText="Log In"
					modalComponent={<LoginFormModal />}
					buttonName="login-button"
					/>
					</div>
					<div>
					<OpenModalButton
					buttonText="Sign Up"
					modalComponent={<SignupFormModal />}
					buttonName="signup-button"
					/>
					</div>
				</div> :
				<ProfileButton user={sessionUser} />}
			</div>
		</div>
	);
}

export default Navigation;
