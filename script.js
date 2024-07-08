//clearing searchDatabase form
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

function addWanted() {
    //adds new input field for animal we want to see
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
        input.name = 'wanted[]';
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
}
function addNotWanted() {
    //adds new input field for animal we do not want to see
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

    const wantedValues = Array.from(document.querySelectorAll('.wanted-input')).map(input => input.value);
    const notWantedValues = Array.from(document.querySelectorAll('.not-wanted-input')).map(input => input.value);

    /*
    console.log('Odkud:', fromValue);
    console.log('Kam:', toValue);
    console.log('Chci vidět:', wantedValues);
    console.log('Nechci vidět:', notWantedValues);
     */

    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'handleMapSearch.php', true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function () {
        if (xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            const result = response.data.result;
            drawPath(result);
        }
    };

    const data = `from=${encodeURIComponent(fromValue)}&to=${encodeURIComponent(toValue)}`;
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

    if (shortestPath.length > 1) {
        const latlngs = shortestPath.map(point => [point.lat, point.lon]);

        polyline = L.polyline(latlngs, { color: 'blue' }).addTo(map);
        map.fitBounds(polyline.getBounds());
    }
}

