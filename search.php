<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <title>Zoo</title>

</head>
<body>
<form method="POST">
    <div id="search">
        <input type="search-input" name="title" id="search" placeholder="Podle nazvu...">

    </div>
    <div id = "complexSearch">
        <?php
        include 'db.php';
        global $allContinents,$allBiotopes,$allOrders,$allClasses;
        echo 'kontinenty <br>';
        foreach ($allContinents as $continent)
        {
            echo '<input type="checkbox" id="'. $continent .'" value="'. $continent .'" name="continents[]"><label for="'. $continent .'" checked >'. $continent .'</label><br>';
        }
        echo 'biotopy <br>';
        foreach ($allBiotopes as $biotope)
        {
            echo '<input type="checkbox" id="'. $biotope .'" value="'. $biotope .'" name="continents[]"><label for="'. $biotope .'" checked>'. $biotope .'</label><br>';
        }
        echo 'trida <br>';
        foreach ($allClasses as $class)
        {
            echo '<input type="checkbox" id="'. $class .'" value="'. $class .'" name="continents[]"><label for="'. $class .'" checked>'. $class .'</label><br>';
        }
        echo 'rad <br>';
        foreach ($allOrders as $order)
        {
            echo '<input type="checkbox" id="'. $order .'" value="'. $order .'" name="continents[]"><label for="'. $order .'" checked>'. $order .'</label><br>';
        }
        ?>
    </div>
</form>



<div>
    <?php
    function vytvorOdkazNaZvieratko($animal){
        return '<li><a href="detail.php?title='.$animal['title'].'">'.$animal['title'] .'</a></li>';
    }
    function form_handler()
    {
        global $hladanyNazov, $continents,$hladanyRad,$hladanaTrieda ;

        if (isset($_POST['title'])) {
            $hladanyNazov = htmlspecialchars($_POST['title']);
        }
        else{
            $hladanyNazov = '';
        }
        if (isset($_POST['order'])) {
            $hladanyRad = htmlspecialchars($_POST['order']);
        }
        else{
            $hladanyRad = '';
        }
        if (isset($_POST['classes'])) {
            $hladanaTrieda = htmlspecialchars($_POST['classes']);
        }
        else{
            $hladanaTrieda = '';
        }
        if (isset($_POST['continents'])) {
            $continents = $_POST['continents'];
        }
        else
        {
            $continents = getAllContinents();/////////////////////////////////////////////////////////////////////////////////////
        }

    }
form_handler();
    global $hladanyNazov, $continents,$hladanyRad,$hladanaTrieda ;

    $byTitle = getAnimalsBySearchedTitle($hladanyNazov);

    $byOrder = getAnimalsByOrder($byTitle, '');

    /*if (count($vyhovujuceZvieratka) > 0) {
        echo '<ol>';
        foreach ($vyhovujuceZvieratka as $animal) {
            echo vytvorOdkazNaZvieratko($animal);
        }
        echo '</ol>';
    }*/

    $vyhovujuceZvieratka = getAnimalsByContinent($byTitle,$continents);

    function listOfFoundAnimals($vyhovujuceZvieratka)
    {
        if (count($vyhovujuceZvieratka) > 0) {
            echo '<ol>';
            foreach ($vyhovujuceZvieratka as $animal) {
                echo vytvorOdkazNaZvieratko($animal);
            }
            echo '</ol>';
        }
    }
    listOfFoundAnimals($vyhovujuceZvieratka)
    ?>
</div>
</body>
</html>
<?php