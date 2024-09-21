document.addEventListener('DOMContentLoaded', function() {
    var msgs = document.getElementById('msgs');
    if (msgs) {
        setTimeout(function() {
            var alerts = msgs.querySelectorAll('.alert');
            alerts.forEach(function(alert) {
                alert.style.transition = 'opacity 3s';
                alert.style.opacity = '0';
            });
        }, 5000);

        setTimeout(function() {
            msgs.remove();
        }, 8000);
    }
});