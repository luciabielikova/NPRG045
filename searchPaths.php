<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Zoo</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <link rel="stylesheet" href="styles.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script src="script.js"></script>
    <link rel="icon" href="favicon-16x16.png" type="image/png">

</head>
<body>
<?php

include "header.php";
require_once 'functions.php';

if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// Presmerovanie na info stránku, ak mapa pre danú ZOO nie je dostupná
if (!isMapAvailable($_SESSION['zooID'])){
    header('Location: mapNotAvailable.php');
    exit;
}

$translation = getTranslation($_SESSION['language']);

?>


<div class="Map">
    <div class="white-column">

    <div class="search-container-from">
    <div class="label-input-wrapper">
        <label><?=$translation['from'] . ":" ?></label>
        <input type="text" id="searchFrom" autocomplete="off" placeholder= <?=$translation['search']?>...>
        <div class="resultsFrom" id="resultsFrom"></div>
    </div>
</div>
<div class="search-container-wanted">
    <!-- Tu sa dynamicky zobrazia wanted/not-wanted inputy -->
    <div class="wanted-container" id="wanted-container"></div>
    <div class="resultsWanted" id="resultsWanted"></div>

    <div class="not-wanted-container" id="not-wanted-container"></div>
    <div class="resultsNotWanted" id="resultsNotWanted"></div>
</div>
<div class="search-container-to">
    <div class="label-input-wrapper">
        <label><?=$translation['to'] . ":" ?></label>
        <input type="text" id="searchTo" autocomplete="off" placeholder=<?=$translation['search']?>...>
        <div class="resultsTo" id="resultsTo"></div>
    </div>
</div>
    <br>
    <div class="buttons-container">
        <!-- Vyhľadanie trasy, pridanie povinných a zakázaných bodov, reset -->
        <button id="submitBtn"><?=$translation['search']?></button>
        <button onclick="addWanted()"><?=$translation['mandatory']?></button>
        <button onclick="addNotWanted()"><?=$translation['forbidden']?></button>
        <button id="clearBtn"><?=$translation['clear']?></button>
    </div>


<div id="mapid" class="mapPage"></div>
</div>
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

    // EventListener na vyhľadávanie počas písania

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

    // Leaflet mapa – východzia pozícia nastavená podľa súradníc
    var map = L.map('mapid').setView([50.1173, 14.406], 16);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);


    function addInputField(parentId, inputClass, inputName, labelText, fetchFunction, count, maxCount) {
        if (count >= maxCount) {
            alert("<?=htmlspecialchars($translation['selectMax']) ?>" + maxCount + '.');
            return;
        }
        const parent = document.getElementById(parentId);
        const wrapper = document.createElement('div');
        wrapper.classList.add('label-input-wrapper');
        const label = document.createElement('label');
        label.textContent = labelText;
        const input = document.createElement('input');
        input.type = 'text';
        input.placeholder = "<?= htmlspecialchars($translation['search']) ?>..."
        input.name = inputName;
        input.className = inputClass;
        input.autocomplete = "off";
        const resultsContainer = document.createElement('div');
        resultsContainer.className = 'results-container';
        wrapper.appendChild(label);
        wrapper.appendChild(input);
        wrapper.appendChild(resultsContainer);
        parent.appendChild(wrapper);
        input.addEventListener('input', () => {
            fetchFunction(input.value, resultsContainer, input);
            resultsContainer.style.display = 'block';
        });

        document.addEventListener('click', (event) => {
            if (!wrapper.contains(event.target)) {
                resultsContainer.style.display = 'none';
            }
        });
    }

    function addWanted() {
        addInputField('wanted-container', 'wanted-input', 'wanted[]', '<?= $translation["mandatory"].":"?>', fetchResultsWanted, wantedCount, 3, resultsWantedContainer);
        wantedCount++;
    }

    function addNotWanted() {
        addInputField('not-wanted-container', 'not-wanted-input', 'notWanted[]', '<?= $translation["forbidden"].":"?>', fetchResultsNotWanted, notWantedCount, 3, resultsNotWantedContainer);
        notWantedCount++;
    }


</script>
</div>
    <?php
    include 'footer.php';

    ?>

</body>

</html>
