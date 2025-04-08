<?php

function validate_csv($filepath, $expected_headers) {
    if (($handle = fopen($filepath, "r")) !== false) {
        $headers = fgetcsv($handle);
        fclose($handle);
        return $headers === $expected_headers;
    }
    return false;
}





function validate_json_simple($filepath, $expected_keys) {
    $data = json_decode(file_get_contents($filepath), true);
    if (!is_array($data)) return false;
    foreach ($data as $item) {
        if (!is_array($item)) return false;
        foreach ($expected_keys as $key) {
            if (!array_key_exists($key, $item)) {
                return false;
            }
        }
    }
    return true;
}

function validate_json_with_translations($filepath, $required_langs = ["cs", "en", "de"], $extra_required_keys = []) {
    $data = json_decode(file_get_contents($filepath), true);
    if (!is_array($data)) return false;

    foreach ($data as $item) {
        if (!isset($item['id']) || !is_int($item['id'])) return false;

        foreach ($extra_required_keys as $key) {
            if (!isset($item[$key])) return false;
        }

        if (!isset($item['translations']) || !is_array($item['translations'])) return false;

        foreach ($required_langs as $lang) {
            if (!isset($item['translations'][$lang])) return false;
            $t = $item['translations'][$lang];
            if (!isset($t['name']) || !isset($t['description'])) return false;
        }
    }

    return true;
}


if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $city = $_POST['city'] ?? '';
    $contact_person = $_POST['contact_person'] ?? '';
    $data_format = $_POST['data_format'] ?? '';
    $default_language = $_POST['default_language'] ?? 'en';
    $name = $_POST['name'] ?? [];
    $description = $_POST['description'] ?? [];
    $location = $_POST['location'] ?? [];
    $zoo_metadata = [
        "default_language" => $default_language,
        "name" => $name,
        "description" => $description,
        "location" => $location
    ];

    file_put_contents("uploads/zoo_info.json", json_encode($zoo_metadata, JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE));

    $upload_dir = "uploads/" . $city . "/";
    if (!is_dir($upload_dir)) {
        mkdir($upload_dir, 0777, true);
    }

    $errors = [];

    $schemas = [
        "continents" => [
            "csv" => ["id", "lang", "name", "description"],
            "json_translated" => true
        ],
        "habitats" => [
            "csv" => ["id", "lang", "name", "description"],
            "json_translated" => true
        ],
        "classes" => [
            "csv" => ["id", "lang", "name", "description"],
            "json_translated" => true
        ],

        "orders" => [
            "csv" => ["id", "class_id", "lang", "name", "description"],
            "json_translated" => true,
            "required_keys" => ["id", "class_id"]
        ],
        "animals" => [
            "csv" => ["lang", "id", "latin_name", "image_src", "class_id", "order_id", "habitats", "continents", "localities_url", "name", "description", "spread_note", "food", "food_note", "proportions", "reproduction", "attractions", "projects_note", "breeding", "localities_title"],
            "json" => ["id", "order_id", "name", "description"]
        ]
    ];

    foreach ($schemas as $file_key => $structure) {
        if (isset($_FILES[$file_key]) && $_FILES[$file_key]['error'] == 0) {

            $file_tmp = $_FILES[$file_key]['tmp_name'];
            $file_name = basename($_FILES[$file_key]['name']);
            $target_file = $upload_dir . $file_name;

            $valid = false;

            if ($data_format === "csv") {
               $valid = isset($structure["csv"]) ? validate_csv($file_tmp, $structure["csv"]) : false;
            } elseif ($data_format === "json") {
                if (!empty($structure["json_translated"])) {
                    $extra_keys = $structure["required_keys"] ?? [];
                    $valid = validate_json_with_translations($file_tmp, ["cs", "en", "de"], $extra_keys);
                } elseif (isset($structure["json"])) {
                    $valid = validate_json_simple($file_tmp, $structure["json"]);
                }
            }

            if ($valid) {
                move_uploaded_file($file_tmp, $target_file); // <== až po validácii
            } else {
                $errors[] = "Súbor '$file_name' nemá správnu štruktúru pre formát $data_format.";
            }
        } else {
            $errors[] = "Súbor '$file_key' nebol úspešne nahraný.";
        }
    }


    if (empty($errors)) {
        echo "<p>Formulár bol úspešne odoslaný a všetky súbory boli validované!</p>";
    } else {
        echo "<p>Chyby pri validácii súborov:</p><ul><li>" . implode("</li><li>", $errors) . "</li></ul>";
    }
}
?>


<!DOCTYPE html>
<html lang="sk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload dát ZOO</title>
    <style>
        .tooltip {
            display: inline-block;
            position: relative;
            cursor: pointer;
        }
        .tooltip .tooltip-text {
            visibility: hidden;
            width: 250px;
            background-color: #333;
            color: #fff;
            text-align: center;
            border-radius: 5px;
            padding: 5px;
            position: absolute;
            z-index: 1;
            bottom: 100%;
            left: 50%;
            transform: translateX(-50%);
            opacity: 0;
            transition: opacity 0.3s;
        }
        .tooltip:hover .tooltip-text {
            visibility: visible;
            opacity: 1;
        }
    </style>
</head>
<body>
<form action="" method="post" enctype="multipart/form-data">
    <label for="contact_person">Kontaktná osoba (e-mail):</label>
    <input type="email" id="contact_person" name="contact_person" required><br><br>

    <!-- Názvy ZOO -->
        <legend>Názov ZOO</legend>
        <label>CS:</label> <input type="text" name="name[cs]" required><br>
        <label>EN:</label> <input type="text" name="name[en]" required><br>
        <label>DE:</label> <input type="text" name="name[de]" required><br>

        <legend>Popis ZOO</legend>
        <label>CS:</label> <textarea name="description[cs]"></textarea><br>
        <label>EN:</label> <textarea name="description[en]"></textarea><br>
        <label>DE:</label> <textarea name="description[de]"></textarea><br>

        <label for="country">Krajina:</label>
        <input type="text" id="country" name="location[country]" required><br>
        <label for="city">Mesto:</label>
        <input type="text" id="city" name="location[city]" required><br>
    <label for="zoo_name">Názov ZOO:</label>
    <input type="text" id="zoo_name" name="zoo_name" required><br><br>


    <label for="data_format">Formát dát:</label>
    <select id="data_format" name="data_format">
        <option value="csv">CSV</option>
        <option value="json">JSON</option>
    </select><br><br>

    <label for="continents">Nahrať súbor continents (CSV/JSON):</label>
    <input type="file" id="continents" name="continents" accept=".csv,.json" required>
    <span class="tooltip">❓
            <span class="tooltip-text">Pre CSV: id,lang,name,description\nPre JSON: [{"id":1, "lang":"sk", "name":"Európa", "description":"Kontinent"}]</span>
        </span>
    <br><br>

    <label for="habitats">Nahrať súbor habitats (CSV/JSON):</label>
    <input type="file" id="habitats" name="habitats" accept=".csv,.json" required>
    <span class="tooltip">❓
            <span class="tooltip-text">Pre CSV: id,habitat_id,name,description\nPre JSON: [{"id":1, "habitat_id":1, "name":"Les", "description":"Zelený habitat"}]</span>
        </span>
    <br><br>

    <label for="classes">Nahrať súbor classes (CSV/JSON):</label>
    <input type="file" id="classes" name="classes" accept=".csv,.json" required>
    <span class="tooltip">❓
            <span class="tooltip-text">Pre CSV: id,class_id,name,description\nPre JSON: [{"id":1, "class_id":1, "name":"Les", "description":"Zelený habitat"}]</span>
        </span>
    <br><br>

    <label for="orders">Nahrať súbor orders (CSV/JSON):</label>
    <input type="file" id="orders" name="orders" accept=".csv,.json" required>
    <span class="tooltip">❓
            <span class="tooltip-text">Pre CSV: id,order_id,name,description\nPre JSON: [{"id":1, "order_id":1, "name":"Les", "description":"Zelený order"}]</span>
        </span>
    <br><br>

    <label for="animals">Nahrať súbor animals (CSV/JSON):</label>
    <input type="file" id="animals" name="animals" accept=".csv,.json" required>
    <span class="tooltip">❓
            <span class="tooltip-text">Pre CSV: "zoo","lang","id","latin_name","image_src","class_id","order_id","habitats","continents","localities_url","name","description","spread_note","food","food_note","proportions","reproduction","attractions","projects_note","breeding","localities_title"\nPre JSON: [{"id":1, "order_id":1, "name":"Les", "description":"Zelený order"}]</span>
        </span>
    <br><br>
    <label for="default_language">Predvolený jazyk:</label>
    <select id="default_language" name="default_language" required>
        <option value="cs">Čeština</option>
        <option value="en">English</option>
        <option value="de">Deutsch</option>
    </select><br><br>


    <button type="submit">Odoslať</button>
</form>
</body>
</html>


