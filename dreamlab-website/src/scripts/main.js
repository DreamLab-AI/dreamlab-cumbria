// ===== DreamLab AI Consulting Website JavaScript ===== //

// Initialize AOS (Animate On Scroll)
document.addEventListener('DOMContentLoaded', function() {
  AOS.init({
    duration: 800,
    easing: 'ease-in-out',
    once: true,
    offset: 100
  });
});

// ===== Alpine.js Components ===== //

// Contact Form Component
function contactForm() {
  return {
    form: {
      name: '',
      email: '',
      phone: '',
      company: '',
      interest: '',
      message: '',
      newsletter: false
    },
    submitting: false,
    submitted: false,
    error: null,

    async submitForm() {
      if (this.submitting) return;
      
      // Basic validation
      if (!this.form.name || !this.form.email || !this.form.interest) {
        this.error = 'Please fill in all required fields.';
        return;
      }

      this.submitting = true;
      this.error = null;

      try {
        // Simulate form submission
        await new Promise(resolve => setTimeout(resolve, 2000));
        
        // In a real implementation, you would send the data to your backend
        console.log('Form submitted:', this.form);
        
        this.submitted = true;
        this.resetForm();
        
        // Show success message
        this.showNotification('Thank you! Your message has been sent successfully.', 'success');
        
      } catch (error) {
        console.error('Form submission error:', error);
        this.error = 'Sorry, there was an error sending your message. Please try again.';
        this.showNotification('Error sending message. Please try again.', 'error');
      } finally {
        this.submitting = false;
      }
    },

    resetForm() {
      this.form = {
        name: '',
        email: '',
        phone: '',
        company: '',
        interest: '',
        message: '',
        newsletter: false
      };
    },

    showNotification(message, type) {
      // Create notification element
      const notification = document.createElement('div');
      notification.className = `notification notification--${type}`;
      notification.innerHTML = `
        <div class="notification-content">
          <span class="notification-message">${message}</span>
          <button class="notification-close" onclick="this.parentElement.parentElement.remove()">×</button>
        </div>
      `;
      
      // Add styles
      notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: ${type === 'success' ? '#27ae60' : '#e74c3c'};
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        z-index: 1000;
        transform: translateX(400px);
        transition: transform 0.3s ease-in-out;
        max-width: 400px;
      `;
      
      // Add to page
      document.body.appendChild(notification);
      
      // Animate in
      setTimeout(() => {
        notification.style.transform = 'translateX(0)';
      }, 100);
      
      // Auto remove after 5 seconds
      setTimeout(() => {
        notification.style.transform = 'translateX(400px)';
        setTimeout(() => {
          if (notification.parentElement) {
            notification.remove();
          }
        }, 300);
      }, 5000);
    }
  };
}

// ===== Smooth Scrolling ===== //
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      const navHeight = document.querySelector('.navbar').offsetHeight;
      const targetPosition = target.offsetTop - navHeight;
      
      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    }
  });
});

// ===== Navbar Scroll Effect ===== //
let lastScrollTop = 0;
const navbar = document.querySelector('.navbar');

window.addEventListener('scroll', function() {
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  
  // Add/remove scrolled class for styling
  if (scrollTop > 100) {
    navbar.classList.add('navbar--scrolled');
  } else {
    navbar.classList.remove('navbar--scrolled');
  }
  
  // Hide/show navbar on scroll (optional)
  if (scrollTop > lastScrollTop && scrollTop > 200) {
    navbar.style.transform = 'translateY(-100%)';
  } else {
    navbar.style.transform = 'translateY(0)';
  }
  
  lastScrollTop = scrollTop;
});

// ===== Gallery Functionality ===== //
document.addEventListener('DOMContentLoaded', function() {
  const galleryThumbs = document.querySelectorAll('.gallery-thumbs img');
  const galleryMain = document.querySelector('.gallery-main img');
  
  if (galleryThumbs.length && galleryMain) {
    galleryThumbs.forEach(thumb => {
      thumb.addEventListener('click', function() {
        const newSrc = this.src;
        const newAlt = this.alt;
        
        // Add fade effect
        galleryMain.style.opacity = '0.5';
        
        setTimeout(() => {
          galleryMain.src = newSrc;
          galleryMain.alt = newAlt;
          galleryMain.style.opacity = '1';
        }, 200);
        
        // Update active state
        galleryThumbs.forEach(t => t.classList.remove('active'));
        this.classList.add('active');
      });
    });
  }
});

// ===== Hero Video Background ===== //
document.addEventListener('DOMContentLoaded', function() {
  const heroVideo = document.querySelector('.hero-video');
  
  if (heroVideo) {
    // Pause video on mobile to save bandwidth
    if (window.innerWidth < 768) {
      heroVideo.style.display = 'none';
      
      // Add fallback background image
      const heroBackground = document.querySelector('.hero-background');
      heroBackground.style.backgroundImage = 'url("/assets/images/hero-fallback.jpg")';
      heroBackground.style.backgroundSize = 'cover';
      heroBackground.style.backgroundPosition = 'center';
    }
    
    // Handle video load errors
    heroVideo.addEventListener('error', function() {
      console.warn('Hero video failed to load, using fallback');
      this.style.display = 'none';
      
      const heroBackground = document.querySelector('.hero-background');
      heroBackground.style.backgroundImage = 'url("/assets/images/hero-fallback.jpg")';
      heroBackground.style.backgroundSize = 'cover';
      heroBackground.style.backgroundPosition = 'center';
    });
  }
});

// ===== Intersection Observer for Animations ===== //
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('animate-in');
    }
  });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', function() {
  const animateElements = document.querySelectorAll('.feature-card, .training-card, .stat-item');
  animateElements.forEach(el => observer.observe(el));
});

// ===== Training Program Filtering (Optional Enhancement) ===== //
function initializeTrainingFilter() {
  const filterButtons = document.querySelectorAll('.training-filter-btn');
  const trainingCards = document.querySelectorAll('.training-card');
  
  if (filterButtons.length && trainingCards.length) {
    filterButtons.forEach(button => {
      button.addEventListener('click', function() {
        const filter = this.dataset.filter;
        
        // Update active button
        filterButtons.forEach(btn => btn.classList.remove('active'));
        this.classList.add('active');
        
        // Filter cards
        trainingCards.forEach(card => {
          if (filter === 'all' || card.dataset.category === filter) {
            card.style.display = 'block';
            card.style.animation = 'fadeInUp 0.5s ease-in-out';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }
}

// ===== Loading Animation ===== //
window.addEventListener('load', function() {
  const loader = document.querySelector('.loader');
  if (loader) {
    loader.style.opacity = '0';
    setTimeout(() => {
      loader.style.display = 'none';
    }, 500);
  }
  
  // Trigger entrance animations
  document.body.classList.add('loaded');
});

// ===== Performance Optimizations ===== //

// Lazy load images
if ('IntersectionObserver' in window) {
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.classList.remove('lazy');
        imageObserver.unobserve(img);
      }
    });
  });

  document.querySelectorAll('img[data-src]').forEach(img => {
    imageObserver.observe(img);
  });
}

// Preload critical resources
function preloadCriticalResources() {
  const criticalImages = [
    '/assets/images/hero-background.jpg',
    '/assets/images/accommodation-main.jpg'
  ];
  
  criticalImages.forEach(src => {
    const link = document.createElement('link');
    link.rel = 'preload';
    link.as = 'image';
    link.href = src;
    document.head.appendChild(link);
  });
}

// ===== Accessibility Enhancements ===== //

// Skip to main content
document.addEventListener('DOMContentLoaded', function() {
  const skipLink = document.createElement('a');
  skipLink.href = '#main';
  skipLink.textContent = 'Skip to main content';
  skipLink.className = 'skip-link sr-only';
  skipLink.style.cssText = `
    position: absolute;
    top: -40px;
    left: 6px;
    background: var(--color-primary);
    color: white;
    padding: 8px;
    text-decoration: none;
    border-radius: 4px;
    z-index: 1000;
    transition: top 0.3s;
  `;
  
  skipLink.addEventListener('focus', function() {
    this.style.top = '6px';
    this.classList.remove('sr-only');
  });
  
  skipLink.addEventListener('blur', function() {
    this.style.top = '-40px';
    this.classList.add('sr-only');
  });
  
  document.body.insertBefore(skipLink, document.body.firstChild);
});

// Focus management for mobile menu
document.addEventListener('DOMContentLoaded', function() {
  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.querySelector('.nav-menu');
  const navLinks = document.querySelectorAll('.nav-link');
  
  if (navToggle && navMenu) {
    navToggle.addEventListener('click', function() {
      const isOpen = navMenu.classList.contains('nav-menu--open');
      
      if (isOpen) {
        // Focus first nav link when menu opens
        setTimeout(() => {
          navLinks[0]?.focus();
        }, 100);
      }
    });
    
    // Close menu on escape key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && navMenu.classList.contains('nav-menu--open')) {
        navToggle.click();
        navToggle.focus();
      }
    });
  }
});

// ===== Error Handling ===== //
window.addEventListener('error', function(e) {
  console.error('JavaScript error:', e.error);
  
  // Log to analytics service in production
  // analytics.track('javascript_error', {
  //   message: e.message,
  //   filename: e.filename,
  //   lineno: e.lineno,
  //   colno: e.colno
  // });
});

// ===== Initialize Everything ===== //
document.addEventListener('DOMContentLoaded', function() {
  preloadCriticalResources();
  initializeTrainingFilter();
  
  console.log('DreamLab AI Consulting website initialized successfully');
});

// ===== Export for module use ===== //
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    contactForm,
    initializeTrainingFilter,
    preloadCriticalResources
  };
}