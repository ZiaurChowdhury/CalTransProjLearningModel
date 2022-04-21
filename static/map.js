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
      // testChart(this);
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
    var options = {'title':'Pizza sold ','width':400,'height':150};
                   
    var node        = document.createElement('div'),
        infoWindow  = new google.maps.InfoWindow(),
        chart       = new google.visualization.PieChart(node);
        
        chart.draw(data, options);
        infoWindow.setContent(node);
        infoWindow.open(marker.getMap(),marker);
  }
/***** */
function testChart(marker) {
  var options = {region: 'US', resolution: 'provinces'};
        var dimension = "population";
        $.ajax({
          url: "viewcount.php",
          dataType: "JSON"
        }).done(function(data) {
                var statesArray = [["State",dimension]];
                $.each(data.states, function() {
                    var stateitem = [this.abbrev, this[dimension]];
                    statesArray.push(stateitem);
                });
          var statesData = google.visualization.arrayToDataTable(statesArray);
          let node = document.createElement('div'), info = new google.maps.InfoWindow();
          var chart = new google.visualization.GeoChart(document.getElementById(node));
          chart.draw(statesData, options);
          info.setContent(node);
          info.open(marker.getMap(),marker);
          $("h3").append(" Sorted by  "+dimension);
        });
}
/***** */    
google.load('visualization', '1.0', {'packages':['corechart']});
// google.setOnLoadCallback(drawChart);
google.setOnLoadCallback(testChart);

