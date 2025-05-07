
<?php

//interaktívne zobrazuje zvieratá ktoré vyhovujú vyhľadávanému reťazcu

require_once 'db.php';

//funkcia na odstránenie diakritiky
function removeDiacritics($string) {
    $normalized = iconv('UTF-8', 'ASCII//TRANSLIT//IGNORE', $string);
    return strtolower($normalized);
}

$animalNames = getAnimalTitles($_SESSION['zooID'], $_SESSION['language']);

if (isset($_GET['query'])) {
    $query = $_GET['query'];
    $filteredValues = array_filter($animalNames, function($value) use ($query) {
        $normalizedValue = removeDiacritics($value);
        $normalizedQuery = removeDiacritics($query);
        return strpos($normalizedValue, $normalizedQuery) !== false;
    });

    header('Content-Type: application/json');
    echo json_encode(array_values($filteredValues));
}
?>