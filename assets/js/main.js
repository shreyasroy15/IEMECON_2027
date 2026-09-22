// Countdown Timer
const countdownDate = new Date("February 4, 2027 09:00:00").getTime();

const x = setInterval(function () {
    const now = new Date().getTime();
    const distance = countdownDate - now;

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));
    const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((distance % (1000 * 60)) / 1000);

    if (document.getElementById("days")) {
        document.getElementById("days").innerHTML = days < 10 ? "0" + days : days;
        document.getElementById("hours").innerHTML = hours < 10 ? "0" + hours : hours;
        document.getElementById("minutes").innerHTML = minutes < 10 ? "0" + minutes : minutes;
        document.getElementById("seconds").innerHTML = seconds < 10 ? "0" + seconds : seconds;
    }

    if (distance < 0) {
        clearInterval(x);
        if (document.getElementById("countdown")) {
            document.getElementById("countdown").innerHTML = "CONFERENCE STARTED";
        }
    }
}, 1000);

// Sticky Navbar effect
window.onscroll = function () {
    const nav = document.querySelector('nav');
    const isMobile = window.innerWidth <= 992;
    
    if (window.pageYOffset > 50) {
        nav.style.height = isMobile ? "60px" : "65px";
        nav.style.background = "rgba(255, 255, 255, 0.98)";
        nav.style.boxShadow = "0 5px 20px rgba(0,0,0,0.1)";
    } else {
        nav.style.height = isMobile ? "70px" : "80px";
        nav.style.background = isMobile ? "rgba(255, 255, 255, 0.9)" : "rgba(255, 255, 255, 0.8)";
        nav.style.boxShadow = "none";
    }
};

// Application Logic
document.addEventListener('DOMContentLoaded', () => {

    // Mobile Menu Functionality with Anime.js
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const closeBtn = document.querySelector('.close-menu');
    const mobileMenu = document.querySelector('.mobile-menu');
    const mobileLinks = document.querySelectorAll('.mobile-nav-links > li');
    const mobileFooter = document.querySelector('.mobile-menu-footer');
    let isMenuOpen = false;

    const toggleMenu = (open) => {
        isMenuOpen = open;
        if (open) {
            mobileMenu.classList.add('active');
            document.body.classList.add('menu-open');
            
            // Entrance Animation
            anime.timeline({ easing: 'easeOutExpo' })
                .add({
                    targets: '.mobile-menu-header',
                    translateY: [-50, 0],
                    opacity: [0, 1],
                    duration: 800
                })
                .add({
                    targets: mobileLinks,
                    translateX: [50, 0],
                    opacity: [0, 1],
                    delay: anime.stagger(100),
                    duration: 800
                }, '-=400')
                .add({
                    targets: mobileFooter,
                    translateY: [20, 0],
                    opacity: [0, 1],
                    duration: 600
                }, '-=400');
        } else {
            mobileMenu.classList.remove('active');
            document.body.classList.remove('menu-open');
        }
    };

    if (menuBtn && mobileMenu) {
        menuBtn.addEventListener('click', () => toggleMenu(true));
    }

    if (closeBtn) {
        closeBtn.addEventListener('click', () => toggleMenu(false));
    }

    // Accordion Logic for Mobile Menu
    const dropdownTitles = document.querySelectorAll('.mobile-dropdown-title, .mobile-nested-title');
    dropdownTitles.forEach(title => {
        title.addEventListener('click', (e) => {
            const content = title.nextElementSibling;
            const isOpen = title.classList.contains('active');
            
            // Toggle current
            title.classList.toggle('active');
            
            if (!isOpen) {
                content.style.display = 'block';
                const height = content.scrollHeight;
                content.style.height = '0px';
                
                anime({
                    targets: content,
                    height: [0, height],
                    opacity: [0, 1],
                    duration: 500,
                    easing: 'easeOutQuart'
                });
            } else {
                anime({
                    targets: content,
                    height: 0,
                    opacity: 0,
                    duration: 400,
                    easing: 'easeInQuart',
                    complete: () => {
                        content.style.display = 'none';
                    }
                });
            }
            
            e.stopPropagation();
        });
    });

    // Close menu when a simple link is clicked
    const simpleLinks = document.querySelectorAll('.mobile-nav-links a:not(.mobile-dropdown-title a)');
    simpleLinks.forEach(link => {
        link.addEventListener('click', () => toggleMenu(false));
    });

    // Carousel Functionality
    const carousel = document.querySelector('.carousel');
    const items = document.querySelectorAll('.carousel-item');
    const prevBtn = document.querySelector('.prev');
    const nextBtn = document.querySelector('.next');
    let currentIndex = 0;

    if (carousel && items.length > 0) {
        const updateCarousel = () => {
            const itemWidth = items[0].offsetWidth;
            const gap = 30; // Matches CSS gap
            const scrollAmount = currentIndex * (itemWidth + gap);
            carousel.style.transform = `translateX(-${scrollAmount}px)`;
        };

        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                const itemsPerView = window.innerWidth >= 992 ? 2 : 1;
                if (currentIndex < items.length - itemsPerView) {
                    currentIndex++;
                } else {
                    currentIndex = 0; // Loop back
                }
                updateCarousel();
            });
        }

        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                const itemsPerView = window.innerWidth >= 992 ? 2 : 1;
                if (currentIndex > 0) {
                    currentIndex--;
                } else {
                    currentIndex = items.length - itemsPerView; // Loop to end
                }
                updateCarousel();
            });
        }

        // Auto-slide
        let autoSlide = setInterval(() => {
            const itemsPerView = window.innerWidth >= 992 ? 2 : 1;
            if (currentIndex < items.length - itemsPerView) {
                currentIndex++;
            } else {
                currentIndex = 0;
            }
            updateCarousel();
        }, 5000);

        // Reset auto-slide on interaction
        const resetAutoSlide = () => {
            clearInterval(autoSlide);
            autoSlide = setInterval(() => {
                const itemsPerView = window.innerWidth >= 992 ? 2 : 1;
                if (currentIndex < items.length - itemsPerView) {
                    currentIndex++;
                } else {
                    currentIndex = 0;
                }
                updateCarousel();
            }, 5000);
        };

        if (nextBtn) nextBtn.addEventListener('click', resetAutoSlide);
        if (prevBtn) prevBtn.addEventListener('click', resetAutoSlide);

        // Update on resize
        window.addEventListener('resize', () => {
            currentIndex = 0; // Reset to avoid alignment issues on resize
            updateCarousel();
        });
    }

    // Hero Slider Functionality
    const heroSlides = document.querySelectorAll('.hero-slide');
    const heroDots = document.querySelectorAll('.dot');
    const heroNext = document.querySelector('.hero-next');
    const heroPrev = document.querySelector('.hero-prev');
    let heroIndex = 0;
    let heroAutoPlay;

    if (heroSlides.length > 0) {
        const showHeroSlide = (index) => {
            heroSlides.forEach(slide => slide.classList.remove('active'));
            heroDots.forEach(dot => dot.classList.remove('active'));
            
            heroSlides[index].classList.add('active');
            heroDots[index].classList.add('active');
            
            // Text entrance animation
            const content = heroSlides[index].querySelector('.hero-content');
            anime({
                targets: content.children,
                translateY: [30, 0],
                opacity: [0, 1],
                delay: anime.stagger(150),
                duration: 800,
                easing: 'easeOutExpo'
            });
        };

        const nextHeroSlide = () => {
            heroIndex = (heroIndex + 1) % heroSlides.length;
            showHeroSlide(heroIndex);
        };

        const prevHeroSlide = () => {
            heroIndex = (heroIndex - 1 + heroSlides.length) % heroSlides.length;
            showHeroSlide(heroIndex);
        };

        if (heroNext) heroNext.addEventListener('click', () => {
            nextHeroSlide();
            resetHeroAuto();
        });

        if (heroPrev) heroPrev.addEventListener('click', () => {
            prevHeroSlide();
            resetHeroAuto();
        });

        heroDots.forEach((dot, idx) => {
            dot.addEventListener('click', () => {
                heroIndex = idx;
                showHeroSlide(heroIndex);
                resetHeroAuto();
            });
        });

        const resetHeroAuto = () => {
            clearInterval(heroAutoPlay);
            heroAutoPlay = setInterval(nextHeroSlide, 8000);
        };

        heroAutoPlay = setInterval(nextHeroSlide, 8000);
        
        // Initial animation for first slide
        showHeroSlide(0);
    }
});
