(function ($) {
 "use strict";

/*-- Menu Sticky --*/
var $window = $(window);
$window.on('scroll', function() {    
	var scroll = $window.scrollTop();
	if (scroll < 300) {
		$(".sticker").removeClass("stick");
	}else{
		$(".sticker").addClass("stick");
	}
});
    
/*-- Mobile Menu --*/
$('.main-menu nav').meanmenu({
	meanScreenWidth: '767',
	meanMenuContainer: '.mobile-menu',
	meanMenuClose: '<i class="zmdi zmdi-close"></i>',
	meanMenuOpen: '<i class="zmdi zmdi-menu"></i>',
	meanRevealPosition: 'right',
	meanMenuCloseSize: '30px',
});
    
/*-- Toogle Search -- */
$('.search-toggle').on('click', function() {
    $(this).toggleClass('active');
    $('.search-form').toggleClass('open');
    return false;
});
    
/*-- Hero Slider --*/
$('#hero-slider').nivoSlider({
    prevText: '<i class="zmdi zmdi-long-arrow-left"></i>',
    nextText: '<i class="zmdi zmdi-long-arrow-right"></i>',
    controlNav: false,
    pauseTime: 5000,
});
    
/*-- Testimonial Slider --*/
$('.testimonial-slider').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    dots: true,
});
    
/*-- Teacher Slider --*/
$('.teacher-slider').slick({
    slidesToShow: 4,
    slidesToScroll: 1,
    prevArrow: '<button class="slick-prev"><i class="zmdi zmdi-long-arrow-left"></i></button>',
    nextArrow: '<button class="slick-next"><i class="zmdi zmdi-long-arrow-right"></i></button>',
    responsive: [
        {
        breakpoint: 1199,
            settings: {
                slidesToShow: 3,
            }
        },
        {
        breakpoint: 991,
            settings: {
                slidesToShow: 2,
            }
        },
        {
        breakpoint: 767,
            settings: {
                slidesToShow: 1,
            }
        },
    ],
});
    
/*-- Course Match Height --*/
$('.course-wrapper > div').matchHeight();
    
/*-- Progress Bar Animation --*/
$('.progress').appear(function() {
    var pW = $(this).find('.progress-bar').data('progress')
    $(this).find('.progress-bar').animate({
        width: pW,
        opacity: 1,
    }, 1500, 'linear')
});
 
/*-- ScrollUp -- */	
$.scrollUp({
    scrollText: '<i class="fa fa-angle-up"></i>',
    easingType: 'linear',
    scrollSpeed: 900,
    animation: 'fade'
}); 	   
    
/*-- Counter Up -- */	
$('.counter').counterUp({
    delay: 70,
    time: 5000
}); 
    
/*-- Gallery Popup --*/
var imagePopup = $('.image-popup');
imagePopup.magnificPopup({
	type: 'image',
});

/*-- Ajax Contact Form JS --*/
$(function () {
    // Get the form.
    var form = $('#contact-form');
    // Get the messages div.
    var formMessages = $('.form-message');
    // Set up an event listener for the contact form.
    $(form).submit(function (e) {
        // Stop the browser from submitting the form.
        e.preventDefault();
        // Serialize the form data.
        var formData = $(form).serialize();
        // Submit the form using AJAX.
        $.ajax({
            type: 'POST',
            url: $(form).attr('action'),
            data: formData,
        })
        .done(function (response) {
        // Make sure that the formMessages div has the 'success' class.
        $(formMessages).removeClass('error');
        $(formMessages).addClass('success');

        // Set the message text.
        $(formMessages).text(response);

        // Clear the form.
        $('#contact-form input,#contact-form textarea').val('');
        })
        .fail(function (data) {
        // Make sure that the formMessages div has the 'error' class.
        $(formMessages).removeClass('success');
        $(formMessages).addClass('error');

        // Set the message text.
        if (data.responseText !== '') {
            $(formMessages).text(data.responseText);
        } else {
            $(formMessages).text(
                'Oops! An error occured and your message could not be sent.'
            );
        }
        });
    });
});

/*-- Wow js active -- */
new WOW().init();

 
})(jQuery); 
