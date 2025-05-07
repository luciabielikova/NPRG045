<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css" />
    <title>Zoo</title>
    <script src="script.js"></script>
    <link rel="icon" href="favicon-16x16.png" type="image/png">
</head>
<?php

if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
include "header.php";
?>
<body class="nav">
<div class="wrapper">
    <div class="content">
        <div class="container">
            <?php
                // Načítanie funkcií a jazykových prekladov
                include "functions.php";
                require_once "languages.php";
                // Prístup ku globálnej premennej s názvami zoo (už načítané vo functions.php)
                global $zooTitles;
                // Nastavenie aktuálneho jazyka
                $currentLanguage = isset($_SESSION['language']) ? $_SESSION['language'] : 'en';
                // Preposlanie jazyka do JavaScriptu
                echo '<script>let selectedLanguage = "' . htmlspecialchars($currentLanguage, ENT_QUOTES) . '";</script>';
                // Vygenerovanie tlačidiel pre každú zoo
                foreach ($zooTitles as $id => $title) {
                    echo '<button class="zooButton" data-zooid="' . htmlspecialchars($id) . '">' . htmlspecialchars($title) . '</button>';
                    }
            ?>
        </div>
    </div>
</div>
<?php
include 'footer.php';
?>
</body>
</html>
