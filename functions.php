<?php

require_once 'db.php';

global $defaultDir;

if (isset($_GET['dir'])) {
    $dir = $_GET['dir'];
}
else{
    $dir = $defaultDir;
}




$allAnimals = getAllAnimals($dir);

$allContinents = getAllContinents($dir);

$allBiotopes = getAllBiotopes($dir);

$allClasses = getAllClasses($dir);

$allOrders = getAllOrders($dir);

$zooTitles = getZooTitles();

$allZoos = getAllZoos();

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

function createLinkToAnimal($animal){
    return '<li><a href="detail.php?title='.$animal['title'].'">'.$animal['title'] .'</a></li>';
}



function listOfFoundAnimals($suitableAnimals)
{
    if (count($suitableAnimals) > 0) {
        echo '<ol>';
        foreach ($suitableAnimals as $animal) {
            echo createLinkToAnimal($animal);
        }
        echo '</ol>';
    }
    else{
        echo 'Pro zvolené kritériá nemáme zvířátko-.';
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

function formHandlerSearchDB($dir)
{
    global $searchedTitle, $chosenBiotopes, $chosenContinents, $chosenOrders, $chosenClasses, $allClasses, $allOrders, $allContinents, $allBiotopes;

    if (isset($_POST['title'])) {
        $searchedTitle = htmlspecialchars($_POST['title'], ENT_QUOTES);
    } else {
        $searchedTitle = '';
    }

    if (isset($_POST['continents'])) {
        $chosenContinents = array_map(function($continent) {
            return htmlspecialchars($continent, ENT_QUOTES);
        }, $_POST['continents']);
    } else {
        $chosenContinents = $allContinents;
    }

    if (isset($_POST['biotopes'])) {
        $chosenBiotopes = array_map(function($biotope) {
            return htmlspecialchars($biotope, ENT_QUOTES);
        }, $_POST['biotopes']);
    } else {
        $chosenBiotopes = $allBiotopes;
    }

    if (isset($_POST['classes'])) {
        $chosenClasses = array_map(function($class) {
            return htmlspecialchars($class, ENT_QUOTES);
        }, $_POST['classes']);
    } else {
        $chosenClasses = $allClasses;
    }

    if (isset($_POST['orders'])) {
        $chosenOrders = array_map(function($order) {
            return htmlspecialchars($order, ENT_QUOTES);
        }, $_POST['orders']);
    } else {
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
        <?php
    }
    else return;
}

?>
