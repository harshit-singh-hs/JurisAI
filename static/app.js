/* ============================================================
   JurisAI — app.js
   Premium dark UI logic
   ============================================================ */

// DOM Elements
const authContainer    = document.getElementById('auth-container');
const appContainer     = document.getElementById('app-container');
const loginForm        = document.getElementById('login-form');
const registerForm     = document.getElementById('register-form');
const showRegisterLink = document.getElementById('show-register');
const showLoginLink    = document.getElementById('show-login');
const loginEmailInput  = document.getElementById('login-email');
const loginPasswordInput   = document.getElementById('login-password');
const registerEmailInput   = document.getElementById('register-email');
const registerPasswordInput= document.getElementById('register-password');
const loginError    = document.getElementById('login-error');
const registerError = document.getElementById('register-error');

const chatBox        = document.getElementById('chat-box');
const welcomeScreen  = document.getElementById('welcome-screen');
const userInput      = document.getElementById('user-input');
const sendBtn        = document.getElementById('send-btn');
const newChatBtn     = document.getElementById('new-chat-btn');
const chatList       = document.getElementById('chat-list');
const logoutBtn      = document.getElementById('logout-btn');
const activeChatTitle= document.getElementById('active-chat-title');
const userEmailEl    = document.getElementById('user-email');
const userAvatarEl   = document.getElementById('user-avatar');
const menuBtn        = document.getElementById('menu-btn');
const closeSidebarBtn= document.getElementById('close-sidebar-btn');
const sidebar        = document.getElementById('sidebar');

// State
let token         = localStorage.getItem('jurisai_token');
let activeSessionId = null;

// ============================================================
// Auth toggle
// ============================================================
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

// ============================================================
// Mobile sidebar
// ============================================================
if (menuBtn)        menuBtn.addEventListener('click', () => sidebar.classList.add('open'));
if (closeSidebarBtn) closeSidebarBtn.addEventListener('click', () => sidebar.classList.remove('open'));

// ============================================================
// Helpers
// ============================================================
function generateSessionId() {
    return crypto.randomUUID ? crypto.randomUUID()
        : Math.random().toString(36).slice(2) + Date.now().toString(36);
}

function showError(el, msg) {
    el.textContent = msg;
    el.classList.remove('hidden');
}

function hideError(el) { el.classList.add('hidden'); }

/** Show welcome state (no messages yet) */
function showWelcome() {
    chatBox.classList.add('hidden');
    chatBox.innerHTML = '';
    welcomeScreen.classList.remove('hidden');
    activeChatTitle.textContent = 'New Consultation';
}

/** Switch to chat view (messages visible) */
function showChatBox() {
    welcomeScreen.classList.add('hidden');
    chatBox.classList.remove('hidden');
}

// ============================================================
// Auth check on boot
// ============================================================
async function checkAuth() {
    if (!token) { showAuthScreen(); return; }
    try {
        const res = await fetch('/api/auth/me', {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        if (res.ok) {
            const user = await res.json();
            showAppScreen(user.email);
        } else { logout(); }
    } catch { logout(); }
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

// ============================================================
// Register
// ============================================================
registerForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    hideError(registerError);
    const email    = registerEmailInput.value.trim();
    const password = registerPasswordInput.value;

    if (password.length < 8) {
        showError(registerError, 'Password must be at least 8 characters.');
        return;
    }
    try {
        const res  = await fetch('/api/auth/register', {
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

// ============================================================
// Login
// ============================================================
loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    hideError(loginError);
    const email    = loginEmailInput.value.trim();
    const password = loginPasswordInput.value;

    try {
        const res  = await fetch('/api/auth/login', {
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

// ============================================================
// Logout
// ============================================================
function logout() {
    token = null;
    localStorage.removeItem('jurisai_token');
    loginEmailInput.value      = '';
    loginPasswordInput.value   = '';
    registerEmailInput.value   = '';
    registerPasswordInput.value= '';
    chatList.innerHTML = '';
    chatBox.innerHTML  = '';
    showAuthScreen();
}
logoutBtn.addEventListener('click', logout);

// ============================================================
// Add message bubble
// ============================================================
function addMessage(sender, text) {
    showChatBox();

    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${sender}-message`;

    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.textContent = sender === 'user' ? (userAvatarEl.textContent || 'U') : '⚖';

    const content = document.createElement('div');
    content.className = 'content';

    if (sender === 'ai') {
        content.innerHTML = marked.parse(text);
    } else {
        // Escape HTML in user text
        content.textContent = text;
    }

    if (sender === 'user') {
        msgDiv.appendChild(content);
        msgDiv.appendChild(avatar);
    } else {
        msgDiv.appendChild(avatar);
        msgDiv.appendChild(content);
    }

    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
    return msgDiv;
}

// Animated typing indicator
function addTypingIndicator() {
    showChatBox();
    const msgDiv = document.createElement('div');
    msgDiv.className = 'message ai-message typing';
    msgDiv.id = 'typing-indicator';

    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.textContent = '⚖';

    const content = document.createElement('div');
    content.className = 'content';
    content.innerHTML = `
        <div class="dot-flashing">
            <span></span><span></span><span></span>
        </div>
    `;

    msgDiv.appendChild(avatar);
    msgDiv.appendChild(content);
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
    return msgDiv;
}

function removeTypingIndicator() {
    const el = document.getElementById('typing-indicator');
    if (el) el.remove();
}

// ============================================================
// Starter prompt buttons
// ============================================================
document.querySelectorAll('.starter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const prompt = btn.dataset.prompt;
        if (prompt) {
            userInput.value = prompt;
            userInput.focus();
        }
    });
});

// ============================================================
// New Chat
// ============================================================
function startNewChat() {
    activeSessionId = generateSessionId();
    showWelcome();
    document.querySelectorAll('.chat-item').forEach(i => i.classList.remove('active'));
    if (sidebar) sidebar.classList.remove('open');
}
newChatBtn.addEventListener('click', startNewChat);

// ============================================================
// Load chat history sidebar list
// ============================================================
async function loadChatHistoryList() {
    try {
        const res = await fetch('/api/chats', {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        if (!res.ok) return;
        const chats = await res.json();
        chatList.innerHTML = '';

        chats.forEach(chat => {
            const item = document.createElement('div');
            item.className = `chat-item ${chat.id === activeSessionId ? 'active' : ''}`;
            item.dataset.id = chat.id;

            const titleSpan = document.createElement('span');
            titleSpan.className = 'chat-item-title';
            titleSpan.textContent = chat.title;
            titleSpan.title = chat.title;

            const deleteBtn = document.createElement('button');
            deleteBtn.className = 'btn-delete-chat';
            deleteBtn.innerHTML = '✕';
            deleteBtn.title = 'Delete consultation';
            deleteBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                deleteConsultation(chat.id);
            });

            item.appendChild(titleSpan);
            item.appendChild(deleteBtn);
            item.addEventListener('click', () => switchChat(chat.id, chat.title));
            chatList.appendChild(item);
        });
    } catch (e) {
        console.error('Failed to load chat history', e);
    }
}

// ============================================================
// Switch to an existing chat
// ============================================================
async function switchChat(sessionId, title) {
    activeSessionId = sessionId;
    activeChatTitle.textContent = title;

    document.querySelectorAll('.chat-item').forEach(i => {
        i.classList.toggle('active', i.dataset.id === sessionId);
    });

    chatBox.innerHTML = '';
    showChatBox();

    const loader = addTypingIndicator();

    try {
        const res = await fetch(`/api/chats/${sessionId}/messages`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });

        removeTypingIndicator();

        if (res.ok) {
            const messages = await res.json();
            if (messages.length === 0) {
                showWelcome();
            } else {
                messages.forEach(m => addMessage(m.role === 'user' ? 'user' : 'ai', m.content));
            }
        } else {
            showWelcome();
        }
    } catch {
        removeTypingIndicator();
        showWelcome();
    }

    if (sidebar) sidebar.classList.remove('open');
}

// ============================================================
// Delete chat
// ============================================================
async function deleteConsultation(sessionId) {
    if (!confirm('Delete this consultation? This cannot be undone.')) return;
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
        console.error('Failed to delete consultation', e);
    }
}

// ============================================================
// Send message
// ============================================================
async function sendMessage() {
    const text = userInput.value.trim();
    if (!text || !token) return;

    userInput.value = '';
    autoResize();

    addMessage('user', text);
    addTypingIndicator();

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

        if (res.ok) {
            const data = await res.json();
            addMessage('ai', data.response);
            loadChatHistoryList(); // Refresh sidebar (title may have been generated)
        } else {
            const err = await res.json().catch(() => ({}));
            addMessage('ai', `⚠️ ${err.detail || 'Something went wrong. Please try again.'}`);
        }
    } catch {
        removeTypingIndicator();
        addMessage('ai', '⚠️ Could not connect to the server. Please check your connection.');
    }
}

// ============================================================
// Auto-resize textarea
// ============================================================
function autoResize() {
    userInput.style.height = 'auto';
    userInput.style.height = Math.min(userInput.scrollHeight, 160) + 'px';
}

userInput.addEventListener('input', autoResize);

sendBtn.addEventListener('click', sendMessage);

userInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

// ============================================================
// Boot
// ============================================================
checkAuth();
