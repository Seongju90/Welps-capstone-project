import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from 'react-redux';
import { useHistory, useLocation } from 'react-router-dom';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import OpenModalButton from '../OpenModalButton';
import RestaurantFormModal from '../RestaurantFormModal';
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import { thunkSearchRestaurants } from "../../store/search";

import redCloudLogo from '../../icons/red-cloud-logo.svg'
import whiteCloudLogo from '../../icons/white-cloud-svg.svg'

function Navigation(){
	const sessionUser = useSelector(state => state.session.user);
	const dispatch = useDispatch()
	const history = useHistory()
	const location = useLocation()

	// search state
	const [searchQuery, setSearchQuery] = useState('')

	const handleSearch = () => {
		dispatch(thunkSearchRestaurants(searchQuery))
	}

	// styling state
	const [loginStyling, setLoginStyling] = useState('login-splash-button')
	const [allRestaurantStyling, setAllRestaurantStyling] = useState('nav-list-all-restaurants')
	const [createRestaurantStyling, setCreateRestaurantStyling] = useState('nav-create-restaurant-button')
	const [logoColor, setLogoColor] = useState(whiteCloudLogo)
	const [textColor, setTextColor] = useState('app-text-heading-splash')

	useEffect(() => {
		if (location.pathname === '/') {
			setLoginStyling('login-splash-button')
			setAllRestaurantStyling('nav-list-all-restaurants')
			setCreateRestaurantStyling('nav-create-restaurant-button')
			setLogoColor(whiteCloudLogo)
			setTextColor('app-text-heading-splash')
		} else {
			setLoginStyling('login-button-nonsplash')
			setAllRestaurantStyling('nav-list-all-restaurants-nonsplash')
			setCreateRestaurantStyling('nav-create-restaurant-button-nonsplash')
			setLogoColor(redCloudLogo)
			setTextColor('app-text-heading-nonsplash')
		}
	},[setLoginStyling, setAllRestaurantStyling, setCreateRestaurantStyling, setLogoColor, setTextColor, location.pathname])

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
				<span className={textColor} onClick={clickHome}>Welp</span>
				<img
					onClick={clickHome}
					height="50px"
					width="50px"
					src={logoColor}
					alt="app-logo"
				/>
			</div>
			<div>
				<input
					type="text"
					placeholder="Search for restaurants..."
					value={searchQuery}
					onChange={(e) => setSearchQuery(e.target.value)}
				/>
				<button onClick={handleSearch}>Search</button>
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
