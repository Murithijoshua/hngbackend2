$(document).ready(function(){
    $('.sidenav').sidenav();
  });
  

//  // collapsable element
//   $(document).ready(function(){
//     $('.collapsible').collapsible();
//   });
$(document).ready(function(){
  $('.sidenav')
      .sidenav()
      .on('click tap', 'li a', () => {
          $('.sidenav').sidenav('close');
      });
});

$(document).on('click', 'a[href^="#"]', function (event) {
  event.preventDefault();

  $('html, body').animate({
      scrollTop: $($.attr(this, 'href')).offset().top
  }, 500);
});
  