<?php
// Spustenie session, ak ešte nebeží
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

// Nastavenie jazyka z GET parametra, ak bol odoslaný
if (isset($_GET['language'])) {
    $_SESSION['language'] = $_GET['language'];
}
if (!isset($_SESSION['language'])) {
    $_SESSION['language'] = 'en';
}
?>


<?php
require_once 'languages.php';

$selectedLang = $_SESSION['language'];

$languages = getLanguages();

$translation = getTranslation($selectedLang);

?>

<!DOCTYPE html>
<html lang="<?= $selectedLang ?>">
<head>
    <title>Zoo</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
</head>
<body>

<header>
    <?php
    $currentPage = basename($_SERVER['PHP_SELF']);

    // Dynamické nadpisy podľa stránky alebo stavu session
    if ($currentPage === 'index.php'){
        echo "<h1>". $translation['welcome']. "</h1>";
    }
    elseif ($currentPage === 'form.php'){
        echo "<h1>". $translation['add_zoo']. "</h1>";
    }
    elseif ($currentPage === 'mapNotAvailable.php'){
        // Ak nie je dostupná mapa, zobrazí sa názov zoo a info o jej príprave
        echo "<h1>". getZooById($_SESSION['zooID'])['name'][$_SESSION['language']]. "</h1>";
        echo "<h3>". $translation['preparingData']. "</h3>";
    }
    elseif(!isset($_SESSION['zooID'])){
        // Ak nie je vybraná žiadna zoo, zobrazí sa varovanie a fallback
        echo "<h1>". $translation['zooNotSet']. "</h1>";
        echo "<h3>". $translation['curPragueZoo']. "</h3>";
    }
    else{
        // Štandardné zobrazenie názvu a popisu zoo
        echo "<h1>". getZooById($_SESSION['zooID'])['name'][$_SESSION['language']]. "</h1>";
        echo "<h3>". getZooById($_SESSION['zooID'])['description'][$_SESSION['language']]. "</h3>";
    }

    ?>


    <!-- Výber jazyka -->
    <div class="language-selector">
        <label for="language"> <?= $translation['language'] . "🌍" ?> </label>
        <select id="language">
            <?php foreach ($languages as $code => $name): ?>
                <option value="<?= $code ?>" <?= ($selectedLang == $code) ? 'selected' : '' ?>>
                    <?= $name ?>
                </option>
            <?php endforeach; ?>
        </select>
    </div>
</header>

<!-- JavaScript na spracovanie zmeny jazyka -->
<script src="script.js"></script>

</body>
</html>



