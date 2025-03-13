$(document).ready(function () {
    $(".show-more").click(function () {
        $(".hide-category").css({"visibility": "visible", "height": "auto"});
        $(".show-more").hide();
        $(".show-less").show();
    });

    $(".show-less").click(function () {
        $(".hide-category").css({"visibility": "hidden", "height": "0"});
        $(".show-less").hide();
        $(".show-more").show();
    });
});


// Swiper script \\
var swiper = new Swiper(".mySwiper", {
    spaceBetween: 30,
    centeredSlides: true,
    autoplay: {
      delay: 2500,
      disableOnInteraction: false,
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
// /Swiper script \\



