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
});
