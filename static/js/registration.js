function updateDateTime() {
    let now = new Date();

    let optionsDate = { timeZone: "Asia/Tashkent", day: "2-digit", month: "2-digit", year: "numeric" };
    let formattedDate = new Intl.DateTimeFormat("en-GB", optionsDate).format(now);
    document.getElementById("date").textContent = formattedDate.replace(/\//g, "."); // Convert format to dd.mm.yyyy

  
    let optionsTime = { timeZone: "Asia/Tashkent", hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false };
    let formattedTime = new Intl.DateTimeFormat("en-GB", optionsTime).format(now);
    document.getElementById("time").textContent = formattedTime;
}


setInterval(updateDateTime, 1000);
updateDateTime();


$(document).ready(function () {
    $("#phone").on("input", function () {
        let phoneInput = $(this).val();
        let phoneError = $("#phoneError");

        
        phoneInput = phoneInput.replace(/\D/g, '');

        
        if (phoneInput.length > 9) {
            phoneInput = phoneInput.substring(0, 9);
        }

        
        let formattedPhone = phoneInput
            .replace(/(\d{2})(\d{0,3})/, "$1-$2") 
            .replace(/(\d{2}-\d{3})(\d{0,2})/, "$1-$2") 
            .replace(/(\d{2}-\d{3}-\d{2})(\d{0,2})/, "$1-$2"); 

        $(this).val(formattedPhone); 

        
        if (phoneInput.startsWith("998")) {
            phoneError.text("❌ Please enter only the remaining 9 digits (without +998).");
        } else if (phoneInput.length < 9) {
            phoneError.text("⚠️ Phone number must be exactly 9 digits.");
        } else {
            phoneError.text(""); 
        }
    });
});



// Password Strongness Checker && Confirm Password

$(document).ready(function () {
    
    $(".toggle-password").click(function () {
        let input = $(this).prev("input");
        let type = input.attr("type") === "password" ? "text" : "password";
        input.attr("type", type);

        
        $(this).find("i").toggleClass("fa-eye fa-eye-slash");
    });

    $("#password1").on("keyup", function () {
        let password = $(this).val();
        let strengthBar = $("#strengthBar");
        let strengthMessage = $("#strengthMessage");
        let strength = 0;

        
        if (password.length >= 8) strength++; 
        if (password.match(/[A-Z]/)) strength++; 
        if (password.match(/[0-9]/)) strength++; 
        if (password.match(/[\W]/)) strength++; 

        
        let barWidth = (strength / 4) * 100;
        strengthBar.css("width", barWidth + "%");

        
        if (strength === 0) {
            strengthMessage.text("");
            strengthBar.removeClass();
        } else if (strength === 1) {
            strengthMessage.text("Very Weak 😢").css("color", "red");
            strengthBar.removeClass().addClass("very-weak");
        } else if (strength === 2) {
            strengthMessage.text("Weak 😐").css("color", "orange");
            strengthBar.removeClass().addClass("weak");
        } else if (strength === 3) {
            strengthMessage.text("Medium 🙂").css("color", "#yellow");
            strengthBar.removeClass().addClass("medium");
        } else {
            strengthMessage.text("Strong 💪").css("color", "green");
            strengthBar.removeClass().addClass("strong");
        }
    });

    // Password Confirmation Check
    $("#password1, #password2").on("keyup", function () {
        let password1 = $("#password1").val();
        let password2 = $("#password2").val();
        let matchMessage = $("#passwordMatchMessage");

        if (password1 === password2 && password1.length > 0) {
            matchMessage.text("Passwords Match").css("color", "green");
        } else if (password2.length > 0) {
            matchMessage.text("Passwords Do Not Match ").css("color", "red");
        } else {
            matchMessage.text("");
        }
    });
});