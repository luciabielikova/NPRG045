<?php

// Načítanie potrebných súborov – implementácia Dijkstrova algoritmu a jazykové preklady
require_once 'dijkstra.php';
require_once 'languages.php';

// Zistenie zvoleného jazyka zo session
$selectedLang = $_SESSION['language'];

// Načítanie všetkých dostupných jazykov
$languages = getLanguages();

// Načítanie prekladov pre aktuálny jazyk
$translation = getTranslation($selectedLang);


if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $from = isset($_POST['from']) ? trim($_POST['from']) : '';
    $to = isset($_POST['to']) ? trim($_POST['to']) : '';

    // Rozdelenie, čistenie a filtrovanie zoznamu povinných a zakázaných zastávok
    $mandatory = isset($_POST['mandatory']) && trim($_POST['mandatory']) !== ''
        ? array_unique(array_filter(array_map('trim', explode(',', $_POST['mandatory']))))
        : [];

    $forbidden = isset($_POST['forbidden']) && trim($_POST['forbidden']) !== ''
        ? array_unique(array_filter(array_map('trim', explode(',', $_POST['forbidden']))))
        : [];

    $conflicts = [];

    // Kontrola, či počiatočný alebo cieľový bod nie sú zakázané
    if (in_array($from, $forbidden)) {
        $conflicts[] = "From ($from)";
    }
    if (in_array($to, $forbidden)) {
        $conflicts[] = "To ($to)";
    }
    // Kontrola, či sa niektorá povinná zastávka nenachádza aj v zakázaných
    $commonMandatory = array_intersect($mandatory, $forbidden);

    if (!empty($commonMandatory)) {
        $conflicts[] = "Mandatory values (" . implode(', ', $commonMandatory) . ")";
    }

    // Ak existujú konfliktné vstupy, vráti sa chybová správa
    if (!empty($conflicts)) {
        $errorMessage = $translation['pathNotFound'];
        echo json_encode(['error' => $errorMessage]);
        exit;
    }

    // Skontroluj, či sú počiatočné a cieľové body platné
    if (!empty($from) && !empty($to) && getFirstCoordinateFromName($from) !== "" && getFirstCoordinateFromName($to) !== "") {
        // Výpočet najkratšej cesty so zadanými podmienkami
        $shortestPath = get_path($from, $to, $mandatory, $forbidden);
        // Vytvorenie odpovede so získanými údajmi
        $response = array(
            'status' => 'success',
            'message' => 'Data received successfully',
            'data' => array(
                'from' => $from,
                'to' => $to,
                'mandatory' => $mandatory,
                'forbidden' => $forbidden,
                'result' => $shortestPath
            )
        );
    }
    else {
        $response = array(
            'status' => 'error',
            'message' => 'Invalid input data'
        );
    }
} else {
    $response = array(
        'status' => 'error',
        'message' => 'Invalid request method'
    );
}
// Nastavenie hlavičky a výstup JSON odpovede
header('Content-Type: application/json');
echo json_encode($response);
?>



