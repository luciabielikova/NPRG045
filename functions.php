<?php

require_once 'db.php';

if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

if (isset($_SESSION['zooID'])) {
    $zooID = $_SESSION['zooID'];
}
else{
    $zooID = 'prague';
}

if (isset($_SESSION['language'])) {
    $language = $_SESSION['language'];
}
else{
    $language = 'en';
}
if (!function_exists('getTranslation')) {
    function getTranslation($language){
        $translations = loadTranslations();
        return $translations[$language];
    }
}



$allAnimals = getAllAnimals($zooID, $language);

$allAnimalTitles = getAnimalTitles($zooID, $language);

$allContinents = getAllContinents($zooID, $language);

$allHabitats = getAllHabitats($zooID, $language);

$allClasses = getAllClasses($zooID,$language);

$allOrders = getAllOrders($zooID,$language);

$zooTitles = getZooTitles($language);


function removeDiacritics($string) {
    $normalized = iconv('UTF-8', 'ASCII//TRANSLIT//IGNORE', $string);
    return strtolower($normalized);
}

function getAnimalsBySearchedTitle($foundAnimals, $searchedTitle, $language)
{
    $suitableAnimals = array();
    $normalizedQuery = removeDiacritics($searchedTitle);

    foreach ($foundAnimals as $animal) {
        if (isset($animal['names'][$language])) {
            $animalName = $animal['names'][$language];
            $normalizedAnimalName = removeDiacritics($animalName);
            if (strpos($normalizedAnimalName, $normalizedQuery) !== false) {
                $suitableAnimals[] = $animal;
            }
        }
    }
    return $suitableAnimals;
}

function getCompleteAnimalDetail($animalID, $zooID, $language){
    $animal = getAnimalDetail($animalID, $zooID, $language);

    if ($animal != null){
        $categories = getAnimalCategories($animalID, $zooID);
        $animal['id'] = $animalID;
        $animal["image_src"] = $categories["image_src"];
        $animal["class_id"] = getClassByID($categories["class_id"]);
        $animal["order_id"] = getOrderByID($categories["order_id"]);
        $animal["habitats"] = getHabitatsByID($categories["habitats"]);
        $animal["continents"] = getContinentsByID($categories["continents"]);
    } else {
        $animal = null;
    }
    return $animal;
}




function getAnimalsByContinent($foundAnimals, $wantedContinents)
{
    $suitableAnimals = array();
    if (count($wantedContinents) != 0){
        foreach ($foundAnimals as $animal) {
            if (isset($animal['continents']) && is_array($animal['continents'])) {
                $wantedContinents = array_map('intval', $wantedContinents);
                if (!empty(array_intersect($animal['continents'], $wantedContinents))) {
                    array_push($suitableAnimals, $animal);
                }
            }
        }
        return $suitableAnimals;
    }
    else{
        return $foundAnimals;
    }
}

function getAnimalsByHabitat($foundAnimals,$wantedHabitats)
{
    $suitableAnimals = array();
    foreach ($foundAnimals as $animal) {
        if (isset($animal['habitats'])&& is_array($animal['habitats'])) {
            if (!empty(array_intersect($animal['habitats'], $wantedHabitats))) {

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
        if (isset($animal['class_id'])) {
            if (in_array($animal['class_id'], $wantedClasses)) {
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
        if (isset($animal['order_id'])) {
            if (in_array($animal['order_id'], $wantedOrders)) {
                array_push($suitableAnimals, $animal);
            }
        }
    }
    return $suitableAnimals;
}



function createLinkToAnimal($id,$name){

    return '<li><a href="detail.php?animalID='.$id.'">'.$name .'</a></li>';
}

function listOfFoundAnimals($suitableAnimals, $language = 'en')
{
    if (count($suitableAnimals) > 0) {
        echo '<ol>';
        foreach ($suitableAnimals as $animal) {
            if (isset( $animal["names"][$language])) {
                echo createLinkToAnimal($animal['id'], $animal["names"][$language]);
            }
        }
        echo '</ol>';
    }
    else{
        $translations = loadTranslations();
        echo $translations[$_SESSION['language']]['animal_not_found'];
    }
}


function listOfAnimals($suitableAnimals)
{
    var_dump($suitableAnimals);
    if (count($suitableAnimals) > 0) {
        echo '<ol>';
        foreach ($suitableAnimals as $id => $name) {
            echo createLinkToAnimal($id, $name);
        }
        echo '</ol>';
    }
    else{
        echo 'Pro zvolené kritériá nemáme zvířátko-.';
    }
}

function filterAnimals($searchedTitle,$chosenHabitats, $chosenContinents,$chosenOrders,$chosenClasses){
    global $allAnimals;

    $suitableAnimals = getAnimalsBySearchedTitle($allAnimals, $searchedTitle, $_SESSION['language']);
    $suitableAnimals = getAnimalsByContinent($suitableAnimals,$chosenContinents);
    $suitableAnimals = getAnimalsByHabitat($suitableAnimals, $chosenHabitats);
    $suitableAnimals = getAnimalsByClass($suitableAnimals, $chosenClasses);
    $suitableAnimals = getAnimalsByOrder($suitableAnimals, $chosenOrders);
    return $suitableAnimals ;
}

function formHandlerSearchDB($id)
{
    global $searchedTitle, $chosenHabitats, $chosenContinents, $chosenOrders, $chosenClasses, $allClasses, $allOrders, $allContinents, $allHabitats;

    if (isset($_POST['title'])) {
        $searchedTitle = htmlspecialchars($_POST['title'], ENT_QUOTES);
    } else {
        $searchedTitle = '';
    }

    if (isset($_POST['continents'])) {
        $chosenContinents = array_map(function($continent) {
            return htmlspecialchars($continent, ENT_QUOTES);
        },
            $_POST['continents']);
    } else {
        $chosenContinents = array_keys($allContinents);

    }

    if (isset($_POST['habitats'])) {
        $chosenHabitats = array_map(function($habitat) {
            return htmlspecialchars($habitat, ENT_QUOTES);
        }, $_POST['habitats']);
    } else {
        $chosenHabitats = array_keys($allHabitats);
    }

    if (isset($_POST['classes'])) {
        $chosenClasses = array_map(function($class) {
            return htmlspecialchars($class, ENT_QUOTES);
        }, $_POST['classes']);
    } else {
        $chosenClasses = array_keys($allClasses);
    }

    if (isset($_POST['orders'])) {
        $chosenOrders = array_map(function($order) {
            return htmlspecialchars($order, ENT_QUOTES);
        }, $_POST['orders']);
    } else {
        $chosenOrders = array_keys($allOrders);
    }
}

function isMapAvailable($zooID)
{
    return loadHighways($zooID) !== null;
}

?>
