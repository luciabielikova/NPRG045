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

<div id="animalDetails">

    <?php


    require_once 'funkcie.php';

    $title = isset($_GET['title']) ? $_GET['title'] : '';//nejaky redirect
    if ($title === ''){
        require ('redirect.php');

    }
    $animal = getAnimalDetail($title);

    echo createAnimalHTML($animal);

    function createAnimalHTML($animal)
    {
        $html = '<div class="animal">';
        if (isset($animal['image_src'])) {
            $html .= '<img src="' . $animal['image_src'] . '" alt="' . $animal['image_alt'] . '">';
        }
        $html .= '<h2>' . $animal['title'] . '</h2>';
        if (isset($animal['latin_title'])) {
            $html .= '<h3>' . $animal['latin_title'] . '</h3>';
        }
        $html .= '<p><b>ZÁKLADNÍ INFORMACE</b></p>';
        if (isset($animal['classes'])) {
            $html .= '<p><b>Třída: </b>' . $animal['classes'] . '</p>';
        }
        if (isset($animal['order'])) {
            $html .= '<p><b>Řád: </b>' . $animal['order'] . '</p>';
        }
        if (isset($animal['continents'])) {
            $html .= '<p><b>Kontinenty: </b>' . $animal['continents'] . '</p>';
        }
        if (isset($animal['spread_note'])) {
            $html .= '<p><b>Rozšíření: </b>' . $animal['spread_note'] . '</p>';
        }
        if (isset($animal['description'])) {
            $html .= '<p><b>Popis: </b><br>' . $animal['description'] . '</p>';
        }
        if (isset($animal['biotop'])) {
            $html .= '<p><b>Biotop: </b> ' . $animal['biotop'] . '</p>';
        }
        if (isset($animal['food'])) {
            $html .= '<p><b>Potrava:</b> ' . $animal['food'] . '</p>';
        }
        if (isset($animal['attractions'])) {
            $html .= '<p><b>Zajímavosti:</b><br>' . $animal['attractions'] . '</p>';
        }

        $html .= '</div>';
        return $html;
    }
?>
</div>
<div id="mapid"></div>
<?php

    function createMap($animal){
        if (isset($animal['coordinates'])) {
            ?>
            <script>
                var map = L.map('mapid').setView( <?php echo $animal['coordinates']; ?>, 24);
                L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                    maxZoom: 18,
                    attribution: '© OpenStreetMap contributors'
                }).addTo(map);

                fetch('load_geojson.php')
                    .then(response => response.json())
                    .then(data => {
                        L.geoJSON(data, {
                            style: myStyle,
                            pointToLayer: function (feature, latlng) {
                                return null;
                            }
                        }).addTo(map);
                    });
            </script>
            <?php
        }
        else return;
    }

    createMap($animal);
    ?>


</body>
<?php
include 'footer.php';
?>
</html>
