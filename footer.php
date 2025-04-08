<?php
require_once "languages.php";

$selectedLang = $_SESSION['language'];

$translation = getTranslation($selectedLang);
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
            <a href="searchDatabase.php"><?= $translation['search']  ?></a>
            <a href="searchMap.php"><?= $translation['map']  ?></a>
            <a href="index.php"><?= $translation['change_zoo']  ?></a>

        </ul>
    </nav>
</footer>