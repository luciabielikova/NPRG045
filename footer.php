<?php
// Načítanie jazykových prekladov pre aktuálny jazyk používateľa
require_once "languages.php";
$selectedLang = $_SESSION['language'];
$translation = getTranslation($selectedLang);
?>

<!-- Hlavička stránky s metadátami -->
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css" />
    <title>Zoo</title>

</head>

<!-- Päta stránky s navigáciou -->
<footer id="pageFooter">
    <nav>
        <ul>
            <!-- Odkaz na zmenu zoo -->
            <a href="index.php"><?= $translation['change_zoo']  ?></a>
            <!-- Odkaz na vyhľadávanie zvierat -->
            <a href="searchAnimals.php"><?= $translation['searchDB']  ?></a>
            <!-- Odkaz na mapu ciest/zvierat -->
            <a href="searchPaths.php"><?= $translation['map']  ?></a>
            <!-- Odkaz na formulár pre pridanie novej zoo -->
            <a href="form.php"><?= $translation['add_zoo']  ?></a>

        </ul>
    </nav>
</footer>