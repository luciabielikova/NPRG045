<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Zoo</title>
</head>
<body>
<div id="animalDetails">
    <?php
    //    header("Location: http://localhost:63342/untitled/detail.php", true, 302);


    $path = 'lexikon_zvirat.json';
    $jsonString = file_get_contents($path);
    $data = json_decode($jsonString, true);


    function createAnimalHTML($animal) {
        $html = '<HR><div class="animal">';
        if (isset($animal['image_src'])) {
            $html .= '<img src="' . $animal['image_src'] . '" alt="' . $animal['image_alt'] . '">';
        }
        $html .= '<h2>' . $animal['title'] . '</h2>';
        if (isset($animal['latin_title'])) {
            $html .= '<h3>' . $animal['latin_title'] . '</h3>';
        }
        $html .= '<p><b>ZÁKLADNÍ INFORMACE</b></p>';
        if (isset($animal['classes'])) {
            $html .= '<p><b>Třída:</b>' . $animal['classes'] . '</p>';
        }
        if (isset($animal['order'])) {
            $html .= '<p><b>Řád:</b>' . $animal['order'] . '</p>';
        }
        if (isset($animal['spread_note'])) {
            $html .= '<p><b>Rozšíření:</b>' . $animal['spread_note'] . '</p>';
        }
        if (isset($animal['description'])) {
            $html .= '<p><b>Popis:</b><br>' . $animal['description'] . '</p>';
        }
        if (isset($animal['biotop'])) {
            $html .= '<p><b>Biotop:</b> ' . $animal['biotop'] . '</p>';
        }
        if (isset($animal['food'])) {
            $html .= '<p><b>Potrava:</b> ' . $animal['food'] . '</p>';
        }
        if (isset($animal['attractions'])) {
            $html .= '<p><b>Zajímavosti:</b><br>' . $animal['attractions'] . '</p>';
        }
        else{
            die('zvieratko bez nazvu');
        }
        $html .= '</div>';
        return $html;
    }


    global $data;

    foreach ($data as $animal) {
        echo createAnimalHTML($animal);
    }



    ?>
</div>
</body>
</html>
<?php
