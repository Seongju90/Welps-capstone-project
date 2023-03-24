import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import OpenModalButton from '../OpenModalButton';
import RestaurantFormModal from '../RestaurantFormModal';



function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
		<div className="nav-bar-main-container">
			<div className="home-button-container">
				<NavLink exact to="/">Home</NavLink>
			</div>
			<OpenModalButton
				buttonText="List a Restaurant"
				modalComponent={RestaurantFormModal}
			/>
			{isLoaded && (
				<div className="profile-button-container">
					<ProfileButton user={sessionUser} />
				</div>
			)}
		</div>
	);
}

export default Navigation;
