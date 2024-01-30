console.log("Hola mundo");

$('#staticBackdrop').on('shown.bs.modal', function(event) {

    const options = {
        enableHighAccuracy: true, //mejora la ubicacion en gps
    };

    //posiciones del rectangulo en el mapa al dar click
    var bounds = [[54.559322, -5.767822], [56.1210604, -3.021240]];
let df=undefined;

    var map = L.map('mapa_maps').setView([51.505, -0.09], 13);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    
    df=L.marker([51.5, -0.09]).addTo(map)
        .bindPopup('A pretty CSS popup.<br> Easily customizable.')
        .openPopup();

        var geocoder = L.Control.geocoder({
            defaultMarkGeocode: false
          })
            .on('markgeocode', function(e) {
              var bbox = e.geocode.bbox;
              var poly = L.polygon([
                bbox.getSouthEast(),
                bbox.getNorthEast(),
                bbox.getNorthWest(),
                bbox.getSouthWest()
              ]).addTo(map);
              map.fitBounds(poly.getBounds());
            })
            .addTo(map);


    var geocoder = L.Control.Geocoder.nominatim();
    
    map.on('click', function(e) {
        lat=e.latlng.lat
        lng=e.latlng.lng;
        console.log(lat+" --- "+lng);
        if(df!=undefined){
          map.removeLayer(df);
          df=L.marker([lat,lng]).addTo(map)
          .bindPopup('USUARIO')
          .openPopup();

          geocoder.reverse(e.latlng, map.options.crs.scale(map.getZoom()), function(results) {
            //L.rectangle(bounds, {color: "#ff7800", weight: 1}).addTo(map);
            //map.fitBounds(bounds);
            console.log(results);
            document.getElementById("id_address").value=results[0].name;       
          });

        }
        
    })

});


