<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>

    <title>Zoo</title>
</head>
<body>
<?php
include "header.php";
?>

<div id="animalDetails">

    <?php

    require_once 'functions.php';
    require_once 'db.php';
    if (session_status() === PHP_SESSION_NONE) {
        session_start();
    }
    $animalID = isset($_GET['animalID']) ? $_GET['animalID'] : '';

    if ($animalID === ''){
        require('errorPage.php');

    }
    $animal = getAnimalDetail($animalID, $_SESSION['zooID'], $_SESSION['language'] );
    $animalCategories = getAnimalCategories($animalID, $_SESSION['zooID'], $_SESSION['language'] );;
    echo createAnimalHTML($animal, $animalCategories, $_SESSION['language']);



    function createAnimalHTML($animal, $animalCategories, $language = 'cs')
    {
        $translations = loadTranslations();


        $t = $translations[$language];

        $html = '<div class="animal">';
        if (!empty($animalCategories['image_src'])) {
            $html .= '<img src="' . htmlspecialchars($animalCategories['image_src']) . '">';
        }
        $html .= '<h2>' . htmlspecialchars($animal['name']) . '</h2>';
        if (!empty($animalCategories['latin_name'])) {
            $html .= '<h3>' . htmlspecialchars($animalCategories['latin_name']) . '</h3>';
        }
        $html .= '<p><b>' . $t['basic_info'] . '</b></p>';

        if (!empty($animalCategories['class_id'])) {
            $html .= '<p><b>' . $t['class'] . ': </b>' . htmlspecialchars($animalCategories['class_id']) . '</p>';
        }
        if (!empty($animalCategories['order_id'])) {
            $html .= '<p><b>' . $t['order'] . ': </b>' . htmlspecialchars($animalCategories['order_id']) . '</p>';
        }
        if (!empty($animalCategories['continents'])) {
            $html .= '<p><b>' . $t['continents'] . ': </b>' . htmlspecialchars($animalCategories['continents']) . '</p>';
        }
        if (!empty($animal['spread_note'])) {
            $html .= '<p><b>' . $t['spread'] . ': </b>' . htmlspecialchars($animal['spread_note']) . '</p>';
        }
        if (!empty($animal['description'])) {
            $html .= '<p><b>' . $t['description'] . ': </b><br>' . htmlspecialchars($animal['description']) . '</p>';
        }
        if (!empty($animalCategories['habitats'])) {
            $html .= '<p><b>' . $t['habitats'] . ': </b>' . htmlspecialchars($animalCategories['habitats']) . '</p>';
        }
        if (!empty($animal['food'])) {
            $html .= '<p><b>' . $t['food'] . ':</b> ' . htmlspecialchars($animal['food']) . '</p>';
        }
        if (!empty($animal['attractions'])) {
            $html .= '<p><b>' . $t['attractions'] . ':</b><br>' . htmlspecialchars($animal['attractions']) . '</p>';
        }
        if (!empty($animal['coordinates'])) {
            $html .= '<div id="mapid" class="detailPage"></div>';
        }
        $html .= '</div>';

        return $html;
    }



    displayCoordinates($animal);

    ?>

</div>
<?php
include 'footer.php';
?>
</body>
</html>
