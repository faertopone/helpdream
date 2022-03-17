window.addEventListener('DOMContentLoaded', function(){


  let selector = document.querySelectorAll('input[type="tel"]');

  let im = new Inputmask('+7 (999) 999-99-99')
  im.mask(selector);


  let forms = document.querySelector('.launge-form')

    forms.addEventListener('change', function (){
                  forms.submit()
  })



});


