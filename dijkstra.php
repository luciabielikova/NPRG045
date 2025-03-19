<?php

require_once 'db.php'; // Načíta potrebné súbory (napr. pripojenie k databáze)

class Graph {
    private $vertices = []; // Pole na uloženie vrcholov
    private $edges = []; // Pole na uloženie hrán

    // Pridanie nového vrcholu s jeho geografickými súradnicami
    public function addVertex($name, $longitude, $latitude) {
        $this->vertices[$name] = ['lon' => $longitude, 'lat' => $latitude];
    }

    // Pridanie hrany medzi dvoma vrcholmi s vzdialenosťou
    public function addEdge($start, $end, $distance) {
        $this->edges[$start][$end] = $distance; // Hrana zo start do end
        $this->edges[$end][$start] = $distance; // Hrana zo end do start (neorientovaná hrana)
    }

    // Získanie všetkých vrcholov grafu
    public function getVertices() {
        return $this->vertices;
    }

    // Získanie všetkých hrán grafu
    public function getEdges() {
        return $this->edges;
    }

    // Funkcia na nájdenie najbližšieho bodu v grafe na základe geografických súradníc
    public function findClosestPoint($wanted) {
        $closestPoint = null;
        $dist = PHP_INT_MAX; // Začneme s maximálnou možnou vzdialenosťou

        // Prechádzame všetky vrcholy grafu a hľadáme najbližší bod
        foreach ($this->vertices as $name => $point) {
            // Ak súradnice neodpovedajú požiadavkám, vypočíta vzdialenosť
            if ($wanted[0] != $point['lon'] && $wanted[1] != $point['lat']) {
                $temp_dist = euclideanDistance([$wanted[0], $wanted[1]], [$point['lon'], $point['lat']]);
                // Ak je nájdený bod bližšie, ulož ho
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
    private $graph; // Graf, pre ktorý sa bude počítať najkratšia cesta
    private $distances = []; // Vzdialenosti od počiatočného bodu k ostatným vrcholom
    private $previous = []; // Predchodcovia jednotlivých vrcholov pre rekonštrukciu cesty
    private $queue = []; // Fronta vrcholov na spracovanie
    private $notWanted = []; // Nežiaduce vrcholy, ktoré budeme obchádzať

    public function __construct($graph) {
        $this->graph = $graph; // Inicializácia grafu
    }

    // Nastavenie nežiaducich uzlov, ktoré sa nebudú zohľadňovať pri výpočte cesty
    public function setNotWantedNodes($nodes) {
        global $graph;

        $this->notWanted = [];

        foreach ($nodes as $node) {
            $coords = getCoordsFromName($node); // Získame súradnice uzla
            if (!empty($coords)) {
                // Nájdeme najbližší vrchol v grafe
                $closestPoint = $graph->findClosestPoint($coords);
                if ($closestPoint !== null) {
                    $this->notWanted[] = $closestPoint; // Uložíme nežiaduci vrchol
                }
            }
        }
    }

    // Algoritmus Dijkstra na hľadanie najkratšej cesty medzi dvoma vrcholmi
    public function shortestPath($start, $end) {
        $this->distances = [];
        $this->previous = [];
        $this->queue = [];
        $this->notWanted = [];

        // Inicializácia vzdialeností a predchodcov pre každý vrchol
        foreach ($this->graph->getVertices() as $vertex => $data) {
            if (in_array($vertex, $this->notWanted)) {
                continue; // Ak je uzol nežiaduci, preskočíme ho
            }
            if ($vertex === $start) {
                $this->distances[$vertex] = 0; // Počiatočná vzdialenosť je 0
            } else {
                $this->distances[$vertex] = INF; // Inak neexistujúca cesta
            }
            $this->previous[$vertex] = null; // Žiadny predchodca
            $this->queue[$vertex] = $this->distances[$vertex]; // Pridáme vrchol do fronty
        }

        // Hľadanie najkratšej cesty pomocou algoritmu Dijkstra
        while (!empty($this->queue)) {
            $u = array_search(min($this->queue), $this->queue); // Vyberieme vrchol s najnižšou vzdialenosťou
            if ($u === $end) {
                break; // Ak sme dosiahli cieľ, ukončíme
            }

            unset($this->queue[$u]); // Odstránime spracovaný vrchol

            if (!isset($this->graph->getEdges()[$u])) {
                continue;
            }

            // Pre každý susedný vrchol urobíme update vzdialenosti
            foreach ($this->graph->getEdges()[$u] as $neighbor => $distance) {
                if (in_array($neighbor, $this->notWanted)) {
                    continue; // Preskočíme nežiaduci sused
                }
                $alt = $this->distances[$u] + $distance;
                if ($alt < $this->distances[$neighbor]) {
                    $this->distances[$neighbor] = $alt; // Aktualizujeme vzdialenosť
                    $this->previous[$neighbor] = $u; // Uložíme predchodcu
                    $this->queue[$neighbor] = $alt; // Pridáme suseda do fronty
                }
            }
        }

        // Rekonštrukcia najkratšej cesty
        $path = [];
        $u = $end;
        while (isset($this->previous[$u])) {
            array_unshift($path, $u); // Pridáme uzol do cesty
            $u = $this->previous[$u]; // Prejdeme na predchodcu
        }

        if (!empty($path)) {
            array_unshift($path, $start); // Pridáme počiatočný bod na začiatok cesty
        }

        // Preloženie vrcholov na geografické súradnice
        $pathWithCoordinates = [];
        foreach ($path as $vertex) {
            $data = $this->graph->getVertices()[$vertex];
            $pathWithCoordinates[] = [
                'vertex' => $vertex,
                'lon' => $data['lon'],
                'lat' => $data['lat'],
            ];
        }

        return $pathWithCoordinates; // Vrátime cestu s geografickými súradnicami
    }
}

// Euklidovská vzdialenosť medzi dvoma bodmi
function euclideanDistance($point1, $point2) {
    return sqrt(pow($point1[0] - $point2[0], 2) + pow($point1[1] - $point2[1], 2));
}

// Získanie geografických súradníc pre názov bodu
function getCoordsFromName($name){
    global $animals;
    foreach ($animals['features'] as $feature) {
        if ($name == $feature['properties']['name']){
            return $feature['geometry']['coordinates']; // Vráti súradnice
        }
    }
    return ""; // Ak neexistujú, vráti prázdny reťazec
}

// Načítanie GeoJSON dát zo súboru
$highwaysFile = loadHighways();
$highways = json_decode($highwaysFile, true);

// Vytvorenie grafu z údajov GeoJSON
function createGraph() {
    global $highways;
    $graph = new Graph();
    $counter = 1;

    // Pridáme všetky vrcholy do grafu
    foreach ($highways['features'] as $feature) {
        if ($feature['geometry']['type'] === 'LineString') {
            $coordinates = $feature['geometry']['coordinates'];
            foreach($coordinates as $point){
                $graph->addVertex($counter, $point[0], $point[1]);
                $counter += 1;
            }
        }
    }

    // Pridáme všetky hrany medzi vrcholmi
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

// Vytvárame graf z údajov o diaľniciach
$graph = createGraph();

// Iniciujeme algoritmus Dijkstra
$dijkstra = new Dijkstra($graph);

// Načítame údaje o zvieratách
$animalsFile = loadAnimalsGeojson();
$animals = json_decode($animalsFile, true);

$animalNames = [];
// Prechádzame všetky zvieratá a vytvárame zoznam ich názvov
foreach ($animals['features'] as $feature) {
    if ($feature['properties']['name'] != null) {
        array_push($animalNames, $feature['properties']['name']);
    }
}

/* Funkcia na získanie cesty medzi dvoma bodmi s možnosťou prechádzania cez povinné a nežiadúce uzly */
function get_path($start, $end, $wantedNodes = [], $notWantedNodes = []) {
    global $graph, $dijkstra;

    // Získanie súradníc pre počiatočný a koncový bod
    $startCoords = getCoordsFromName($start);
    $endCoords = getCoordsFromName($end);

    if (!$startCoords || !$endCoords) {
        return []; // Ak neexistujú súradnice, vráti prázdnu cestu
    }

    // Nájdeme najbližšie body k startu a endu
    $closestToStart = $graph->findClosestPoint($startCoords);
    $closestToEnd = $graph->findClosestPoint($endCoords);

    // Ak sú zadané nežiadúce uzly, nastavíme ich
    if ($notWantedNodes && is_array($notWantedNodes)) {
        $dijkstra->setNotWantedNodes($notWantedNodes);
    }

    // Mapujeme názvy uzlov na konkrétne vrcholy v grafe
    $nameMapping = [
        $closestToStart => $start,
        $closestToEnd => $end
    ];

    $waypointNodes = [];
    // Ak sú zadané povinné uzly, pridáme ich do mapovania
    if (!empty($wantedNodes) && is_array($wantedNodes)) {
        foreach ($wantedNodes as $waypoint) {
            $waypointCoords = getCoordsFromName($waypoint);
            if (!$waypointCoords) continue;
            $closestWaypoint = $graph->findClosestPoint($waypointCoords);
            $nameMapping[$closestWaypoint] = $waypoint;
            $waypointNodes[] = $closestWaypoint;
        }
    }

    // Generujeme permutácie pre povinné uzly a počítame najkratšiu cestu
    $nodePermutations = permute($waypointNodes);
    $shortestPath = null;
    $minDistance = INF;

    // Prechadzame vsetky permutacie povinnych bodov
    foreach ($nodePermutations as $perm) {
        $currentStart = $closestToStart;
        $fullPath = [];
        $totalDistance = 0;

        // Vytvorenie celej trasy s pevne danymi startom a koncom
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

        // Pridanie posledneho segmentu do ciela
        $finalSegment = $dijkstra->shortestPath($currentStart, $closestToEnd);
        if (empty($finalSegment)) {
            continue;
        }
        $finalSegmentDistance = array_sum(array_column($finalSegment, 'distance') ?? []);
        $totalDistance += $finalSegmentDistance;
        $fullPath = array_merge($fullPath, $finalSegment);

        // Aktualizacia najkratsej cesty, ak je lepsia
        if ($totalDistance < $minDistance) {
            $minDistance = $totalDistance;
            $shortestPath = $fullPath;
        }
    }

    // Prelozenie nazvov uzlov spat na povodne
    foreach ($shortestPath as &$point) {
        if (isset($nameMapping[$point['vertex']])) {
            $point['vertex'] = $nameMapping[$point['vertex']];
        }
    }

    return $shortestPath;
}






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


