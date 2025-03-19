<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
if (isset($_POST['zooID'])) {
    $_SESSION['zooID'] = $_POST['zooID'];
}

if (isset($_POST['language'])) {
    $_SESSION['language'] = $_POST['language'];
}

echo "Session updated";
?>
