<?php

if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

function loadTranslations() {
    $detailTemplateFile = 'datasets/translations.json';
    if (!file_exists($detailTemplateFile)) {
        return [];
    }
    $jsonContent = file_get_contents($detailTemplateFile);
    return json_decode($jsonContent, true) ?: [];
}


function getZooTitles($language){
    $zooTitleFile =  'datasets/allZoosList.json';
    $zooData = json_decode(file_get_contents($zooTitleFile), true);
    $zooTitles = array();

    foreach ($zooData as $zoo){

        if (isset($zoo['name'][$language])) {
            $zooTitles[$zoo["id"]] = $zoo['name'][$language];
        } else {
            $zooTitles[$zoo["id"]] = $zoo['name'][$zoo['default_language']];
        }
    }

    return $zooTitles;
}

function getZooById( $id) {
    $zooTitleFile =  'datasets/allZoosList.json';
    $data = json_decode(file_get_contents($zooTitleFile), true);

    foreach ($data as $zoo) {
        if ($zoo['id'] == $id) {
            return $zoo;
        }
    }
    return null;
}

function getClassByID($classID)
{
    global $allClasses;
    return $allClasses[$classID];
}

function getOrderByID($orderID)
{
    global $allOrders;
    return $allOrders[$orderID];
}

function getHabitatsByID($habitatIDs)
{
    global $allHabitats;
    $names = "";

    foreach ($habitatIDs as $id){
        $names .= $allHabitats[$id] . ", ";
    }

    return substr($names, 0, -2);
}

function getContinentsByID($continentIDs)
{
    global $allContinents;
    $names = "";

    foreach ($continentIDs as $id){
        $names .= $allContinents[$id] . ", ";
    }

    return substr($names, 0, -2);
}

function getAnimalDetail($animalID, $zooID, $language){
    $filename = "datasets/zoos/$zooID/translations/$language/$animalID.json";

    if (file_exists($filename)){
        $animal = json_decode(file_get_contents($filename), true);
    }
    else{
        $animal = null;
    }
    return $animal;

}

function getAnimalCategories($animalID, $zooID){
    $filename = "datasets/zoos/$zooID/animals.json";
    if (file_exists($filename)) {
        $data = json_decode(file_get_contents($filename), true);
        foreach ($data as $animal) {
            if ($animal['id'] == $animalID) {
                return $animal;
            }
        }
    }
    return null;
}


function getAnimalTitles($zooID = null, $language = "en") {
    $zooData = getZooById($zooID);
    $animalFile = $zooData["animals_path"];

    $jsonString = file_get_contents($animalFile);
    $animals = json_decode($jsonString, true);

    $filteredAnimals = [];
    foreach ($animals as $animal) {
        if (isset($animal["id"]) && isset($animal["names"]) && isset($animal["names"][$language])) {
            $filteredAnimals[$animal["id"]] = $animal["names"][$language];
        }
    }
    return $filteredAnimals;
}

function getAnimalByNameAndLanguage( $name, $lang, $zooID = null, $language = "en") {
    $zooData = getZooById($zooID);
    $animalFile = $zooData["animals_path"];

    $jsonString = file_get_contents($animalFile);
    $animals = json_decode($jsonString, true);

    foreach ($animals as $animal) {
        if (isset($animal['names'][$lang]) && mb_strtolower($animal['names'][$lang]) === mb_strtolower($name)) {
            return $animal;
        }
    }
    return null;
}





function getAllAnimals($zooID = null) {
    $zooData = getZooById($zooID);
    $animalFile = $zooData["animals_path"];
    $jsonString = file_get_contents($animalFile);
    $animals = json_decode($jsonString, true);
    return $animals;
}

function getAllContinents($zooID = null, $language = "en") {
    $zooData = getZooById($zooID);
    $continentsFile = $zooData["continents_path"];
    $jsonString = file_get_contents($continentsFile);
    $continentsData = json_decode($jsonString, true);

    $continentTitles = array();

    foreach ($continentsData as $continent) {
        if (isset($continent['translations'][$language]['name'])) {
            $continentTitles[$continent["id"]] =  $continent['translations'][$language]['name'];
        } else {
            $continentTitles[$continent["id"]] = "N/A";
        }
    }

    return $continentTitles;
}

function getAllHabitats($zooID = null, $language = "en") {
    $zooData = getZooById($zooID);
    $habitatsFile = $zooData["habitats_path"];
    $jsonString = file_get_contents($habitatsFile);
    $habitatsData = json_decode($jsonString, true);

    $habitatsTitles = array();

    foreach ($habitatsData as $habitat) {
        if (isset($habitat['translations'][$language]['name'])) {
            $habitatsTitles[$habitat["id"]] =  $habitat['translations'][$language]['name'];
        } else {
            $habitatsTitles[$habitat["id"]]  = "N/A";
        }
    }

    return $habitatsTitles;
}

function getAllClasses($zooID = null, $language = "en") {
    $zooData = getZooById($zooID);
    $classesFile = $zooData["classes_path"];
    $jsonString = file_get_contents($classesFile);
    $classesData = json_decode($jsonString, true);

    $classesTitles = array();

    foreach ($classesData as $class) {
        if (isset($class['translations'][$language]['name'])) {
            $classesTitles[$class["id"]] =  $class['translations'][$language]['name'];
        } else {
            $classesTitles[$class["id"]] =  "N/A";
        }
    }

    return $classesTitles;
}
function getAllOrders($zooID = null, $language = "en") {
    $zooData = getZooById($zooID);
    $ordersFile = $zooData["orders_path"];
    $jsonString = file_get_contents($ordersFile);
    $ordersData = json_decode($jsonString, true);

    $ordersTitles = array();

    foreach ($ordersData as $order) {
        if (isset($order['translations'][$language]['name'])) {
            $ordersTitles[$order["id"]] =  $order['translations'][$language]['name'];
        } else {
            $ordersTitles[$order["id"]] = "N/A";
        }
    }

    return $ordersTitles;
}



function loadHighways($zooID = null){
    $zooData = getZooById($zooID);
    if (isset($zooData["highways_path"])){
        return file_get_contents($zooData["highways_path"]);
    }
    else {
        return null;
    }
}