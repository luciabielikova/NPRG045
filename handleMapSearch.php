<?php
require_once 'dijkstra.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $from = isset($_POST['from']) ? $_POST['from'] : '';
    $to = isset($_POST['to']) ? $_POST['to'] : '';

    if (!empty($from) && !empty($to)) {
        $shortestPath = get_path($from, $to);

        $response = array(
            'status' => 'success',
            'message' => 'Data received successfully',
            'data' => array(
                'from' => $from,
                'to' => $to,
                'result' => $shortestPath
            )
        );
    } else {
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



