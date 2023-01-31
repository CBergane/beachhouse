function initMap() {
    const myLatLng = { lat: 56.6484407, lng: 12.885896 };
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 14,
        center: myLatLng });
    
    new google.maps.Marker({
        position: myLatLng,
        map,
        title: "Our office.",
    });
}
window.initMap = initMap;