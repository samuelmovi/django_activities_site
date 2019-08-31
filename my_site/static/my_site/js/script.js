$(document).ready(()=>{
    // responsive top bar
	var contactBurger =  $("#contact-burger");
	var contactBar = $("#contact-bar");
	contactBurger.click(function(){
		contactBar.toggleClass("responsive");
	});
	// responsive navbar
	var navbarBurger =  $("#navbar-burger");
	var navBar = $("#navbar");
	navbarBurger.click(function(){
		navBar.toggleClass("responsive");
	});
    // photo carousel
    var allPhotos = $("#carousel").find('.carousel-photo');
    var photoIndex = 0;
    function slidePhotos(){
        var i;
        for (i = 0; i < allPhotos.length; i++) {
        allPhotos.eq(i).hide();
        }
        photoIndex++;
        if (photoIndex > allPhotos.length) {
        photoIndex = 0;
        }
        allPhotos.eq(photoIndex-1).show();
        setTimeout(slidePhotos, 2000); // Change image every 2.5 seconds
    }
    slidePhotos();

    // date picker in form
    $(function() {
        $( ".datepicker" ).datepicker({
          changeMonth: true,
          changeYear: true,
          yearRange: "2019:2025",
          // You can put more options here.

        });
      });

});
