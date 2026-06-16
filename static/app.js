/* ═══════════════════════════════════════════════════════
   JurisAI — Application Logic
   All API endpoints preserved: /api/auth/*, /api/chat, /api/chats/*
   ═══════════════════════════════════════════════════════ */

// ── DOM References ──
const authContainer  = document.getElementById('auth-container');
const appContainer   = document.getElementById('app-container');

const loginForm      = document.getElementById('login-form');
const registerForm   = document.getElementById('register-form');
const showRegisterLink = document.getElementById('show-register');
const showLoginLink  = document.getElementById('show-login');

const loginEmailInput    = document.getElementById('login-email');
const loginPasswordInput = document.getElementById('login-password');
const registerEmailInput    = document.getElementById('register-email');
const registerPasswordInput = document.getElementById('register-password');

const loginError    = document.getElementById('login-error');
const registerError = document.getElementById('register-error');

const chatBox        = document.getElementById('chat-box');
const userInput      = document.getElementById('user-input');
const sendBtn        = document.getElementById('send-btn');
const newChatBtn     = document.getElementById('new-chat-btn');
const chatList       = document.getElementById('chat-list');
const logoutBtn      = document.getElementById('logout-btn');
const activeChatTitle = document.getElementById('active-chat-title');
const userEmailEl    = document.getElementById('user-email');
const userAvatarEl   = document.getElementById('user-avatar');

const menuBtn        = document.getElementById('menu-btn');
const closeSidebarBtn = document.getElementById('close-sidebar-btn');
const sidebar        = document.getElementById('sidebar');
const sidebarBackdrop = document.getElementById('sidebar-backdrop');

// ── State ──
let token = localStorage.getItem('jurisai_token');
let activeSessionId = null;

// ═══════════════════════════════════════
// AUTH FORMS
// ═══════════════════════════════════════

showRegisterLink.addEventListener('click', (e) => {
  e.preventDefault();
  loginForm.classList.add('hidden');
  registerForm.classList.remove('hidden');
});

showLoginLink.addEventListener('click', (e) => {
  e.preventDefault();
  registerForm.classList.add('hidden');
  loginForm.classList.remove('hidden');
});

// ── Register ──
registerForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  registerError.classList.add('hidden');

  const email    = registerEmailInput.value.trim();
  const password = registerPasswordInput.value;

  if (password.length < 8) {
    showError(registerError, 'Password must be at least 8 characters.');
    return;
  }

  try {
    const res = await fetch('/api/auth/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    if (res.ok) {
      token = data.access_token;
      localStorage.setItem('jurisai_token', token);
      showAppScreen(email);
    } else {
      showError(registerError, data.detail || 'Registration failed.');
    }
  } catch {
    showError(registerError, 'Network error. Please try again.');
  }
});

// ── Login ──
loginForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  loginError.classList.add('hidden');

  const email    = loginEmailInput.value.trim();
  const password = loginPasswordInput.value;

  try {
    const res = await fetch('/api/auth/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    if (res.ok) {
      token = data.access_token;
      localStorage.setItem('jurisai_token', token);
      showAppScreen(email);
    } else {
      showError(loginError, data.detail || 'Invalid email or password.');
    }
  } catch {
    showError(loginError, 'Network error. Please try again.');
  }
});

function showError(el, msg) {
  el.textContent = msg;
  el.classList.remove('hidden');
}

// ── Auth Check ──
async function checkAuth() {
  if (!token) { showAuthScreen(); return; }

  try {
    const res = await fetch('/api/auth/me', {
      headers: { 'Authorization': `Bearer ${token}` }
    });

    if (res.ok) {
      const user = await res.json();
      showAppScreen(user.email);
    } else {
      logout();
    }
  } catch {
    logout();
  }
}

function showAuthScreen() {
  authContainer.classList.remove('hidden');
  appContainer.classList.add('hidden');
}

function showAppScreen(email) {
  authContainer.classList.add('hidden');
  appContainer.classList.remove('hidden');
  userEmailEl.textContent = email;
  userAvatarEl.textContent = email.charAt(0).toUpperCase();

  loadChatHistoryList();
  startNewChat();
}

// ── Logout ──
function logout() {
  token = null;
  localStorage.removeItem('jurisai_token');
  loginEmailInput.value = '';
  loginPasswordInput.value = '';
  registerEmailInput.value = '';
  registerPasswordInput.value = '';
  chatList.innerHTML = '';
  chatBox.innerHTML = '';
  showAuthScreen();
}
logoutBtn.addEventListener('click', logout);

// ═══════════════════════════════════════
// SIDEBAR (MOBILE)
// ═══════════════════════════════════════

function openSidebar() {
  sidebar.classList.add('open');
  sidebarBackdrop.classList.add('visible');
}

function closeSidebar() {
  sidebar.classList.remove('open');
  sidebarBackdrop.classList.remove('visible');
}

if (menuBtn)         menuBtn.addEventListener('click', openSidebar);
if (closeSidebarBtn) closeSidebarBtn.addEventListener('click', closeSidebar);
if (sidebarBackdrop) sidebarBackdrop.addEventListener('click', closeSidebar);

// ═══════════════════════════════════════
// CHAT LOGIC
// ═══════════════════════════════════════

function generateSessionId() {
  return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
}

// ── Welcome Screen ──
function displayWelcome() {
  chatBox.innerHTML = '';

  const welcome = document.createElement('div');
  welcome.className = 'welcome-screen';
  welcome.innerHTML = `
    <div class="welcome-logo" aria-hidden="true">⚖️</div>
    <h2>How can I assist you?</h2>
    <p>Your elite AI legal advisor for Indian Constitutional Law, Business & Corporate regulations, Property transactions, and Contract analysis.</p>
    <div class="feature-grid">
      <div class="feature-card" data-prompt="What are my legal rights if someone breaches a contract with me?">
        <span class="feature-icon">📋</span>
        <h4>Contract Breach</h4>
        <span>Know your rights &amp; remedies</span>
      </div>
      <div class="feature-card" data-prompt="What legal documents do I need to start a new business in India?">
        <span class="feature-icon">🏢</span>
        <h4>Starting a Business</h4>
        <span>Registrations &amp; legal requirements</span>
      </div>
      <div class="feature-card" data-prompt="What should I check before buying a property to avoid legal issues?">
        <span class="feature-icon">🏠</span>
        <h4>Property Purchase</h4>
        <span>Due diligence &amp; verification</span>
      </div>
      <div class="feature-card" data-prompt="How can I file a consumer complaint if a company refuses a refund?">
        <span class="feature-icon">🛡️</span>
        <h4>Consumer Rights</h4>
        <span>Complaints &amp; legal recourse</span>
      </div>
    </div>
  `;

  chatBox.appendChild(welcome);

  // Feature card click → fill input
  welcome.querySelectorAll('.feature-card').forEach(card => {
    card.addEventListener('click', () => {
      const prompt = card.dataset.prompt;
      if (prompt) {
        userInput.value = prompt;
        userInput.focus();
        autoResizeTextarea();
      }
    });
  });
}

// ── New Chat ──
function startNewChat() {
  activeSessionId = generateSessionId();
  activeChatTitle.textContent = 'New Consultation';
  displayWelcome();

  const items = chatList.querySelectorAll('.chat-item');
  items.forEach(i => i.classList.remove('active'));

  createSidebarChat(activeSessionId, 'New Consultation', true);
  closeSidebar();
}
newChatBtn.addEventListener('click', startNewChat);

// ── Chat History List ──
async function loadChatHistoryList() {
  try {
    const res = await fetch('/api/chats', {
      headers: { 'Authorization': `Bearer ${token}` }
    });

    if (res.ok) {
      const chats = await res.json();
      chatList.innerHTML = '';
      chats.forEach(chat => createSidebarChat(chat.id, chat.title));
    }
  } catch (e) {
    console.error('Failed to load chat history list', e);
  }
}

function createSidebarChat(sessionId, title, prepend = false) {
  if (!sessionId) return;
  if (chatList.querySelector(`.chat-item[data-id="${sessionId}"]`)) return;

  const item = document.createElement('div');
  item.className = `chat-item ${sessionId === activeSessionId ? 'active' : ''}`;
  item.dataset.id = sessionId;
  item.setAttribute('role', 'listitem');

  const titleSpan = document.createElement('span');
  titleSpan.className = 'chat-item-title';
  titleSpan.textContent = title || 'Untitled consultation';
  titleSpan.title = title || '';

  const deleteBtn = document.createElement('button');
  deleteBtn.className = 'btn-delete-chat';
  deleteBtn.innerHTML = '🗑';
  deleteBtn.title = 'Delete consultation';
  deleteBtn.setAttribute('aria-label', `Delete ${title || 'consultation'}`);

  deleteBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    showDeleteConfirm(sessionId, title || 'this consultation');
  });

  // Click → switch chat
  item.addEventListener('click', () => switchChat(sessionId, titleSpan.textContent));

  // Double-click → rename
  titleSpan.addEventListener('dblclick', (e) => {
    e.stopPropagation();
    const input = document.createElement('input');
    input.type = 'text';
    input.className = 'chat-title-edit';
    input.value = titleSpan.textContent;

    input.addEventListener('keydown', (ev) => {
      if (ev.key === 'Enter') input.blur();
      if (ev.key === 'Escape') {
        item.replaceChild(titleSpan, input);
      }
    });

    input.addEventListener('blur', async () => {
      const newTitle = input.value.trim() || 'Untitled consultation';
      titleSpan.textContent = newTitle;
      titleSpan.title = newTitle;
      if (input.parentNode === item) {
        item.replaceChild(titleSpan, input);
      }
      try {
        await fetch(`/api/chats/${sessionId}/title`, {
          method: 'PATCH',
          headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${token}` },
          body: JSON.stringify({ title: newTitle })
        });
      } catch (err) {
        console.warn('Failed to persist chat title', err);
      }
    });

    item.replaceChild(input, titleSpan);
    input.focus();
    input.select();
  });

  item.appendChild(titleSpan);
  item.appendChild(deleteBtn);

  if (prepend && chatList.firstChild) {
    chatList.insertBefore(item, chatList.firstChild);
  } else {
    chatList.appendChild(item);
  }
}

// ── Switch Chat ──
async function switchChat(sessionId, title) {
  activeSessionId = sessionId;
  activeChatTitle.textContent = title;

  const items = chatList.querySelectorAll('.chat-item');
  items.forEach(i => {
    i.classList.toggle('active', i.dataset.id === sessionId);
  });

  chatBox.innerHTML = '';
  showTypingIndicator('Loading consultation…');

  try {
    const res = await fetch(`/api/chats/${sessionId}/messages`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });

    removeTypingIndicator();

    if (res.ok) {
      const messages = await res.json();
      if (messages.length === 0) {
        displayWelcome();
      } else {
        messages.forEach(m => {
          addMessage(m.role === 'user' ? 'user' : 'ai', m.content);
        });
      }
    } else {
      displayWelcome();
    }
  } catch {
    removeTypingIndicator();
    displayWelcome();
  }

  closeSidebar();
}

// ── Delete with custom confirm modal ──
function showDeleteConfirm(sessionId, title) {
  const overlay = document.createElement('div');
  overlay.className = 'confirm-overlay';
  overlay.innerHTML = `
    <div class="confirm-modal">
      <h3>Delete Consultation</h3>
      <p>Are you sure you want to delete "<strong>${escapeHtml(title)}</strong>"? This action cannot be undone.</p>
      <div class="confirm-actions">
        <button class="btn-cancel" id="confirm-cancel">Cancel</button>
        <button class="btn-danger" id="confirm-delete">Delete</button>
      </div>
    </div>
  `;

  document.body.appendChild(overlay);

  overlay.querySelector('#confirm-cancel').addEventListener('click', () => overlay.remove());
  overlay.addEventListener('click', (e) => { if (e.target === overlay) overlay.remove(); });

  overlay.querySelector('#confirm-delete').addEventListener('click', async () => {
    overlay.remove();
    await deleteConsultation(sessionId);
  });
}

async function deleteConsultation(sessionId) {
  try {
    const res = await fetch(`/api/chats/${sessionId}`, {
      method: 'DELETE',
      headers: { 'Authorization': `Bearer ${token}` }
    });

    if (res.ok) {
      if (activeSessionId === sessionId) startNewChat();
      loadChatHistoryList();
    }
  } catch (e) {
    console.error('Failed to delete chat session', e);
  }
}

// ═══════════════════════════════════════
// MESSAGES
// ═══════════════════════════════════════

function addMessage(sender, text) {
  // Remove welcome screen if present
  const welcome = chatBox.querySelector('.welcome-screen');
  if (welcome) welcome.remove();

  const msgDiv = document.createElement('div');
  msgDiv.className = `message ${sender}-message`;

  const avatar = document.createElement('div');
  avatar.className = 'avatar';
  avatar.textContent = sender === 'user' ? userAvatarEl.textContent : 'AI';

  const content = document.createElement('div');
  content.className = 'message-content';

  if (sender === 'ai') {
    try {
      content.innerHTML = marked.parse(text || '');
    } catch {
      content.textContent = text;
    }
  } else {
    content.textContent = text;
  }

  if (sender === 'ai') {
    msgDiv.appendChild(avatar);
    msgDiv.appendChild(content);
  } else {
    msgDiv.appendChild(content);
    msgDiv.appendChild(avatar);
  }

  chatBox.appendChild(msgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

// ── Typing Indicator ──
function showTypingIndicator(text = 'Analyzing legal precedents…') {
  removeTypingIndicator();

  const indicator = document.createElement('div');
  indicator.className = 'message ai-message';
  indicator.id = 'typing-indicator';

  indicator.innerHTML = `
    <div class="avatar">AI</div>
    <div class="message-content">
      <div class="typing-indicator">
        <div class="typing-dots">
          <div class="typing-dot"></div>
          <div class="typing-dot"></div>
          <div class="typing-dot"></div>
        </div>
        <span class="typing-text">${escapeHtml(text)}</span>
      </div>
    </div>
  `;

  chatBox.appendChild(indicator);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function removeTypingIndicator() {
  const existing = document.getElementById('typing-indicator');
  if (existing) existing.remove();
}

// ═══════════════════════════════════════
// SEND MESSAGE
// ═══════════════════════════════════════

async function sendMessage() {
  const text = userInput.value.trim();
  if (!text) return;

  addMessage('user', text);
  userInput.value = '';
  autoResizeTextarea();

  sendBtn.disabled = true;
  showTypingIndicator();

  try {
    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ message: text, session_id: activeSessionId })
    });

    removeTypingIndicator();
    sendBtn.disabled = false;

    if (res.ok) {
      const data = await res.json();
      addMessage('ai', data.response);
      loadChatHistoryList();
    } else {
      const errData = await res.json().catch(() => ({}));
      addMessage('ai', `⚠️ Error: ${errData.detail || 'Internal server error.'}`);
    }
  } catch {
    removeTypingIndicator();
    sendBtn.disabled = false;
    addMessage('ai', '⚠️ Could not connect to the server. Please try again.');
  }
}

sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
});

// ═══════════════════════════════════════
// TEXTAREA AUTO-RESIZE
// ═══════════════════════════════════════

function autoResizeTextarea() {
  userInput.style.height = 'auto';
  userInput.style.height = Math.min(userInput.scrollHeight, 140) + 'px';
}

userInput.addEventListener('input', autoResizeTextarea);

// ═══════════════════════════════════════
// UTILITIES
// ═══════════════════════════════════════

function escapeHtml(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

// ═══════════════════════════════════════
// INIT
// ═══════════════════════════════════════
checkAuth();
