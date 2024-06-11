<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>GeoJSON</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <link rel="stylesheet" href="styles.css" />

    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script src="mapa.js"></script>
    <script src="script.js"></script>


</head>

<div class="search-container-from">
    <input type="text" id="searchFrom" placeholder="Odkud">
    <div class="resultsFrom" id="resultsFrom"></div>
    <input type="text" id="searchTo" placeholder="Kam">
    <div class="resultsTo" id="resultsTo"></div>
    <button id="submitBtn">Odeslat</button>

</div>


<script>
    const searchInputFrom = document.getElementById('searchFrom');
    const searchInputTo = document.getElementById('searchTo');
    const resultsFromContainer = document.getElementById('resultsFrom');
    const resultsToContainer = document.getElementById('resultsTo');
    const submitBtn = document.getElementById('submitBtn');
    let polyline;

    function vykresli(shortestPath){

        if (polyline) {
            map.removeLayer(polyline);
            console.log("vymazane");
        }
        else{
            console.log("nevymazane");
        }

        if (shortestPath.length > 1) {
            // Create an array to store LatLng points
            const latlngs = [];

            // Loop through each point in shortestPath and add LatLng coordinates to latlngs array
            shortestPath.forEach(point => {
                latlngs.push([point.lat, point.lon]);
            });

            // Add the polyline to the map
            polyline = L.polyline(latlngs, {color: 'blue'}).addTo(map);

            // Fit the map to the polyline
            map.fitBounds(polyline.getBounds());
        }
    }
    function fetchResultsFrom(query) {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', 'vyhladavac.php?query=' + encodeURIComponent(query), true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                const results = JSON.parse(xhr.responseText);
                displayResultsFrom(results);
            }
        };
        xhr.send();
    }

    function displayResultsFrom(results) {
        resultsFromContainer.innerHTML = '';
        if (results.length > 0) {
            const ul = document.createElement('ul');
            results.forEach(result => {
                const li = document.createElement('li');
                li.textContent = result;
                li.addEventListener('click', () => {
                    searchInputFrom.value = result;
                    resultsFromContainer.style.display = 'none';
                });
                ul.appendChild(li);
            });
            resultsFromContainer.appendChild(ul);
            resultsFromContainer.style.display = 'block';
        } else {
            resultsFromContainer.style.display = 'none';
        }
    }

    searchInputFrom.addEventListener('input', (e) => {
        const query = e.target.value;
        if (query) {
            fetchResultsFrom(query);
        } else {
            resultsFromContainer.innerHTML = '';
            resultsFromContainer.style.display = 'none';
        }
    });
    // Skrytie výsledkov pri kliknutí mimo
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.search-container-from')) {
            resultsFromContainer.style.display = 'none';
        }
    });

    function fetchResultsTo(query) {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', 'vyhladavac.php?query=' + encodeURIComponent(query), true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                const results = JSON.parse(xhr.responseText);
                displayResultsTo(results);
            }
        };
        xhr.send();
    }

    function displayResultsTo(results) {
        resultsToContainer.innerHTML = '';
        if (results.length > 0) {
            const ul = document.createElement('ul');
            results.forEach(result => {
                const li = document.createElement('li');
                li.textContent = result;
                li.addEventListener('click', () => {
                    searchInputTo.value = result;
                    resultsToContainer.style.display = 'none';
                });
                ul.appendChild(li);
            });
            resultsToContainer.appendChild(ul);
            resultsToContainer.style.display = 'block';
        } else {
            resultsToContainer.style.display = 'none';
        }
    }

    searchInputTo.addEventListener('input', (e) => {
        const query = e.target.value;
        if (query) {
            fetchResultsTo(query);
        } else {
            resultsToContainer.innerHTML = '';
            resultsToContainer.style.display = 'none';
        }
    });
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.search-container-to')) {
            resultsToContainer.style.display = 'none';
        }
    });

    function handleSubmit() {
        const fromValue = searchInputFrom.value;
        const toValue = searchInputTo.value;
        console.log('Odkud:', fromValue);
        console.log('Kam:', toValue);

        const xhr = new XMLHttpRequest();
        xhr.open('POST', 'handle_form.php', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function() {
            if (xhr.status === 200) {
                //console.log('Response:', xhr.responseText);
                const response = JSON.parse(xhr.responseText);
                const result = response.data.result;
                vykresli(result);
            }
        };
        xhr.send(`from=${encodeURIComponent(fromValue)}&to=${encodeURIComponent(toValue)}`);
    }


    submitBtn.addEventListener('click', handleSubmit);





</script>


<div id="mapid"></div>
<script>


    var map = L.map('mapid').setView([50.1173, 14.406], 16);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    fetch('load_geojson.php')
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            L.geoJSON(data, {
                style: myStyle,
                pointToLayer: function (feature, latlng) {
                    return null;
                }
            },).addTo(map);
        });
</script>

</body>
</html>
