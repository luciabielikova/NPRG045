//clearing searchDatabase form
let startMarker = null;
let endMarker = null;
let midMarker = null;
let waypointsMarkers = [];



function uncheckAll() {
    var checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(function(checkbox) {
        checkbox.checked = false;
    });
}

function uncheck(selector ) {
    var checkboxes = document.querySelectorAll(selector);
    checkboxes.forEach(function(checkbox) {
        checkbox.checked = false;
    });
}
function clearSearch(){
    return document.getElementById("search").value = "";
}

function clearAll() {
    uncheckAll(); clearSearch();
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

function addInputField(containerId, className, inputName, labelText, fetchFunction, counter, maxCount, resultsContainer) {
    if (counter < maxCount) {
        counter++;
        let container = document.getElementById(containerId);
        let wrapper = document.createElement('div');
        wrapper.className = 'label-input-wrapper';

        let label = document.createElement('label');
        let labelNode = document.createTextNode(labelText);
        let input = document.createElement('input');
        input.type = 'text';
        input.placeholder = 'Vyhledat...';
        input.className = className;
        input.name = inputName;
        label.appendChild(labelNode);
        wrapper.appendChild(label);
        wrapper.appendChild(input);
        container.appendChild(wrapper);

        input.addEventListener('input', (e) => {
            const query = e.target.value;
            if (query) {
                fetchFunction(query, input);
            } else {
                resultsContainer.innerHTML = '';
                resultsContainer.style.display = 'none';
            }
        });
    } else {
        alert('Vyberte nejvýše ' + maxCount + '.');
    }
}

function addWanted() {
    addInputField('wanted-container', 'wanted-input', 'wanted[]', 'Chci vidět:', fetchResultsWanted, wantedCount, 3, resultsWantedContainer);
    wantedCount++;
}

function addNotWanted() {
    addInputField('not-wanted-container', 'not-wanted-input', 'notWanted[]', 'Nechci vidět:', fetchResultsNotWanted, notWantedCount, 3, resultsNotWantedContainer);
    notWantedCount++;
}

function fetchResults(query, container, input) {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'displayMatchingAnimals.php?query=' + encodeURIComponent(query), true);
    xhr.onload = function() {
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

function fetchResultsWanted(query, input) {
    fetchResults(query, resultsWantedContainer, input);
}

function displayResultsWanted(results, input) {
    displayResults(results, resultsWantedContainer, input);
}

function fetchResultsNotWanted(query, input) {
    fetchResults(query, resultsNotWantedContainer, input);
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

    // Odstrániť predchádzajúce značky (ak existujú)
    if (startMarker) map.removeLayer(startMarker);
    if (endMarker) map.removeLayer(endMarker);
    if (waypointsMarkers) {
        waypointsMarkers.forEach(marker => map.removeLayer(marker));
    }

    waypointsMarkers = [];

    if (shortestPath.length > 1) {
        const latlngs = shortestPath.map(point => [point.lat, point.lon, point.vertex]);
        // Vytvorenie polyline pre cestu
        polyline = L.polyline(latlngs, { color: 'blue' }).addTo(map);
        map.fitBounds(polyline.getBounds());

        // Pridanie značky pre začiatok
        startMarker = L.marker(latlngs[0], { title: latlngs[0][2] }).addTo(map)
        .bindPopup(latlngs[0][2]);

        // Pridanie značky pre koniec
        endMarker = L.marker(latlngs[latlngs.length - 1],  { title: latlngs[latlngs.length - 1][2] }).addTo(map)
            .bindPopup(latlngs[latlngs.length - 1][2]);

        for (let i = 1; i < latlngs.length - 1; i++) {
            if (isNaN(latlngs[i][2])) {
            let marker = L.marker(latlngs[i], { title: latlngs[i][2]  }).addTo(map)
                .bindPopup(latlngs[i][2] );
            waypointsMarkers.push(marker);
        }
        }

    }
}

