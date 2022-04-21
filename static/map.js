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
      // infowindow.open(map, marker);
      drawChart(this);
    });
  }

  //************** */
  function drawChart(marker) {

    // Create the data table.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Topping');
    data.addColumn('number', 'Slices');
    data.addRows([
      ['Mushrooms', 3],
      ['Onions', 1],
      ['Olives', 1],
      ['Zucchini', 1],
      ['Pepperoni', 2]
    ]);

    // Set chart options
    var options = {'title':'Pizza sold @ ','width':400,'height':150};
                   
    var node        = document.createElement('div'),
        infoWindow  = new google.maps.InfoWindow(),
        chart       = new google.visualization.PieChart(node);
        
        chart.draw(data, options);
        infoWindow.setContent(node);
        infoWindow.open(marker.getMap(),marker);
  }
google.load('visualization', '1.0', {'packages':['corechart']});
google.setOnLoadCallback(drawChart);