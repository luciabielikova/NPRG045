<?php
require_once 'db.php';

function getLanguages(){
    $data = loadTranslations();
    foreach ($data as $key => $value) {
        $languages[$key] = $value['lang'];
    }
    return $languages;
}

function getTranslation($language){
    $translations = loadTranslations();
    return $translations[$language];
}