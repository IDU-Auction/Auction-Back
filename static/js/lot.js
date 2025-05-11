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

const deadline = new Date("May 25, 2025 23:59:59").getTime();
startCountdown(deadline);


// Function to handle the "Place Bid" button click
$(document).ready(function () {
    const MIN_PRICE = 38910000000;

    function formatNumberWithSpaces(number) {
        return number.toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    }

    function parseFormattedNumber(str) {
        return parseInt(str.replace(/\s/g, ""), 10);
    }

    const $input = $(".extra-lot-item input");
    const $currentPrice = $("#currentPrice");
    const $addButton = $(".add-button");

    // Initial check: enforce minimum price
    let currentValue = parseFormattedNumber($currentPrice.text());
    if (isNaN(currentValue) || currentValue < MIN_PRICE) {
        currentValue = MIN_PRICE;
        $currentPrice.text(formatNumberWithSpaces(currentValue) + ".00 UZS");
    }

    // Format input while typing
    $input.on("input", function () {
        let rawValue = parseFormattedNumber($(this).val());
        if (isNaN(rawValue)) {
            $(this).val("");
            return;
        }
        $(this).val(formatNumberWithSpaces(rawValue));
    });

    // On button click, validate and update price
    $addButton.on("click", function () {
        let enteredValue = parseFormattedNumber($input.val());

        if (!isNaN(enteredValue) && enteredValue > currentValue) {
            currentValue = enteredValue;
            $currentPrice.text(formatNumberWithSpaces(currentValue) + ".00 UZS");
        } else {
            alert("Please enter a value greater than the current price.");
        }
    });
});

