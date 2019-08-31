$(document).ready(()=>{

    // contact bar
	var contactBurger =  $("#contact-burger");
	var contactBar = $("#contact-bar");
	contactBurger.click(function(){
		contactBar.toggleClass("responsive");
	});

    // carousel

    // navbar
	var navbarBurger =  $("#navbar-burger");
	var navBar = $("#navbar");
	navbarBurger.click(function(){
		navBar.toggleClass("responsive");
	});


});
