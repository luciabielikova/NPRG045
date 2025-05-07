<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <title>Zoo</title>
    <link rel="icon" href="favicon-16x16.png" type="image/png">
</head>
<body>
<?php
include "header.php";
?>

<div id="animalDetails">

    <?php

    require_once 'functions.php';
    if (session_status() === PHP_SESSION_NONE) {
        session_start();
    }
    // Získanie ID zvieraťa z URL
    $animalID = isset($_GET['animalID']) ? $_GET['animalID'] : '';
    if ($animalID === ''){
        header('Location: errorPage.php');
        exit;
    }
    // Získanie kompletného detailu zvieraťa (vrátane kategórií) pre aktuálny jazyk a zoo
    $animal = getCompleteAnimalDetail($animalID, $_SESSION['zooID'], $_SESSION['language']);
    echo createAnimalHTML($animal, $_SESSION['language']);

     //Funkcia na vytvorenie HTML zobrazenia detailu zvieraťa
    function createAnimalHTML($animal, $language = 'cs')
    {
        // Načítanie jazykových prekladov
        $translations = loadTranslations();
        $t = $translations[$language];
        $html = '<div class="animal">';

        if (!empty($animal['image_src'])) {
            $html .= '<img src="' . htmlspecialchars($animal['image_src']) . '">';
        }
        $html .= '<h2>' . htmlspecialchars($animal['name']) . '</h2>';
        if (!empty($animal['latin_name'])) {
            $html .= '<h3>' . htmlspecialchars($animal['latin_name']) . '</h3>';
        }
        $html .= '<p><b>' . $t['basic_info'] . '</b></p>';

        if (!empty($animal['class_id'])) {
            $html .= '<p><b>' . $t['class'] . ': </b>' . htmlspecialchars($animal['class_id']) . '</p>';
        }

        if (!empty($animal['order_id'])) {
            $html .= '<p><b>' . $t['order'] . ': </b>' . htmlspecialchars($animal['order_id']) . '</p>';
        }
        if (!empty($animal['continents'])) {
            $html .= '<p><b>' . $t['continents'] . ': </b>' . htmlspecialchars($animal['continents']) . '</p>';
        }
        if (!empty($animal['spread_note'])) {
            $html .= '<p><b>' . $t['spread'] . ': </b>' . htmlspecialchars($animal['spread_note']) . '</p>';
        }
        if (!empty($animal['description'])) {
            $html .= '<p><b>' . $t['description'] . ': </b><br>' . htmlspecialchars($animal['description']) . '</p>';
        }
        if (!empty($animal['habitats'])) {
            $html .= '<p><b>' . $t['habitats'] . ': </b>' . htmlspecialchars($animal['habitats']) . '</p>';
        }
        if (!empty($animal['food'])) {
            $html .= '<p><b>' . $t['food'] . ':</b> ' . htmlspecialchars($animal['food']) . '</p>';
        }
        if (!empty($animal['attractions'])) {
            $html .= '<p><b>' . $t['attractions'] . ':</b><br>' . htmlspecialchars($animal['attractions']) . '</p>';
        }
        $html .= '</div>';

        return $html;
    }

    ?>

</div>
<?php
include 'footer.php';
?>
</body>
</html>
