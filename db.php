<?php

require_once 'filesManager.php';

$allAnimals = getAllAnimals();

$allContinents = getAllContinents();

$allBiotopes = getAllBiotopes();

$allClasses = getAllClasses();

$allOrders = getAllOrders();

/*
$classesArray = array();

$allOrders = array();

$foundOrders = array();

//nelubi sa mi to mat niekde ulozene, ale zaroven sa mi nelubi to hladat zakazdym
//anyway, to treba v javascripte
//<a href="<?php $_SERVER['PHP_SELF']; ?>">Recargar</a>?????????????????????????????????????????????????


function type(){
    $file = 'jsons/classesFromWeb.json';
    $jsonString = file_get_contents($file);
    $data = json_decode($jsonString, true);
    global $classesArray,$ordersArray;

    foreach ($data as $row){
        if ($row['type'] == 'class' )
        {
            array_push($classesArray, $row);
        }
        elseif($row['type'] == 'order')
        {
            array_push($ordersArray, $row);

        }

    }
}

function getOrdersForClass($classTitle)
{
    global $classesArray, $ordersArray;
    $classID = 0;
    foreach ($classesArray as $row)
    {
        if ($row['title'] == $classTitle)
        {
           $classID = $row['id_total'] ;
        }
    }
    foreach ($ordersArray as $row)
    {
        if ($row['id_reference'] == $classID){
           array_push( $foundOrders, $row['title']);
        }
    }
    return $foundOrders;
}

*/



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

?>
