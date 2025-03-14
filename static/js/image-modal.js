document.addEventListener('DOMContentLoaded', function() {
    // Create modal container
    const modal = document.createElement('div');
    modal.className = 'modal';
    document.body.appendChild(modal);

    // Handle image click
    document.querySelectorAll('.noticia-imagen').forEach(img => {
        img.addEventListener('click', function() {
            const modalImg = document.createElement('img');
            modalImg.src = this.src;
            modal.innerHTML = '';
            modal.appendChild(modalImg);
            modal.style.display = 'block';
        });
    });

    // Close modal when clicking outside the image
    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });
});