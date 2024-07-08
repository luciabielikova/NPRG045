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
<body>
<div class="search-container-from">
    <div class="label-input-wrapper">
        <label>Odkud:</label>
        <input type="text" id="searchFrom" placeholder="Vyhledat...">
        <div class="resultsFrom" id="resultsFrom"></div>
    </div>
</div>
<div class="search-container-wanted">
    <div class="wanted-container" id="wanted-container"></div>
    <div class="resultsWanted" id="resultsWanted"></div>

    <div class="not-wanted-container" id="not-wanted-container"></div>
    <div class="resultsNotWanted" id="resultsNotWanted"></div>
</div>
<div class="search-container-to">
    <div class="label-input-wrapper">
        <label>Kam:</label>
        <input type="text" id="searchTo" placeholder="Vyhledat...">
        <div class="resultsTo" id="resultsTo"></div>
    </div>
</div>
    <br>
    <div class="buttons-container">
        <button id="submitBtn">Najdi</button>
        <button onclick="addInput(true)">Chci vidět</button>
        <button onclick="addInput(false)">Nechci vidět</button>
        <button id="clear">Vyčistit</button>
    </div>


<div id="mapid"></div>

<script>
    const searchInputFrom = document.getElementById('searchFrom');
    const searchInputTo = document.getElementById('searchTo');
    const resultsFromContainer = document.getElementById('resultsFrom');
    const resultsToContainer = document.getElementById('resultsTo');
    const wantedContainer = document.getElementById('wanted-container');
    const notWantedContainer = document.getElementById('not-wanted-container');
    const resultsWantedContainer = document.getElementById('resultsWanted');
    const resultsNotWantedContainer = document.getElementById('resultsNotWanted');
    const submitBtn = document.getElementById('submitBtn');

    let polyline;
    let wantedCount = 0;
    let notWantedCount = 0;

    function clearInputs() {
        searchInputFrom.value = '';
        searchInputTo.value = '';

        document.querySelectorAll('.wanted-input').forEach(input => {
            input.value = '';
        });

        document.querySelectorAll('.not-wanted-input').forEach(input => {
            input.value = '';
        });
    }

    document.getElementById('clear').addEventListener('click', clearInputs);



    function addInput(wanted) {
        if (wanted) {
            if (wantedCount < 3) {
                wantedCount++;
                let container = document.getElementById('wanted-container');
                let wrapper = document.createElement('div');
                wrapper.className = 'label-input-wrapper';

                let label = document.createElement('label');
                let labelText = document.createTextNode('Chci vidět:');
                let input = document.createElement('input');
                input.type = 'text';
                input.placeholder = 'Vyhledat...';
                input.className = 'wanted-input';
                input.name = 'wanted[]'; // Add name attribute for easier form handling
                label.appendChild(labelText);
                wrapper.appendChild(label);
                wrapper.appendChild(input);
                container.appendChild(wrapper);

                input.addEventListener('input', (e) => {
                    const query = e.target.value;
                    if (query) {
                        fetchResultsWanted(query, input);
                    } else {
                        resultsWantedContainer.innerHTML = '';
                        resultsWantedContainer.style.display = 'none';
                    }
                });
            } else {
                alert('Vyberte nejvýš 3.');
            }
        } else {
            if (notWantedCount < 3) {
                notWantedCount++;
                let container = document.getElementById('not-wanted-container');
                let wrapper = document.createElement('div');
                wrapper.className = 'label-input-wrapper';

                let label = document.createElement('label');
                let labelText = document.createTextNode('Nechci vidět:');
                let input = document.createElement('input');
                input.type = 'text';
                input.placeholder = 'Vyhledat...';
                input.className = 'not-wanted-input';
                input.name = 'notWanted[]';
                label.appendChild(labelText);
                wrapper.appendChild(label);
                wrapper.appendChild(input);
                container.appendChild(wrapper);

                input.addEventListener('input', (e) => {
                    const query = e.target.value;
                    if (query) {
                        fetchResultsNotWanted(query, input);
                    } else {
                        resultsNotWantedContainer.innerHTML = '';
                        resultsNotWantedContainer.style.display = 'none';
                    }
                });
            } else {
                alert('Vyberte nejvýše 3.');
            }
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

    document.addEventListener('click', (e) => {
        if (!e.target.closest('.search-container-from')) {
            resultsFromContainer.style.display = 'none';
        }
    });

    function fetchResultsTo(query) {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', 'vyhladavac.php?query=' + encodeURIComponent(query), true);
        xhr.onload = function () {
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

    function fetchResultsWanted(query, input) {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', 'vyhladavac.php?query=' + encodeURIComponent(query), true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                const results = JSON.parse(xhr.responseText);
                displayResultsWanted(results, input);
            }
        };
        xhr.send();
    }

    function displayResultsWanted(results, input) {
        resultsWantedContainer.innerHTML = '';
        if (results.length > 0) {
            const ul = document.createElement('ul');
            results.forEach(result => {
                const li = document.createElement('li');
                li.textContent = result;
                li.addEventListener('click', () => {
                    input.value = result;
                    resultsWantedContainer.style.display = 'none';
                });
                ul.appendChild(li);
            });
            resultsWantedContainer.appendChild(ul);
            resultsWantedContainer.style.display = 'block';
        } else {
            resultsWantedContainer.style.display = 'none';
        }
    }

    document.addEventListener('click', (e) => {
        if (!e.target.closest('.wanted-container')) {
            resultsWantedContainer.style.display = 'none';
        }
    });

    function fetchResultsNotWanted(query, input) {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', 'vyhladavac.php?query=' + encodeURIComponent(query), true);
        xhr.onload = function() {
            if (xhr.status === 200) {
                const results = JSON.parse(xhr.responseText);
                displayResultsNotWanted(results, input);
            }
        };
        xhr.send();
    }

    function displayResultsNotWanted(results, input) {
        resultsNotWantedContainer.innerHTML = '';
        if (results.length > 0) {
            const ul = document.createElement('ul');
            results.forEach(result => {
                const li = document.createElement('li');
                li.textContent = result;
                li.addEventListener('click', () => {
                    input.value = result;
                    resultsNotWantedContainer.style.display = 'none';
                });
                ul.appendChild(li);
            });
            resultsNotWantedContainer.appendChild(ul);
            resultsNotWantedContainer.style.display = 'block';
        } else {
            resultsNotWantedContainer.style.display = 'none';
        }
    }

    document.addEventListener('click', (e) => {
        if (!e.target.closest('.not-wanted-container')) {
            resultsNotWantedContainer.style.display = 'none';
        }
    });

    function handleSubmit() {
        const fromValue = searchInputFrom.value;
        const toValue = searchInputTo.value;

        const wantedValues = Array.from(document.querySelectorAll('.wanted-input')).map(input => input.value);
        const notWantedValues = Array.from(document.querySelectorAll('.not-wanted-input')).map(input => input.value);

        console.log('Odkud:', fromValue);
        console.log('Kam:', toValue);
        console.log('Chci vidět:', wantedValues);
        console.log('Nechci vidět:', notWantedValues);

        const xhr = new XMLHttpRequest();
        xhr.open('POST', 'handle_form.php', true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function () {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                const result = response.data.result;
                vykresli(result);
            }
        };

        const data = `from=${encodeURIComponent(fromValue)}&to=${encodeURIComponent(toValue)}&wanted=${encodeURIComponent(JSON.stringify(wantedValues))}&notWanted=${encodeURIComponent(JSON.stringify(notWantedValues))}`;
        xhr.send(data);
    }

    submitBtn.addEventListener('click', handleSubmit);

    function vykresli(shortestPath) {
        if (polyline) {
            map.removeLayer(polyline);
        }

        if (shortestPath.length > 1) {
            const latlngs = shortestPath.map(point => [point.lat, point.lon]);

            polyline = L.polyline(latlngs, { color: 'blue' }).addTo(map);
            map.fitBounds(polyline.getBounds());
        }
    }

    var map = L.map('mapid').setView([50.1173, 14.406], 16);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    fetch('load_geojson.php')
        .then(response => response.json())
        .then(data => {
            L.geoJSON(data, {
                style: myStyle,
                pointToLayer: function (feature, latlng) {
                    return null;
                }
            }).addTo(map);
        });
</script>
</body>
<?php
    include 'footer.php';
?>
</html>
