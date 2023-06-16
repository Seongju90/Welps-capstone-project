import React, { useState, useEffect, useRef } from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import { useHistory, useLocation } from "react-router-dom";


import profile2 from "../../icons/profile-user2.svg"
import profile1 from "../../icons/profile-user.svg"

function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const history = useHistory();
  const location = useLocation();

  const [showMenu, setShowMenu] = useState(false);
  const ulRef = useRef();

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (!ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const handleLogout = (e) => {
    e.preventDefault();
    dispatch(logout());
    history.push(`/`)
  };

  const clickMyProfile = (e) => {
    e.preventDefault();
    history.push(`/users/${user.id}/myprofile`)
    setShowMenu(false)
  }

  const ulClassName = "profile-dropdown" + (showMenu ? "" : " hidden");

  return (
    <>
      {location.pathname === "/" ?
          <img
            className="nav-profile-user-img"
            src={profile1}
            alt={"profile-svg-2"}
            onClick={openMenu}
          /> :
          <img
          className="nav-profile-user-img"
          src={profile2}
          alt={"profile-svg-2"}
          onClick={openMenu}
        />
      }
      <div className={ulClassName} ref={ulRef}>
          <div className="drop-down-name">{user.username}</div>
          <div className="drop-down-email">{user.email}</div>
          <div className="drop-down-myprofile"onClick={clickMyProfile}>My Profile</div>
          <div className="drop-down-logout"onClick={handleLogout}>Log Out</div>
      </div>
    </>
  );
}

export default ProfileButton;
