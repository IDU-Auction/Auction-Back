$(document).ready(function() {
    $(".accordion-button").click(function() {
        var content = $(this).next(".accordion-content");
        var icon = $(this).find("i");
        var isActive = $(this).hasClass("active");
        
        $(".accordion-content").slideUp();
        $(".accordion-button").removeClass("active");
        $(".accordion-button i").removeClass("fa-chevron-up").addClass("fa-chevron-down");
        
        if (!isActive) {
            content.slideDown();
            $(this).addClass("active");
            icon.removeClass("fa-chevron-down").addClass("fa-chevron-up");
        }
    });
});

function startCountdown(endDate) {
    function updateCountdown() {
        const now = new Date().getTime();
        const timeLeft = endDate - now;

        if (timeLeft > 0) {
            const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
            const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

            document.getElementById("days").textContent = String(days).padStart(2, '0');
            document.getElementById("hours").textContent = String(hours).padStart(2, '0');
            document.getElementById("minutes").textContent = String(minutes).padStart(2, '0');
            document.getElementById("seconds").textContent = String(seconds).padStart(2, '0');
        } else {
            document.querySelector(".countdown-wrapper").innerHTML = "<p style='color: red; font-size: 20px;'>EXPIRED</p>";
        }
    }

    updateCountdown();
    setInterval(updateCountdown, 1000);
}

const deadline = new Date("March 20, 2025 23:59:59").getTime();
startCountdown(deadline);
