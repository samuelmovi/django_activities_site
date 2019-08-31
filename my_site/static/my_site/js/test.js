$(document).ready(()=>{
	var contactBurger =  $("#contact-burger");
	var contactBar = $("#contact-bar");
	contactBurger.click(function(){
		contactBar.toggleClass("responsive");
	});
	var navbarBurger =  $("#navbar-burger");
	var navBar = $("#navbar");
	navbarBurger.click(function(){
		navBar.toggleClass("responsive");
	});

    var allPhotos = $("#carousel").find('.carousel-photo');
    var i;
    for (i = 0; i < allPhotos.length; i++) {
        allPhotos[i].hide();
        var source = allPhotos[i].children().css();
        alert(source);
    }

    /*
     var photoIndex = 0;
    function carousel() {
      var i;
      for (i = 0; i < allPhotos.length; i++) {
        allPhotos[i].hide();
      }
      photoIndex++;
      if (photoIndex > allPhotos.length) {
        photoIndex = 0;
      }
      allPhotos[photoIndex-1].show();
      setTimeout(carousel, 2000); // Change image every 2.5 seconds
    }

    carousel();
    */
});
