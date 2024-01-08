<?php
function getAllAnimals()
{
    $animalfile =  'jsons/lexikon_zvirat.json';
    $jsonString = file_get_contents($animalfile);
    return json_decode($jsonString, true);
}

function getAllContinents(){
    $continentsFile = 'jsons/continents.json';
    $jsonString = file_get_contents($continentsFile);
    $ContinentsData = json_decode($jsonString, true);
    $continentTitles = array();
    foreach ($ContinentsData as $continent){
        array_push($continentTitles, $continent['continent']);
    }
    return $continentTitles;
}

function getAllBiotopes(){
    $biotopesFile = 'jsons/biotop.json';
    $jsonString = file_get_contents($biotopesFile);
    $BiotopesData = json_decode($jsonString, true);
    $biotopTitles = array();
    foreach ($BiotopesData as $biotop){
        array_push($biotopTitles, $biotop['biotop']);
    }
    return $biotopTitles;
}

function getAllClasses(){
    $classesFile = 'jsons/classes.json';
    $jsonString = file_get_contents($classesFile);
    $ClassesData = json_decode($jsonString, true);
    $ClassesTitles = array();
    foreach ($ClassesData as $class){
        array_push($ClassesTitles, $class['classes']);
    }
    return $ClassesTitles;
}

function getAllOrders(){
    $ordersFile = 'jsons/order.json';
    $jsonString = file_get_contents($ordersFile);
    $OrdersData = json_decode($jsonString, true);
    $orderTitles = array();
    foreach ($OrdersData as $order){
        array_push($orderTitles, $order['order']);
    }
    return $orderTitles;
}