document.addEventListener("DOMContentLoaded", function () {
    const chatInput = document.querySelector(".chat-input input[type='text']");
    const sendButton = document.querySelector(".chat-input button");
    const chatMessage = document.querySelector(".chat-message");

    function getUzbekistanTime() {
        const now = new Date();
        const options = {
            hour: '2-digit',
            minute: '2-digit',
            hour12: true,
            timeZone: 'Asia/Tashkent'
        };
        return new Intl.DateTimeFormat('en-US', options).format(now);
    }

    function addMyMessage(text) {
        if (!text.trim()) return;

        const messageWrapper = document.createElement("div");
        messageWrapper.className = "my-message";

        const message = document.createElement("div");
        message.className = "message";

        const p = document.createElement("p");
        p.textContent = text;

        const time = document.createElement("span");
        time.className = "time";
        time.textContent = getUzbekistanTime();

        message.appendChild(p);
        message.appendChild(time);
        messageWrapper.appendChild(message);
        chatMessage.appendChild(messageWrapper);

        chatMessage.scrollTop = chatMessage.scrollHeight;
        chatInput.value = "";
    }

    sendButton.addEventListener("click", () => {
        addMyMessage(chatInput.value);
    });

    chatInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            e.preventDefault();
            addMyMessage(chatInput.value);
        }
    });
});