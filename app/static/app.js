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
  