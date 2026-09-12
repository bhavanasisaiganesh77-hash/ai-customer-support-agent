import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AI Support",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html = r"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>AI Support</title>

<style>

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display",
                 "SF Pro Text", "Segoe UI", Arial, sans-serif;
    background: #f5f5f7;
    color: #1d1d1f;
}

.page {
    min-height: 820px;
    padding: 28px;
}

/* NAVBAR */

.navbar {
    max-width: 1250px;
    margin: auto;
    height: 64px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 0 24px;

    background: rgba(255,255,255,0.82);
    backdrop-filter: blur(20px);

    border: 1px solid rgba(0,0,0,0.07);
    border-radius: 20px;

    box-shadow: 0 8px 30px rgba(0,0,0,0.05);
}

.logo {
    display: flex;
    align-items: center;
    gap: 12px;
}

.logo-icon {
    width: 34px;
    height: 34px;
    border-radius: 50%;

    background: #1d1d1f;
    color: white;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 17px;
}

.logo-text {
    font-size: 18px;
    font-weight: 600;
    letter-spacing: -0.3px;
}

.nav-right {
    display: flex;
    align-items: center;
    gap: 20px;
}

.status {
    display: flex;
    align-items: center;
    gap: 7px;

    font-size: 13px;
    color: #6e6e73;
}

.status-dot {
    width: 8px;
    height: 8px;
    background: #34c759;
    border-radius: 50%;
}

/* MAIN */

.main {
    max-width: 1250px;
    margin: 28px auto;

    display: grid;
    grid-template-columns: 360px 1fr;

    gap: 24px;
}

/* LEFT */

.left-card {
    background: white;
    border-radius: 28px;
    padding: 38px;

    min-height: 700px;

    border: 1px solid rgba(0,0,0,0.06);

    box-shadow: 0 12px 40px rgba(0,0,0,0.06);

    display: flex;
    flex-direction: column;
}

.ai-symbol {
    width: 70px;
    height: 70px;

    border-radius: 20px;

    background: #1d1d1f;
    color: white;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 27px;

    margin-bottom: 35px;
}

.left-title {
    font-size: 38px;
    line-height: 1.08;

    font-weight: 650;

    letter-spacing: -1.5px;

    margin-bottom: 18px;
}

.left-description {
    color: #6e6e73;

    font-size: 15px;
    line-height: 1.65;
}

.line {
    height: 1px;
    background: #e5e5e7;

    margin: 34px 0;
}

.info {
    margin-bottom: 25px;
}

.info-title {
    font-size: 12px;

    text-transform: uppercase;

    letter-spacing: 1px;

    color: #86868b;

    margin-bottom: 7px;
}

.info-text {
    font-size: 14px;
    color: #424245;

    line-height: 1.5;
}

.left-bottom {
    margin-top: auto;
}

.secure {
    background: #f5f5f7;

    border-radius: 16px;

    padding: 15px;

    font-size: 12px;

    color: #6e6e73;

    line-height: 1.5;
}

/* CHAT */

.chat-card {
    background: white;

    border-radius: 28px;

    min-height: 700px;

    border: 1px solid rgba(0,0,0,0.06);

    box-shadow: 0 12px 40px rgba(0,0,0,0.06);

    display: flex;
    flex-direction: column;

    overflow: hidden;
}

.chat-header {
    padding: 32px 36px 24px;

    border-bottom: 1px solid #e5e5e7;
}

.chat-title {
    font-size: 29px;

    font-weight: 650;

    letter-spacing: -0.8px;

    margin-bottom: 7px;
}

.chat-subtitle {
    color: #86868b;

    font-size: 14px;
}

/* CHAT BODY */

.chat-body {
    flex: 1;

    min-height: 480px;

    padding: 28px;

    overflow-y: auto;

    display: flex;
    flex-direction: column;
    gap: 18px;
}

/* WELCOME */

.welcome {
    flex: 1;

    display: flex;
    flex-direction: column;

    align-items: center;
    justify-content: center;

    padding: 45px;
}

.welcome-icon {
    width: 72px;
    height: 72px;

    border-radius: 22px;

    background: #f5f5f7;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 30px;

    margin-bottom: 24px;
}

.welcome-title {
    font-size: 30px;

    font-weight: 650;

    letter-spacing: -0.8px;

    margin-bottom: 10px;
}

.welcome-text {
    color: #86868b;

    font-size: 14px;

    text-align: center;

    margin-bottom: 35px;
}

/* SUGGESTIONS */

.suggestions {
    width: 100%;
    max-width: 700px;

    display: grid;

    grid-template-columns: 1fr 1fr;

    gap: 12px;
}

.suggestion {
    background: #f5f5f7;

    border: 1px solid #e5e5e7;

    border-radius: 15px;

    padding: 16px;

    text-align: left;

    font-size: 13px;

    color: #424245;

    cursor: pointer;

    transition: all 0.2s ease;
}

.suggestion:hover {
    background: #1d1d1f;

    color: white;

    transform: translateY(-2px);
}

/* MESSAGES */

.message-row {
    display: flex;

    width: 100%;
}

.message-row.user {
    justify-content: flex-end;
}

.message-row.assistant {
    justify-content: flex-start;
}

.message {
    max-width: 75%;

    padding: 14px 17px;

    border-radius: 17px;

    font-size: 14px;

    line-height: 1.55;

    white-space: pre-wrap;
}

.message.user {
    background: #1d1d1f;

    color: white;

    border-bottom-right-radius: 5px;
}

.message.assistant {
    background: #f5f5f7;

    color: #1d1d1f;

    border-bottom-left-radius: 5px;
}

/* LOADING */

.typing {
    display: flex;

    align-items: center;

    gap: 5px;

    background: #f5f5f7;

    padding: 14px 17px;

    border-radius: 17px;

    width: fit-content;
}

.typing span {
    width: 6px;
    height: 6px;

    background: #86868b;

    border-radius: 50%;

    animation: typing 1.2s infinite;
}

.typing span:nth-child(2) {
    animation-delay: 0.15s;
}

.typing span:nth-child(3) {
    animation-delay: 0.3s;
}

@keyframes typing {

    0%, 60%, 100% {
        opacity: 0.3;
        transform: translateY(0);
    }

    30% {
        opacity: 1;
        transform: translateY(-3px);
    }

}

/* INPUT */

.input-area {
    padding: 22px 28px;

    border-top: 1px solid #e5e5e7;

    background: #fff;
}

.input-box {
    height: 54px;

    border: 1px solid #d2d2d7;

    border-radius: 16px;

    display: flex;

    align-items: center;

    padding: 0 8px 0 18px;

    background: #fbfbfd;

    transition: 0.2s;
}

.input-box:focus-within {
    border-color: #1d1d1f;

    background: white;

    box-shadow: 0 0 0 3px rgba(0,0,0,0.05);
}

.input-box input {
    flex: 1;

    border: none;

    outline: none;

    background: transparent;

    font-size: 14px;

    color: #1d1d1f;
}

.input-box input::placeholder {
    color: #86868b;
}

.send {
    width: 40px;
    height: 40px;

    border-radius: 12px;

    border: none;

    background: #1d1d1f;

    color: white;

    font-size: 17px;

    cursor: pointer;

    transition: 0.2s;
}

.send:hover {
    transform: scale(1.05);
}

/* FOOTER */

.footer {
    text-align: center;

    font-size: 11px;

    color: #86868b;

    margin-top: 10px;
}

/* NEW CHAT */

.new-chat {
    border: 1px solid #e5e5e7;

    background: #f5f5f7;

    border-radius: 12px;

    padding: 9px 14px;

    font-size: 12px;

    cursor: pointer;

    color: #6e6e73;

    margin-bottom: 12px;
}

.new-chat:hover {
    background: #1d1d1f;

    color: white;
}

/* RESPONSIVE */

@media (max-width: 900px) {

    .page {
        padding: 15px;
    }

    .main {
        grid-template-columns: 1fr;
    }

    .left-card {
        min-height: auto;
    }

    .chat-card {
        min-height: 650px;
    }

}

@media (max-width: 600px) {

    .navbar {
        padding: 0 15px;
    }

    .nav-right {
        display: none;
    }

    .left-card {
        padding: 28px;
    }

    .left-title {
        font-size: 32px;
    }

    .chat-header {
        padding: 25px;
    }

    .welcome {
        padding: 25px;
    }

    .suggestions {
        grid-template-columns: 1fr;
    }

    .message {
        max-width: 88%;
    }

}

</style>

</head>

<body>

<div class="page">

    <!-- NAVBAR -->

    <div class="navbar">

        <div class="logo">

            <div class="logo-icon">
                ✦
            </div>

            <div class="logo-text">
                AI Support
            </div>

        </div>

        <div class="nav-right">

            <div class="status">

                <span class="status-dot"></span>

                Available to help

            </div>

        </div>

    </div>


    <!-- MAIN -->

    <div class="main">


        <!-- LEFT PANEL -->

        <div class="left-card">

            <div class="ai-symbol">
                ✦
            </div>

            <div class="left-title">
                Support,<br>
                simplified.
            </div>

            <div class="left-description">

                Get clear and helpful answers
                to your customer-support questions
                in a simple conversation.

            </div>

            <div class="line"></div>


            <div class="info">

                <div class="info-title">
                    Fast
                </div>

                <div class="info-text">
                    Get assistance without
                    navigating complicated menus.
                </div>

            </div>


            <div class="info">

                <div class="info-title">
                    Intelligent
                </div>

                <div class="info-text">
                    Your question is understood
                    and matched with relevant support.
                </div>

            </div>


            <div class="info">

                <div class="info-title">
                    Simple
                </div>

                <div class="info-text">
                    One conversation.
                    One clear answer.
                </div>

            </div>


            <div class="left-bottom">

                <div class="secure">

                    🔒 Your privacy matters.<br>

                    Never share passwords,
                    verification codes,
                    or sensitive account information.

                </div>

            </div>

        </div>


        <!-- CHAT PANEL -->

        <div class="chat-card">


            <div class="chat-header">

                <div class="chat-title">
                    How can we help?
                </div>

                <div class="chat-subtitle">
                    Ask a question and our support assistant
                    will help you find an answer.
                </div>

            </div>


            <!-- CHAT BODY -->

            <div
                class="chat-body"
                id="chatBody"
            >

                <div
                    class="welcome"
                    id="welcome"
                >

                    <div class="welcome-icon">
                        💬
                    </div>

                    <div class="welcome-title">
                        Welcome
                    </div>

                    <div class="welcome-text">
                        Choose a common question below
                        or type your own message.
                    </div>


                    <div class="suggestions">

                        <div
                            class="suggestion"
                            onclick="setQuestion('My bill is too high')"
                        >
                            My bill is too high
                        </div>


                        <div
                            class="suggestion"
                            onclick="setQuestion('My internet is not working')"
                        >
                            My internet is not working
                        </div>


                        <div
                            class="suggestion"
                            onclick="setQuestion('My router has a red light')"
                        >
                            My router has a red light
                        </div>


                        <div
                            class="suggestion"
                            onclick="setQuestion('I cannot log into my account')"
                        >
                            I cannot log into my account
                        </div>

                    </div>

                </div>

            </div>


            <!-- INPUT -->

            <div class="input-area">

                <div class="input-box">

                    <input
                        id="message"
                        type="text"
                        placeholder="Ask a question..."
                        autocomplete="off"
                        onkeydown="handleEnter(event)"
                    >

                    <button
                        class="send"
                        id="sendButton"
                        onclick="sendMessage()"
                    >
                        ↑
                    </button>

                </div>

                <div class="footer">

                    AI Support · Please do not share sensitive information

                </div>

            </div>


        </div>

    </div>

</div>


<script>

/*
    FASTAPI BACKEND
*/

const API_URL = "http://127.0.0.1:8000/api/chat";


/*
    SET QUESTION
*/

function setQuestion(question) {

    const input = document.getElementById("message");

    input.value = question;

    input.focus();

}


/*
    ENTER KEY
*/

function handleEnter(event) {

    if (event.key === "Enter") {

        event.preventDefault();

        sendMessage();

    }

}


/*
    ADD USER MESSAGE
*/

function addUserMessage(message) {

    const chatBody =
        document.getElementById("chatBody");

    const row =
        document.createElement("div");

    row.className =
        "message-row user";

    const bubble =
        document.createElement("div");

    bubble.className =
        "message user";

    bubble.textContent =
        message;

    row.appendChild(bubble);

    chatBody.appendChild(row);

    chatBody.scrollTop =
        chatBody.scrollHeight;

}


/*
    ADD AI MESSAGE
*/

function addAssistantMessage(message) {

    const chatBody =
        document.getElementById("chatBody");

    const row =
        document.createElement("div");

    row.className =
        "message-row assistant";

    const bubble =
        document.createElement("div");

    bubble.className =
        "message assistant";

    bubble.textContent =
        message;

    row.appendChild(bubble);

    chatBody.appendChild(row);

    chatBody.scrollTop =
        chatBody.scrollHeight;

}


/*
    SHOW LOADING
*/

function showTyping() {

    const chatBody =
        document.getElementById("chatBody");

    const row =
        document.createElement("div");

    row.className =
        "message-row assistant";

    row.id =
        "typingRow";

    const typing =
        document.createElement("div");

    typing.className =
        "typing";

    typing.innerHTML =
        "<span></span><span></span><span></span>";

    row.appendChild(typing);

    chatBody.appendChild(row);

    chatBody.scrollTop =
        chatBody.scrollHeight;

}


/*
    REMOVE LOADING
*/

function removeTyping() {

    const typing =
        document.getElementById("typingRow");

    if (typing) {

        typing.remove();

    }

}


/*
    SEND MESSAGE
*/

async function sendMessage() {

    const input =
        document.getElementById("message");

    const sendButton =
        document.getElementById("sendButton");

    const message =
        input.value.trim();

    if (!message) {

        return;

    }


    /*
        Remove welcome screen
    */

    const welcome =
        document.getElementById("welcome");

    if (welcome) {

        welcome.remove();

    }


    /*
        Disable input
    */

    input.disabled = true;

    sendButton.disabled = true;

    sendButton.style.opacity = "0.5";


    /*
        Show user message
    */

    addUserMessage(message);

    input.value = "";


    /*
        Show loading animation
    */

    showTyping();


    try {

        const response =
            await fetch(
                API_URL,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        message: message
                    })
                }
            );


        /*
            Check HTTP status
        */

        if (!response.ok) {

            throw new Error(
                "Backend returned HTTP " +
                response.status
            );

        }


        /*
            Read JSON
        */

        const data =
            await response.json();


        /*
            Remove loading
        */

        removeTyping();


        /*
            Display AI answer
        */

        if (data.response) {

            addAssistantMessage(
                data.response
            );

        } else {

            addAssistantMessage(
                "Sorry, I couldn't generate a response."
            );

        }

    }

    catch (error) {

        console.error(
            "Backend error:",
            error
        );


        removeTyping();


        addAssistantMessage(
            "Sorry, I couldn't connect to AI Support. " +
            "Please make sure the backend is running."
        );

    }


    /*
        Enable input again
    */

    input.disabled = false;

    sendButton.disabled = false;

    sendButton.style.opacity = "1";

    input.focus();

}

</script>

</body>

</html>
"""

components.html(
    html,
    height=900,
    scrolling=True
)
