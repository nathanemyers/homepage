var map;

function initMap() {
  map =  new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34, lng: 150},
    zoom: 8,
    streetViewControl: false,
    mapTypeId: google.maps.MapTypeId.SATELLITE
  });

  var marker = new google.maps.Marker({
    position: {lat: -34, lng: 150},
    map: map,
    title: 'hello, world!'
  });
}
