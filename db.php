<?php

$defaultDir = 'cs-prague';

function getZooTitles(){
    $zooTitleFile =  'jsons/listOfZoos.json';
    $zooData = json_decode(file_get_contents($zooTitleFile), true);
    $zooTitles = array();
    foreach ($zooData as $zoo){
        array_push($zooTitles, $zoo['title']);
    }

    return $zooTitles;
}

function getAllZoos()
{
    $zooFile =  'jsons/listOfZoos.json';
    $jsonString = file_get_contents($zooFile);
    return json_decode($jsonString, true);
}


function getAllAnimals($dir = null) {

    $animalFile = "jsons/$dir/lexikon_zvirat.json";

    if (file_exists($animalFile)) {
        $jsonString = file_get_contents($animalFile);
        return json_decode($jsonString, true);
    } else {
        return [];
    }
}

function getAllContinents($dir = null){
    $continentsFile = "jsons/$dir/continents.json";
    $jsonString = file_get_contents($continentsFile);
    $ContinentsData = json_decode($jsonString, true);
    $continentTitles = array();
    foreach ($ContinentsData as $continent){
        array_push($continentTitles, $continent['continent']);
    }
    return $continentTitles;
}

function getAllBiotopes($dir = null){
    $biotopesFile = "jsons/$dir/biotop.json";
    $jsonString = file_get_contents($biotopesFile);
    $BiotopesData = json_decode($jsonString, true);
    $biotopTitles = array();
    foreach ($BiotopesData as $biotop){
        array_push($biotopTitles, $biotop['biotop']);
    }
    return $biotopTitles;
}

function getAllClasses($dir = null){
    $classesFile = "jsons/$dir/classes2.json";
    $jsonString = file_get_contents($classesFile);
    $ClassesData = json_decode($jsonString, true);
    $ClassesTitles = array();
    foreach ($ClassesData as $class){
        array_push($ClassesTitles, $class['title']);
    }
    return $ClassesTitles;
}
function getAllOrders($dir = null){
    $classesFile = "jsons/$dir/classes2.json";
    $jsonString = file_get_contents($classesFile);
    $ClassesData = json_decode($jsonString, true);
    $orderTitles = array();
    foreach ($ClassesData as $class){
        foreach ($class['orders'] as $order){
            array_push($orderTitles, $order['title']);
        }
    }
    return $orderTitles;
}

function loadAnimalsGeojson(){
    return file_get_contents('jsons/cs-prague/animals.geojson');
}

function loadZooGeojson(){
    return file_get_contents('jsons/cs-prague/zoo.geojson');
}

function loadHighways(){
    return file_get_contents('jsons/cs-prague/highways.geojson');
}