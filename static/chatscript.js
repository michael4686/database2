const chatMessages = document.getElementById('chat-messages');
const chatInput = document.getElementById('chat-input');
const chatSubmit = document.getElementById('chat-submit');

function addMessage(message) {
  var author = fname ;
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('chat-message');
  messageDiv.innerHTML = `
    <div class="message-sender">you</div>
    <div class="message-text">${message.text}</div>
    <div class="message-time">${message.time}</div>
  `;
  chatMessages.appendChild(messageDiv);
}

chatSubmit.addEventListener('click', () => {
  const messageText = chatInput.value;
  if (messageText.trim() !== '') {
    const message = { text: messageText, time: new Date().toLocaleString() };
    addMessage(message);
    chatInput.value = '';
  }
});

chatInput.addEventListener('keyup', (event) => {
  if (event.keyCode === 13) {
    chatSubmit.click();
  }
});