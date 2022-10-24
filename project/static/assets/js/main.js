$(document).ready(function() {
    $('.minus').click(function () {
        var $input = $(this).parent().find('input');
        var count = parseInt($input.val()) - 1;
        count = count < 1 ? 1 : count;
        $input.val(count);
        $input.change();
        return false;
    });
    $('.plus').click(function () {
        var $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) + 1);
        $input.change();
        return false;
    });

    $maxHeight = 0;
    $("[data-class='same-height']").each(function(){
        if($(this).height() > $maxHeight) {
          $maxHeight = $(this).height();
        }
    });
    $("[data-class='same-height']").height($maxHeight);
//    $('html,body').animate({
//        scrollTop : $(".di").offset().top
//    });
});


var new_scroll_position = 0;
var last_scroll_position;
// var header = document.getElementById("header");
var header = document.querySelector('.headersss');

window.addEventListener('scroll', function(e) {
    last_scroll_position = window.scrollY;

    // Scrolling down
    if (new_scroll_position < last_scroll_position && last_scroll_position > 80) {
        // header.removeClass('slideDown').addClass('slideUp');
        header.classList.remove("slideDown");
        header.classList.add("slideUp");

    // Scrolling up
    } else if (new_scroll_position > last_scroll_position) {
        // header.removeClass('slideUp').addClass('slideDown');
        header.classList.remove("slideUp");
        header.classList.add("slideDown");
    }

    new_scroll_position = last_scroll_position;
});

$(function () {
    "use strict";
    //ScrollTo The Top
    $(window).scroll(function () {
        var height = $(window).scrollTop();
        if (height > 100) {
            $('.scrollTop').show();
        } else {
            $('.scrollTop').hide();
        }
    });
    scrollTop('js-scroll-top', 150);

    function scrollTop(el, duration) {
    const target = document.getElementById(el);
    target.addEventListener('click', function() {
        let currentY = window.pageYOffset; 
        let step = duration/currentY > 1 ? 10 : 100; 
        let timeStep = duration/currentY * step; 
        let intervalId = setInterval(scrollUp, timeStep);
        function scrollUp(){
        currentY = window.pageYOffset;
        if(currentY === 0) {
            clearInterval(intervalId);
        } else {
            scrollBy( 0, -step );
        }
        }
    });
    }
    // Team slider
    $(document).ready(function () {
        $('.owl-carousel').owlCarousel({
            rtl: true,
            loop: true,
            margin: 30,
            autoplay: true,
            autoplayTimeout: 2000,
            autoplayHoverPause: true,
            navText: ['<i class="fas fa-chevron-right"></i>', '<i class="fas fa-chevron-left"></i>'],
            responsive: {
                0: {
                    items: 1
                },
                600: {
                    items: 2
                },
                1000: {
                    items: 4
                }
            }
        });
    });

    // PickImg
    // $("select").imagepicker();

    //Upload Img
    const readURL = (input) => {
        if (input.files && input.files[0]) {
            const reader = new FileReader()
            reader.onload = (e) => {
                $('#preview').attr('src', e.target.result)
            }
            reader.readAsDataURL(input.files[0])
        }
    }
    $('.choose').on('change', function () {
        readURL(this)
        let i
        if ($(this).val().lastIndexOf('\\')) {
            i = $(this).val().lastIndexOf('\\') + 1
        } else {
            i = $(this).val().lastIndexOf('/') + 1
        }
        const fileName = $(this).val().slice(i)
        $('.label').text(fileName)
    })

});

document.addEventListener('DOMContentLoaded', function() {
    'use strict';
    var link = document.querySelector('[data-toggle-menu]');
    link.addEventListener('click', function() {
        if (link.classList.contains('toggle-menu--clicked')) {
            link.classList.remove('toggle-menu--clicked');
        } else {
            link.classList.add('toggle-menu--clicked');
        }
    }, false);
}, false);

$('#check').change(function(){
    if($(this).is(":checked")) {
        $('.reqired-select').removeAttr("disabled");
    } else {
        $('.reqired-select').attr("disabled", true);
    }
});

$(window).on('load', function () {
    $('#loading-section').fadeOut('slow');
});


