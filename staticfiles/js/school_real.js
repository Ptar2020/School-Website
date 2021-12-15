
    // Back to top button
        $(window).scroll(function () {
            if ($(this).scrollTop() > 150) {
                $('.back-to-top').fadeIn('slow');
            } else {
                $('.back-to-top').fadeOut('slow');
            }
        });
        $('.back-to-top').click(function () {
            $('html, body').animate({scrollTop: 0}, 750);
            return true;
        });
         // Sticky Navbar
        $(window).scroll(function () {
            if ($(this).scrollTop() > 150) {
                $('.nav-bar').addClass('nav-sticky').css('color','green');
            } else {
                $('.nav-bar').removeClass('nav-sticky');
            }
        });
    // When the user scrolls down 80px from the top of the document, resize the navbar's padding and the logo's font size
    window.onscroll = function() {scrollFunction()};

    function scrollFunction() {
      if (document.body.scrollTop > 120 || document.documentElement.scrollTop > 120) {
        document.getElementById("navbarNavDropdown").style.fontSize = "16px";} 
      else {$('#navbarNavDropdown').css('font-size','19px');
        }
    } 
        


