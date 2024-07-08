
<?php

//interactively displays matching strings from search

require_once 'db.php';

$animalsFile = loadAnimalsGeojson();
$animals = json_decode($animalsFile, true);


$animalNames = [];

foreach ($animals['features'] as $feature) {
    if ($feature['properties']['name'] != null) {
        array_push($animalNames,$feature['properties']['name']);
    }
}

$values = $animalNames;

if (isset($_GET['query'])) {
    $query = $_GET['query'];


    $filteredValues = array_filter($values, function($value) use ($query) {
        return stripos($value, $query) !== false;
    });

    header('Content-Type: application/json');
    echo json_encode(array_values($filteredValues));
}
?>