<?php
require_once 'db.php';
header('Content-Type: application/json');
echo loadAnimalsGeojson();
?>
