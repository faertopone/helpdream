window.addEventListener('DOMContentLoaded', function(){

    var delay = 4000; /* 4 секунды*/
    let URL = document.querySelector('a').getAttribute('href')


        setTimeout(function(){ window.location = URL; }, delay);


});