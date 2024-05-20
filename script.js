
function uncheckAll() {
    var checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(function(checkbox) {
        checkbox.checked = false;
    });
}




function uncheck(selector ) {
    var checkboxes = document.querySelectorAll(selector);
    checkboxes.forEach(function(checkbox) {
        checkbox.checked = false;
    });
}
function clearSearch(){
    return document.getElementById("search").value = "";
}

function clearAll() {
    uncheckAll(); clearSearch();
}