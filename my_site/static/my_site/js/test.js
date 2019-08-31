$(document).ready(function(){

    // contact bar
    const contact-burger = $(".contact-burger")
    contact-burger.click( function()=>{
        $(".contact-bar").toggleClass("responsive");
    })

    /*
    function fold_contact_buttons(){
        $("#contact-bar").toggle("responsive");
    }
    */
    function sticky_contact_bar() {
        let offSet = contact_bar.offsetTop;
        const bar = $("#ishow-contact-bar");
        if (window.pageYOffset > offSet){
            bar.addClass("sticky");
        }
        else{
            bar.removeClass("sticky");
        }
    }

    window.onscroll = function() {sticky_contact_bar(); };

    // carousel
    photoIndex = 0;
    function carousel() {
      let i;
      const x = $(".photo-slide");
      for (i = 0; i < x.length; i++) {
        x[i].css("display", "none");
      }
      photoIndex++;
      if (photoIndex > x.length) {photoIndex = 1}
      x[photoIndex-1].css("display", "block");
      //x[photoIndex-1].style.display = "block";
      setTimeout(carousel, 2500); // Change image every 2.5 seconds
    }
    carousel();

    // navbar
    function fold_nav_buttons(){
        const x = $("#navbar");
        if ("navbar" in x.attr("class")){
            x.addClass("responsive");
        }

        if (x.className === "navbar") {
            x.className += " responsive";
        } else {
            x.className = "navbar";
        }
    }

    // content

    // date picker in form
    $(function() {
        $( ".datepicker" ).datepicker({
          changeMonth: true,
          changeYear: true,
          yearRange: "2019:2025",
          // You can put more options here.

        });
      });

})