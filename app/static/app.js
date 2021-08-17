$(document).ready(function(){

  // Initialize materialize data picker
  $('select').formSelect();

});
// for the side navigation
document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, options);
  });

  $(document).ready(function(){
    $('.sidenav').sidenav();
  });
  

 
