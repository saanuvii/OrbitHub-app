document.addEventListener('DOMContentLoaded', () => {
    // Enable Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    // Handle saving favorites
    const favoriteBtns = document.querySelectorAll('.save-favorite-btn');
    favoriteBtns.forEach(btn => {
        btn.addEventListener('click', async (e) => {
            e.preventDefault();
            const btnEl = e.currentTarget;
            const dataStr = btnEl.getAttribute('data-payload');
            
            if (!dataStr) return;
            
            try {
                const payload = JSON.parse(dataStr);
                btnEl.disabled = true;
                btnEl.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Saving...';
                
                const response = await fetch('/favorites/add', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(payload)
                });
                
                const result = await response.json();
                
                if (result.success) {
                    showToast('Success', 'Added to favorites!', 'success');
                    btnEl.innerHTML = '<i class="fas fa-check text-success"></i> Saved';
                } else {
                    showToast('Error', result.message || 'Failed to save', 'danger');
                    btnEl.disabled = false;
                    btnEl.innerHTML = '<i class="far fa-heart"></i> Save';
                }
            } catch (error) {
                console.error('Error saving favorite:', error);
                showToast('Error', 'An error occurred', 'danger');
                btnEl.disabled = false;
                btnEl.innerHTML = '<i class="far fa-heart"></i> Save';
            }
        });
    });
});

// Toast notification function
function showToast(title, message, type = 'info') {
    const toastContainer = document.getElementById('toast-container');
    if (!toastContainer) return;
    
    const toastEl = document.createElement('div');
    toastEl.className = `toast bg-${type} text-white border-0`;
    toastEl.setAttribute('role', 'alert');
    toastEl.setAttribute('aria-live', 'assertive');
    toastEl.setAttribute('aria-atomic', 'true');
    
    toastEl.innerHTML = `
        <div class="toast-header bg-${type} text-white border-0">
            <strong class="me-auto">${title}</strong>
            <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
        <div class="toast-body">
            ${message}
        </div>
    `;
    
    toastContainer.appendChild(toastEl);
    const toast = new bootstrap.Toast(toastEl, { delay: 3000 });
    toast.show();
    
    toastEl.addEventListener('hidden.bs.toast', () => {
        toastEl.remove();
    });
}
