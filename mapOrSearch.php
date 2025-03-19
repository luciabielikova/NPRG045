<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css" />
    <script src="script.js"></script>
    <title>Navigace</title>
</head>
<?php
include "header.php";
require 'functions.php';
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
$translations = loadTranslations();
$t = $translations[$_SESSION['language']];

?>
<body class="nav">
<div class="wrapper">
    <div class="content">
        <div class="container">
            <a href="searchDatabase.php" class="button"><?=$t['lexicon']?></a>
            <a href="searchMap.php" class="button"><?=$t['map']?></a>
        </div>
    </div>
</div>
<?php
include 'footer.php';
?>
</body>
</html>
