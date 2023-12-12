<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <title>Zoo</title>

</head>
<body>
<form method="POST">
    <div id="search">
        <span class="search-icon material-symbols-outlined">search</span>
        <input type="search-input" name="search" id="search" placeholder="Hledat...">
        <!--<input type="submit" name ="submit" id="search-input" value="Vyhledej">--!>
    </div>
</form>
<div id="animalDetails">
    <?php
//    header("Location: http://localhost:63342/untitled/index.php", true, 302);

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

    function vytvorOdkazNaZvieratko($animal){
        return '<li><a href="detail.php">'.$animal['title'] .'</a></li>';
    }

    global $data;
    $zVyhladavania = '';
    if (isset($_POST['search'])) {
        $zVyhladavania = htmlspecialchars($_POST['search']);
    }

    $vyhovujuceZvieratka = array();


    foreach ($data as $animal) {
        $pattern = '/' . $zVyhladavania . '/i';
        if (isset($animal['title'])) {
            if (preg_match_all($pattern, $animal['title'], $matches)) {
                array_push($vyhovujuceZvieratka, $animal);
            }
        }
    }
    if (count($vyhovujuceZvieratka) > 0) {
        echo '<ol>';
        foreach ($vyhovujuceZvieratka as $animal) {
            echo vytvorOdkazNaZvieratko($animal);
        }
        echo '</ol>';
    }



    ?>
</div>
</body>
</html>
<?php
