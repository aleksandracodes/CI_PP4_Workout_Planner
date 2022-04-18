// Automatically dismiss messages

setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2000);


// Dropdown exercises filters
$(document).ready(function(){
    $(".show-filters-small").hide();
    $(".expand").click(function(){
        $(this).parent().next().slideToggle(600);
    
    });
});
