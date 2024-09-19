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