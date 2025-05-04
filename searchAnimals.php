<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <link rel="stylesheet" href="styles.css">
    <title>Zoo</title>
    <script src="script.js"></script>
    <link rel="icon" href="favicon-16x16.png" type="image/png">
</head>

<body>
<?php
include "header.php";
require_once "languages.php";
include 'functions.php';
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $_SESSION['filter_data'] = $_POST;
    header("Location: " . strtok($_SERVER["REQUEST_URI"], '?'));
    exit;
}

if (isset($_SESSION['filter_data'])) {
    $_POST = $_SESSION['filter_data'];
    unset($_SESSION['filter_data']);
}

?>

<div id="main-container">
    <div id="filter">
        <form method="POST">
            <div id="searchTitle">

                <?php

                $translation = getTranslation($_SESSION['language']);
                $lastSearched = (isset($_POST['title']) && $_POST['title'] !== "") ? 'value=' . $_POST['title'] : 'placeholder="' . htmlspecialchars($translation['by_title'], ENT_QUOTES, 'UTF-8') . '"';
                echo '<input type="search-input" name="title" id="search"  ' . $lastSearched . '>';
                echo '<input type="submit" value="🔍">';
                echo '<button onclick="clearSearch()">🗘</button>';
                echo '<button onclick="clearAll()">🗙</button>';
                ?>
            </div>

            <div id="advancedSearch">
                <?php
                global $allContinents, $allHabitats, $allOrders, $allClasses;
                echo '<div class="filter-header">';
                echo '<b>' . $translation['continents'] . '</b>';
                echo '<button type="button" onclick="uncheck(\'.continent\')">🗘</button>';
                echo '</div>';

                foreach ($allContinents as $id => $continent) {
                    $isChecked = (isset($_POST['continents']) && in_array($id, $_POST['continents'])) ? 'checked="checked"' : '';
                    echo '<input type="checkbox" class="continent" id="continent_' . htmlspecialchars($id, ENT_QUOTES) . '" value="' . htmlspecialchars($id, ENT_QUOTES) . '" name="continents[]" ' . $isChecked . '>';
                    echo '<label for="continent_' . htmlspecialchars($id, ENT_QUOTES) . '">' . htmlspecialchars($continent, ENT_QUOTES) . '</label><br>';
                }


                echo '<div class="filter-header">';
                echo '<br><b>' . $translation['habitats'] . '</b>';
                echo '<button type="button" onclick="uncheck(\'.habitat\')">🗘</button><br>';
                echo '</div>';

                foreach ($allHabitats as $id => $habitat) {
                    $isChecked = (isset($_POST['habitats']) && in_array($id, $_POST['habitats'])) ? 'checked="checked"' : '';
                    echo '<input type="checkbox" class="habitat" id="habitat_' . htmlspecialchars($id, ENT_QUOTES) . '" value="' . htmlspecialchars($id, ENT_QUOTES) . '" name="habitats[]" ' . $isChecked . '>';
                    echo '<label for="habitat_' . htmlspecialchars($id, ENT_QUOTES) . '">' . htmlspecialchars($habitat, ENT_QUOTES) . '</label><br>';
                }

                echo '<br><b>' . $translation['classes'] . '</b>';
                echo '<button type="button" onclick="uncheck(\'.class\')">🗘</button><br>';

                foreach ($allClasses as $id => $class) {
                    $isChecked = (isset($_POST['classes']) && in_array($id, $_POST['classes'])) ? 'checked="checked"' : '';
                    echo '<input type="checkbox" class="class" id="class_' . htmlspecialchars($id, ENT_QUOTES) . '" value="' . htmlspecialchars($id, ENT_QUOTES) . '" name="classes[]" ' . $isChecked . '>';
                    echo '<label for="class_' . htmlspecialchars($id, ENT_QUOTES) . '">' . htmlspecialchars($class, ENT_QUOTES) . '</label><br>';
                }

                echo '<br><b>' . $translation['orders'] . '</b>';
                echo '<button type="button" onclick="uncheck(\'.order\')">🗘</button><br>';

                foreach ($allOrders as $id => $order) {
                    $isChecked = (isset($_POST['orders']) && in_array($id, $_POST['orders'])) ? 'checked="checked"' : '';
                    echo '<input type="checkbox" class="order" id="order_' . htmlspecialchars($id, ENT_QUOTES) . '" value="' . htmlspecialchars($id, ENT_QUOTES) . '" name="orders[]" ' . $isChecked . '>';
                    echo '<label for="order_' . htmlspecialchars($id, ENT_QUOTES) . '">' . htmlspecialchars($order, ENT_QUOTES) . '</label><br>';
                }

                echo '<br>';
                ?>
            </div>
        </form>
    </div>
    <div id="content">
        <div>
            <?php
            global $searchedTitle, $chosenHabitats, $chosenContinents, $chosenOrders, $chosenClasses, $allAnimalTitles, $allAnimals;
            formHandlerSearchDB($_SESSION['zooID']);
            listOfFoundAnimals(filterAnimals( $searchedTitle,$chosenHabitats, $chosenContinents,$chosenOrders,$chosenClasses), $_SESSION['language']);
            ?>
        </div>
    </div>
</div>





<?php
include 'footer.php';
?>
</body>

</html>