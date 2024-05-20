<?php
header('Content-Type: application/json');
echo file_get_contents("jsons/zoo.geojson");  // Uistite sa, že cesta k súboru je správna
?>
