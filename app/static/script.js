document.addEventListener('DOMContentLoaded', function() {
    // Cache DOM elements
    const uploadForm = document.querySelector('#file-upload form');
    const chatForm = document.getElementById('chat-form');
    const chatHistory = document.getElementById('chat-history');
    const chatInput = document.getElementById('chat-input');
    const modelSelect = document.getElementById('model-select');
    const temperature = document.getElementById('temperature');
    const maxTokens = document.getElementById('max-tokens');
    const dataPreview = document.getElementById('data-preview');

    // Update temperature display
    temperature.addEventListener('input', function(e) {
        document.getElementById('temp-value').textContent = e.target.value;
    });
    
    // File Upload Handler
    uploadForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const formData = new FormData(this);
        const uploadBtn = this.querySelector('button[type="submit"]');
        
        // Disable upload button and show loading state
        uploadBtn.disabled = true;
        uploadBtn.innerHTML = '<span class="loading"></span> Uploading...';
        
        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            if (data.success) {
                showAlert('success', 'File uploaded successfully!');
                
                // Show and update data preview
                if (data.preview) {
                    dataPreview.classList.remove('d-none');
                    dataPreview.querySelector('.table-responsive').innerHTML = data.preview;
                }
                
                // Enable chat interface
                chatInput.disabled = false;
                chatForm.querySelector('button').disabled = false;
            } else {
                showAlert('danger', data.error || 'Error uploading file');
            }
        } catch (error) {
            showAlert('danger', 'Error uploading file: ' + error.message);
        } finally {
            uploadBtn.disabled = false;
            uploadBtn.innerHTML = 'Upload';
        }
    });
    
    // Chat Form Handler
    chatForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const message = chatInput.value.trim();
        if (!message) return;
        
        // Add user message to chat
        appendMessage('user', message);
        chatInput.value = '';
        
        const sendBtn = this.querySelector('button[type="submit"]');
        sendBtn.disabled = true;
        sendBtn.innerHTML = '<span class="loading"></span>';
        
        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: message,
                    model: modelSelect.value,
                    temperature: parseFloat(temperature.value),
                    maxTokens: parseInt(maxTokens.value)
                })
            });
            
            const data = await response.json();
            if (data.success) {
                appendMessage('assistant', data.response);
            } else {
                showAlert('danger', data.error || 'Error getting response');
            }
        } catch (error) {
            showAlert('danger', 'Error: ' + error.message);
        } finally {
            sendBtn.disabled = false;
            sendBtn.innerHTML = 'Send';
        }
    });
    
    // Helper function to append messages to chat
    function appendMessage(role, content) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}-message`;
        
        // Format code blocks if present
        content = content.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
        
        messageDiv.innerHTML = `
            <div class="message-header">
                <strong>${role === 'user' ? 'You' : 'Assistant'}</strong>
                <small class="text-muted">${new Date().toLocaleTimeString()}</small>
            </div>
            <div class="message-content">${content}</div>
        `;
        
        chatHistory.appendChild(messageDiv);
        chatHistory.scrollTop = chatHistory.scrollHeight;
    }
    
    // Helper function to show alerts
    function showAlert(type, message) {
        const alertDiv = document.createElement('div');
        alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
        alertDiv.innerHTML = `
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        `;
        
        // Insert alert at the top of the container
        const container = document.querySelector('.container');
        container.insertBefore(alertDiv, container.firstChild);
        
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            alertDiv.remove();
        }, 5000);
    }
    
    // Initialize: disable chat until file is uploaded
    chatInput.disabled = true;
    chatForm.querySelector('button').disabled = true;
});