import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
		<div className="nav-bar-main-container">
			<div className="home-button-container">
				<NavLink exact to="/">Home</NavLink>
			</div>
			{isLoaded && (
				<div className="profile-button-container">
					<ProfileButton user={sessionUser} />
				</div>
			)}
		</div>
	);
}

export default Navigation;
