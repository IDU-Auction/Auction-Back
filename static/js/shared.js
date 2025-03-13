function showDateTime() {
    let now = new Date();
    let options = { timeZone: "Asia/Tashkent" };
    let uzbTime = new Date(now.toLocaleString("en-US", options));

    let day = String(uzbTime.getDate()).padStart(2, '0');
    let month = String(uzbTime.getMonth() + 1).padStart(2, '0');
    let year = uzbTime.getFullYear();
    let hours = String(uzbTime.getHours()).padStart(2, '0');
    let minutes = String(uzbTime.getMinutes()).padStart(2, '0');
    let seconds = String(uzbTime.getSeconds()).padStart(2, '0');

    document.getElementById("currentDateTime").innerText = 
        `${day}.${month}.${year} ${hours}:${minutes}:${seconds} (GMT +5)`;
}


setInterval(showDateTime, 1000);


window.onload = showDateTime;
