<!DOCTYPE html>
<html lang="sk">
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
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
//prázdna stránka s chybovou hláškou v hlavičke


include "header.php";

require_once 'languages.php';

$selectedLang = $_SESSION['language'];

$languages = getLanguages();

$translation = getTranslation($selectedLang);


?>
</body>
