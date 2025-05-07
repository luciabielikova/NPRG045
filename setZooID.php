<?php
// Spustenie session, ak ešte nebola spustená
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
// Ak je v požiadavke POST odoslaný zooID, uložíme ho do session
if (isset($_POST['zooID'])) {
    $_SESSION['zooID'] = $_POST['zooID'];
}
// Ak je v požiadavke POST odoslaný jazyk (language), uložíme ho do session
if (isset($_POST['language'])) {
    $_SESSION['language'] = $_POST['language'];
}

?>
