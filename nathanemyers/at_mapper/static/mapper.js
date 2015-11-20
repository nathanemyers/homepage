var map;

function initMap() {
  map =  new google.maps.Map(document.getElementById('map'), {
    center: {lat: 40.03765833333333, lng: -77.35314166666667},
    zoom: 12,
    streetViewControl: false,
    mapTypeId: google.maps.MapTypeId.SATELLITE
  });


  $.getJSON("/static/gps.json", function(data) {

    data = data;
    for(var i = 0; i < data.image_locs.length; i++) {
      new MarkerWithLabel({
        position: {
          lat: data.image_locs[i][0], 
          lng: data.image_locs[i][1] 
        },
        icon: ' ',
        map: map,
        labelContent: '<i class="fa fa-star" style="color:yellow"></i>'
      });
    }

  });
}


