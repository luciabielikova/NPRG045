<?php
require_once 'db.php';
// Funkcia, ktorá vráti zoznam dostupných jazykov
function getLanguages(){
    $data = loadTranslations();
    foreach ($data as $key => $value) {
        $languages[$key] = $value['lang'];
    }
    return $languages;
}

// Funkcia, ktorá vráti všetky preklady pre daný jazyk
function getTranslation($language){
    $translations = loadTranslations();
    if (array_key_exists($language, $translations)) {
        return $translations[$language];
    } else {
        $_SESSION['language'] = 'en';
        return $translations['en'];
    }
}
