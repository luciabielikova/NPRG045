<!DOCTYPE html>
<html lang="sk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width">
    <link rel="stylesheet" href="styles.css">
    <title>Zoo</title>
    <script src="script.js"></script>
    <link rel="icon" href="favicon-16x16.png" type="image/png">
</head>
<body>
<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
include "header.php";

require_once 'languages.php';

$selectedLang = $_SESSION['language'];

$languages = getLanguages();

$translation = getTranslation($selectedLang);

?>

<form id="zoo-upload-form" class="zoo-form" action="" method="post" enctype="multipart/form-data">
    <label for="contact_person"><?= $translation['contact']?> (e-mail):</label>
    <input type="email" id="contact_person" name="contact_person" required><br><br>

    <div id="name-fields">
        <label><?= $translation['name_label']?></label><br>
        <div class="translation-group">
            <select name="name_lang[]">
                <option value="cs">Čeština</option>
                <option value="en">English</option>
                <option value="de">Deutsch</option>
            </select>
            <input type="text" name="name_text[]" placeholder="<?= $translation['placeholder_name']?>">
        </div>
    </div>
    <div class="button-wrapper2">
        <button type="button"  id="ff" onclick="addNameField()"><?= $translation['add_name']?></button>
    </div>

    <div id="desc-fields">
        <label><?= $translation['desc_label']?></label><br>
        <div class="translation-group">
            <select name="desc_lang[]">
                <option value="cs">Čeština</option>
                <option value="en">English</option>
                <option value="de">Deutsch</option>
            </select>
            <textarea name="desc_text[]" placeholder="<?= $translation['placeholder_desc']?>"></textarea>
        </div>
    </div>
    <div class="button-wrapper2">
        <button type="button" id="ff" onclick="addDescField()"><?= $translation['add_description']?></button>
    </div>

    <label for="country"><?= $translation['country']?></label>
        <input type="text" id="country" name="location[country]" required><br>
        <label for="city"><?= $translation['city']?></label>
        <input type="text" id="city" name="location[city]" required><br>
    <label for="zoo_name"><?= $translation['zooTitle']?></label>
    <input type="text" id="zoo_name" name="zoo_name" required><br><br>


    <label for="data_format"><?= $translation['dataFormat']?></label>
    <select id="data_format" name="data_format">
        <option value="csv">CSV</option>
        <option value="json">JSON</option>
    </select><br><br>

    <label for="continents"><?= $translation['addFile']?> continents (CSV/JSON):</label>
    <input type="file" id="continents" name="continents" accept=".csv,.json" required>

    <br><br>

    <label for="habitats"><?= $translation['addFile']?> habitats (CSV/JSON):</label>
    <input type="file" id="habitats" name="habitats" accept=".csv,.json" required>
    <br><br>

    <label for="classes"><?= $translation['addFile']?> classes (CSV/JSON):</label>
    <input type="file" id="classes" name="classes" accept=".csv,.json" required>

    <br><br>

    <label for="orders"><?= $translation['addFile']?> orders (CSV/JSON):</label>
    <input type="file" id="orders" name="orders" accept=".csv,.json" required>

    <br><br>

    <label for="animals"><?= $translation['addFile']?> animals (CSV/JSON):</label>
    <input type="file" id="animals" name="animals" accept=".csv,.json" required>

    <br><br>
    <label for="default_language"><?= $translation['preferredLanguage']?></label>
    <select id="default_language" name="default_language" required>
        <option value="en">English</option>
        <option value="cs">Čeština</option>
        <option value="de">Deutsch</option>
    </select><br><br>

    <div class="button-wrapper2">
        <button type="submit" id="ff"><?= $translation['submit']?></button>
    </div>

    <p style="text-align: center; margin-top: 30px; font-size: 0.95em; color: #555;">
        <?= $translation['contactInfo']?> <a href="mailto:lucia.bielikova836@student.cuni.cz">lucia.bielikova836@student.cuni.cz</a>.
    </p>

</form>
<?php
include 'footer.php';
?>
</body>
</html>


<script>

    function addNameField() {
        const div = document.createElement('div');
        div.className = 'translation-group';
        div.innerHTML = `
        <select name="name_lang[]">
            <option value="en">English</option>
            <option value="cs">Čeština</option>
            <option value="de">Deutsch</option>
        </select>
        <input type="text" name="name_text[]" placeholder="<?= $translation['placeholder_name']?>">
    `;
        document.getElementById('name-fields').appendChild(div);
    }

    function addDescField() {
        const div = document.createElement('div');
        div.className = 'translation-group';
        div.innerHTML = `
        <select name="desc_lang[]">
            <option value="en">English</option>
            <option value="cs">Čeština</option>
            <option value="de">Deutsch</option>
        </select>
        <textarea name="desc_text[]" placeholder="<?= $translation['placeholder_desc']?>"></textarea>
    `;
        document.getElementById('desc-fields').appendChild(div);
    }
</script>
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

