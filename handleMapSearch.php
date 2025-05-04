<?php
require_once 'dijkstra.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $from = isset($_POST['from']) ? $_POST['from'] : '';
    $to = isset($_POST['to']) ? $_POST['to'] : '';
    $mandatory = isset($_POST['mandatory']) ? explode(',', $_POST['mandatory']) : [];
    $forbidden = isset($_POST['forbidden']) ? explode(',', $_POST['forbidden']) : [];



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



