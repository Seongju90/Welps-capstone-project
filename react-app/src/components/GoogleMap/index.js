// src/components/Map.js
import React, { useState } from 'react';
import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';


const Map = () => {
  const [locations, setLocations] = useState([]);
  const apiKey=process.env.GOOGLE_MAPS_API_KEY;

  const mapStyles = {
    height: '400px',
    width: '100%',
  };

  const defaultCenter = { lat: 0, lng: 0 }; // Default center coordinates

  return (
    <LoadScript
      googleMapsApiKey={apiKey}
    >
      <GoogleMap
        mapContainerStyle={mapStyles}
        zoom={2}
        center={defaultCenter}
      >
        {locations.map((location, index) => (
          <Marker
            key={index}
            position={location.coordinates}
            title={location.name}
          />
        ))}
      </GoogleMap>
    </LoadScript>
  );
};

export default Map;
