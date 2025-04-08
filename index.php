<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css" />
    <title>Zoo Page</title>
    <script src="script.js"></script>
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

        include "functions.php";
        require_once "languages.php";
            global $zooTitles;

            $currentLanguage = isset($_SESSION['language']) ? $_SESSION['language'] : 'en';

            echo '<script>let selectedLanguage = "' . htmlspecialchars($currentLanguage, ENT_QUOTES) . '";</script>';
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
