window.addEventListener('DOMContentLoaded', function(){


  let selector = document.querySelectorAll('input[type="tel"]');

  let im = new Inputmask('+7 (999) 999-99-99')
  im.mask(selector);

  // Изменения языка
  let forms = document.querySelector('.launge-form')
    if (forms){
         forms.addEventListener('change', function (){
                  forms.submit()
            })
         }


   // модальное окно пополнения баланса
   const input_balance = document.querySelector('.form__balance_up .auth-input');
    if (input_balance) {
            input_balance.addEventListener('keydown', function (event) {
                // Разрешаем: backspace, delete, tab и escape
                if (event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 || event.keyCode == 27 ||
                    // Разрешаем: Ctrl+A
                    (event.keyCode == 65 && event.ctrlKey === true) ||
                    // Разрешаем: home, end, влево, вправо
                    (event.keyCode >= 35 && event.keyCode <= 39)) {

                    // Ничего не делаем
                    return;
                } else {
                            // Запрещаем все, кроме цифр на основной клавиатуре, а так же Num-клавиатуре
                            if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105)) {
                                event.preventDefault();
                            }
                }
            });
    }

    const id_amount = document.querySelector('#id_amount')

        if (id_amount) {
            id_amount.addEventListener('keydown', function (event) {
                // Разрешаем: backspace, delete, tab и escape
                if (event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 || event.keyCode == 27 ||
                    // Разрешаем: Ctrl+A
                    (event.keyCode == 65 && event.ctrlKey === true) ||
                    // Разрешаем: home, end, влево, вправо
                    (event.keyCode >= 35 && event.keyCode <= 39)) {

                    // Ничего не делаем
                    return;
                } else {
                            // Запрещаем все, кроме цифр на основной клавиатуре, а так же Num-клавиатуре
                            if ((event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105)) {
                                event.preventDefault();
                            }
                }
            });
    }

        // Модальное окно пополнения баланса в личном кабинете
          const balance_up_wrap = document.querySelector('.balance_up_wrapp')
          const modal_balance_up = document.querySelector('#modal_balance_up')
          const closed_modal_lk = document.querySelector('#model-closed_balance_up_lk')

          const dop_info_up_wrapp = document.querySelector('.dop_info_up_wrapp')
          const closed_dop_info = document.querySelector('#model-closed_dop_info')
          const button_dop_info_user_link = document.querySelector('#button_dop_info_user_link')



          if (modal_balance_up) {

              //скрипт управления пополеннеим баланса модальное
              modal_balance_up.addEventListener('click', function () {
                  if (dop_info_up_wrapp){
                     dop_info_up_wrapp.classList.remove('dop_info_up_wrapp--active')
                  }

                  modal_balance_up.classList.toggle('modal_balance_up--active')
                  // modal_balance_up.innerHTML = "Закрыть"
                  balance_up_wrap.classList.toggle('balance_up_wrapp--active')
              })

              closed_modal_lk.addEventListener('click', function () {

                  modal_balance_up.classList.toggle('modal_balance_up--active')
                  balance_up_wrap.classList.toggle('balance_up_wrapp--active')
              })

              //скрипт управления дополнением информации
                if (button_dop_info_user_link) {
                    button_dop_info_user_link.addEventListener('click', function()  {
                  modal_balance_up.classList.remove('modal_balance_up--active')
                  balance_up_wrap.classList.remove('balance_up_wrapp--active')
                  button_dop_info_user_link.classList.toggle('dop_info_user_link--active')
                  dop_info_up_wrapp.classList.toggle('dop_info_up_wrapp--active')

              })

              closed_dop_info.addEventListener('click', function () {
                  button_dop_info_user_link.classList.toggle('dop_info_user_link--active')
                  dop_info_up_wrapp.classList.toggle('dop_info_up_wrapp--active')
              })

                }



          }




    // Логика при редактировании мечтв  личном кабинете, отмена- поднять наверх, активирвоать
    btn_active = document.querySelectorAll('.btn_active')
    btn_cancel = document.querySelectorAll('.btn_cancel')
    btn_push_up = document.querySelectorAll('.btn_push_up')
    btn_delete = document.querySelectorAll('.btn_delete')

    //Если на странице есть эти кнопки что б js срабатывал (не хотел отедльно делать на эту страницу)
    if (btn_active){

        // Если нажать Активировать
        btn_active.forEach((el) => {

            el.addEventListener('click', function (e) {

                // Все инпуты делаю true
                document.querySelectorAll('#id_active').forEach((el) => {
                    el.value = true;
                })
                // инпут поднять на верх списка
                document.querySelectorAll('#id_push_up').forEach((el) => {
                    el.value = false;
                })
                // инпут отменить
                document.querySelectorAll('#id_cancel').forEach((el) => {
                    el.value = false;
                })

               // инпут удалить
                document.querySelectorAll('#id_delete').forEach((el) => {
                    el.value = false;
                })
            })
        })
         // Если нажать ПОДНЯТЬ НА ВЕРХ
         btn_push_up.forEach((el) => {

             el.addEventListener('click', function (e) {

                 // Все инпуты делаю true
                 document.querySelectorAll('#id_active').forEach((el) => {
                     el.value = false;
                 })
                 // инпут поднять на верх списка
                 document.querySelectorAll('#id_push_up').forEach((el) => {
                     el.value = true;
                 })
                 // инпут отменить
                 document.querySelectorAll('#id_cancel').forEach((el) => {
                     el.value = false;
                 })

                // инпут удалить
                document.querySelectorAll('#id_delete').forEach((el) => {
                    el.value = false;
                })
             })
         })
         // Если нажать ОТМЕНИТЬ
         btn_cancel.forEach((el) => {

                el.addEventListener('click', function (e)  {

                    // Все инпуты делаю true
                    document.querySelectorAll('#id_active').forEach((el) => {
                        el.value = false;
                    })
                     // инпут поднять на верх списка
                    document.querySelectorAll('#id_push_up').forEach((el) => {
                        el.value = false;
                    })
                    // инпут отменить
                    document.querySelectorAll('#id_cancel').forEach((el) => {
                        el.value = true;
                    })

                       // инпут удалить
                    document.querySelectorAll('#id_delete').forEach((el) => {
                        el.value = false;
                    })
                })
         })

        // Если нажать УДАЛИТЬ
         btn_delete.forEach((el) => {

                el.addEventListener('click', function (e)  {

                    // Все инпуты делаю true
                    document.querySelectorAll('#id_active').forEach((el) => {
                        el.value = false;
                    })
                     // инпут поднять на верх списка
                    document.querySelectorAll('#id_push_up').forEach((el) => {
                        el.value = false;
                    })
                    // инпут отменить
                    document.querySelectorAll('#id_cancel').forEach((el) => {
                        el.value = false;
                    })

                   // инпут удалить
                    document.querySelectorAll('#id_delete').forEach((el) => {
                    el.value = true;
                    })
                })
         })




      // Будем ограничивать максимальное значение
     id_price = document.querySelector('#id_price')

    function allowNumbersOnly(e) {
          var code = (e.which) ? e.which : e.keyCode;
          if (code > 31 && (code < 48 || code > 57)) {
              e.preventDefault();
          }
        }
        // Если есть такой вход
       if (id_price){
            id_price.addEventListener('keypress', (e) => {
              allowNumbersOnly(e);
            });

            let max_price = id_price.dataset.price
                id_price.addEventListener('change', function (){
                   if (Number(id_price.value) > Number(max_price)) {
                    id_price.value = max_price
                    }
                })

               id_price.addEventListener('keyup', function (){
                     if (Number(id_price.value) > Number(max_price)) {
                        id_price.value = max_price
                        }
                    })

        }


    }

    // SWIPER
      const slider1 = document.querySelector('.swiper');
     const swiper = new Swiper(slider1, {
    // Optional parameters
    direction: 'horizontal',
    loop: true,

    effect: 'coverflow',

    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
  // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },

    autoplay: {
      delay: 5000,
    },
  });

      // тултипы
    // With the above scripts loaded, you can call `tippy()` with a CSS
      // selector and a `content` prop:
      tippy('.js-tooltip-right', {
        maxWidth: 265,
        theme: 'style_tooltip',
        delay: [100, 300],
        placement: 'right',
      });

      tippy('.js-tooltip', {
        maxWidth: 265,
        theme: 'style_tooltip',
        delay: [100, 300],
        placement: 'top',
      });

       tippy('.js-tooltip--logout', {
        maxWidth: 265,
        theme: 'style_tooltip--logout',
        delay: [100, 300],
        placement: 'right',
      });






    const all_human_review = document.querySelectorAll('.human_review')
    let  windonw_width_x = document.querySelector('.reviews_block ')

    if (windonw_width_x) {
        const windonw_width = windonw_width_x.clientWidth


        if (all_human_review){
                    //Эта хрень при повторным клике убирает иконку обратно в загон)
                    all_human_review.forEach((one) => {
                        let pos_human_item = one.offsetLeft;
                        //150px block

                        new_coordinat_x = (windonw_width / 2) - 150;


                            one.addEventListener('click', function (event) {
                                let human_itemHeight_cur = event.currentTarget.offsetTop;
                                let human_itemHeight = human_itemHeight_cur - 150
                                      if (one.classList.contains('human_review--active'))
                            {
                                one.classList.remove('human_review--active')
                                one.style.transform = null;
                                one.style.position = 'unset';
                            } else {
                                    all_human_review.forEach((e) => {
                                       e.classList.remove('human_review--active')
                                        e.style.transform = null;
                                        e.style.position = 'unset';
                                    })

                                    console.log(human_itemHeight)
                                 one.classList.add('human_review--active')
                                 one.style.position = 'absolute'
                                 one.style.transform = `translate(${new_coordinat_x}px, ${human_itemHeight}px)`
                            }

                            })
                    })
        }
    }

    const header = document.querySelector('.header')
    //Вычислет высоту блока хедер
    if (header){
        const headerHeight = header.offsetHeight;

            window.addEventListener('scroll', () => {
                let scrollDistance = window.scrollY

                if (scrollDistance === 0) {
                    header.style.top = null;
                    header.style.position = 'relative';
                } else if ((scrollDistance) >= headerHeight) {
                    header.style.position = 'fixed';
                    header.style.top = '-31px';
                }
            });

            //функция прокрутки наверх старницы
            $(function() {
              // при нажатии на кнопку scrollup
              $('#topNubex').click(function() {
                // переместиться в верхнюю часть страницы
                $("html, body").animate({
                  scrollTop:0
                },300);
              })
            })
    }





    // Валидатор для того кто хочет помочь - ограничиваем максимальное значение

    const max_price_user = document.querySelector('#id_amount')

        if (max_price_user && document.querySelector('.popolnenie__form')){
                 let max_price_value = Number(max_price_user.dataset.maxprice)
            // Текущее значение
            // Валидцаия на странице detaildream - максимальное чилсо ограничено
                  new JustValidate('.popolnenie__form', {
                    rules:
                        {price:
                            {required: true,
                                 function: () => {
                                    return (max_price_value >= Number(max_price_user.value)) && (Number(max_price_user.value) > 0 )
                                 }
                            }

                        },

                    colorWrong: 'red',
                    messages: {
                        price: `Нельзя вводить 0 и больше чем ${max_price_value}₽`
                    },


                  });
        }



    // валидатора на BOXDREAM пополенние

        if (document.querySelector('.boxdream__form')){
            let max_balance = document.querySelector('#id_max_balance_user').value

            // Валидцаия на странице detaildream - максимальное чилсо ограничено
                  new JustValidate('.boxdream__form', {
                    rules:
                        {price_box:
                            {required: true,
                                 function: () => {
                                        let curren_price_box_value = document.querySelector('#id_amount_box').value
                                    return   ( Number(max_balance) >= Number(curren_price_box_value) ) &&  (Number(curren_price_box_value)  > 0 )
                                 }
                            }

                        },

                    colorWrong: 'red',
                    messages: {
                        price_box: `Нельзя вводить 0 и больше чем ${max_balance}₽`
                    },


                  });
        }

    //








    // Валидцаия на странице detaildream - максимальное чилсо ограничено
        feedback_form = document.querySelector('.form__feedback')

        if (feedback_form){
            let validatorformfeedback = function (selector){

                // Валидатор на обратную форму
                new JustValidate(selector, {
                            rules:
                                {name:
                                    {required: true,
                                         minLength: 4,
                                    },
                                email: {
                                    required: true,
                                    email: 'email',
                                     },
                                text:
                                    {required: true
                                    }
                                },

                            colorWrong: 'red',

                            messages: {
                                    name: {
                                        minLength: 'Минимум 4 символа для имени'
                                    },
                                    email: {
                                        email: 'Введите корректный email адрес'
                                    },
                                    text: 'Напишите хоть что то..'

                            },
                      });

                };



             // валидатор с формы фиидбаек,
            validatorformfeedback('.form__feedback')

        }


    const filter_form = document.querySelector('#form__filter')
    if(filter_form){
        filter_form.addEventListener('change', function (){
            filter_form.submit()
        })
    }


});


