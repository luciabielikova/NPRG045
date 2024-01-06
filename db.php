<?php


function get_animals()
{
    $animalfile = 'lexikon_zvirat.json';
    $jsonString = file_get_contents($animalfile);
    return json_decode($jsonString, true);
}

function get_continents(){
    $continentsFile = 'continents.json';
    $jsonString = file_get_contents($continentsFile);
    $ContinentsData = json_decode($jsonString, true);
    $continentTitles = array();
    foreach ($ContinentsData as $continent){
        array_push($continentTitles, $continent['name_c']);
    }
    return $continentTitles;
}

$continents = get_continents();



function getAnimalByTitle($zVyhladavania)
{
    $vyhovujuceZvieratka = array();
    foreach (get_animals() as $animal) {
        $pattern = '/' . $zVyhladavania . '/i';
        if (isset($animal['title'])) {
            if (preg_match_all($pattern, $animal['title'], $matches)) {
                array_push($vyhovujuceZvieratka, $animal);
            }
        }
    }
    return $vyhovujuceZvieratka;
}

function getAnimalByOrder($zVyhladavania)
{
    global $animalData;
    $vyhovujuceZvieratka = array();
    foreach ($animalData as $animal) {
        $pattern = '/' . $zVyhladavania . '/i';
        if (isset($animal['order'])) {
            if (preg_match_all($pattern, $animal['title'], $matches)) {
                array_push($vyhovujuceZvieratka, $animal);
            }
        }
    }
    return $vyhovujuceZvieratka;
}


function getAnimalByClass($zVyhladavania)
{
    global $animalData;
    $vyhovujuceZvieratka = array();
    foreach ($animalData as $animal) {
        $pattern = '/' . $zVyhladavania . '/i';
        if (isset($animal['classes'])) {
            if (preg_match_all($pattern, $animal['title'], $matches)) {
                array_push($vyhovujuceZvieratka, $animal);
            }
        }
    }
    return $vyhovujuceZvieratka;
}



?>
