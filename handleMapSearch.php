<?php
require_once 'dijkstra.php';
require_once 'languages.php';
$selectedLang = $_SESSION['language'];
$languages = getLanguages();
$translation = getTranslation($selectedLang);



if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $from = isset($_POST['from']) ? trim($_POST['from']) : '';
    $to = isset($_POST['to']) ? trim($_POST['to']) : '';
    $mandatory = isset($_POST['mandatory']) && trim($_POST['mandatory']) !== ''
        ? array_unique(array_filter(array_map('trim', explode(',', $_POST['mandatory']))))
        : [];

    $forbidden = isset($_POST['forbidden']) && trim($_POST['forbidden']) !== ''
        ? array_unique(array_filter(array_map('trim', explode(',', $_POST['forbidden']))))
        : [];

    $conflicts = [];

    if (in_array($from, $forbidden)) {
        $conflicts[] = "From ($from)";
    }

    if (in_array($to, $forbidden)) {
        $conflicts[] = "To ($to)";
    }

    $commonMandatory = array_intersect($mandatory, $forbidden);

    if (!empty($commonMandatory)) {
        $conflicts[] = "Mandatory values (" . implode(', ', $commonMandatory) . ")";
    }


    if (!empty($conflicts)) {
        $errorMessage = $translation['pathNotFound'];
        echo json_encode(['error' => $errorMessage]);
        exit;
    }





    if (!empty($from) && !empty($to) && getFirstCoordinateFromName($from) !== "" && getFirstCoordinateFromName($to) !== "") {
        $shortestPath = get_path($from, $to, $mandatory, $forbidden);

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

header('Content-Type: application/json');
echo json_encode($response);
?>



