// DOM Elements
const authContainer = document.getElementById('auth-container');
const appContainer = document.getElementById('app-container');

const loginForm = document.getElementById('login-form');
const registerForm = document.getElementById('register-form');
const showRegisterLink = document.getElementById('show-register');
const showLoginLink = document.getElementById('show-login');

const loginEmailInput = document.getElementById('login-email');
const loginPasswordInput = document.getElementById('login-password');
const registerEmailInput = document.getElementById('register-email');
const registerPasswordInput = document.getElementById('register-password');

const loginError = document.getElementById('login-error');
const registerError = document.getElementById('register-error');

const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const newChatBtn = document.getElementById('new-chat-btn');
const chatList = document.getElementById('chat-list');
const logoutBtn = document.getElementById('logout-btn');
const activeChatTitle = document.getElementById('active-chat-title');
const userEmailEl = document.getElementById('user-email');
const userAvatarEl = document.getElementById('user-avatar');

// Sidebar toggle (Mobile)
const menuBtn = document.getElementById('menu-btn');
const closeSidebarBtn = document.getElementById('close-sidebar-btn');
const sidebar = document.getElementById('sidebar');

// State variables
let token = localStorage.getItem('jurisai_token');
let activeSessionId = null;

// Auth Forms Toggle
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

// Mobile Sidebar Logic
if (menuBtn && sidebar) {
    menuBtn.addEventListener('click', () => sidebar.classList.add('open'));
}
if (closeSidebarBtn && sidebar) {
    closeSidebarBtn.addEventListener('click', () => sidebar.classList.remove('open'));
}

// Generate unique session ID
function generateSessionId() {
    return Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
}

// Check if user is logged in
async function checkAuth() {
    if (!token) {
        showAuthScreen();
        return;
    }
    
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
    } catch (e) {
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

// Register
registerForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    registerError.classList.add('hidden');
    
    const email = registerEmailInput.value.trim();
    const password = registerPasswordInput.value;
    
    if (password.length < 8) {
        registerError.textContent = 'Password must be at least 8 characters long.';
        registerError.classList.remove('hidden');
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
            registerError.textContent = data.detail || 'Registration failed.';
            registerError.classList.remove('hidden');
        }
    } catch (err) {
        registerError.textContent = 'Network error. Please try again.';
        registerError.classList.remove('hidden');
    }
});

// Login
loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    loginError.classList.add('hidden');
    
    const email = loginEmailInput.value.trim();
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
            loginError.textContent = data.detail || 'Invalid email or password.';
            loginError.classList.remove('hidden');
        }
    } catch (err) {
        loginError.textContent = 'Network error. Please try again.';
        loginError.classList.remove('hidden');
    }
});

// Logout
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

// Add Message to Chat Box
function addMessage(sender, text) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${sender}-message`;

    const avatar = document.createElement('div');
    avatar.className = 'avatar';
    avatar.textContent = sender === 'user' ? 'U' : 'AI';

    const content = document.createElement('div');
    content.className = 'message-content';

    // Parse Markdown if AI, plain-escaped text if user
    if (sender === 'ai') {
        try {
            content.innerHTML = marked.parse(text || '');
        } catch (e) {
            content.textContent = text;
        }
    } else {
        content.textContent = text;
    }

    // Place avatar on left for AI, right for user
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

// Show/Hide Welcome Message
function displayWelcome() {
    chatBox.innerHTML = '';
    const welcomeText = `👋 Welcome to **JurisAI**, your elite AI Legal & Contract Advisor. I specialize in Indian Constitutional Law, Business/Corporate regulations, Property transactions, and Contract drafting/analysis.

Here is what I can help you with:
1. **Indian Constitution & Fundamental Rights**: Ask about any Article, Schedule, or Part of the Constitution, including rights, duties, and state policies.
2. **Contract Analysis & Review**: Paste a contract clause to analyze risks, identify ambiguities, or find missing protections.
3. **Contract Drafting Assistance**: Get help drafting clauses for NDAs, Employment Agreements, Service Contracts, and more.
4. **General Legal Proceedings & Compliance**: Ask about general legal procedures, business incorporation, property transactions, or court filings.

How can I assist you with your legal needs today?`;
    addMessage('ai', welcomeText);
}

// New Chat Button click handler
function startNewChat() {
    activeSessionId = generateSessionId();
    activeChatTitle.textContent = "New Consultation";
    displayWelcome();

    // Remove active styling from list items
    const items = chatList.querySelectorAll('.chat-item');
    items.forEach(i => i.classList.remove('active'));

    // Create a local sidebar entry so users can rename immediately
    createSidebarChat(activeSessionId, 'New Consultation', true);

    // Close sidebar on mobile if open
    if (sidebar) sidebar.classList.remove('open');
}
newChatBtn.addEventListener('click', startNewChat);

// Load previous chats lists
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
    // Avoid duplicates
    if (!sessionId) return;
    if (chatList.querySelector(`.chat-item[data-id="${sessionId}"]`)) return;

    const item = document.createElement('div');
    item.className = `chat-item ${sessionId === activeSessionId ? 'active' : ''}`;
    item.dataset.id = sessionId;

    const titleSpan = document.createElement('span');
    titleSpan.className = 'chat-item-title';
    titleSpan.textContent = title || 'Untitled consultation';
    titleSpan.title = title || '';

    const deleteBtn = document.createElement('button');
    deleteBtn.className = 'btn-delete-chat';
    deleteBtn.innerHTML = '🗑️';
    deleteBtn.title = 'Delete consultation';

    deleteBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        deleteConsultation(sessionId);
    });

    // Click to switch
    item.addEventListener('click', () => switchChat(sessionId, titleSpan.textContent));

    // Double-click to rename
    titleSpan.addEventListener('dblclick', (e) => {
        e.stopPropagation();
        const input = document.createElement('input');
        input.type = 'text';
        input.className = 'chat-title-edit';
        input.value = titleSpan.textContent;
        input.addEventListener('keydown', async (ev) => {
            if (ev.key === 'Enter') {
                input.blur();
            }
        });
        input.addEventListener('blur', async () => {
            const newTitle = input.value.trim() || 'Untitled consultation';
            titleSpan.textContent = newTitle;
            titleSpan.title = newTitle;
            item.replaceChild(titleSpan, input);
            // Persist to backend if this chat belongs to server
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

// Switch Active Chat
async function switchChat(sessionId, title) {
    activeSessionId = sessionId;
    activeChatTitle.textContent = title;
    
    // Set active item styling
    const items = chatList.querySelectorAll('.chat-item');
    items.forEach(i => {
        if (i.dataset.id === sessionId) {
            i.classList.add('active');
        } else {
            i.classList.remove('active');
        }
    });
    
    chatBox.innerHTML = '';
    
    // Show typing state or loader
    const loaderDiv = document.createElement('div');
    loaderDiv.className = 'message ai-message typing';
    loaderDiv.innerHTML = '<div class="avatar">AI</div><div class="content">Retrieving legal consultation records...</div>';
    chatBox.appendChild(loaderDiv);
    
    try {
        const res = await fetch(`/api/chats/${sessionId}/messages`, {
            headers: { 'Authorization': `Bearer ${token}` }
        });
        
        chatBox.removeChild(loaderDiv);
        
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
    } catch (e) {
        chatBox.removeChild(loaderDiv);
        displayWelcome();
    }
    
    // Close sidebar on mobile
    if (sidebar) sidebar.classList.remove('open');
}

// Delete Chat Session
async function deleteConsultation(sessionId) {
    if (!confirm('Are you sure you want to delete this consultation record?')) return;
    
    try {
        const res = await fetch(`/api/chats/${sessionId}`, {
            method: 'DELETE',
            headers: { 'Authorization': `Bearer ${token}` }
        });
        
        if (res.ok) {
            if (activeSessionId === sessionId) {
                startNewChat();
            }
            loadChatHistoryList();
        }
    } catch (e) {
        console.error('Failed to delete chat session', e);
    }
}

// Send Message
async function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;
    
    addMessage('user', text);
    userInput.value = '';
    
    // Show typing indicator
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message ai-message typing';
    typingDiv.innerHTML = '<div class="avatar">AI</div><div class="content">Analyzing legal precedents...</div>';
    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
    
    try {
        const res = await fetch('/api/chat', {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${token}`
            },
            body: JSON.stringify({ message: text, session_id: activeSessionId })
        });
        
        chatBox.removeChild(typingDiv);
        
        if (res.ok) {
            const data = await res.json();
            addMessage('ai', data.response);
            // Refresh history list (in case a new chat is added or title needs updating)
            loadChatHistoryList();
        } else {
            const errData = await res.json();
            addMessage('ai', `Error processing query: ${errData.detail || 'Internal server error.'}`);
        }
    } catch (error) {
        chatBox.removeChild(typingDiv);
        addMessage('ai', 'Error connecting to the server.');
    }
}

// Click listener for interactive follow-up suggestions
sendBtn.addEventListener('click', sendMessage);
userInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
    }
});

// Init on boot
checkAuth();
