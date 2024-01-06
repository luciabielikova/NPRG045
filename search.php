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
        <span class="search-icon material-symbols-outlined">search</span>
        <input type="search-input" name="search" id="search" placeholder="Hledat...">
    </div>
    <div id = "complexSearch">
        <?php
        include 'db.php';
        global $continents;
        foreach ($continents as $continent)
        {
            echo '<input type="checkbox" id="continent" value="'. $continent .'"><label for="continent">'. $continent .'</label><br>';
        }
        ?>
    </div>
</form>



<div id="animalDetails">
    <?php
    $zVyhladavania = '';
    if (isset($_POST['search'])) {
        $zVyhladavania = htmlspecialchars($_POST['search']);
    }
    else{
        $zVyhladavania = '';
    }
    function vytvorOdkazNaZvieratko($animal){
        return '<li><a href="detail.php?title='.$animal['title'].'">'.$animal['title'] .'</a></li>';
    }

    $vyhovujuceZvieratka = getAnimalByTitle($zVyhladavania);
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