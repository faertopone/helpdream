window.addEventListener('DOMContentLoaded', function(){

  let selector = document.querySelectorAll('input[type="tel"]');
  let im = new Inputmask('89999999999')

  im.mask(selector);


  //
  // let validateForms = function (selector, rules, succesModal, YaGoal) {
  //   new window.JustValidate(selector, {
  //     rules: rules,
  //
  //   });
  // }
  //
  // validateForms('.register_form',
  //     {
  //       email:
  //           {required: true, email: true},
  //       tel: {required: true}
  //     }, '.thanks-popup', 'send goal'
  //     )



  const swiper = new Swiper('.swiper', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,

    effect: 'coverflow',

    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },

    autoplay: {
      delay: 5000,
    },
  });


});


