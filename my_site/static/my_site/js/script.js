

<!-- Contact Bar -->
<!-- responsive contact bar folding -->
function fold_contact_buttons(){
	var x = document.getElementById("contact-bar");
	if (x.className === "contact-bar") {
		x.className += " responsive";
	} else {
		x.className = "contact-bar";
	}
}

<!-- sticky contact bar -->
function sticky_topbar() {
  var contact_bar = document.getElementById("ishow-contact-bar");
  var offSet = contact_bar.offsetTop;
  if (window.pageYOffset > offSet) {
    contact_bar.classList.add("sticky")
  } else {
    contact_bar.classList.remove("sticky");
  }
}

window.onscroll = function() {sticky_topbar(); };

<!-- iShow Navbar -->
<!-- responsive navbar folding -->
function fold_nav_buttons(){
	var x = document.getElementById("navbar");

	if (x.className === "navbar") {
		x.className += " responsive";
	} else {
		x.className = "navbar";
	}
}


<!-- Carousel -->
var myIndex = 0;
carousel();

<!-- iShow Super Banner -->
<!-- carousel script -->
function carousel() {
  var i;
  var x = document.getElementsByClassName("photo-slide");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}
  x[myIndex-1].style.display = "block";
  setTimeout(carousel, 2500); // Change image every 2.5 seconds
}

// date picker in form
$(function() {
    $( ".datepicker" ).datepicker({
      changeMonth: true,
      changeYear: true,
      yearRange: "2019:2025",
      // You can put more options here.

    });
  });