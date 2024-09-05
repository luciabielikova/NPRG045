<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <link rel="stylesheet" href="styles.css">
    <title>Zoo</title>
    <script src="script.js"></script>
</head>
<body>
<div id="main-container">
<div id = "filter">
    <form method="POST">
        <div id="searchTitle">
            <?php
            $lastSearched = (isset($_POST['title']) && $_POST['title'] !== "") ? 'value=' . $_POST['title'] : 'placeholder="Podle názvu..."';
            echo '<input type="search-input" name="title" id="search"  '. $lastSearched .'>';
            echo '<input type="submit" value="🔍">';
            echo '<button onclick="clearSearch()">🗘</button>';
            echo '<button onclick="clearAll()">🗙</button>';
            ?>
        </div>

        <div id = "advancedSearch">
            <?php
                include 'functions.php';
                global $allContinents,$allBiotopes,$allOrders,$allClasses;
                echo '<br><b>Kontinenty</b>';
                echo '<button type="button" onclick="uncheck(\'.continent\')">🗘</button><br>';
                foreach ($allContinents as $continent)
                {
                    $isChecked = (isset($_POST['continents']) && in_array($continent, $_POST['continents'])) ? 'checked="checked"' : '';
                    echo '<input type="checkbox" class="continent" id="'. htmlspecialchars($continent, ENT_QUOTES) .'" value="'. $continent .'" name="continents[]" ' . $isChecked . ' ><label for="'. $continent .'">'. $continent .'</label><br>';

                    //echo '<input type="checkbox" id="'. $continent .'" value="'. $continent .'" name="continents[]" ' . $isChecked . '><label for="'. $continent .'">'. $continent .'</label><br>';
                }


                echo '<br><b>Biotopy</b>';
            echo '<button type="button" onclick="uncheck(\'.biotope\')">🗘</button><br>';

            foreach ($allBiotopes as $biotope)
                {
                    $isChecked = (isset($_POST['biotopes']) && in_array($biotope, $_POST['biotopes'])) ? 'checked="checked"' : '';
                    echo '<input type="checkbox" class="biotope" id="'. htmlspecialchars($biotope, ENT_QUOTES) .'" value="'. $biotope .'" name="biotopes[]" ' . $isChecked . '><label for="'. $biotope .'">'. $biotope .'</label><br>';
                }

                echo '<br><b>Třídy</b>';
            echo '<button type="button" onclick="uncheck(\'.class\')">🗘</button><br>';

            foreach ($allClasses as $class)
                {
                    $isChecked = (isset($_POST['classes']) && in_array($class, $_POST['classes'])) ? 'checked="checked"' : '';
                    echo '<input type="checkbox" class="class" id="'. htmlspecialchars($class, ENT_QUOTES) .'" value="'. $class .'" name="classes[]" ' . $isChecked . '><label for="'. $class .'">'. $class .'</label><br>';
                }

                echo '<br><b>Řády</b>';
            echo '<button type="button" onclick="uncheck(\'.order\')">🗘</button><br>';

            foreach ($allOrders as $order)
                {
                    $isChecked = (isset($_POST['orders']) && in_array($order, $_POST['orders'])) ? 'checked="checked"' : '';
                    echo '<input type="checkbox" class="order" id="'. htmlspecialchars($order, ENT_QUOTES) .'" value="'. $order .'" name="orders[]" ' . $isChecked . '><label for="'. $order .'" >'. $order .'</label><br>';
                }

            echo '<br>';
            ?>
        </div>
    </form>
</div>
    <div id="content">
        <div>
            <?php
            global $searchedTitle,$chosenBiotopes, $chosenContinents,$chosenOrders,$chosenClasses;
            formHandlerSearchDB();
            listOfFoundAnimals(filterAnimals( $searchedTitle,$chosenBiotopes, $chosenContinents,$chosenOrders,$chosenClasses))
            ?>
        </div>
    </div>
</div>
<?php
include 'footer.php';
?>
</body>
</html>
