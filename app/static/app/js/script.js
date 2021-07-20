$(document).on('ready', function(){

	"use strict";

  // Form field focus hover
	$('.default').on({
		            mouseenter: function () {
		                $(this).addClass('pickfield');
		            },
		            mouseleave: function () {
		                $(this).removeClass('pickfield');
		            }
	});

  // Hover destination preview
	$('.grid-item').on({
		            mouseenter: function () {
		                $(this).find('.link').addClass('lopen');
		            },
		            mouseleave: function () {
		                 $(this).find('.link').removeClass('lopen');
		            }
	});

  // Hover section popular
	$('.popular .wraptext .dtbl .cell').on({
		            mouseenter: function () {
		                $(this).addClass('hover');
		                $(this).find('.price').addClass('open');
		            },
		            mouseleave: function () {
		                 $(this).removeClass('hover');
		                 $(this).find('.price').removeClass('open');
		            }
	});

  // Setting for datepicker form
	$('.datepicker').datepicker({
      minDate: 0
  });

  // Background banner when click the form
  $('.wrapform').on('click', function(){
    	$('.wrapbg').addClass('wrapbg_on');
    	$('.closenow').addClass('open');
    	$('.header').addClass('hde');
  });

  // Close the background banner
  $('.closenow').on('click', function(){
    	$('.wrapbg').removeClass('wrapbg_on');
    	$(this).removeClass('open');
    	$('.header').removeClass('hde');
  });

  // Button click to scroll to form
  $('.btnbooknow').on('click', function(){
    	$(this).scrollTop();
  });

  // Setting for mobile menu
	$(".mobilemenu").on("click", function(){
		$(this).toggleClass("open");
		$('.nav').toggleClass("open");
	})

  $(".nav ul li a").on('click',function(){
    $(".mobilemenu").removeClass("open");
    $(".nav").removeClass("open");
  });

  // Grid destination preview
  var $grid = $('.grid').masonry({
	 	columnWidth: '.grid-sizer',
		gutter: '.gutter-sizer',
		itemSelector: '.grid-item',
		percentPosition: true
	});
	$grid.imagesLoaded().on('progress',function() {
	  $grid.masonry('layout');
	});

  // Slider section popular
	var swiper = new Swiper('.swiper-container-pgoffer', {
      slidesPerView: 5,
      spaceBetween: 30,
      freeMode: true,
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
      breakpoints: {
        1024: {
          slidesPerView: 4,
          spaceBetween: 40,
        },
        768: {
          slidesPerView: 3,
          spaceBetween: 30,
        },
        640: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        320: {
          slidesPerView: 1,
          spaceBetween: 10,
        }
      }
    });

    // Slider section special
    var swiperspecial = new Swiper('.swiper-container-pgspecial', {
      slidesPerView: 'auto',
      centeredSlides: true,
      spaceBetween: 30,
      autoplay: {
	    delay: 4000,
	  },
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
    });

    // Setup navigation fix top when scroll
    $(window).on('scroll', function (e) {    
        var scroll = $(window).scrollTop();
        var winheight = '200';
        var classwrapnav = $('.header');
        if (scroll > winheight) {
            classwrapnav.addClass('fixtop');
        }else{
            classwrapnav.removeClass('fixtop');
        }   
    });

    
    //Email Validation
    function isValidEmailAddress(emailAddress) {
          var pattern = /^([a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+(\.[a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+)*|"((([ \t]*\r\n)?[ \t]+)?([\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*(([ \t]*\r\n)?[ \t]+)?")@(([a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.)+([a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.?$/i;
          return pattern.test(emailAddress);
    };


    //Form Contact Validation
    $('#form1').on('submit', function(){
      var check = false;
      var name = $('#fname').val();
      var email = $('#femail').val();
      var phone = $('#phone').val();
      var destination = $('#destinationform').val();
      var startdate = $('#startdate').val();
      var enddate = $('#enddate').val();
      var adult = $('#adult').val();
      var children = $('#children').val();

      //check name field
      if (name == ""){
        $('p.notif').text("Field name cannot be empty!").fadeIn();
        check = false;
        return false;
      }else{
        check = true;
      }
      //check email field
      if (email == ""){
        $('p.notif').text("Field email cannot be empty!").fadeIn();
        check = false;
        return false;
      }else{
        if( !isValidEmailAddress( email ) ) {
          $('p.notif').text("Email must be correct format!").fadeIn();
          check = false;
          return false;
        }else{
          check = true;
        }
      }
      //check phone field
      if (phone == ""){
        $('p.notif').text("Field phone cannot be empty!").fadeIn();
        check = false;
        return false;
      }else{
        check = true;
      }
      //check destination field
      if (destination == ""){
        $('p.notif').text("Field destination cannot be empty!").fadeIn();
        check = false;
        return false;
      }else{
        check = true;
      }
      //check startdate field
      if (startdate == ""){
        $('p.notif').text("Field startdate cannot be empty!").fadeIn();
        check = false;
        return false;
      }else{
        check = true;
      }
      //check enddate field
      if (enddate == ""){
        $('p.notif').text("Field enddate cannot be empty!").fadeIn();
        check = false;
        return false;
      }else{
        check = true;
      }
      //check adult field
      if (adult == ""){
        $('p.notif').text("Field adult cannot be empty!").fadeIn();
        check = false;
        return false;
      }else{
        check = true;
      }
      //check children field
      if (children == ""){
        $('p.notif').text("Field children cannot be empty!").fadeIn();
        check = false;
        return false;
      }else{
        check = true;
      }

      if (check == true){
        $("#btncontactsend").prop('disabled', true);
        $("#btncontactsend").prop('value', 'Sending in progress...'); 
        $.ajax({
          type: "POST",
          url: "postcontact.php",
          data: $('#form1').serialize(),
          success: function(data){
            $('p.notif').html('<label>'+ data +'</label>').fadeIn();
            $("#btncontactsend").prop('disabled', false);
            check = false;
            $('#fname').val();
            $('#femail').val();
            $('#phone').val();
            $('#destination').val();
            $('#startdate').val();
            $('#enddate').val();
            $('#adult').val();
            $('#children').val();
            $("#btncontactsend").prop('value', 'Book Now'); 
          }
        });
        return false;
      }
    });

});