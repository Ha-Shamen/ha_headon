import React, { useRef, useEffect, useState } from 'react';
import maplibregl from 'maplibre-gl';
import axios from 'axios'
import 'maplibre-gl/dist/maplibre-gl.css';
import './map.css';

export default function Map() {
    const mapContainer = useRef(null);
    const map = useRef(null);
    const [lng] = useState(139.753);
    const [lat] = useState(35.6844);
    const [zoom] = useState(14);
    const [API_KEY] = useState('sEnYawWlhALyqHmgBl4Z');
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [data, setData] = useState(null);
  

    useEffect(() => {
        const fetchData = async () => {
            try {
              // Set loading to true while fetching data
              setLoading(true);
      
              // Fetch data from the API endpoint
              const response = await axios.get('https://localhost:3001/weather-sites');
      
              // Set the fetched data in the state
              setData(response.data);
            } catch (error) {
              // Handle errors
              setError(error);
            } finally {
              // Set loading to false after fetching data (whether successful or not)
              setLoading(false);
            }
          };
        if (map.current) return; // stops map from intializing more than once
        fetchData();
        map.current = new maplibregl.Map({
          container: mapContainer.current,
          style: `https://api.maptiler.com/maps/streets-v2/style.json?key=${API_KEY}`,
          center: [lng, lat],
          zoom: zoom
        });

        map.current.addControl(new maplibregl.NavigationControl(), 'top-right');
        let temp ='www';
        new maplibregl.Marker({color: "#FF0000"})
        .setLngLat([139.7525,35.6846])
        .addTo(map.current);

        const markerPopup = new maplibregl.Popup({
            closeOnClick: true,
          }).setHTML(`<b>${temp} </b>`);
          // Connect the popup to a new marker
          new maplibregl.Marker().setLngLat([-61.653889, 15.966636]).setPopup(markerPopup).addTo(map);

      }, [API_KEY, lng, lat, zoom]);
    
      return (
        <div className="map-wrap">
            {loading && <p>Loading...</p>}
      {error && <p>Error: {error.message}</p>}
      {data && (
          <div ref={mapContainer} className="map" />
          )}
        </div>
       
      );
  }