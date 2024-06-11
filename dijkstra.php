<?php

class Graph {
    private $vertices = [];
    private $edges = [];

    public function addVertex($name, $longitude, $latitude) {
        $this->vertices[$name] = ['lon' => $longitude, 'lat' => $latitude];
    }

    public function addEdge($start, $end, $distance) {
        $this->edges[$start][$end] = $distance;
        $this->edges[$end][$start] = $distance;
    }

    public function getVertices() {
        return $this->vertices;
    }

    public function getEdges() {
        return $this->edges;
    }

    public function findClosestPoint($wanted) {
        $closestPoint = null;
        $dist = PHP_INT_MAX;
        foreach ($this->vertices as $name => $point) {
            if ($wanted[0] != $point['lon'] && $wanted[1] != $point['lat']) {
                $temp_dist = euclidean_distance([$wanted[0], $wanted[1]], [$point['lon'], $point['lat']]);
                if ($temp_dist < $dist) {
                    $dist = $temp_dist;
                    $closestPoint = $name;
                }
            }
        }
        return $closestPoint;
    }


}
class Dijkstra {
    private $graph;
    private $distances = [];
    private $previous = [];
    private $queue = [];

    public function __construct($graph) {
        $this->graph = $graph;
    }

    public function shortestPath($start, $end) {
        $this->distances = [];
        $this->previous = [];
        $this->queue = [];

        foreach ($this->graph->getVertices() as $vertex => $data) {
            if ($vertex === $start) {
                $this->distances[$vertex] = 0;
            } else {
                $this->distances[$vertex] = INF;
            }
            $this->previous[$vertex] = null;
            $this->queue[$vertex] = $this->distances[$vertex];
        }

        while (!empty($this->queue)) {
            $u = array_search(min($this->queue), $this->queue);
            if ($u === $end) {
                break;
            }

            unset($this->queue[$u]);

            if (!isset($this->graph->getEdges()[$u])) {
                continue;
            }

            foreach ($this->graph->getEdges()[$u] as $neighbor => $distance) {
                $alt = $this->distances[$u] + $distance;
                if ($alt < $this->distances[$neighbor]) {
                    $this->distances[$neighbor] = $alt;
                    $this->previous[$neighbor] = $u;
                    $this->queue[$neighbor] = $alt;
                }
            }
        }

        $path = [];
        $u = $end;
        while (isset($this->previous[$u])) {
            array_unshift($path, $u);
            $u = $this->previous[$u];
        }

        if (!empty($path)) {
            array_unshift($path, $start);
        }

        $pathWithCoordinates = [];
        foreach ($path as $vertex) {
            $data = $this->graph->getVertices()[$vertex];
            $pathWithCoordinates[] = [
                'vertex' => $vertex,
                'lon' => $data['lon'],
                'lat' => $data['lat'],

            ];
        }

        return $pathWithCoordinates;
    }
}


function euclidean_distance($point1, $point2) {
    return sqrt(pow($point1[0] - $point2[0], 2) + pow($point1[1] - $point2[1], 2));
}


function getGeoFromName($name){
    global $animals;
    foreach ($animals['features'] as $feature)
    {
        #echo $feature['properties']['name'];
        if ($name == $feature['properties']['name']){
            return $feature['geometry']['coordinates'];
        }
    }
}

// Load GeoJSON data from a file
$highwaysFile = file_get_contents('C:\Moje dokumenty\ZS\rocnikovy projekt\python\highways.geojson');
$highways = json_decode($highwaysFile, true);

function createGraph()
{
    global $highways;
    $graph = new Graph();

    $counter = 1;
    foreach ($highways['features'] as $feature) {
        if ($feature['geometry']['type'] === 'LineString') {
            $coordinates = $feature['geometry']['coordinates'];
            foreach($coordinates as $point){
                $graph->addVertex($counter,$point[0], $point[1] );
                $counter+=1;
            }
        }
    }

    foreach ($highways['features'] as $feature) {
        if ($feature['geometry']['type'] === 'LineString') {
            $coordinates = $feature['geometry']['coordinates'];
            // Find vertex names by coordinates
            $previousName = null;
            $previousCoords = null;
            foreach ($coordinates as $key => $coord) {
                $currentName = null;
                $currentCoords = null;
                foreach ($graph->getVertices() as $name => $vertex) {
                    if ($vertex['lat'] == $coord[1] && $vertex['lon'] == $coord[0]) {
                        $currentName = $name;
                        $currentCoords = $coord;
                        break;
                    }
                }
                if ($previousName && $currentName) {
                    $distance = round(euclidean_distance($previousCoords, $currentCoords)*100000);
                    $graph->addEdge($previousName, $currentName, $distance);
                }
                $previousName = $currentName;
                $previousCoords = $currentCoords;
            }
        }
    }
    return $graph;
}

$graph = createGraph();

$dijkstra = new Dijkstra($graph);





$animalsFile = file_get_contents('C:\Moje dokumenty\ZS\rocnikovy projekt\python\animals.geojson');
$animals = json_decode($animalsFile, true);


$animalNames = [];

foreach ($animals['features'] as $feature) {
    if ($feature['properties']['name'] != null) {
        array_push($animalNames,$feature['properties']['name']);
    }
}




function get_path($start, $end) {
    global $graph, $dijkstra;
    $startCoords = getGeoFromName($start);
    $endCoords = getGeoFromName($end);
    $closestToStart = $graph->findClosestPoint($startCoords);
    $closestToEnd = $graph->findClosestPoint($endCoords);
    return $dijkstra->shortestPath($closestToStart, $closestToEnd);
}
