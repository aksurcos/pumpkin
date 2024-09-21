document.addEventListener('DOMContentLoaded', function() {
    const msgs = document.getElementById('msgs');
    if (msgs) {
        setTimeout(() => {
            const alerts = msgs.querySelectorAll('.alert');
            alerts.forEach(alert => {
                alert.style.transition = 'opacity 3s';
                alert.style.opacity = '0';
            });
        }, 5000);

        setTimeout(() => {
            msgs.remove();
        }, 8000);
    }
});

const dropdowns = document.querySelectorAll('.dropdown');
dropdowns.forEach(dropdown => {
    dropdown.addEventListener('mouseover', function() {
        this.querySelector('.dropdown-menu').classList.add('show');
    });
    dropdown.addEventListener('mouseout', function() {
        this.querySelector('.dropdown-menu').classList.remove('show');
    });
});