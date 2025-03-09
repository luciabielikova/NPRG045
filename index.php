<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css" />
    <title>Navigace</title>

</head>

<body class="nav">
<div class="container">
    <h1>Seznam Zoo</h1>
    <?php
        include "functions.php";
        //asi nejake ine classy a tak celkovo podobny ale iny dizajn
        global $zooTitles, $allZoos;


        foreach ($allZoos as $zoo) {
            echo '<form action="mapOrSearch.php" method="POST" style="display: inline;">';
            echo '<input type="hidden" name="dir" value="' . htmlspecialchars($zoo['dir']) . '">';
            echo '<button type="submit" class="button">' . htmlspecialchars($zoo['title']) . '</button>';
            echo '</form>';
        }
    ?>
    <!--<a href="searchDatabase.php" class="button">Vyhledávání</a>
    <a href="searchMap.php" class="button">Mapa</a> -->
</div>
</body>
</html>
