//clearing searchDatabase form
let startMarker = null;
let endMarker = null;
let midMarker = null;
let waypointsMarkers = [];


function uncheckAll() {
    var checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(function (checkbox) {
        checkbox.checked = false;
    });
}

function uncheck(selector) {
    var checkboxes = document.querySelectorAll(selector);
    checkboxes.forEach(function (checkbox) {
        checkbox.checked = false;
    });
}

function uncheck(selector) {
    document.querySelectorAll(selector).forEach(el => {
        if (el instanceof HTMLInputElement) {
            el.checked = false;
        }
    });
}


function clearSearch() {
    return document.getElementById("search").value = "";
}

function clearAll() {
    uncheckAll();
    clearSearch();
}


//map style
function myStyle(feature) {
    return {
        weight: 1,
        opacity: 0,
        color: 'blue',
        fillOpacity: 0
    };
}

function fetchResults(query, container, input) {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'listMatchingAnimals.php?query=' + encodeURIComponent(query), true);
    xhr.onload = function () {
        if (xhr.status === 200) {
            const results = JSON.parse(xhr.responseText);
            displayResults(results, container, input);
        }
    };
    xhr.send();
}

function displayResults(results, container, input) {
    container.innerHTML = '';
    if (results.length > 0) {
        const ul = document.createElement('ul');
        results.forEach(result => {
            const li = document.createElement('li');
            li.textContent = result;
            li.addEventListener('click', () => {
                input.value = result;
                container.style.display = 'none';
            });
            ul.appendChild(li);
        });
        container.appendChild(ul);
        container.style.display = 'block';
    } else {
        container.style.display = 'none';
    }
}


function fetchResultsFrom(query) {
    fetchResults(query, resultsFromContainer, searchInputFrom);
}

function displayResultsFrom(results) {
    displayResults(results, resultsFromContainer, searchInputFrom);
}

function fetchResultsTo(query) {
    fetchResults(query, resultsToContainer, searchInputTo);
}

function displayResultsTo(results) {
    displayResults(results, resultsToContainer, searchInputTo);
}

function fetchResultsWanted(query, container, input) {
    fetchResults(query, container, input);
}

function fetchResultsNotWanted(query, container, input) {
    fetchResults(query, container, input);
}


function displayResultsWanted(results, input) {
    displayResults(results, resultsWantedContainer, input);
}

function displayResultsNotWanted(results, input) {
    displayResults(results, resultsNotWantedContainer, input);
}


function handleSubmit() {
    const fromValue = searchInputFrom.value;
    const toValue = searchInputTo.value;

    const wantedValues = Array.from(document.querySelectorAll('.wanted-input'))
        .map(input => input.value)
        .filter(value => value.trim() !== "");
    const notWantedValues = Array.from(document.querySelectorAll('.not-wanted-input'))
        .map(input => input.value)
        .filter(value => value.trim() !== "");

    console.log('Odkud:', fromValue);
    console.log('Kam:', toValue);
    console.log('Chci vidět:', wantedValues);
    console.log('Nechci vidět:', notWantedValues);


    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'handleMapSearch.php', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

    xhr.onload = function () {
        if (xhr.status === 200) {
            console.log(xhr.responseText);
            const response = JSON.parse(xhr.responseText);
            const result = response.data.result;

            console.log(result);
            drawPath(result);
        }
    };
    console.log('Raw response:', xhr.responseText);

    const data = `from=${encodeURIComponent(fromValue)}&to=${encodeURIComponent(toValue)}&mandatory=${encodeURIComponent(wantedValues.join(','))}&forbidden=${encodeURIComponent(notWantedValues.join(','))}`;
    xhr.send(data);
}

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

function drawPath(shortestPath) {
    if (polyline) {
        map.removeLayer(polyline);
    }

    if (startMarker) map.removeLayer(startMarker);
    if (endMarker) map.removeLayer(endMarker);
    if (waypointsMarkers) {
        waypointsMarkers.forEach(marker => map.removeLayer(marker));
    }

    waypointsMarkers = [];

    if (shortestPath.length > 1) {
        const latlngs = shortestPath.map(point => [point.lat, point.lon, point.vertex]);
        polyline = L.polyline(latlngs, {color: 'blue'}).addTo(map);
        map.fitBounds(polyline.getBounds());

        startMarker = L.marker(latlngs[0], {title: latlngs[0][2]}).addTo(map)
            .bindPopup(latlngs[0][2]);

        endMarker = L.marker(latlngs[latlngs.length - 1], {title: latlngs[latlngs.length - 1][2]}).addTo(map)
            .bindPopup(latlngs[latlngs.length - 1][2]);

        for (let i = 1; i < latlngs.length - 1; i++) {
            if (isNaN(latlngs[i][2])) {
                let marker = L.marker(latlngs[i], {title: latlngs[i][2]}).addTo(map)
                    .bindPopup(latlngs[i][2]);
                waypointsMarkers.push(marker);
            }
        }

    }
}

document.addEventListener("DOMContentLoaded", function () {
    const languageDropdown = document.getElementById("language");

    languageDropdown.addEventListener("change", function () {
        const selectedLang = this.value;
        const urlParams = new URLSearchParams(window.location.search);

        urlParams.set("language", selectedLang);

        window.location.search = urlParams.toString();
    });
});


document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('.zooButton').forEach(button => {
        button.addEventListener('click', function() {
            let zooID = this.getAttribute('data-zooid');

            fetch('setZooID.php', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: 'zooID=' + encodeURIComponent(zooID) + '&language=' + encodeURIComponent(selectedLanguage)
            }).then(() => {
                window.location.href = 'mapOrSearch.php';
            });
        });
    });
});

