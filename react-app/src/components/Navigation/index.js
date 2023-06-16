import React, { useEffect, useState } from "react";
import { useSelector } from 'react-redux';
import { useHistory, useLocation } from 'react-router-dom';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import OpenModalButton from '../OpenModalButton';
import RestaurantFormModal from '../RestaurantFormModal';
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";


import cloudLogo from '../../icons/noun-cloud.svg'

function Navigation(){
	const sessionUser = useSelector(state => state.session.user);
	const history = useHistory()
	const location = useLocation()

	const [loginStyling, setLoginStyling] = useState('login-splash-button')
	const [allRestaurantStyling, setAllRestaurantStyling] = useState('nav-list-all-restaurants')
	const [createRestaurantStyling, setCreateRestaurantStyling] = useState('nav-create-restaurant-button')

	useEffect(() => {
		if (location.pathname === '/') {
			setLoginStyling('login-splash-button')
			setAllRestaurantStyling('nav-list-all-restaurants')
			setCreateRestaurantStyling('nav-create-restaurant-button')
		} else {
			setLoginStyling('login-button-nonsplash')
			setAllRestaurantStyling('nav-list-all-restaurants-nonsplash')
			setCreateRestaurantStyling('nav-create-restaurant-button-nonsplash')
		}
	})

	const clickListRestaurants = (e) => {
		e.preventDefault();
		history.push(`/restaurants`)
	}

	const clickHome = (e) => {
		e.preventDefault();
		history.push(`/`)
	}

	return (
		<div className="nav-bar-main-container">
			<div className="home-button-container">
				<img
					onClick={clickHome}
					height="100px"
					width="100px"
					src={cloudLogo}
				/>
			</div>
			<div className="right-nav-container">
				<div className="create-main-container">
					<div className={allRestaurantStyling} onClick={clickListRestaurants}>
						Browse the Restaurants
					</div>
					{/* conditionally render the create restaurant */}
					{ sessionUser &&
						<div className="create-restaurant-main-container">
							<OpenModalButton
								buttonText="List a Restaurant"
								modalComponent={<RestaurantFormModal/>}
								buttonName={createRestaurantStyling}
							/>
						</div>
					}
			</div>
			{!sessionUser ?
				<div className="login-signup-container">
					<div>
					<OpenModalButton
					buttonText="Log In"
					modalComponent={<LoginFormModal />}
					buttonName={loginStyling}
					/>
					</div>
					<div>
					<OpenModalButton
					buttonText="Sign Up"
					modalComponent={<SignupFormModal />}
					buttonName="signup-splash-button"
					/>
					</div>
				</div> :
				<ProfileButton user={sessionUser}/>}
			</div>
		</div>
	);
}

export default Navigation;
