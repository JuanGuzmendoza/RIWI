const apiKey = 'AIzaSyCvtF5V6FLQpmhJnmln-jD0HMU3eqJ3qWI';
const model = 'gemini-2.0-flash';
const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/${model}:streamGenerateContent?key=${apiKey}`;

// Historial de la conversación
const conversationHistory = [];

const form = document.getElementById('chat-form');
const input = document.getElementById('user-input');
const chatWindow = document.getElementById('chat-window');

form.addEventListener('submit', async e => {
  e.preventDefault();
  const userText = input.value.trim();
  if (!userText) return;

  appendMessage(userText, 'user');
  input.value = '';

  // Guardar entrada del usuario
  conversationHistory.push({
    role: 'user',
    parts: [{ text: userText }]
  });

  await sendToGemini();
});

function appendMessage(text, sender) {
  const div = document.createElement('div');
  div.className = `message ${sender}`;
  div.innerText = text;
  chatWindow.appendChild(div);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

async function sendToGemini() {
  appendMessage('...', 'bot');
  const botMsg = document.querySelector('#chat-window .bot:last-child');

  try {
    const payload = {
      contents: conversationHistory,
      generationConfig: {
        responseMimeType: 'text/plain'
      }
    };

    const resp = await fetch(apiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });

    const chunks = await resp.json();
    let full = '';

    for (const chunk of chunks) {
      const part = chunk.candidates[0].content.parts[0].text;
      full += part;
      botMsg.innerText = full;
      chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    // Guardar respuesta del modelo
    conversationHistory.push({
      role: 'model',
      parts: [{ text: full }]
    });

  } catch (err) {
    console.error(err);
    botMsg.innerText = 'Error al contactar la API.';
  }
}
