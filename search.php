<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <link rel="stylesheet" href="styles.css">
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
        echo '<br>kontinenty <br>';
        foreach ($allContinents as $continent)
        {
            echo '<input type="checkbox" id="'. $continent .'" value="'. $continent .'" name="continents[]"><label for="'. $continent .'"  >'. $continent .'</label>';
        }
        echo '<br>biotopy <br>';
        foreach ($allBiotopes as $biotope)
        {
            echo '<input type="checkbox" id="'. $biotope .'" value="'. $biotope .'" name="biotopes[]"><label for="'. $biotope .'">'. $biotope .'</label>';
        }
        echo '<br>trida <br>';
        foreach ($allClasses as $class)
        {
            echo '<input type="checkbox" id="'. $class .'" value="'. $class .'" name="classes[]"><label for="'. $class .'">'. $class .'</label>';
        }
        echo '<br>rad <br>';
        foreach ($allOrders as $order)
        {
            echo '<input type="checkbox" id="'. $order .'" value="'. $order .'" name="orders"><label for="'. $order .'" >'. $order .'</label>';
        }
        echo '<br>';



        ?>
        <input type="submit">
    </div>
</form>



<div>
    <?php
    function vytvorOdkazNaZvieratko($animal){
        return '<li><a href="detail.php?title='.$animal['title'].'">'.$animal['title'] .'</a></li>';
    }
    function form_handler()
    {
        global $searchedTitle, $chosenContinents,$chosenOrders,$chosenClasses, $allClasses, $allOrders, $allContinents, $allBiotopes ;

        if (isset($_POST['title'])) {
            $searchedTitle = $_POST['title'];
        }
        else{
            $searchedTitle = '';
        }
        if (isset($_POST['continents'])) {
            $chosenContinents = $_POST['continents'];
        }
        else
        {
            $chosenContinents = $allContinents;
        }
        if (isset($_POST['biotopes'])) {
            $chosenBiotopes = $_POST['biotopes'];
        }
        else
        {
            $chosenBiotopes = $allBiotopes;
        }
        if (isset($_POST['classes'])) {
            $chosenClasses = $_POST['classes'];
        }
        else{
            $chosenClasses = $allClasses;
        }
        if (isset($_POST['order'])) {
            $chosenOrders = ($_POST['order']);
        }
        else{
            $chosenOrders = $allOrders;
        }
    }
form_handler();
    $url = 'search.php?';

    global $searchedTitle, $chosenContinents,$chosenOrders,$chosenClasses, $allAnimals ;

    $suitableAnimals = getAnimalsBySearchedTitle($searchedTitle, $allAnimals);
    $suitableAnimals = getAnimalsByClass($suitableAnimals, $chosenClasses);
    $suitableAnimals = getAnimalsByOrder($suitableAnimals, $chosenOrders);
    $suitableAnimals = getAnimalsByContinent($suitableAnimals,$chosenContinents);

    function listOfFoundAnimals($suitableAnimals)
    {
        if (count($suitableAnimals) > 0) {
            echo '<ol>';
            foreach ($suitableAnimals as $animal) {
                echo vytvorOdkazNaZvieratko($animal);
            }
            echo '</ol>';
        }
        else{
            echo 'pre zvolene kriteria nemame zvieratko';
        }
    }
    listOfFoundAnimals($suitableAnimals)
    ?>
</div>
</body>
</html>
<?php