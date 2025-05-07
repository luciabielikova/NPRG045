<?php

require_once 'db.php';

// Trieda reprezentujúca graf
class Graph {
    private $vertices = [];
    private $edges = [];

    //pridanie vrcholu do grafu
    public function addVertex($name, $longitude, $latitude) {
        $this->vertices[$name] = ['lon' => $longitude, 'lat' => $latitude];
    }

    // Pridanie hrany do grafu
    public function addEdge($start, $end, $distance) {
        $this->edges[$start][$end] = $distance;
        $this->edges[$end][$start] = $distance;
    }
    // Získanie zoznamu vrcholov
    public function getVertices() {
        return $this->vertices;
    }
    // Získanie zoznamu hrán
    public function getEdges() {
        return $this->edges;
    }
    // Nájde najbližší vrchol v grafe k daným súradniciam
    public function findClosestPoint($wanted) {
        $closestPoint = null;
        $dist = PHP_INT_MAX;

        foreach ($this->vertices as $name => $point) {
            if ($wanted[0] != $point['lon'] && $wanted[1] != $point['lat']) {
                $temp_dist = euclideanDistance([$wanted[0], $wanted[1]], [$point['lon'], $point['lat']]);
                if ($temp_dist < $dist) {
                    $dist = $temp_dist;
                    $closestPoint = $name;
                }
            }
        }

        return $closestPoint;
    }
}

// Implementácia Dijkstrovho algoritmu
class Dijkstra {
    private $graph;
    private $distances = [];
    private $previous = [];
    private $queue = [];
    private $notWanted = [];

    public function __construct($graph) {
        $this->graph = $graph;
    }

    // Nájde najkratšiu cestu medzi dvoma bodmi
    public function shortestPath($start, $end) {
        if (in_array($start, $this->notWanted) || in_array($end, $this->notWanted)) {
            return [];
        }

        $this->distances = [];
        $this->previous = [];
        $this->queue = [];

        // Inicializácia vzdialeností a fronty
        foreach ($this->graph->getVertices() as $vertex => $data) {
            if (in_array($vertex, $this->notWanted)) {
                continue;
            }
            $this->distances[$vertex] = ($vertex === $start) ? 0 : INF;
            $this->previous[$vertex] = null;
            $this->queue[$vertex] = $this->distances[$vertex];
        }
        // Hlavný cyklus algoritmu
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
                if (in_array($neighbor, $this->notWanted)) {
                    continue;
                }
                $alt = $this->distances[$u] + $distance;
                if ($alt < $this->distances[$neighbor]) {
                    $this->distances[$neighbor] = $alt;
                    $this->previous[$neighbor] = $u;
                    $this->queue[$neighbor] = $alt;
                }
            }
        }
        // Rekonštrukcia cesty
        $path = [];
        $u = $end;
        while (isset($this->previous[$u])) {
            array_unshift($path, $u);
            $u = $this->previous[$u];
        }

        if (!empty($path)) {
            array_unshift($path, $start);
        }
        // Pridanie súradníc k ceste
        $pathWithCoordinates = [];
        $lastPoint = null;
        foreach ($path as $vertex) {
            $data = $this->graph->getVertices()[$vertex];
            $point = [
                'vertex' => $vertex,
                'lon' => $data['lon'],
                'lat' => $data['lat'],
            ];
            if ($lastPoint !== null) {
                $point['distance'] = euclideanDistance([$lastPoint['lon'], $lastPoint['lat']], [$point['lon'], $point['lat']]);
            } else {
                $point['distance'] = 0;
            }
            $lastPoint = $point;
            $pathWithCoordinates[] = $point;
        }

        return $pathWithCoordinates;
    }
    // Nastavenie zakázaných uzlov podľa názvu zvieraťa
    function setNotWantedNodes($nodes) {
        global $graph;

        $this->notWanted = [];

        foreach ($nodes as $node) {
            $coords = getCoordsFromName($node);
            if (!empty($coords)) {
                foreach ($coords as $coord){
                    $closestPoint = $graph->findClosestPoint($coord);
                    //echo $node; var_dump($closestPoint);
                    if ($closestPoint !== null) {
                        $this->notWanted[] = $closestPoint;
                    }}
            }
        }
    }
}

// Výpočet euklidovskej vzdialenosti medzi dvoma bodmi
function euclideanDistance($point1, $point2) {
    return sqrt(pow($point1[0] - $point2[0], 2) + pow($point1[1] - $point2[1], 2));
}

// Načítanie dát a vytvorenie grafu zo súboru ciest (napr. cestičky v ZOO)
$highwaysFile = loadHighways($_SESSION['zooID']);
$highways = json_decode($highwaysFile, true);

// Vytvára a inicializuje graf na základe dát z GeoJSON
function createGraph() {
    global $highways;
    $graph = new Graph();
    $counter = 1;
    // Pridanie všetkých bodov ako vrcholov
    foreach ($highways['features'] as $feature) {
        if ($feature['geometry']['type'] === 'LineString') {
            $coordinates = $feature['geometry']['coordinates'];
            foreach($coordinates as $point){
                $graph->addVertex($counter, $point[0], $point[1]);
                $counter += 1;
            }
        }
    }
    // Pridanie hrán medzi po sebe idúcimi bodmi
    foreach ($highways['features'] as $feature) {
        if ($feature['geometry']['type'] === 'LineString') {
            $coordinates = $feature['geometry']['coordinates'];
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
                    $distance = round(euclideanDistance($previousCoords, $currentCoords) * 100000);
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

// Získanie prvej súradnice daného zvieraťa
function getFirstCoordinateFromName($name){
    $animal = getAnimalByNameAndLanguage($name, $_SESSION['language'], $_SESSION['zooID']);
    if (isset($animal['coords'])) {
        return $animal['coords'][0];
    }
    else {
        return [];
    }
}

// Získanie všetkých súradníc daného zvieraťa
function getCoordsFromName($name){
    $animal = getAnimalByNameAndLanguage($name, $_SESSION['language'], $_SESSION['zooID']);
    if (isset($animal['coords'])) {
        return $animal['coords'];
    }
    else {
        return [];
    }
}

// Získanie optimalizovanej cesty medzi dvoma bodmi s možnosťou prechodu cez niektoré body a vynechania iných
function get_path($start, $end, $wantedNodes = [], $notWantedNodes = []) {
    global $graph, $dijkstra;

    $startCoords = getFirstCoordinateFromName($start);
    $endCoords = getFirstCoordinateFromName($end);

    if (!$startCoords || !$endCoords) {
        return [];
    }

    $closestToStart = $graph->findClosestPoint($startCoords);
    $closestToEnd = $graph->findClosestPoint($endCoords);



    if ($notWantedNodes && is_array($notWantedNodes)) {
        $dijkstra->setNotWantedNodes($notWantedNodes);
    }

    // Mapa premenovania vrcholov na zmysluplné mená
    $nameMapping = [
        $closestToStart => $start,
        $closestToEnd => $end
    ];

    $waypointNodes = [];
    if (!empty($wantedNodes) && is_array($wantedNodes)) {
        foreach ($wantedNodes as $waypoint) {
            $waypointCoords = getFirstCoordinateFromName($waypoint);
            if (!$waypointCoords) continue;
            $closestWaypoint = $graph->findClosestPoint($waypointCoords);
            $nameMapping[$closestWaypoint] = $waypoint;
            $waypointNodes[] = $closestWaypoint;
        }
    }
    // Permutácie medzibodov pre nájdenie najkratšej možnej trasy
    $nodePermutations = permute($waypointNodes);
    $shortestPath = null;
    $minDistance = INF;

    foreach ($nodePermutations as $perm) {
        $currentStart = $closestToStart;
        $fullPath = [];
        $totalDistance = 0;

        foreach ($perm as $nextNode) {
            $segment = $dijkstra->shortestPath($currentStart, $nextNode);
            if (empty($segment)) {
                continue 2;
            }

            $segmentDistance = array_sum(array_column($segment, 'distance') ?? []);
            $totalDistance += $segmentDistance;
            array_pop($segment);
            $fullPath = array_merge($fullPath, $segment);
            $currentStart = $nextNode;
        }

        $finalSegment = $dijkstra->shortestPath($currentStart, $closestToEnd);
        if (empty($finalSegment)) {
            continue;
        }
        // Finálny segment do cieľa
        $finalSegmentDistance = array_sum(array_column($finalSegment, 'distance') ?? []);
        $totalDistance += $finalSegmentDistance;
        $fullPath = array_merge($fullPath, $finalSegment);

        // Aktualizácia najkratšej cesty
        if ($totalDistance < $minDistance) {
            $minDistance = $totalDistance;
            $shortestPath = $fullPath;
        }
    }
    // Nahradenie ID vrcholov späť na názvy
    foreach ($shortestPath as &$point) {
        if (isset($nameMapping[$point['vertex']])) {
            $point['vertex'] = $nameMapping[$point['vertex']];
        }
    }
    return $shortestPath;
}

// Pomocná funkcia na generovanie všetkých permutácií
function permute($items, $perms = []) {
    if (empty($items)) {
        return [$perms];
    }
    $result = [];
    foreach ($items as $key => $item) {
        $newItems = $items;
        unset($newItems[$key]);
        $result = array_merge($result, permute(array_values($newItems), array_merge($perms, [$item])));
    }
    return $result;
}



