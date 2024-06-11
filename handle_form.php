<?php
// Include the functions file
require_once 'dijkstra.php';

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get the 'from' and 'to' values from the POST request
    $from = isset($_POST['from']) ? $_POST['from'] : '';
    $to = isset($_POST['to']) ? $_POST['to'] : '';

    // Validate or process the input values
    if (!empty($from) && !empty($to)) {
        // Call the function from the included file
        $shortestPath = get_path($from, $to);

        // Create a response array
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
        // If validation fails, create an error response
        $response = array(
            'status' => 'error',
            'message' => 'Invalid input data'
        );
    }
} else {
    // If the request method is not POST, return an error response
    $response = array(
        'status' => 'error',
        'message' => 'Invalid request method'
    );
}

// Set the content type to JSON and return the response
header('Content-Type: application/json');
echo json_encode($response);
?>
