import React from 'react'
import { GoogleMap, useJsApiLoader } from '@react-google-maps/api';

const containerStyle = {
  width: '500px',
  height: '400px'
};

const center = {
  lat: -3.745,
  lng: -38.523
};

export default function Map() {
    const { isLoaded } = useJsApiLoader({
        id: 'google-map-script',
        googleMapsApiKey: 'AIzaSyC_7Mgk9VvxfpQPw4v7_65dQuULouNZdUE'
    })



  return isLoaded ? (
      <GoogleMap
        mapContainerStyle={containerStyle}
        center={center}
        zoom={10}
      >
      </GoogleMap>
  ) : <></>
}
