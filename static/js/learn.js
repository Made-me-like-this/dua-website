document.addEventListener('DOMContentLoaded', function() {
    // Toggle section content
    const sectionHeaders = document.querySelectorAll('.learn-section-header');

    sectionHeaders.forEach(header => {
        header.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const contentElement = document.getElementById(targetId);
            const chevronIcon = this.querySelector('.fa-chevron-down');
            const section = this.closest('.learn-section');

            // Toggle the active class on content
            contentElement.classList.toggle('active');

            // Toggle chevron icon rotation
            chevronIcon.classList.toggle('rotate');

            // Toggle active class on section
            section.classList.toggle('active');

            // Toggle max-height for smooth animation
            if (contentElement.classList.contains('active')) {
                contentElement.style.maxHeight = contentElement.scrollHeight + 'px';
            } else {
                contentElement.style.maxHeight = '0';
            }

            // Close other sections (optional)
            // closeOtherSections(targetId);
        });
    });

    // Toggle card content
    const cardHeaders = document.querySelectorAll('.learn-card-header');

    cardHeaders.forEach(header => {
        header.addEventListener('click', function(e) {
            // Stop event propagation to prevent parent section toggle
            e.stopPropagation();

            const targetId = this.getAttribute('data-target');
            const contentElement = document.getElementById(targetId);
            const chevronIcon = this.querySelector('.fa-chevron-down');

            // Toggle the active class
            contentElement.classList.toggle('active');

            // Toggle chevron icon rotation
            chevronIcon.classList.toggle('rotate');

            // Toggle max-height for smooth animation
            if (contentElement.classList.contains('active')) {
                contentElement.style.maxHeight = contentElement.scrollHeight + 'px';
            } else {
                contentElement.style.maxHeight = '0';
            }
        });
    });

    // Function to close other sections
    function closeOtherSections(currentId) {
        const allSectionContents = document.querySelectorAll('.learn-section-content');

        allSectionContents.forEach(content => {
            if (content.id !== currentId && content.classList.contains('active')) {
                content.classList.remove('active');
                content.style.maxHeight = '0';

                const parentSection = content.closest('.learn-section');
                const header = parentSection.querySelector('.learn-section-header');
                const chevronIcon = header.querySelector('.fa-chevron-down');

                parentSection.classList.remove('active');
                chevronIcon.classList.remove('rotate');
            }
        });
    }

    // Open section if URL has hash
    if (window.location.hash) {
        const targetSection = document.querySelector(`[data-target="${window.location.hash.substring(1)}"]`);
        if (targetSection) {
            // Simulate click to open the section
            setTimeout(() => targetSection.click(), 100);

            // Scroll to section
            setTimeout(() => {
                targetSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }, 200);
        }
    }

    // Add search functionality for the page content
    const searchInput = document.getElementById('learn-search');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase().trim();

            if (query.length < 2) {
                // Reset highlights
                resetHighlights();
                return;
            }

            // Search in all content
            const allContent = document.querySelectorAll('.learn-card-content p, .learn-card-content li, .hadith-text, .hadith-lesson');
            let foundCount = 0;

            allContent.forEach(element => {
                const text = element.innerText;
                if (text.toLowerCase().includes(query)) {
                    foundCount++;

                    // Highlight matching text
                    element.innerHTML = highlightText(text, query);

                    // Open parent sections and cards
                    openParentContainers(element);
                }
            });

            // Show search results count
            const searchResults = document.getElementById('search-results-count');
            if (searchResults) {
                searchResults.textContent = `Found ${foundCount} matches`;
                searchResults.style.display = foundCount > 0 ? 'block' : 'none';
            }
        });
    }

    function resetHighlights() {
        const highlightedElements = document.querySelectorAll('.learn-card-content p, .learn-card-content li, .hadith-text, .hadith-lesson');
        highlightedElements.forEach(el => {
            el.innerHTML = el.innerText;
        });

        const searchResults = document.getElementById('search-results-count');
        if (searchResults) {
            searchResults.style.display = 'none';
        }
    }

    function highlightText(text, query) {
        const regex = new RegExp(`(${query})`, 'gi');
        return text.replace(regex, '<span class="highlight">$1</span>');
    }

    function openParentContainers(element) {
        // Open the parent card
        const parentCard = element.closest('.learn-card');
        if (parentCard) {
            const cardContent = parentCard.querySelector('.learn-card-content');
            const cardHeader = parentCard.querySelector('.learn-card-header');
            const chevronIcon = cardHeader.querySelector('.fa-chevron-down');

            cardContent.classList.add('active');
            cardContent.style.maxHeight = cardContent.scrollHeight + 'px';
            chevronIcon.classList.add('rotate');
        }

        // Open the parent section
        const parentSection = element.closest('.learn-section');
        if (parentSection) {
            const sectionContent = parentSection.querySelector('.learn-section-content');
            const sectionHeader = parentSection.querySelector('.learn-section-header');
            const sectionChevron = sectionHeader.querySelector('.fa-chevron-down');

            sectionContent.classList.add('active');
            sectionContent.style.maxHeight = sectionContent.scrollHeight + 'px';
            sectionChevron.classList.add('rotate');
            parentSection.classList.add('active');
        }
    }
});
const chatBubble = document.querySelector('.chat-bubble');
const chatWindow = document.querySelector('.chat-window');
chatBubble.addEventListener('click', () => { chatWindow.classList.toggle('visible'); });