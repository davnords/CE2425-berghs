document.addEventListener("DOMContentLoaded", () => {
    const messagesContainer = document.getElementById("chatbot-messages");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    function addMessage(content, sender) {
        const message = document.createElement("p");
        message.classList.add(sender); // 'user' or 'bot'
        message.textContent = content;
        messagesContainer.appendChild(message);
        messagesContainer.scrollTop = messagesContainer.scrollHeight; // Auto-scroll to the bottom
    }

    async function getBotResponse(userMessage) {
        if (!userMessage) {
            console.error("DEBUG: User message is empty.");
            addMessage("Please enter a message.", "bot");
            return;
        }

        console.log("DEBUG: Sending payload:", JSON.stringify({ message: userMessage }));

        try {
            const response = await fetch("http://127.0.0.1:5000/api/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ message: userMessage }),
            });

            console.log("DEBUG: Raw response:", response);

            const data = await response.json();
            console.log("DEBUG: Parsed response from backend:", data);

            if (data.reply) {
                addMessage(data.reply, "bot");
            } else if (data.error) {
                addMessage(`Error: ${data.error}`, "bot");
            } else {
                addMessage("Unexpected response from the server.", "bot");
            }
        } catch (error) {
            console.error("Error:", error);
            addMessage("Something went wrong. Try again later.", "bot");
        }
    }

    sendButton.addEventListener("click", () => {
        const userMessage = userInput.value.trim();
        if (userMessage) {
            addMessage(userMessage, "user");
            userInput.value = ""; // Clear input field
            getBotResponse(userMessage);
        }
    });

    userInput.addEventListener("keypress", (e) => {
        if (e.key === "Enter") {
            sendButton.click();
        }
    });
});
