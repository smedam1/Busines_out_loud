
from .hero_section import get_magazine_homepage_hero_section
from .more_magazines import get_more_magazines
from .magazine_page_hero_section import get_magazine_hero_section

EMPTY_MAGAZINE_TEMPLATE= """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Magazine</title>
    <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
    <script src="https://unpkg.com/@phosphor-icons/web@2.0.3"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&family=IBM+Plex+Sans:wght@600&family=Inter:wght@500&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,800&family=Roboto:wght@500&display=swap"
      rel="stylesheet"
    />
    <link rel="icon" type="image/png" href="/static/icon/website_icon.png" />

    <!-- PDF.js and Page Flip libraries -->
    <script src="https://cdn.jsdelivr.net/npm/pdfjs-dist@3.11.174/build/pdf.min.js"></script>
    <script>
      pdfjsLib.GlobalWorkerOptions.workerSrc =
        "https://cdn.jsdelivr.net/npm/pdfjs-dist@3.11.174/build/pdf.worker.min.js";
    </script>
    <link
      rel="stylesheet"
      type="text/css"
      href="https://cdn.jsdelivr.net/npm/page-flip/dist/css/page-flip.min.css"
    />

    <style>
      /* Original non-header styles from magazine_page_read_only.html */
      /* @media screen and (min-width: 1024px) {
        body {
            transform: scale(1.33);
            transform-origin: 0 0;
            width: 75.3%;
        }
    } */
      ::-webkit-scrollbar {
        display: none;
      }
      body {
        -ms-overflow-style: none;
        scrollbar-width: none;
      }
      .gradient-bg {
        background: linear-gradient(146.84deg, #3533cd 0%, #1b1a67 95.28%);
      }
      .gradient-text {
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-fill-color: transparent;
      }
      .strip-startups {
        background-image: linear-gradient(
          93.43deg,
          #000000 6.93%,
          #3533cd 94.41%
        );
      }
      .strip-ai {
        background-image: linear-gradient(
          211.98deg,
          #000000 19.22%,
          #3533cd 94.53%
        );
      }
      .strip-business {
        background-image: linear-gradient(
          105.57deg,
          #000000 2.6%,
          #3533cd 60.9%
        );
      }
      .strip-entrepreneur {
        background-image: linear-gradient(
          90.82deg,
          #000000 3.28%,
          #3533cd 140.89%
        );
      }
      .strip-events {
        background-image: linear-gradient(
          260.78deg,
          #000000 43.02%,
          #3533cd 106.67%
        );
      }
      .strip-brands {
        background-image: linear-gradient(
          104.28deg,
          #000000 3.4%,
          #3533cd 101.3%
        );
      }
      .strip-trends {
        background-image: linear-gradient(
          264.46deg,
          #000000 -20.15%,
          #3533cd 54.42%
        );
      }
      .podcast-title-gradient {
        background: linear-gradient(269.15deg, #000000 47.22%, #3533cd 97.69%);
      }
      .hero-title-gradient {
        background: linear-gradient(90deg, #ffffff 0%, #3533cd 100%);
      }
      .footer-italic-gradient {
        background: linear-gradient(90deg, #c4c3ff 0%, #10e2ff 100%);
      }
      input[type="checkbox"]:checked {
        background-color: #3533cd;
        border-color: #3533cd;
        background-image: url("+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M12.207 4.793a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0l-2-2a1 1 0 011.414-1.414L6.5 9.086l4.293-4.293a1 1 0 011.414 0z'/%3e%3c/svg%3e");
        background-size: 100% 100%;
        background-position: center;
        background-repeat: no-repeat;
      }
      .location-input-wrapper::after {
        content: "";
        position: absolute;
        width: 0;
        height: 0;
        border-left: 5px solid transparent;
        border-right: 5px solid transparent;
        border-top: 6px solid #414141;
        right: 15px;
        top: 50%;
        transform: translateY(-50%);
        pointer-events: none;
      }
      @media (min-width: 768px) {
        .animate-marquee {
          animation: marquee 30s linear infinite;
        }
        @keyframes marquee {
          0% {
            transform: translateX(0%);
          }
          100% {
            transform: translateX(-50%);
          }
        }
      }
      /* Header styles from trial.html */
      @keyframes slideDown {
        from {
          transform: translateY(-10px);
          opacity: 0;
        }
        to {
          transform: translateY(0);
          opacity: 1;
        }
      }
      .slide-down {
        animation: slideDown 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }
      :root {
        --clr-dark-black: #121212;
        --clr-bdr-gray: #2a2a2a;
        --clr-white: #fff;
        --clr-primary: #9747ff;
        --clr-primary-light: #cda7ff;
        --clr-gray-800: #1e1e1e;
      }
      .mobile-menu-item {
        padding: 0.875rem 1rem;
        background: var(--clr-dark-black);
        border-bottom: solid 1px var(--clr-bdr-gray);
        color: var(--clr-white);
        cursor: pointer;
        display: flex;
        align-items: center;
        transition: background-color 0.2s ease;
      }
      .mobile-menu-item:hover {
        background-color: #1a1a1a;
      }
      .mobile-menu-item:active {
        background-color: #252525;
      }
      .item-title {
        flex-grow: 1;
        margin-left: 0.75rem;
        font-weight: 500;
      }
      .hamburger-line {
        transition: all 0.3s ease;
      }
      .hamburger-active .hamburger-line:nth-child(1) {
        transform: translateY(7px) rotate(45deg);
      }
      .hamburger-active .hamburger-line:nth-child(2) {
        opacity: 0;
      }
      .hamburger-active .hamburger-line:nth-child(3) {
        transform: translateY(-7px) rotate(-45deg);
      }
      .search-input {
        transition: all 0.2s ease;
      }
      .search-input:focus {
        box-shadow: 0 0 0 2px rgba(151, 71, 255, 0.5);
      }
      @keyframes shine {
        from {
          transform: translateX(-100%);
        }
        to {
          transform: translateX(100%);
        }
      }
      .login-btn {
        transition: all 0.2s ease;
      }
      .login-btn:hover {
        transform: translateY(-1px);
        box-shadow: 0 2px 8px rgba(205, 167, 255, 0.4);
      }

      /* Flipbook Styles */
      .flipbook-page.--odd {
        background-color: #e9ecef; /* Keep distinct from even for clarity */
      }
      .flipbook-page[data-density="hard"] {
        background-color: #2c3e50; /* Darker, like a cover */
        color: white;
        font-weight: bold;
        font-size: 2rem;
      }
      /* Ensure flipbook pages themselves are ready for flex centering */
      .flipbook-page {
        background-color: #f8f9fa; /* A light default background for pages */
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden; /* Prevent content spill during resize */
      }

      .stf__parent {
        position: relative;
        z-index: 1;
      }
      .stf__block {
        position: relative;
        z-index: 2;
      }
      .stf__item {
        position: absolute;
        z-index: 2;
      }
      .stf__item.--active {
        z-index: 5;
      }
      .stf__outerShadow {
        z-index: 3;
      }
      @keyframes spin {
        from {
          transform: rotate(0deg);
        }
        to {
          transform: rotate(360deg);
        }
      }
      .spinner {
        animation: spin 1s linear infinite;
      }
      /* .book-container {
            border: 3px solid #2c3e50;
            border-radius: 8px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        } */
      .page-placeholder {
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        height: 100%;
        background-color: #f5f5f5;
      }
      .page-loading {
        width: 30px;
        height: 30px;
        border: 3px solid #e0e0e0;
        border-radius: 50%;
        border-top-color: #3498db;
        animation: spin 1s linear infinite;
      }
      .pdf-link-overlay {
        position: absolute;
        background-color: rgba(0, 123, 255, 0.05);
        transition: background-color 0.2s;
        z-index: 1000; /* Ensure links are on top of canvas content */
        cursor: pointer;
      }
      .pdf-link-overlay:hover {
        background-color: rgba(0, 123, 255, 0.2);
      }

      /* Progress Bar Styles */
      .progress-bar-section {
        font-family: "Plus Jakarta Sans", sans-serif;
      }

      .progress-bar-container {
        position: relative;
        user-select: none;
      }

      .progress-bar-container:hover #progress-bar-handle {
        transform: translate(-50%, -50%) scale(1.1);
      }

      #progress-bar-handle {
        left: 0%;
        transform: translate(-50%, -50%);
        transition: all 0.2s ease;
        z-index: 10;
      }

      #progress-bar-handle:active {
        cursor: grabbing;
        transform: translate(-50%, -50%) scale(1.2);
        box-shadow: 0 4px 12px rgba(147, 51, 234, 0.3);
      }

      .progress-bar-container:active {
        cursor: grabbing;
      }

      /* Responsive adjustments */
      @media (max-width: 1024px) {
        /* Default non-fullscreen progress bar width */
        /* Only apply this when NOT in fullscreen mode to avoid conflict */
        body:not(.fullscreen-mode) .App-header .progress-bar-section {
          width: 90% !important;
          max-width: 600px;
        }
      }

      /* Fullscreen Button Styles */
      .fullscreen-button {
        user-select: none;
        cursor: pointer;
      }
      .fullscreen-button:active {
        transform: scale(0.98);
      }

      /* Download Button Styles */
      .download-button {
        user-select: none;
        cursor: pointer;
      }
      .download-button:active {
        transform: scale(0.98);
      }
      .download-button:hover {
        background-color: #e5e7eb !important; /* Tailwind gray-200 */
      }

      /* Styles for when body has .fullscreen-mode */
      body.fullscreen-mode {
        overflow: hidden !important; /* Prevent scrollbars on body */
      }

      /* The .App-header containing the flipbook becomes the fullscreen container */
      body.fullscreen-mode .App-header {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        background-color: #f0f2f5 !important; /* Light background for fullscreen */
        z-index: 2147483640 !important; /* High z-index */
        display: flex !important;
        flex-direction: column !important;
        justify-content: flex-start !important; /* Align items to top */
        align-items: center !important; /* Center flipbook horizontally */
        padding: 20px !important; /* Padding around the content */
        box-sizing: border-box !important;
      }

      /* #flipbook-wrapper in fullscreen mode */
      body.fullscreen-mode #flipbook-wrapper {
        max-width: 95vw !important;
        max-height: calc(
          100vh - 40px - 90px 
        ) !important; /* 100vh - AppHeader.padding*2 - (ProgressBarHeightApprox 50px + its margin 20+20px) */
        margin: 0 auto !important; /* Centered horizontally, specific top/bottom margin handled by flex parent or explicit margin on wrapper*/
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2) !important;
        /* width and height will be set by JavaScript to maintain aspect ratio */
        flex-grow: 1 !important; /* Allow it to grow to fill available space */
        flex-shrink: 1 !important; /* Allow shrinking if necessary but JS will control size */
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        order: 1; /* Ensure flipbook comes before progress bar */
      }

      /* #my-flipbook-container in fullscreen mode - should match its wrapper */
      body.fullscreen-mode #my-flipbook-container {
        /* width and height will be set by JavaScript based on flipbook-wrapper */
      }

      /* .progress-bar-section in fullscreen mode */
      body.fullscreen-mode .progress-bar-section {
        position: relative !important; 
        bottom: auto !important; 
        left: auto !important; 
        transform: none !important; 
        width: clamp(300px, 70vw, 800px) !important;
        max-width: 90% !important; 
        z-index: 2147483641 !important; 
        background: rgba(255, 255, 255, 0.85) !important;
        backdrop-filter: blur(8px) !important;
        -webkit-backdrop-filter: blur(8px) !important;
        padding: 10px 15px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15) !important;
        margin-top: 20px !important; /* Space above progress bar */
        margin-bottom: 0px !important; /* Space at bottom of screen (padding of App-header handles bottom spacing) */
        flex-shrink: 0; /* Prevent it from shrinking */
        order: 2; /* Ensure progress bar comes after flipbook */
      }
      
      /* Hide other major layout elements when in fullscreen. */
      /* Targeting the direct children of the main layout container */
      body.fullscreen-mode > .flex.flex-col.w-full.mx-auto > header:first-of-type, /* Main Site Header */
      body.fullscreen-mode > .flex.flex-col.w-full.mx-auto > footer:last-of-type, /* Main Site Footer */
      body.fullscreen-mode > .flex.flex-col.w-full.mx-auto > div:not(.grid), /* Other direct child divs (like ad banners), but NOT the grid */
      body.fullscreen-mode > .flex.flex-col.w-full.mx-auto > section { /* Other direct child sections */
        display: none !important;
      }

      /* Ensure the .grid div (parent of .App) itself IS visible, but its ad columns are hidden */
      body.fullscreen-mode > .flex.flex-col.w-full.mx-auto > .grid {
        display: grid !important; /* Keep grid display for .App to be part of */
        /* The .App div's .App-header will be taken out of flow by position:fixed, effectively making .App itself seem empty in the grid */
      }
      
      /* Hide ad columns within the grid in fullscreen mode */
      body.fullscreen-mode .ad-column {
        display: none !important;
      }
    </style>
      <style>
        .dropdown-container {
          position: relative;
          padding-bottom: 20px; /* Creates an invisible area below the link for the cursor to travel over */
          margin-bottom: -20px;  /* Negative margin to pull layout back up */
        }
        .dropdown-content {
          position: absolute;
          top: 100%; /* Positions the dropdown right below the parent's padding area */
          left: 50%;
          transform: translateX(-50%);
          width: 320px;
          background: white;
          border-radius: 8px;
          box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
          border: 1px solid #e5e7eb;
          opacity: 0;
          visibility: hidden;
          transition: opacity 0.2s ease, visibility 0.2s;
          z-index: 50;
          pointer-events: none;
          padding: 1rem;
        }
        .dropdown-container:hover .dropdown-content {
          opacity: 1;
          visibility: visible;
          pointer-events: auto;
        }
        
        .line-clamp-2 {
          display: -webkit-box;
          -webkit-line-clamp: 2;
          -webkit-box-orient: vertical;
          overflow: hidden;
        }
        .dropdown-item {
          transition: all 0.2s ease;
        }
        .dropdown-item:hover {
          background-color: #f9fafb;
          transform: translateX(2px);
        }
        .dropdown-item:hover .ph-arrow-right {
          transform: translateX(2px);
          color: #3533CD;
        }
        
        /* --- MOBILE ACCORDION STYLES --- */
        .accordion-toggle .item-title {
          flex-grow: 1;
        }
        .accordion-icon {
          transition: transform 0.3s ease, color 0.3s ease;
        }
        .accordion-toggle[aria-expanded="true"] .accordion-icon {
          transform: rotate(180deg);
          color: white;
        }
        .accordion-content {
          background-color: #1a1a1a;
          overflow: hidden;
          max-height: 0;
          transition: max-height 0.4s cubic-bezier(0.25, 1, 0.5, 1);
        }
        .sub-menu-item {
          display: flex;
          align-items: center;
          padding: 0.5rem;
          border-radius: 0.375rem;
          transition: background-color 0.2s ease;
          color: white;
          text-decoration: none;
        }
        .sub-menu-item:hover {
          background-color: #252525;
        }
      </style>

      <script>
        document.addEventListener('DOMContentLoaded', function() {
          const mobileMenuButton = document.getElementById('mobile-menu-button');
          const mobileMenu = document.getElementById('mobile-menu');
          
          if (mobileMenuButton && mobileMenu) {
            mobileMenuButton.addEventListener('click', function() {
              mobileMenu.classList.toggle('hidden');
              mobileMenuButton.classList.toggle('hamburger-active');
              
              if (!mobileMenu.classList.contains('hidden')) {
                mobileMenu.classList.add('slide-down');
              } else {
                mobileMenu.classList.remove('slide-down');
              }
            });
          }
          
          document.addEventListener('click', function(e) {
            if (e.target.closest('.dropdown-item:not(.know-more-item)')) {
              const item = e.target.closest('.dropdown-item');
              const category = item.getAttribute('data-category');
              const blogId = item.getAttribute('data-id');
              
              console.log('Clicked blog:', { category, blogId });
            }
          });
          
          document.addEventListener('click', function(e) {
            if (e.target.closest('.know-more-item')) {
              const item = e.target.closest('.dropdown-container');
              const category = item.getAttribute('data-category');
              
              console.log('Know More clicked for:', category);
            }
          });
          
          const mobileMenuContainer = document.getElementById('mobile-menu');
          if (mobileMenuContainer) {
            mobileMenuContainer.addEventListener('click', function(e) {
              const toggle = e.target.closest('.accordion-toggle');
              if (!toggle) return;
              e.preventDefault();
              const content = toggle.nextElementSibling;
              const isCurrentlyOpen = toggle.getAttribute('aria-expanded') === 'true';
              mobileMenuContainer.querySelectorAll('.accordion-toggle').forEach(otherToggle => {
                if (otherToggle !== toggle) {
                  otherToggle.setAttribute('aria-expanded', 'false');
                  const otherContent = otherToggle.nextElementSibling;
                  if (otherContent) otherContent.style.maxHeight = '0px';
                }
              });
              if (isCurrentlyOpen) {
                toggle.setAttribute('aria-expanded', 'false');
                content.style.maxHeight = '0px';
              } else {
                toggle.setAttribute('aria-expanded', 'true');
                content.style.maxHeight = content.scrollHeight + 'px';
              }
            });
          }
        });
      </script>

    <script>
      tailwind.config = {
        theme: {
          extend: {
            fontFamily: {
              jakarta: ['"Plus Jakarta Sans"', "sans-serif"],
              helvetica: ['"Helvetica Now Display"', "Arial", "sans-serif"],
              dm: ['"DM Sans"', "sans-serif"],
              "ibm-plex": ['"IBM Plex Sans"', "sans-serif"],
              inter: ['"Inter"', "sans-serif"],
              roboto: ['"Roboto"', "sans-serif"],
              sans: ['"Plus Jakarta Sans"', "sans-serif"],
            },
            colors: {
              "bol-purple": "#3533CD",
              "bol-purple-light": "#C4C3FF",
              "bol-black": "#0D0D0D",
              "bol-gray": "#B8C2CE",
            },
          },
        },
      };
    </script>

    <script>
      // Header script from trial.html
      document.addEventListener("DOMContentLoaded", function () {
        const mobileMenuButton = document.getElementById("mobile-menu-button");
        const mobileMenu = document.getElementById("mobile-menu");
        if (mobileMenuButton && mobileMenu) {
          // Add null checks
          mobileMenuButton.addEventListener("click", function () {
            mobileMenu.classList.toggle("hidden");
            mobileMenuButton.classList.toggle("hamburger-active");
            if (!mobileMenu.classList.contains("hidden")) {
              mobileMenu.classList.add("slide-down");
            } else {
              mobileMenu.classList.remove("slide-down");
            }
          });
        }
      });
    </script>
  </head>
  <body class="font-jakarta bg-white text-bol-black">
    <div class="flex flex-col w-full mx-auto bg-white overflow-x-hidden">
        [[placeholder]]
    <script src="https://cdn.jsdelivr.net/npm/page-flip/dist/js/page-flip.browser.min.js"></script>
    <script>
      (function () {
        "use strict";

        // Global state
        const app = {
          // Core components
          pageFlip: null,
          pdfDocument: null,

          // Cache and queues
          pageCache: new Map(),
          pendingRenderQueue: new Set(),

          // State flags
          isTransitioning: false,
          isResizing: false,

          // Dimensions
          lastKnownWidth: 0,
          lastKnownHeight: 0,

          // DOM elements
          elements: {
            body: document.body, // Added for convenience
            appHeaderForFlipbook: null, // The .App-header that goes fullscreen
            flipBookWrapper: null, 
            flipBook: null,
            loadingOverlay: null,
            fullscreenBtn: null,
            fullscreenIcon: null,
            fullscreenText: null,
            progressBarContainer: null,
            progressBarHandle: null,
            progressBarFill: null,
            currentPageInfo: null,
            totalPagesInfo: null,
            progressBarSection: null, // Added for fullscreen logic
          },

          // Event state
          isDragging: false,
          dragStartX: 0,
          initialProgress: 0,
        };

        // Initialize application
        function init() {
          // Initialize DOM elements
          app.elements.appHeaderForFlipbook = document.querySelector(".App .App-header");
          app.elements.flipBookWrapper = document.getElementById("flipbook-wrapper"); 
          app.elements.flipBook = document.getElementById(
            "my-flipbook-container"
          );
          app.elements.loadingOverlay =
            document.getElementById("loading-overlay");
          app.elements.fullscreenBtn =
            document.getElementById("fullscreen-btn");
          app.elements.fullscreenIcon =
            document.getElementById("fullscreen-icon");
          app.elements.fullscreenText =
            document.getElementById("fullscreen-text");
          app.elements.progressBarContainer = document.querySelector(
            ".progress-bar-container"
          );
          app.elements.progressBarHandle = document.getElementById(
            "progress-bar-handle"
          );
          app.elements.progressBarFill =
            document.getElementById("progress-bar-fill");
          app.elements.currentPageInfo = null; // Element removed but referenced in validation
          app.elements.totalPagesInfo = null; // Element removed but referenced in validation
          app.elements.progressBarSection = document.querySelector(".progress-bar-section");


          // Validate essential elements (exclude intentionally removed elements)
          const missingElements = Object.entries(app.elements)
            .filter(([key, element]) => !element && key !== 'originalStyles' && key !== 'currentPageInfo' && key !== 'totalPagesInfo')
            .map(([key]) => key);

          if (missingElements.length > 0) {
            console.error("Missing required elements:", missingElements);
            // Optionally, provide user feedback here
            if (app.elements.loadingOverlay) {
                app.elements.loadingOverlay.innerHTML = `<p class="text-red-500 p-4">Error: Page components missing. Cannot load magazine viewer. (${missingElements.join(', ')})</p>`;
            }
            return;
          }

          // Initialize app components
          var pdfUrl = "[[pdf_url]]";
          pdfUrl = pdfUrl.replace('-', '/');
          loadPDF(pdfUrl);

          // Delay initialization of UI components that might depend on PDF loaded state or DOM readiness
          setTimeout(() => {
            initializeFullscreenButton();
            initializeDownloadButton();
          }, 500); // Give some time for initial PDF load/DOM paint

          setupHighFiveCounter();
          setupIframeMessageListener();
        }

        // Setup and manage high five counter functionality
        function setupHighFiveCounter() {
          const elements = {
            emojis: document.querySelectorAll(".high-five-emoji"),
            counters: document.querySelectorAll(".count-number"),
          };

          // Validate required elements
          if (!elements.emojis.length || !elements.counters.length) {
            // console.warn("High Five counter elements not found"); // Commented out as these are not in current HTML
            return;
          }

          // Initialize state
          const state = {
            count: parseInt(localStorage.getItem("highFiveCount") || "521"),
            animating: false,
          };

          // Update display across all counter elements
          function updateDisplay() {
            elements.counters.forEach((counter) => {
              counter.textContent = state.count;
              counter.setAttribute("aria-label", `${state.count} high fives`);
            });
          }

          // Handle click animation
          function animateEmoji(emoji) {
            if (state.animating) return;
            state.animating = true;

            emoji.style.transform = "scale(1.2)";
            emoji.style.transition = "transform 0.15s ease";

            setTimeout(() => {
              emoji.style.transform = "scale(1)";
              state.animating = false;
            }, 150);
          }

          // Handle click events
          function handleClick(emoji) {
            return () => {
              state.count++;
              updateDisplay();
              localStorage.setItem("highFiveCount", state.count.toString());
              animateEmoji(emoji);
            };
          }

          // Initialize
          updateDisplay();

          // Set up event listeners
          elements.emojis.forEach((emoji) => {
            emoji.addEventListener("click", handleClick(emoji));
            emoji.setAttribute("role", "button");
            emoji.setAttribute("aria-label", "Give a high five");
            emoji.style.cursor = "pointer";
          });
        }

        // Setup iframe message listener for fullscreen page synchronization
        function setupIframeMessageListener() {
          // Listen for messages from the fullscreen iframe
          window.addEventListener('message', function(event) {
            // For security, you might want to verify the origin
            // if (event.origin !== window.location.origin) return;
            
            try {
              const data = event.data;
              
              // Check if the message is a page change notification from the iframe
              if (data && data.type === 'pageChange' && data.pageNumber !== undefined) {
                console.log('Received page change message from iframe:', data);
                
                // Update the parent flipbook to match the iframe's current page
                if (app.pageFlip && app.pdfDocument) {
                  const targetPageIndex = data.pageNumber - 1; // Convert from 1-based to 0-based
                  
                  // Validate the page number
                  if (targetPageIndex >= 0 && targetPageIndex < app.pdfDocument.numPages) {
                    // Only flip if we're not already on that page
                    const currentPageIndex = app.pageFlip.getCurrentPageIndex();
                    if (currentPageIndex !== targetPageIndex) {
                      console.log(`Syncing parent flipbook to page ${data.pageNumber} (index ${targetPageIndex})`);
                      app.pageFlip.flip(targetPageIndex);
                    }
                  }
                }
              }
            } catch (error) {
              console.error('Error handling message from iframe:', error);
            }
          });
          
          console.log('Iframe message listener setup complete');
        }

        // Initialize resize observer
        const resizeObserver = new ResizeObserver(async (entries) => {
          for (const entry of entries) {
            if (entry.target === app.elements.flipBookWrapper) {
                const { width, height } = entry.contentRect;
                if (
                Math.abs(width - app.lastKnownWidth) > 1 || // More sensitive for better response
                Math.abs(height - app.lastKnownHeight) > 1
                ) {
                app.lastKnownWidth = width;
                app.lastKnownHeight = height;
                if (
                    !app.isResizing && // Check global isResizing, not pageFlip's internal
                    app.pageFlip
                ) {
                    try {
                        app.isResizing = true; 
                        const currentPageIndex = app.pageFlip.getCurrentPageIndex();
                        
                        const containerForFlipInstance = app.elements.flipBook;
                        // Ensure container has valid dimensions before proceeding
                        if (containerForFlipInstance.clientWidth > 0 && containerForFlipInstance.clientHeight > 0) {
                            // --- START CHANGE: Responsive Logic ---
                            const mobileBreakpoint = 768;
                            const isMobile = window.innerWidth < mobileBreakpoint;
                            
                            const pageW = isMobile ? containerForFlipInstance.clientWidth : Math.floor(containerForFlipInstance.clientWidth / 2);
                            const pageH = containerForFlipInstance.clientHeight;

                            await initFlipbookInstance(currentPageIndex, pageW, pageH, isMobile);
                            // --- END CHANGE ---
                        } else {
                            console.warn("ResizeObserver: flipBook container has zero dimensions. Skipping reinitialization.");
                        }
                    } catch (error) {
                     console.error("Error handling resize observer event:", error);
                    } finally {
                     app.isResizing = false; 
                    }
                }
                }
            }
          }
        });

        // Cleanup function
        function cleanup() {
          if (app.pageFlip) {
            app.pageFlip.destroy();
            app.pageFlip = null;
          }
          app.pageCache.clear();
          app.pendingRenderQueue.clear();
          app.isTransitioning = false;
          app.isResizing = false;
          if (app.elements.body.classList.contains("fullscreen-mode")) {
            app.elements.body.classList.remove("fullscreen-mode");
          }
          resizeObserver.disconnect(); // Disconnect observer on unload
        }

        // Set up application
        function setupApp() {
          if (app.elements.flipBookWrapper) {
            resizeObserver.observe(app.elements.flipBookWrapper);
          } else {
            console.error("flipBookWrapper not found for ResizeObserver at setupApp.");
          }
          window.addEventListener("unload", cleanup);
          window.app = app; 
        }

        // Start initialization when DOM is ready
        if (document.readyState === "loading") {
          document.addEventListener("DOMContentLoaded", () => {
            init();
            setupApp();
          });
        } else {
          init();
          setupApp();
        }

        function createPageDiv(pageNumber, totalPages) {
          const pageDiv = document.createElement("div");
          pageDiv.className =
            "flipbook-page bg-gray-50 text-gray-800 flex flex-col justify-center items-center shadow-lg box-border";
          pageDiv.setAttribute("data-page-number", pageNumber);

          if (pageNumber === 1 || pageNumber === totalPages) {
            pageDiv.setAttribute("data-density", "hard");
          }

          const placeholder = document.createElement("div");
          placeholder.className = "page-placeholder";
          placeholder.innerHTML = `<div class="page-loading"></div>`;
          pageDiv.appendChild(placeholder);
          return pageDiv;
        }

        async function renderPageToCanvas(pageNumber) {
          try {
            const useCache =
              !app.isResizing && // Use global resizing flag
              app.pageCache.has(pageNumber) &&
              document.querySelector(`[data-page-number="${pageNumber}"]`);

            if (useCache) {
              return app.pageCache.get(pageNumber);
            }
            
            const page = await app.pdfDocument.getPage(pageNumber);

            const pageFlipSettings = app.pageFlip.getSettings();
            const currentPageWidth = pageFlipSettings.width; 
            const currentPageHeight = pageFlipSettings.height;

            const pagePadding = 0; 
            const containerWidth = currentPageWidth - 2 * pagePadding;
            const containerHeight = currentPageHeight - 2 * pagePadding;

            const viewportOriginal = page.getViewport({ scale: 1.0 });
            const baseScale = Math.min(
              containerWidth / viewportOriginal.width,
              containerHeight / viewportOriginal.height
            );

            const qualityMultiplier = window.devicePixelRatio > 1.5 ? 1.5 : 2; 
            const renderScale = baseScale * qualityMultiplier;
            const viewport = page.getViewport({ scale: renderScale });

            const pageContentHolder = document.createElement("div");
            pageContentHolder.style.position = "relative";
            pageContentHolder.style.width = `${containerWidth}px`;
            pageContentHolder.style.height = `${containerHeight}px`;
            pageContentHolder.style.margin = "auto"; 
            pageContentHolder.style.overflow = "hidden";

            const canvas = document.createElement("canvas");
            canvas.width = viewport.width;
            canvas.height = viewport.height;
            canvas.style.width = `${containerWidth}px`;
            canvas.style.height = `${containerHeight}px`;
            pageContentHolder.appendChild(canvas);

            const context = canvas.getContext("2d");

            const renderContext = {
              canvasContext: context,
              viewport: viewport,
            };

            await page.render(renderContext).promise;

            const linkContainer = document.createElement("div");
            linkContainer.style.position = "absolute";
            linkContainer.style.top = "0";
            linkContainer.style.left = "0";
            linkContainer.style.width = "100%"; 
            linkContainer.style.height = "100%";
            linkContainer.style.pointerEvents = "none"; 

            const annotations = await page.getAnnotations();
            let linkCount = 0;

            for (const annotation of annotations) {
              if (annotation.subtype === "Link") {
                linkCount++;
                const rect = viewport.convertToViewportRectangle(
                  annotation.rect
                );
                const [x1, y1, x2, y2] = rect;

                const linkOverlay = document.createElement("div");
                linkOverlay.className = "pdf-link-overlay";

                const scaleFactorToCanvasStyle =
                  containerWidth / viewport.width;

                linkOverlay.style.left = `${
                  Math.min(x1, x2) * scaleFactorToCanvasStyle
                }px`;
                linkOverlay.style.top = `${
                  Math.min(y1, y2) * scaleFactorToCanvasStyle
                }px`;
                linkOverlay.style.width = `${
                  Math.abs(x2 - x1) * scaleFactorToCanvasStyle
                }px`;
                linkOverlay.style.height = `${
                  Math.abs(y2 - y1) * scaleFactorToCanvasStyle
                }px`;
                linkOverlay.style.pointerEvents = "auto"; 

                if (annotation.url) {
                  linkOverlay.title = annotation.url;
                  linkOverlay.setAttribute("data-url", annotation.url);
                  linkOverlay.addEventListener(
                    "click",
                    (e) => {
                      e.stopPropagation(); 
                      e.preventDefault();
                      window.open(annotation.url, "_blank");
                    },
                    true
                  ); 
                } else if (annotation.dest) {
                  linkOverlay.title = "Go to page";
                  linkOverlay.setAttribute(
                    "data-dest",
                    JSON.stringify(annotation.dest)
                  );
                  linkOverlay.addEventListener(
                    "click",
                    async (e) => {
                      e.stopPropagation();
                      e.preventDefault();
                      try {
                        const destArray = JSON.parse(
                          linkOverlay.getAttribute("data-dest")
                        );
                        const destInfo = await app.pdfDocument.getDestination(
                          destArray
                        );
                        if (destInfo && destInfo.length > 0) {
                          const pageRef = destInfo[0];
                          const targetPageNum =
                            (await app.pdfDocument.getPageIndex(pageRef)) + 1; 
                          if (app.pageFlip) app.pageFlip.flip(targetPageNum - 1); 
                        }
                      } catch (error) {
                        console.error(
                          "Error navigating to internal link:",
                          error
                        );
                      }
                    },
                    true
                  );
                }
                linkContainer.appendChild(linkOverlay);
              }
            }
            if (linkCount > 0) pageContentHolder.appendChild(linkContainer);

            app.pageCache.set(pageNumber, pageContentHolder);
            return pageContentHolder;
          } catch (error) {
            console.error(`Error rendering page ${pageNumber}:`, error);
            const errorElem = document.createElement("div");
            errorElem.className = "text-red-500 p-4 text-center";
            errorElem.innerHTML = `<p>Error loading page ${pageNumber}.</p><p class="text-xs">${error.message || ''}</p>`;
            return errorElem; 
          }
        }

        async function updatePageContent(pageNumber, totalPages) {
          const pageSelector = `[data-page-number="${pageNumber}"]`;
          const pageDiv = document.querySelector(pageSelector);
          if (!pageDiv) {
            return; 
          }
        
          const updateStartTime = Date.now();
          const MIN_UPDATE_DELAY = 100; 

          try {
            pageDiv.innerHTML = `
                    <div class="page-placeholder flex items-center justify-center">
                        <div class="page-loading"></div>
                    </div>`;

            const contentHolder = await Promise.race([
              renderPageToCanvas(pageNumber),
              new Promise((_, reject) =>
                setTimeout(
                  () => reject(new Error("Page render timeout")),
                  10000
                ) 
              ),
            ]);

            const elapsedTime = Date.now() - updateStartTime;
            if (elapsedTime < MIN_UPDATE_DELAY) {
              await new Promise((resolve) =>
                setTimeout(resolve, MIN_UPDATE_DELAY - elapsedTime)
              );
            }

            if (document.contains(pageDiv)) {
                pageDiv.innerHTML = ""; 
                pageDiv.appendChild(contentHolder);
                if (pageNumber > 1 && pageNumber < totalPages) { 
                    if (getComputedStyle(pageDiv).position === "static") {
                        pageDiv.style.position = "relative"; 
                    }
                    // const pageNumDisplay = document.createElement("div");
                    // pageNumDisplay.className =
                    //     "absolute bottom-2 right-2 text-xs text-gray-500 " +
                    //     "bg-white/50 px-2 py-1 rounded backdrop-blur-sm";
                    // pageNumDisplay.textContent = `Page ${pageNumber -1}`; 
                    // pageDiv.appendChild(pageNumDisplay);
                }
            }
          } catch (error) {
            console.error(`Error updating page ${pageNumber}:`, error);
             if (document.contains(pageDiv)) {
                pageDiv.innerHTML = `
                        <div class="flex flex-col items-center justify-center h-full p-4 text-red-500">
                            <svg class="w-6 h-6 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
                            </svg>
                            <div>Error loading page</div>
                        </div>`;
             }
          }
        }

        async function handlePageFlipEvent(e) {
          if (!app.pdfDocument || !app.pageFlip) return;

          const newPageIndex = e.data; 
          const currentPageNumber = newPageIndex + 1; 
          const totalPages = app.pdfDocument.numPages;

          updateProgressBar(newPageIndex, totalPages);

          const pagesToRender = new Set([currentPageNumber]);
          if (
            !app.pageFlip.getSettings().usePortrait && 
            currentPageNumber < totalPages 
          ) {
            pagesToRender.add(currentPageNumber + 1);
          }
          await preRenderPages(Array.from(pagesToRender), totalPages);
        }

        async function preRenderPages(targetPages, totalPages) {
          if (app.isTransitioning || !targetPages.length) return;

          const RANGE = 2; 
          const pagesToRender = new Set(); 

          for (const page of targetPages) { 
            for (let i = -RANGE; i <= RANGE; i++) {
              const neighborPage = page + i;
              if (neighborPage > 0 && neighborPage <= totalPages) { 
                pagesToRender.add(neighborPage);
              }
            }
          }

          app.pendingRenderQueue.clear();
          for (const pageNum of pagesToRender) { 
            if (!app.pageCache.has(pageNum)) {
              app.pendingRenderQueue.add(pageNum);
            }
          }

          const CONCURRENT_RENDERS = 2;
          const pages = Array.from(app.pendingRenderQueue); 

          try {
            await Promise.all(
              Array(CONCURRENT_RENDERS)
                .fill()
                .map(async () => {
                  while (pages.length > 0) {
                    const pageNum = pages.shift(); 
                    try {
                      await updatePageContent(pageNum, totalPages); 
                      app.pendingRenderQueue.delete(pageNum);
                    } catch (error) {
                      // Error already logged in updatePageContent
                    }
                  }
                })
            );
          } catch (error) {
            console.error("Error in pre-rendering process:", error);
          }
        }

        async function loadPDF(pdfUrl) {
          if (!app.elements.loadingOverlay || !app.elements.flipBook) {
            console.error("Essential elements for PDF loading are missing.");
            return;
          }
          app.elements.loadingOverlay.style.display = "flex";

          try {
            app.elements.flipBook.innerHTML = ""; 
            app.pageCache.clear();

            const loadingTask = pdfjsLib.getDocument(pdfUrl);
            app.pdfDocument = await Promise.race([
              loadingTask.promise,
              new Promise((_, reject) =>
                setTimeout(
                  () => reject(new Error("PDF loading timeout")),
                  30000
                )
              ),
            ]);

            const totalPages = app.pdfDocument.numPages;


            for (let i = 1; i <= totalPages; i++) { 
              const pageDiv = createPageDiv(i, totalPages);
              app.elements.flipBook.appendChild(pageDiv);
            }
            
            await waitForReflow();

            const flipbookContainerElement = app.elements.flipBook; 
            const containerWidth = flipbookContainerElement.clientWidth;
            const containerHeight = flipbookContainerElement.clientHeight;
            
            if (containerWidth <= 0 || containerHeight <= 0) {
                console.error("Flipbook container has zero dimensions before initial init.");
                app.elements.flipBook.innerHTML = `<div class="p-5 text-red-500 text-center">Error: Flipbook container has invalid dimensions. Cannot display content.</div>`;
                app.elements.loadingOverlay.style.display = "none";
                return;
            }

            // --- START CHANGE: Responsive Logic ---
            const mobileBreakpoint = 768;
            const isMobile = window.innerWidth < mobileBreakpoint;
            const pageWidth = isMobile ? containerWidth : Math.floor(containerWidth / 2);
            const pageHeight = containerHeight;

            await initFlipbookInstance(0, pageWidth, pageHeight, isMobile); 
            // --- END CHANGE ---

            const initialPages = new Set([
              1, 
              ...(totalPages > 1 ? [2] : []), 
              ...(totalPages > 2 ? [3] : []), 
              ...(totalPages > 3 ? [totalPages] : []), 
            ]);
            
             await Promise.all(
                Array.from(initialPages).map((pageNum) => {
                    if (app.elements.flipBook.querySelector(`[data-page-number="${pageNum}"]`)) {
                        return updatePageContent(pageNum, totalPages);
                    }
                    return Promise.resolve(); 
                })
            );

            await waitForReflow(); 
            initializeProgressBar();
            updateProgressBar(0, totalPages); 
          } catch (error) {
            console.error("Error loading PDF:", error);
            app.elements.flipBook.innerHTML = `
                    <div class="p-5 text-red-500 flex flex-col items-center justify-center">
                        <svg class="w-8 h-8 mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/>
                        </svg>
                        <div>Failed to load PDF: ${error.message}</div>
                    </div>`;
          } finally {
            app.elements.loadingOverlay.style.display = "none";
          }
        }

        // --- START CHANGE: Update function to accept `isMobile` flag ---
        async function initFlipbookInstance(startPageIdx, pageW, pageH, isMobile) {
        // --- END CHANGE ---
          if (app.isResizing && app.pageFlip) {
             return;
          }

          try {
            app.isResizing = true; 

            if (app.pageFlip) {
              const currentIdx = app.pageFlip.getCurrentPageIndex();
              app.pageFlip.destroy();
              app.pageFlip = null;
              startPageIdx = currentIdx; 
            }

            await waitForReflow();
            
            const flipBookElement = app.elements.flipBook;
            if (!flipBookElement || pageW <=0 || pageH <= 0) {
                console.error("Flipbook container not ready or invalid dimensions for init.", pageW, pageH, flipBookElement);
                throw new Error("Flipbook container not ready or invalid dimensions.");
            }

            app.pageFlip = new St.PageFlip(flipBookElement, { 
              width: pageW, 
              height: pageH, 
              size: "fixed", 
              minWidth: Math.min(300, pageW),
              maxWidth: pageW,
              minHeight: Math.min(400, pageH),
              maxHeight: pageH,
              maxShadowOpacity: 0.5,
              showCover: true,
              mobileScrollSupport: true,
              flippingTime: 800,
              // --- START CHANGE: Set usePortrait based on mobile state ---
              usePortrait: isMobile, 
              // --- END CHANGE ---
              startPage: startPageIdx, 
              startZIndex: 20,
              autoSize: false, 
              drawShadow: true,
            });
            
            const pageElements = flipBookElement.querySelectorAll('.flipbook-page');
            if (!pageElements.length) {
                throw new Error("No page elements to load into PageFlip instance.");
            }

            await Promise.race([
              new Promise((resolve) => {
                app.pageFlip.loadFromHTML(pageElements);
                app.pageFlip.flip(startPageIdx, 'immediate'); 
                setTimeout(resolve, 150); 
              }),
              new Promise((_, reject) =>
                setTimeout(() => reject(new Error("PageFlip HTML loading timeout")), 5000)
              ),
            ]);

            app.pageFlip.off("flip");
            app.pageFlip.off("changeState");
            
            app.pageFlip.on("flip", handlePageFlipEvent); 
            app.pageFlip.on("changeState", (e) => { 
                if (e.data === "read") {
                    handlePageFlipEvent({ data: app.pageFlip.getCurrentPageIndex() });
                }
            });
            handlePageFlipEvent({ data: startPageIdx });

            return app.pageFlip;
          } catch (error) {
            console.error("Error initializing flipbook:", error);
            if (app.pageFlip) {
              app.pageFlip.destroy();
              app.pageFlip = null;
            }
          } finally {
            app.isResizing = false; 
          }
        }

        function updateProgressBar(currentPageIndex, totalPages) {
          const elements = {
            fill: document.getElementById("progress-bar-fill"),
            handle: document.getElementById("progress-bar-handle"),
          };

          if (Object.values(elements).some((el) => !el)) {
            return;
          }

          const progress = (() => {
            if (totalPages <= 0) return 0;
            if (totalPages === 1) return currentPageIndex >= 0 ? 100 : 0; 
            return Math.max(
              0,
              Math.min(100, (currentPageIndex / (totalPages - 1)) * 100)
            );
          })();

          const currentPageDisplay = currentPageIndex + 1;
          const progressPercent = Math.round(progress);

          try {
            elements.fill.style.width = `${progress}%`;
            elements.handle.style.left = `${progress}%`;

            elements.handle.setAttribute("aria-valuenow", progressPercent);
            elements.handle.setAttribute("aria-valuemin", "0");
            elements.handle.setAttribute("aria-valuemax", "100");
            elements.handle.setAttribute(
              "aria-valuetext",
              `${progressPercent}% complete`
            );
          } catch (error) {
            console.error("Error updating progress bar:", error);
          }
        }

        function initializeProgressBar() {
          const elements = {
            container: document.querySelector(".progress-bar-container"),
            handle: document.getElementById("progress-bar-handle"),
            fill: document.getElementById("progress-bar-fill"),
            tooltip: document.getElementById("progress-tooltip"),
            tooltipPageInfo: document.getElementById("tooltip-page-info"),
          };

          const missingElements = Object.entries(elements)
            .filter(([key, el]) => !el)
            .map(([key]) => key);

          if (missingElements.length > 0) {
            console.error("Missing progress bar elements for init:", missingElements);
            return;
          }

          const state = {
            isDragging: false,
            dragStartX: 0,
            initialProgress: 0,
          };

          function updatePosition(progress) {
            const validProgress = Math.max(0, Math.min(100, progress));
            elements.fill.style.width = `${validProgress}%`;
            elements.handle.style.left = `${validProgress}%`;
          }

          function updateTooltip(progress, clientX) {
            if (!app.pdfDocument || !elements.tooltip || !elements.tooltipPageInfo) return;
            
            const totalPages = app.pdfDocument.numPages;
            const currentPageIndex = totalPages <= 1 ? 0 : Math.round((progress / 100) * (totalPages - 1));
            const currentPage = currentPageIndex + 1;
            
            elements.tooltipPageInfo.textContent = `${currentPage} of ${totalPages}`;
            
            // Position tooltip at mouse position
            const rect = elements.container.getBoundingClientRect();
            const relativeX = clientX - rect.left;
            const tooltipProgress = (relativeX / rect.width) * 100;
            const clampedProgress = Math.max(0, Math.min(100, tooltipProgress));
            
            elements.tooltip.style.left = `${clampedProgress}%`;
          }

          function showTooltip() {
            if (elements.tooltip) {
              elements.tooltip.style.opacity = '1';
            }
          }

          function hideTooltip() {
            if (elements.tooltip) {
              elements.tooltip.style.opacity = '0';
            }
          }

          function seekToProgress(progress) {
            if (!app.pdfDocument || !app.pageFlip) return;
            const targetPage =
              app.pdfDocument.numPages <= 1
                ? 0
                : Math.round((progress / 100) * (app.pdfDocument.numPages - 1));

            if (targetPage >= 0 && targetPage < app.pdfDocument.numPages) {
              app.pageFlip.flip(targetPage);
            }
          }

          const handlers = {
            startDrag(e) {
              e.preventDefault();
              state.isDragging = true;
              state.dragStartX = e.clientX;
              state.initialProgress =
                parseFloat(elements.handle.style.left) || 0;
              document.addEventListener("mousemove", handlers.drag);
              document.addEventListener("mouseup", handlers.stopDrag);
              document.body.style.userSelect = "none"; 
            },

            startDragTouch(e) {
              e.preventDefault(); 
              state.isDragging = true;
              state.dragStartX = e.touches[0].clientX;
              state.initialProgress =
                parseFloat(elements.handle.style.left) || 0;
              document.addEventListener("touchmove", handlers.dragTouch, {
                passive: false, 
              });
              document.addEventListener("touchend", handlers.stopDragTouch);
            },

            drag(e) {
              if (!state.isDragging || !app.pdfDocument) return;
              const rect = elements.container.getBoundingClientRect();
              const deltaX = e.clientX - state.dragStartX;
              const deltaPercent = (deltaX / rect.width) * 100;
              updatePosition(state.initialProgress + deltaPercent);
            },

            dragTouch(e) {
              if (!state.isDragging || !app.pdfDocument) return;
              e.preventDefault(); 
              const rect = elements.container.getBoundingClientRect();
              const deltaX = e.touches[0].clientX - state.dragStartX;
              const deltaPercent = (deltaX / rect.width) * 100;
              updatePosition(state.initialProgress + deltaPercent);
            },


            stopDrag() {
              if (!state.isDragging) return;
              state.isDragging = false;
              document.removeEventListener("mousemove", handlers.drag);
              document.removeEventListener("mouseup", handlers.stopDrag);
              document.body.style.userSelect = "";
              const progress = parseFloat(elements.handle.style.left) || 0;
              seekToProgress(progress);
            },

            stopDragTouch() {
              if (!state.isDragging) return;
              state.isDragging = false;
              document.removeEventListener("touchmove", handlers.dragTouch);
              document.removeEventListener("touchend", handlers.stopDragTouch);
              const progress = parseFloat(elements.handle.style.left) || 0;
              seekToProgress(progress);
            },

            handleClick(e) {
              if (state.isDragging || !app.pdfDocument || !app.pageFlip) return;
              const rect = elements.container.getBoundingClientRect();
              const progress = ((e.clientX - rect.left) / rect.width) * 100;
              updatePosition(progress);
              seekToProgress(progress);
            },

            handleMouseEnter() {
              showTooltip();
            },
            
            handleMouseLeave() {
              hideTooltip();
            },
            
            handleMouseMove(e) {
              if (!app.pdfDocument) return;
              const rect = elements.container.getBoundingClientRect();
              const progress = ((e.clientX - rect.left) / rect.width) * 100;
              const clampedProgress = Math.max(0, Math.min(100, progress));
              updateTooltip(clampedProgress, e.clientX);
            },
          };

          elements.handle.addEventListener("mousedown", handlers.startDrag);
          elements.handle.addEventListener(
            "touchstart",
            handlers.startDragTouch,
            { passive: false }
          );
          elements.container.addEventListener("click", handlers.handleClick);
          
          // Add hover functionality for tooltip
          elements.container.addEventListener("mouseenter", handlers.handleMouseEnter);
          elements.container.addEventListener("mouseleave", handlers.handleMouseLeave);
          elements.container.addEventListener("mousemove", handlers.handleMouseMove);
        }

        async function waitForReflow() {
          return new Promise((resolve) => {
            requestAnimationFrame(() => {
              requestAnimationFrame(resolve);
            });
          });
        }
        
        // Fullscreen Functionality
        function initializeFullscreenButton() {
            const fullscreenBtn = document.getElementById("fullscreen-btn");
            if (!fullscreenBtn) {
                console.error("Fullscreen button not found.");
                return;
            }

            let fullscreenIframe = null; // Keep a reference to the iframe

            function openFullscreenIframe() {
                if (fullscreenIframe) { // Prevent multiple iframes
                    console.log("Fullscreen iframe already exists or is being created.");
                    return;
                }

                console.log("Attempting to open fullscreen iframe...");
                fullscreenIframe = document.createElement('iframe');
                fullscreenIframe.id = 'fullscreenContentIframe';
                
                // Get current page number
                let currentPageNumber = 1; // Default fallback
                if (app.pageFlip) {
                    currentPageNumber = app.pageFlip.getCurrentPageIndex() + 1; // Convert from 0-based to 1-based
                }
                
                // Construct URL with page_number parameter
                const baseUrl = '/flipbook';
                const fullscreenUrl = `${baseUrl}?magazine_url=[[pdf_url]]&page_number=${currentPageNumber}`;
                
                console.log(`Opening fullscreen with page number: ${currentPageNumber}`);
                fullscreenIframe.setAttribute('src', fullscreenUrl);
                fullscreenIframe.setAttribute('allowfullscreen', '');
                fullscreenIframe.setAttribute('allow', 'fullscreen');
                
                fullscreenIframe.style.position = 'fixed';
                fullscreenIframe.style.top = '0';
                fullscreenIframe.style.left = '0';
                fullscreenIframe.style.width = '100vw';
                fullscreenIframe.style.height = '100vh';
                fullscreenIframe.style.border = 'none';
                fullscreenIframe.style.zIndex = '2147483647';

                fullscreenIframe.onload = function() {
                    console.log('Fullscreen iframe content loaded successfully. Path: ' + fullscreenIframe.src);
                    const requestFullscreenFn =
                        fullscreenIframe.requestFullscreen ||
                        fullscreenIframe.webkitRequestFullscreen ||
                        fullscreenIframe.mozRequestFullScreen ||
                        fullscreenIframe.msRequestFullscreen;

                    if (requestFullscreenFn) {
                        requestFullscreenFn.call(fullscreenIframe).catch(err => {
                            console.error(`Error attempting to enable full-screen mode AFTER iframe load: ${err.message} (${err.name})`);
                            cleanupIframeAndListeners(); // Clean up on error
                        });
                    } else {
                        console.error('Fullscreen API not supported by this iframe after load.');
                        cleanupIframeAndListeners(); // Clean up
                    }
                };

                fullscreenIframe.onerror = function() {
                    console.error('Error loading content into fullscreen iframe. Path: ' + fullscreenIframe.src + '. The iframe will be removed.');
                    cleanupIframeAndListeners(); // Clean up on error
                };
                
                // Add listeners for fullscreen state changes
                document.addEventListener('fullscreenchange', handleExternalFullscreenChange);
                document.addEventListener('webkitfullscreenchange', handleExternalFullscreenChange);
                document.addEventListener('mozfullscreenchange', handleExternalFullscreenChange);
                document.addEventListener('MSFullscreenChange', handleExternalFullscreenChange);

                document.body.appendChild(fullscreenIframe);
                console.log("Fullscreen iframe appended to body. Waiting for load or error event.");
            }

            function cleanupIframeAndListeners() {
                console.log("Cleaning up iframe and listeners.");
                if (fullscreenIframe && fullscreenIframe.parentNode) {
                    fullscreenIframe.parentNode.removeChild(fullscreenIframe);
                }
                fullscreenIframe = null;
                document.removeEventListener('fullscreenchange', handleExternalFullscreenChange);
                document.removeEventListener('webkitfullscreenchange', handleExternalFullscreenChange);
                document.removeEventListener('mozfullscreenchange', handleExternalFullscreenChange);
                document.removeEventListener('MSFullscreenChange', handleExternalFullscreenChange);
            }

            // Renamed to avoid conflict if this function itself is a listener
            function handleExternalFullscreenChange() {
                const isActuallyFullscreen = !!(document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement);
                
                // If browser exits fullscreen mode (e.g. user presses Esc)
                // and our iframe was the one in fullscreen (or if no element is fullscreen)
                if (!isActuallyFullscreen) {
                    console.log("Browser exited fullscreen mode or no element is fullscreen.");
                    cleanupIframeAndListeners();
                }
            }

            // Attach the primary click listener to the button
            fullscreenBtn.addEventListener("click", (event) => {
                event.preventDefault(); // Prevent any default button action
                openFullscreenIframe();
            });
        }


        // Download Functionality
        function initializeDownloadButton() {
          const downloadBtn = document.getElementById("download-btn");
          
          if (!downloadBtn) {
            console.error("Download button not found.");
            return;
          }

          let isDownloading = false;

          downloadBtn.addEventListener("click", function(event) {
            event.preventDefault();
            event.stopPropagation();
            
            if (isDownloading) {
              return;
            }
            
            isDownloading = true;
            
            try {
              var pdfUrl = "[[pdf_url]]";
              pdfUrl = pdfUrl.replace('-', '/');
              const link = document.createElement('a');
              link.href = pdfUrl;
              const filename = pdfUrl.substring(pdfUrl.lastIndexOf('/') + 1) || "download.pdf";
              link.download = filename; 
              link.style.display = 'none'; 
              
              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
              
              setTimeout(() => {
                isDownloading = false;
              }, 1000);
              
            } catch (error) {
              console.error("Error downloading PDF:", error);
              isDownloading = false; 
            }
          });
        }

      })(); // End IIFE
    </script>
  </body>
</html>"""