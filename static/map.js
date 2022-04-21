function initMap() {
    const uluru = { lat: 34.241560, lng: -118.418834 };
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 4,
      center: uluru,
    });

    const marker = new google.maps.Marker({
      position: uluru,
      map: map,
    });

    //add popup window
    const infowindow = new google.maps.InfoWindow({
      content: 'Data Information: Type of Cars, Density, Numbers, Speed'
    });

    marker.addListener("click", function() {
      infowindow.open(map, marker);
    });
  }