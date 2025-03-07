document.addEventListener('DOMContentLoaded', function() {
    // Get the hamburger menu button and nav links
    const hamburgerMenu = document.querySelector('.hamburger-menu');
    const navLinks = document.querySelector('.nav-links');

    // Toggle mobile menu when hamburger is clicked
    hamburgerMenu.addEventListener('click', function() {
        // Toggle active class on nav links to show/hide the menu
        navLinks.classList.toggle('active');

        // Change icon between bars and times (x)
        const icon = hamburgerMenu.querySelector('i');
        if (icon.classList.contains('fa-bars')) {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-times');
        } else {
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        }
    });

    // Close menu when clicking outside
    document.addEventListener('click', function(event) {
        const isClickInside = navLinks.contains(event.target) ||
                              hamburgerMenu.contains(event.target);

        if (!isClickInside && navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');

            // Reset icon to bars
            const icon = hamburgerMenu.querySelector('i');
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        }
    });

    // Close menu when window is resized to desktop size
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) { // Adjust this breakpoint as needed
            navLinks.classList.remove('active');

            // Reset icon to bars
            const icon = hamburgerMenu.querySelector('i');
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars');
        }
    });
});
