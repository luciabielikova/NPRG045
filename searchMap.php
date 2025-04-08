<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Zoo</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <link rel="stylesheet" href="styles.css" />

    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script src="script.js"></script>

</head>
<body>
<?php

include "header.php";
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

?>
<div class="Map">
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
        <button onclick="addWanted()">Chci vidět</button>
        <button onclick="addNotWanted()">Nechci vidět</button>
        <button id="clearBtn">Vyčistit</button>
    </div>


<div id="mapid" class="mapPage"></div>

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
    const clearBtn =  document.getElementById('clearBtn');

    let polyline;
    let wantedCount = 0;
    let notWantedCount = 0;


    searchInputFrom.addEventListener('input', (e) => {
        const query = e.target.value;
        if (query) {
            fetchResultsFrom(query);
        } else {
            resultsFromContainer.innerHTML = '';
            resultsFromContainer.style.display = 'none';
        }
    });

    searchInputTo.addEventListener('input', (e) => {
        const query = e.target.value;
        if (query) {
            fetchResultsTo(query);
        } else {
            resultsToContainer.innerHTML = '';
            resultsToContainer.style.display = 'none';
        }
    });

    submitBtn.addEventListener('click', handleSubmit);

    clearBtn.addEventListener('click', clearInputs);

    document.addEventListener('click', (e) => {
        if (!e.target.closest('.search-container-from')) {
            resultsFromContainer.style.display = 'none';
        }
    });

    document.addEventListener('click', (e) => {
        if (!e.target.closest('.search-container-to')) {
            resultsToContainer.style.display = 'none';
        }
    });

    document.addEventListener('click', (e) => {
        if (!e.target.closest('.wanted-container')) {
            resultsWantedContainer.style.display = 'none';
        }
    });

    document.addEventListener('click', (e) => {
        if (!e.target.closest('.not-wanted-container')) {
            resultsNotWantedContainer.style.display = 'none';
        }
    });




    var map = L.map('mapid').setView([50.1173, 14.406], 16);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    fetch('loadGeojson.php')
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
</div>
    <?php
    require_once 'functions.php';
    include 'footer.php';

    ?>

</body>

</html>
