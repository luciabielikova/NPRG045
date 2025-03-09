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
    <?php
    include 'functions.php';

    // Initialize $dir as null by default
    $dir = null;

    // Check if dir is received via POST
    if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['dir'])) {
        $dir = $_POST['dir'];
        echo "Selected Zoo Directory: " . htmlspecialchars($dir);
    } else {
        echo "No zoo directory selected.";
        // Optionally set a default dir if needed, e.g., $dir = 'cs-prague';
        // $animals = getAllAnimals(); // Uncomment if you want to load default data
    }
    ?>
    <!-- Pass dir as a query parameter in the URLs -->
    <a href="searchDatabase.php<?php echo $dir ? '?dir=' . urlencode($dir) : ''; ?>" class="button">Vyhledávání</a>
    <a href="searchMap.php<?php echo $dir ? '?dir=' . urlencode($dir) : ''; ?>" class="button">Mapa</a>
</div>



</body>
</html>
