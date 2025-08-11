// Main JavaScript for Astronaut Portfolio

// Carousel functionality
let currentIndex = 0;
let itemsPerView = 4;
let totalItems = 0;

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', function() {
    initializeCarousel();
    initializeScrollAnimations();
    initializeSmoothScroll();
    initializeParallax();
});

// Carousel Functions
function initializeCarousel() {
    const carouselTrack = document.querySelector('.carousel-track');
    const techItems = document.querySelectorAll('.tech-item');
    
    if (!carouselTrack || !techItems.length) return;
    
    totalItems = techItems.length;
    
    // Calculate items per view based on screen size
    updateItemsPerView();
    
    // Clone items for infinite scroll effect
    cloneCarouselItems();
    
    // Set initial position
    updateCarouselPosition();
    
    // Add resize listener
    window.addEventListener('resize', function() {
        updateItemsPerView();
        updateCarouselPosition();
    });
}

function updateItemsPerView() {
    const screenWidth = window.innerWidth;
    if (screenWidth < 576) {
        itemsPerView = 1;
    } else if (screenWidth < 768) {
        itemsPerView = 2;
    } else if (screenWidth < 1024) {
        itemsPerView = 3;
    } else {
        itemsPerView = 4;
    }
}

function cloneCarouselItems() {
    const carouselTrack = document.querySelector('.carousel-track');
    const techItems = document.querySelectorAll('.tech-item');
    
    // Clone first few items and append to end
    for (let i = 0; i < itemsPerView; i++) {
        const clone = techItems[i].cloneNode(true);
        clone.classList.add('cloned');
        carouselTrack.appendChild(clone);
    }
    
    // Clone last few items and prepend to beginning
    for (let i = totalItems - itemsPerView; i < totalItems; i++) {
        const clone = techItems[i].cloneNode(true);
        clone.classList.add('cloned');
        carouselTrack.insertBefore(clone, carouselTrack.firstChild);
    }
}

function moveCarousel(direction) {
    const carouselTrack = document.querySelector('.carousel-track');
    if (!carouselTrack) return;
    
    currentIndex += direction;
    
    // Smooth transition
    carouselTrack.style.transition = 'transform 0.5s ease';
    updateCarouselPosition();
    
    // Handle infinite scroll
    setTimeout(() => {
        if (currentIndex >= totalItems) {
            currentIndex = 0;
            carouselTrack.style.transition = 'none';
            updateCarouselPosition();
        } else if (currentIndex < 0) {
            currentIndex = totalItems - 1;
            carouselTrack.style.transition = 'none';
            updateCarouselPosition();
        }
    }, 500);
}

function updateCarouselPosition() {
    const carouselTrack = document.querySelector('.carousel-track');
    const techItem = document.querySelector('.tech-item');
    if (!carouselTrack || !techItem) return;
    
    const itemWidth = techItem.offsetWidth + 20; // 20px gap
    const offset = -((currentIndex + itemsPerView) * itemWidth);
    carouselTrack.style.transform = `translateX(${offset}px)`;
}

// Auto-play carousel
setInterval(() => {
    if (document.querySelector('.tech-carousel')) {
        moveCarousel(1);
    }
}, 4000);

// Scroll Animations
function initializeScrollAnimations() {
    const animatedElements = document.querySelectorAll('.glass-card, .tech-item, .project-card, .certificate-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-on-scroll', 'animated');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    animatedElements.forEach(el => {
        el.classList.add('animate-on-scroll');
        observer.observe(el);
    });
}

// Smooth Scrolling
function initializeSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            
            if (targetElement) {
                const headerHeight = document.querySelector('.navbar').offsetHeight;
                const targetPosition = targetElement.offsetTop - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// Parallax Effect
function initializeParallax() {
    const parallaxElements = document.querySelectorAll('.floating-element');
    
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        
        parallaxElements.forEach((element, index) => {
            const rate = scrolled * -0.5 * (index + 1);
            element.style.transform = `translateY(${rate}px)`;
        });
    });
}

// Navbar scroll effect
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(12, 12, 30, 0.95)';
            navbar.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.3)';
        } else {
            navbar.style.background = 'rgba(12, 12, 30, 0.9)';
            navbar.style.boxShadow = 'none';
        }
    }
});

// Loading animation
window.addEventListener('load', function() {
    const loader = document.querySelector('.loader');
    if (loader) {
        loader.style.opacity = '0';
        setTimeout(() => {
            loader.style.display = 'none';
        }, 500);
    }
    
    // Animate hero elements
    const heroElements = document.querySelectorAll('.hero-content > *');
    heroElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        setTimeout(() => {
            el.style.transition = 'all 0.6s ease';
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }, index * 200);
    });
});

// Add typing effect to hero title
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.innerHTML = '';
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// Initialize typing effect when hero is visible
const heroTitle = document.querySelector('.hero-title');
if (heroTitle) {
    const originalText = heroTitle.textContent;
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                setTimeout(() => {
                    typeWriter(heroTitle, originalText, 80);
                }, 1000);
                observer.disconnect();
            }
        });
    });
    
    observer.observe(heroTitle);
}

// Form enhancements
document.querySelectorAll('.glass-input').forEach(input => {
    input.addEventListener('focus', function() {
        this.parentElement.classList.add('focused');
    });
    
    input.addEventListener('blur', function() {
        if (!this.value) {
            this.parentElement.classList.remove('focused');
        }
    });
});

// Project card interactions
document.querySelectorAll('.project-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-15px) scale(1.02)';
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(-10px) scale(1)';
    });
});

// Copy to clipboard functionality
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        showToast('Copiado para a área de transferência! 🚀', 'success');
    }).catch(function(err) {
        console.error('Erro ao copiar: ', err);
        showToast('Erro ao copiar texto', 'error');
    });
}

// Toast notifications
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
        <div class="toast-content">
            <span>${message}</span>
            <button onclick="this.parentElement.parentElement.remove()">×</button>
        </div>
    `;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.add('show');
    }, 100);
    
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => {
            if (toast.parentElement) {
                toast.remove();
            }
        }, 300);
    }, 3000);
}

// Add CSS for toast notifications
const toastCSS = `
.toast {
    position: fixed;
    top: 100px;
    right: 20px;
    background: rgba(0, 212, 255, 0.9);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 10px;
    padding: 15px 20px;
    color: white;
    font-weight: 500;
    z-index: 9999;
    transform: translateX(400px);
    transition: transform 0.3s ease;
    max-width: 300px;
}

.toast.show {
    transform: translateX(0);
}

.toast-success {
    background: rgba(40, 167, 69, 0.9);
}

.toast-error {
    background: rgba(220, 53, 69, 0.9);
}

.toast-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.toast-content button {
    background: none;
    border: none;
    color: white;
    font-size: 18px;
    cursor: pointer;
    margin-left: 15px;
}
`;

// Inject toast CSS
const style = document.createElement('style');
style.textContent = toastCSS;
document.head.appendChild(style);

// Keyboard navigation
document.addEventListener('keydown', function(e) {
    // Navigate carousel with arrow keys
    if (e.key === 'ArrowLeft') {
        moveCarousel(-1);
    } else if (e.key === 'ArrowRight') {
        moveCarousel(1);
    }
    
    // Close modals with Escape key
    if (e.key === 'Escape') {
        const activeModal = document.querySelector('.modal.show');
        if (activeModal) {
            const modalInstance = bootstrap.Modal.getInstance(activeModal);
            modalInstance.hide();
        }
    }
});

// Performance optimization - lazy loading images
function lazyLoadImages() {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Initialize lazy loading
lazyLoadImages();

// Add mouse trail effect
let mouseTrail = [];
const maxTrailLength = 20;

document.addEventListener('mousemove', function(e) {
    mouseTrail.push({ x: e.clientX, y: e.clientY, time: Date.now() });
    
    if (mouseTrail.length > maxTrailLength) {
        mouseTrail.shift();
    }
    
    updateMouseTrail();
});

function updateMouseTrail() {
    const existingTrail = document.querySelectorAll('.mouse-trail-dot');
    existingTrail.forEach(dot => dot.remove());
    
    mouseTrail.forEach((point, index) => {
        const dot = document.createElement('div');
        dot.className = 'mouse-trail-dot';
        dot.style.cssText = `
            position: fixed;
            left: ${point.x}px;
            top: ${point.y}px;
            width: ${2 + index * 0.5}px;
            height: ${2 + index * 0.5}px;
            background: rgba(0, 212, 255, ${(index + 1) / maxTrailLength});
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            transform: translate(-50%, -50%);
            transition: opacity 0.1s ease;
        `;
        
        document.body.appendChild(dot);
        
        setTimeout(() => {
            if (dot.parentElement) {
                dot.style.opacity = '0';
                setTimeout(() => {
                    if (dot.parentElement) {
                        dot.remove();
                    }
                }, 100);
            }
        }, 100);
    });
}

console.log('🚀 Astronaut Portfolio initialized successfully!');
