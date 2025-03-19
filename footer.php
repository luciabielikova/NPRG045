<?php
require_once 'functions.php';
require_once 'db.php';



$translations = loadTranslations();
?>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css" />
    <title>Navigace</title>

</head>
<footer id="pageFooter">
    <nav>
        <ul>
            <a href="searchDatabase.php"><?= $translations[$_SESSION['language']]['search']  ?></a>
            <a href="searchMap.php"><?= $translations[$_SESSION['language']]['map']  ?></a>
            <a href="index.php"><?= $translations[$_SESSION['language']]['change_zoo']  ?></a>

        </ul>
    </nav>
</footer>