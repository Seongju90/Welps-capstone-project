import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";


import MyProfilePage from "./components/MyProfilePage";
import RestaurantsIndex from "./components/RestaurantsIndex";
import SplashPage from "./components/SplashPage";
import SingleRestaurantPage from "./components/SingleRestaurantPage";


function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route>
          <Route path="/users/:id/myprofile">
            <MyProfilePage/>
          </Route>
          <Route exact path="/restaurants/:restaurantId">
            <SingleRestaurantPage/>
          </Route>
          {/* either place more detail route above, or use exact path for everything */}
          <Route exact path="/search/:query">
            <RestaurantsIndex/>
          </Route>
          <Route exact path="/restaurants">
            <RestaurantsIndex/>
          </Route>
          <Route exact path="/">
            <SplashPage/>
          </Route>
        </Switch>
      )}
    </>
  );
}

export default App;
