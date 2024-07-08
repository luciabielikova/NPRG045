<?php

require_once 'db.php';

$allAnimals = getAllAnimals();

$allContinents = getAllContinents();

$allBiotopes = getAllBiotopes();

$allClasses = getAllClasses();

$allOrders = getAllOrders();



function getAnimalsBySearchedTitle($searchedTitle, $animals)
{
    $suitableAnimals = array();
    foreach ($animals as $animal) {
        $pattern = '/' . $searchedTitle . '/i';
        if (isset($animal['title'])) {
            if (preg_match_all($pattern, $animal['title'], $matches)) {
                array_push($suitableAnimals, $animal);
            }
        }
    }
    return $suitableAnimals;
}


function getAnimalsByContinent($foundAnimals,$wantedContinents)
{
    $suitableAnimals = array();
    foreach ($foundAnimals as $animal) {
        if (isset($animal['continents'])) {
            if (in_array($animal['continents'], $wantedContinents)) {
                array_push($suitableAnimals, $animal);
            }
        }
    }
    return $suitableAnimals;
}

function getAnimalsByBiotope($foundAnimals,$wantedBiotopes)
{
    $suitableAnimals = array();
    foreach ($foundAnimals as $animal) {
        if (isset($animal['biotop'])) {
            if (in_array($animal['biotop'], $wantedBiotopes)) {
                array_push($suitableAnimals, $animal);
            }
        }
    }
    return $suitableAnimals;
}


function getAnimalsByClass($foundAnimals,$wantedClasses)
{
    $suitableAnimals = array();
    foreach ($foundAnimals as $animal) {
        if (isset($animal['classes'])) {
            if (in_array($animal['classes'], $wantedClasses)) {
                array_push($suitableAnimals, $animal);
            }
        }
    }
    return $suitableAnimals;
}



function getAnimalsByOrder($foundAnimals,$wantedOrders)
{
    $suitableAnimals = array();
    foreach ($foundAnimals as $animal) {
        if (isset($animal['order'])) {
            if (in_array($animal['order'], $wantedOrders)) {
                array_push($suitableAnimals, $animal);
            }
        }
    }
    return $suitableAnimals;
}


function getAnimalDetail($title){
    global $allAnimals;
    foreach ($allAnimals as $animal) {
        if ($animal['title'] === htmlspecialchars($title)){
            return $animal;
        }
    }
}

function vytvorOdkazNaZvieratko($animal){
    return '<li><a href="detail.php?title='.$animal['title'].'">'.$animal['title'] .'</a></li>';
}



function listOfFoundAnimals($suitableAnimals)
{
    if (count($suitableAnimals) > 0) {
        echo '<ol>';
        foreach ($suitableAnimals as $animal) {
            echo vytvorOdkazNaZvieratko($animal);
        }
        echo '</ol>';
    }
    else{
        echo 'pre zvolene kriteria nemame zvieratko';
    }
}

function filterAnimals($searchedTitle,$chosenBiotopes, $chosenContinents,$chosenOrders,$chosenClasses){
    global $allAnimals;
    $suitableAnimals = getAnimalsBySearchedTitle($searchedTitle, $allAnimals);
    $suitableAnimals = getAnimalsByContinent($suitableAnimals,$chosenContinents);
    $suitableAnimals = getAnimalsByBiotope($suitableAnimals, $chosenBiotopes);
    $suitableAnimals = getAnimalsByClass($suitableAnimals, $chosenClasses);
    $suitableAnimals = getAnimalsByOrder($suitableAnimals, $chosenOrders);
    return $suitableAnimals ;
}

function form_handler()
{
    global $searchedTitle, $chosenBiotopes, $chosenContinents,$chosenOrders,$chosenClasses, $allClasses, $allOrders, $allContinents, $allBiotopes ;

    if (isset($_POST['title'])) {
        $searchedTitle = $_POST['title'];
    }
    else{
        $searchedTitle = '';
    }
    if (isset($_POST['continents'])) {
        $chosenContinents = $_POST['continents'];
    }
    else
    {
        $chosenContinents = $allContinents;
    }
    if (isset($_POST['biotopes'])) {
        $chosenBiotopes = $_POST['biotopes'];
    }
    else
    {
        $chosenBiotopes = $allBiotopes;
    }
    if (isset($_POST['classes'])) {
        $chosenClasses = $_POST['classes'];
    }
    else{
        $chosenClasses = $allClasses;
    }
    if (isset($_POST['orders'])) {
        $chosenOrders = ($_POST['orders']);
    }
    else{
        $chosenOrders = $allOrders;
    }
}


function displayCoordinates($animal){
    //If set, coordinates will be displayed on the map
    if (isset($animal['coordinates'])) {
        ?>
        <script>
            document.getElementById('mapid').style.height = '500px'

            var map = L.map('mapid').setView(<?php echo $animal['coordinates']; ?>, 24);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 18,
                attribution: '© OpenStreetMap contributors'
            }).addTo(map);
            var marker = L.marker(<?php echo $animal['coordinates']; ?>).addTo(map);


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
        <?php
    }
    else return;
}

?>
