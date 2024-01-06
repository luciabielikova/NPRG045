<?php

function getAllAnimals()
{
    $animalfile = 'lexikon_zvirat.json';
    $jsonString = file_get_contents($animalfile);
    return json_decode($jsonString, true);
}

function getAnimalDetail($title){
    foreach (getAllAnimals() as $animal) {
        if ($animal['title'] === htmlspecialchars($title)){
            return $animal;
        }
    }
}


function getAllContinents(){
    $continentsFile = 'continents.json';
    $jsonString = file_get_contents($continentsFile);
    $ContinentsData = json_decode($jsonString, true);
    $continentTitles = array();
    foreach ($ContinentsData as $continent){
        array_push($continentTitles, $continent['continent']);
    }
    return $continentTitles;
}

$allContinents = getAllContinents();

function getAllBiotopes(){
    $biotopesFile = 'biotop.json';
    $jsonString = file_get_contents($biotopesFile);
    $BiotopesData = json_decode($jsonString, true);
    $biotopTitles = array();
    foreach ($BiotopesData as $biotop){
        array_push($biotopTitles, $biotop['biotop']);
    }
    return $biotopTitles;
}

$allBiotopes = getAllBiotopes();

function getAllClasses(){
    $classesFile = 'classes.json';
    $jsonString = file_get_contents($classesFile);
    $ClassesData = json_decode($jsonString, true);
    $ClassesTitles = array();
    foreach ($ClassesData as $class){
        array_push($ClassesTitles, $class['classes']);
    }
    return $ClassesTitles;
}

$allClasses = getAllClasses();

function getAllOrders(){
    $ordersFile = 'order.json';
    $jsonString = file_get_contents($ordersFile);
    $OrdersData = json_decode($jsonString, true);
    $orderTitles = array();
    foreach ($OrdersData as $continent){
        array_push($orderTitles, $continent['order']);
    }
    return $orderTitles;
}

$allOrders = getAllOrders();






function getAnimalsBySearchedTitle($zVyhladavania)
{
    $vyhovujuceZvieratka = array();
    foreach (getAllAnimals() as $animal) {
        $pattern = '/' . $zVyhladavania . '/i';
        if (isset($animal['title'])) {
            if (preg_match_all($pattern, $animal['title'], $matches)) {
                array_push($vyhovujuceZvieratka, $animal);
            }
        }
    }
    return $vyhovujuceZvieratka;
}

function getAnimalsByOrder($foundAnimals,$zVyhladavania)
{
    $vyhovujuceZvieratka = array();
    foreach ($foundAnimals as $animal) {
        $pattern = '/' . $zVyhladavania . '/i';
        if (isset($animal['order'])) {
            if (preg_match_all($pattern, $animal['title'], $matches)) {
                array_push($vyhovujuceZvieratka, $animal);
            }
        }
    }
    return $vyhovujuceZvieratka;
}


function getAnimalsByClass($foundAnimals,$zVyhladavania)
{
    $vyhovujuceZvieratka = array();
    foreach ($foundAnimals as $animal) {
        $pattern = '/' . $zVyhladavania . '/i';
        if (isset($animal['classes'])) {
            if (preg_match_all($pattern, $animal['title'], $matches)) {
                array_push($vyhovujuceZvieratka, $animal);
            }
        }
    }
    return $vyhovujuceZvieratka;
}

function getAnimalsByContinent($foundAnimals,$wantedContinents)
{
    $vyhovujuceZvieratka = array();
    foreach ($foundAnimals as $animal) {
        if (isset($animal['continents'])) {
            if (in_array($animal['continents'], $wantedContinents)) {
                array_push($vyhovujuceZvieratka, $animal);
            }
        }
    }
    return $vyhovujuceZvieratka;
}



?>
