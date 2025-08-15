
from .hero_section import get_magazine_homepage_hero_section
from .more_magazines import get_more_magazines
from .magazine_page_hero_section import get_magazine_hero_section, get_raw_html

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


        // Download Functionality (proxied through same-origin to avoid Edge blocking)
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
              const filename = pdfUrl.substring(pdfUrl.lastIndexOf('/') + 1) || "document.pdf";
              
              // Proxy via same-origin endpoint to avoid client/extension blocking of external domain
              const proxiedUrl = `${window.location.origin}/download_proxy?pdf=${encodeURIComponent(pdfUrl)}&filename=${encodeURIComponent(filename)}`;
              
              const link = document.createElement('a');
              link.href = proxiedUrl;
              link.download = filename; 
              link.style.display = 'none'; 
              
              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
            } catch (error) {
              console.error("Error downloading PDF:", error);
            } finally {
              setTimeout(() => {
                isDownloading = false;
              }, 500);
            }
          });
        }

      })(); // End IIFE
    </script>
  </body>
</html>"""

def UPLOAD_NEW_MAGAZINE_TEMPLATE():
    return """
    <style>
        /* Keep scrollbar hidden as in homepage */
        ::-webkit-scrollbar { display: none; }
        body {
            -ms-overflow-style: none;
            scrollbar-width: none;
        }

        @keyframes slideDown {
            from { transform: translateY(-10px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        .slide-down { animation: slideDown 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards; }

        :root {
            --clr-dark-black: #121212;
            --clr-bdr-gray: #2a2a2a;
            --clr-white: #fff;
            --clr-primary: #9747FF;
            --clr-primary-bol: #3533CD;
        }

        /* Page-specific (light theme to match homepage) */
        .section-card {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
        }
        .section-title {
            font-family: "Plus Jakarta Sans", sans-serif;
            font-weight: 700;
            color: #0D0D0D;
        }

        /* Form elements (light) */
        .form-label {
            display: block;
            margin-bottom: 0.375rem;
            font-size: 0.875rem;
            font-weight: 600;
            color: #374151;
        }
        .form-input {
            width: 100%;
            background-color: #F9FAFB;
            border: 1px solid #E5E7EB;
            border-radius: 10px;
            padding: 0.75rem 0.875rem;
            color: #0D0D0D;
            transition: all 0.2s ease;
        }
        .form-input:focus {
            outline: none;
            border-color: #3533CD;
            box-shadow: 0 0 0 3px rgba(53, 51, 205, 0.15);
            background-color: #ffffff;
        }

        .file-input-display {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 170px;
            width: 100%;
            background-color: #F9FAFB;
            border: 2px dashed #E5E7EB;
            border-radius: 12px;
            padding: 1.25rem;
            color: #6B7280;
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .file-input-display:hover {
            border-color: #D1D5DB;
            background-color: #FFFFFF;
        }
        .file-input-display.dragover {
            border-color: #3533CD;
            background-color: #EEF2FF;
            transform: scale(1.01);
        }
        .file-input-placeholder { color: #9CA3AF; }

        .form-button {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0.75rem 1.25rem;
            border: none;
            border-radius: 9999px;
            background-color: #3533CD;
            color: white;
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease-in-out;
        }
        .form-button:hover:not(:disabled) { background-color: #2a2ab0; transform: translateY(-1px); }
        .form-button:disabled { background-color: #a7a7e6; cursor: not-allowed; }

        /* Gallery */
        .gallery-item {
            position: relative;
            overflow: hidden;
            border-radius: 12px;
            transition: all 0.2s ease;
            background-color: #F9FAFB;
            border: 1px solid #E5E7EB;
        }
        .gallery-item:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
        }
        .gallery-item .actions {
            position: absolute;
            top: 0.5rem;
            right: 0.5rem;
            display: flex;
            gap: 0.375rem;
            opacity: 0;
            transform: translateY(-8px);
            transition: all 0.25s ease;
            z-index: 10;
            pointer-events: auto;
        }
        .gallery-item:hover .actions {
            opacity: 1;
            transform: translateY(0);
        }
        .gallery-item .actions button {
            border-radius: 9999px;
            padding: 0.4rem;
            background-color: rgba(0,0,0,0.5);
            transition: background-color 0.2s;
        }
        .gallery-item .actions button:hover {
            background-color: rgba(0,0,0,0.7);
        }

        /* Search input underline hover */
        .search-input-container { position: relative; }
        .search-input-container::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            width: 0;
            height: 1px;
            background-color: rgba(17, 24, 39, 0.6);
            transform: translateX(-50%);
            transition: width 0.25s ease-in-out;
        }
        .search-input-container:hover::after,
        .search-input-container.focused::after { width: 100%; }
        .search-input {
            background-color: transparent;
            border: none;
            color: #111827;
        }
        .search-input::placeholder { color: #9CA3AF; }
        .search-input:focus { outline: none; }

        /* Delete modal */
        .delete-modal {
            position: fixed; inset: 0;
            background-color: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
            display: flex; align-items: center; justify-content: center;
            z-index: 1000; opacity: 0; visibility: hidden;
            transition: all 0.25s ease;
        }
        .delete-modal.show { opacity: 1; visibility: visible; }
        .delete-modal-content {
            background: #ffffff;
            border: 1px solid #e5e7eb;
            border-radius: 14px;
            padding: 1.5rem;
            max-width: 520px; width: 90%;
            text-align: center;
            transform: scale(0.96) translateY(8px);
            transition: all 0.25s ease;
        }
        .delete-modal.show .delete-modal-content { transform: scale(1) translateY(0); }
        .delete-modal-icon {
            width: 58px; height: 58px; margin: 0 auto 1rem;
            background: #FEF2F2; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
        }
        .delete-modal-title {
            font-size: 1.15rem; font-weight: 700; color: #111827; margin-bottom: 0.35rem;
        }
        .delete-modal-message { color: #4B5563; margin-bottom: 1.25rem; line-height: 1.55; }
        .delete-modal-actions { display: flex; gap: 0.75rem; justify-content: center; }
        .delete-modal-btn {
            padding: 0.65rem 1.25rem; border-radius: 10px; border: none; font-weight: 600;
            cursor: pointer; transition: all 0.2s ease; min-width: 100px;
        }
        .delete-modal-btn-cancel { background: #F3F4F6; color: #111827; }
        .delete-modal-btn-cancel:hover { background: #E5E7EB; }
        .delete-modal-btn-delete { background: #EF4444; color: white; }
        .delete-modal-btn-delete:hover { background: #DC2626; }

        /* Header styles (copied essentials from homepage) */
        .mobile-menu-item { padding: 0.875rem 1rem; background: #121212; border-bottom: solid 1px #2a2a2a; color: #fff; display: flex; align-items: center; justify-content: space-between; transition: background-color 0.2s ease; }
        .mobile-menu-item:hover { background-color: #1a1a1a; }
        .item-title { flex-grow: 1; margin-left: 0.75rem; font-weight: 500; }
        .hamburger-line { transition: all 0.3s ease; }
        .hamburger-active .hamburger-line:nth-child(1) { transform: translateY(7px) rotate(45deg); }
        .hamburger-active .hamburger-line:nth-child(2) { opacity: 0; }
        .hamburger-active .hamburger-line:nth-child(3) { transform: translateY(-7px) rotate(-45deg); }
    </style>
    <!-- MAIN CONTENT -->
    <!-- MAIN CONTENT -->
    <main class="w-full px-4 md:px-8 py-8 md:py-10">
        <div class="max-w-7xl mx-auto">
            <!-- Page heading -->
            <div class="mb-6 md:mb-8">
                <div class="relative inline-block">
                    <h1 class="section-title text-2xl md:text-3xl">Upload Magazine</h1>
                    <div class="absolute h-1 w-20 bg-[#3533CD] bottom-[-8px] left-0"></div>
                </div>
            </div>

            <!-- Upload Card -->
            <section class="section-card p-5 md:p-8 mb-10">
                <form id="magazineForm" class="space-y-6">
                    <!-- Magazine Name -->
                    <div>
                        <label for="magazineTitle" class="form-label">Magazine Name</label>
                        <input type="text" id="magazineTitle" name="title" class="form-input" placeholder="eg. BOL Magazine - July issue etc." required>
                    </div>

                    <!-- PDF and Thumbnail -->
                    <div class="flex flex-col md:flex-row gap-4 md:gap-6">
                        <!-- PDF -->
                        <div class="flex-1">
                            <label for="magazinePdf" class="form-label">Magazine PDF</label>
                            <div id="pdf-dropzone" class="file-input-display">
                                <span id="pdf-filename" class="file-input-placeholder truncate pr-4">Click or drop PDF here</span>
                                <i data-lucide="file-text" class="w-5 h-5 opacity-60"></i>
                            </div>
                            <input type="file" id="magazinePdf" name="pdf_file" class="hidden" accept="application/pdf" required>
                        </div>
                        <!-- Thumbnail -->
                        <div class="flex-1">
                            <label for="magazineThumbnail" class="form-label">Magazine Thumbnail (Optional)</label>
                            <div id="thumbnail-dropzone" class="file-input-display">
                                <span id="thumbnail-filename" class="file-input-placeholder truncate pr-4">Click or drop image here</span>
                                <i data-lucide="image" class="w-5 h-5 opacity-60"></i>
                            </div>
                            <input type="file" id="magazineThumbnail" name="thumbnail_file" class="hidden" accept="image/jpeg, image/png, image/webp">
                        </div>
                    </div>

                    <!-- Save Button -->
                    <div class="pt-2">
                        <button id="saveMagazineBtn" type="submit" class="form-button" disabled>
                            <i data-lucide="upload" class="w-4 h-4 mr-2"></i>
                            <span id="saveMagazineBtnText">Save Magazine</span>
                        </button>
                    </div>
                </form>
            </section>

            <!-- Gallery Heading -->
            <div class="mb-4 md:mb-6 flex items-end justify-between gap-4">
                <div class="relative inline-block">
                    <h2 class="section-title text-xl md:text-2xl">Magazine Gallery</h2>
                    <div class="absolute h-1 w-16 bg-[#3533CD] bottom-[-6px] left-0"></div>
                </div>
                <div class="relative w-full sm:w-auto sm:flex-1 max-w-xs">
                    <div class="search-input-container">
                        <i data-lucide="search" class="w-4 h-4 absolute left-4 top-1/2 -translate-y-1/2 text-gray-400 z-10"></i>
                        <input type="text" placeholder="Search magazines..." class="search-input w-full py-2 pl-11 pr-4 text-sm rounded-full border border-gray-200 focus:ring-0 focus:outline-none transition" id="searchInput">
                    </div>
                </div>
            </div>

            <!-- Gallery Grid -->
            <section>
                <div id="galleryGrid" class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 gap-4"></div>
                <div id="no-gallery-items" class="text-center py-16 hidden">
                    <i data-lucide="folder-x" class="w-16 h-16 mx-auto text-gray-300 mb-4"></i>
                    <h3 class="text-xl font-medium text-gray-800">No Magazines Found</h3>
                    <p class="text-gray-500 mt-2">Try uploading a new magazine.</p>
                </div>
            </section>
        </div>
    </main>
    <!-- Delete Confirmation Modal (unchanged endpoints/ids) -->
    <div id="deleteModal" class="delete-modal">
        <div class="delete-modal-content">
            <div class="delete-modal-icon">
                <i data-lucide="trash-2" class="w-8 h-8 text-red-500"></i>
            </div>
            <h3 class="delete-modal-title">Delete Magazine</h3>
            <p class="delete-modal-message" id="deleteModalMessage">
                Are you sure you want to delete this magazine? This action cannot be undone.
            </p>
            <div class="delete-modal-actions">
                <button class="delete-modal-btn delete-modal-btn-cancel" id="deleteModalCancel">Cancel</button>
                <button class="delete-modal-btn delete-modal-btn-delete" id="deleteModalConfirm">Delete</button>
            </div>
        </div>
    </div>
    <script>
    let magazineData = [];
    let isLoadingFiles = false;
    const BUCKET_MAPPING = { 'pdf': 'magazine-pdfs' };

    async function fetchMagazines() {
        const bucketName = BUCKET_MAPPING['pdf'];
        if (!bucketName) {
            console.error('No bucket mapping found for file type: pdf');
            return [];
        }
        try {
            const response = await fetch(`/get_file_details?bucket_name=${encodeURIComponent(bucketName)}&user_id=${encodeURIComponent(localStorage.getItem('BOLemail'))}`);
            const result = await response.json();
            if (result.status === 'success' && result.data) {
                const transformedData = result.data.map(file => ({
                    id: file.id,
                    name: file.name,
                    url: file.public_url,
                    thumbnail_url: file.thumbnail_url,
                }));
                return transformedData;
            } else {
                console.error('Failed to fetch magazines:', result.message || 'Unknown error');
                return [];
            }
        } catch (error) {
            console.error('Error fetching magazines:', error);
            return [];
        }
    }

    async function loadAllFiles() {
        if (isLoadingFiles) return;
        isLoadingFiles = true;
        try {
            magazineData = await fetchMagazines();
            renderGallery();
        } catch (error) {
            console.error('Error loading files:', error);
            showToast('Failed to load files from server', 'error');
        } finally {
            isLoadingFiles = false;
        }
    }

    function truncate(str, len) {
        return str.length > len ? str.substring(0, len) + "..." : str;
    }

    function renderGallery() {
        const searchInput = document.getElementById('searchInput');
        const searchTerm = searchInput ? searchInput.value.toLowerCase().trim() : '';
        renderGalleryWithSearch(searchTerm);
    }

    function renderGalleryWithSearch(searchTerm = '') {
        const galleryGrid = document.getElementById('galleryGrid');
        if (!galleryGrid) return;

        let filteredMedia = magazineData;
        if (searchTerm) {
            filteredMedia = magazineData.filter(item =>
                item.name.toLowerCase().includes(searchTerm)
            );
        }

        galleryGrid.innerHTML = '';
        if (filteredMedia.length === 0) {
            document.getElementById('no-gallery-items').classList.remove('hidden');
            galleryGrid.classList.add('hidden');
        } else {
            document.getElementById('no-gallery-items').classList.add('hidden');
            galleryGrid.classList.remove('hidden');
            filteredMedia.forEach(item => {
                const itemEl = document.createElement('div');
                itemEl.className = 'gallery-item group aspect-[4/5] flex flex-col justify-between text-center overflow-hidden';

                const truncatedName = truncate(item.name, 25);

                let thumbnailHTML;
                if (item.thumbnail_url) {
                    thumbnailHTML = `<div class="flex-grow w-full bg-white flex items-center justify-center overflow-hidden"><img src="${item.thumbnail_url}" alt="${item.name}" class="w-full h-full object-cover"></div>`;
                } else {
                    thumbnailHTML = `<div class="flex-grow w-full flex flex-col justify-center items-center bg-white">
                        <i data-lucide="file-text" class="w-16 h-16 text-gray-300"></i>
                    </div>`;
                }

                const content = `
                    ${thumbnailHTML}
                    <div class="w-full p-2 bg-white">
                        <p class="text-sm font-semibold text-gray-800" title="${item.name}">${truncatedName}</p>
                    </div>
                `;

                itemEl.innerHTML = content + `
                    <div class="actions">
                        <button class="action-btn" data-action="view" data-id="${item.id}" data-url="${item.url}" title="View"><i data-lucide="external-link" class="w-4 h-4 text-white"></i></button>
                        <button class="action-btn" data-action="download" data-id="${item.id}" data-url="${item.url}" data-name="${item.name}" title="Download"><i data-lucide="download" class="w-4 h-4 text-white"></i></button>
                        <button class="action-btn" data-action="copy" data-id="${item.id}" data-url="${item.url}" title="Copy URL"><i data-lucide="copy" class="w-4 h-4 text-white"></i></button>
                        <button class="action-btn delete" data-action="delete" data-id="${item.id}" data-name="${item.name}" title="Delete"><i data-lucide="trash" class="w-4 h-4 text-white"></i></button>
                    </div>
                `;
                galleryGrid.appendChild(itemEl);
            });
        }
        lucide.createIcons();
    }

    document.addEventListener('DOMContentLoaded', function() {
        // Auth check functionality
        async function checkAuthentication() {
            const email = localStorage.getItem('BOLemail');
            const password = localStorage.getItem('BOLpassword');
            
            if (!email || !password) {
                showAuthModal();
                return false;
            }
            
            try {
                const response = await fetch('/user_auth', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ email, password })
                });
                
                const result = await response.json();
                
                if (response.ok && result.status === 'success') {
                    return true;
                } else {
                    localStorage.removeItem('BOLemail');
                    localStorage.removeItem('BOLpassword');
                    showAuthModal(result.message || 'Authentication failed');
                    return false;
                }
            } catch (error) {
                console.error('Auth check error:', error);
                showAuthModal('Unable to verify authentication');
                return false;
            }
        }

        function showAuthModal(message = '') {
            const modal = document.createElement('div');
            modal.className = 'delete-modal show';
            modal.style.zIndex = '9999';
            
            modal.innerHTML = `
                <div class="delete-modal-content">
                    <div class="delete-modal-icon">
                        <i data-lucide="lock" class="w-6 h-6 text-red-600"></i>
                    </div>
                    <h3 class="delete-modal-title">Authentication Required</h3>
                    <p class="delete-modal-message">
                        ${message || 'You need to be logged in to access this page. Please log in to continue.'}
                    </p>
                    <div class="delete-modal-actions">
                        <button class="delete-modal-btn delete-modal-btn-delete" onclick="window.location.href='/login'">
                            Go to Login
                        </button>
                    </div>
                </div>
            `;
            
            document.body.appendChild(modal);
            
            // Prevent page interaction
            document.body.style.overflow = 'hidden';
            
            // Create icons for the modal
            lucide.createIcons();
        }

        // Load gallery on page load
        loadAllFiles();

        // Form logic (endpoints and fields unchanged)
        const magazineForm = document.getElementById('magazineForm');
        const saveMagazineBtn = document.getElementById('saveMagazineBtn');
        const saveMagazineBtnText = document.getElementById('saveMagazineBtnText');
        const titleInput = document.getElementById('magazineTitle');
        const pdfInput = document.getElementById('magazinePdf');
        const thumbnailInput = document.getElementById('magazineThumbnail');
        const pdfDropzone = document.getElementById('pdf-dropzone');
        const thumbnailDropzone = document.getElementById('thumbnail-dropzone');
        const pdfFilenameSpan = document.getElementById('pdf-filename');
        const thumbnailFilenameSpan = document.getElementById('thumbnail-filename');

        function validateForm() {
            const isTitleValid = titleInput.value.trim() !== '';
            const isPdfSelected = pdfInput.files.length > 0;
            saveMagazineBtn.disabled = !(isTitleValid && isPdfSelected);
        }

        titleInput.addEventListener('input', validateForm);
        pdfInput.addEventListener('change', validateForm);

        pdfDropzone.addEventListener('click', () => pdfInput.click());
        thumbnailDropzone.addEventListener('click', () => thumbnailInput.click());

        const setupDragDrop = (dropzone, input) => {
            ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
                dropzone.addEventListener(eventName, e => { e.preventDefault(); e.stopPropagation(); });
            });
            ['dragenter', 'dragover'].forEach(eventName => {
                dropzone.addEventListener(eventName, () => dropzone.classList.add('dragover'));
            });
            ['dragleave', 'drop'].forEach(eventName => {
                dropzone.addEventListener(eventName, () => dropzone.classList.remove('dragover'));
            });
            dropzone.addEventListener('drop', (e) => {
                input.files = e.dataTransfer.files;
                const event = new Event('change');
                input.dispatchEvent(event);
            });
        };
        setupDragDrop(pdfDropzone, pdfInput);
        setupDragDrop(thumbnailDropzone, thumbnailInput);

        pdfInput.addEventListener('change', () => {
            if (pdfInput.files.length > 0) {
                pdfFilenameSpan.textContent = pdfInput.files[0].name;
                pdfFilenameSpan.classList.remove('file-input-placeholder');
            } else {
                pdfFilenameSpan.textContent = 'Click or drop PDF here';
                pdfFilenameSpan.classList.add('file-input-placeholder');
            }
        });

        thumbnailInput.addEventListener('change', () => {
            if (thumbnailInput.files.length > 0) {
                thumbnailFilenameSpan.textContent = thumbnailInput.files[0].name;
                thumbnailFilenameSpan.classList.remove('file-input-placeholder');
            } else {
                thumbnailFilenameSpan.textContent = 'Click or drop image here';
                thumbnailFilenameSpan.classList.add('file-input-placeholder');
            }
        });

        magazineForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            if (saveMagazineBtn.disabled) return;

            saveMagazineBtn.disabled = true;
            saveMagazineBtnText.textContent = 'Saving...';

            const formData = new FormData();
            formData.append('title', titleInput.value);
            formData.append('pdf_file', pdfInput.files[0]);
            if (thumbnailInput.files.length > 0) {
                formData.append('thumbnail_file', thumbnailInput.files[0]);
            }
            formData.append('created_by', localStorage.getItem('BOLemail'));

            try {
                const response = await fetch('/create_magazine', {
                    method: 'POST',
                    body: formData
                });
                const result = await response.json();

                if (response.ok && result.status === 'success') {
                    showToast('Magazine saved successfully!', 'success');
                    magazineForm.reset();
                    pdfFilenameSpan.textContent = 'Click or drop PDF here';
                    pdfFilenameSpan.classList.add('file-input-placeholder');
                    thumbnailFilenameSpan.textContent = 'Click or drop image here';
                    thumbnailFilenameSpan.classList.add('file-input-placeholder');
                    validateForm();
                    await loadAllFiles(); // Refresh gallery
                } else {
                    showToast(result.message || 'Failed to save magazine.', 'error');
                }
            } catch (error) {
                showToast('An error occurred during upload.', 'error');
                console.error('Upload error:', error);
            } finally {
                saveMagazineBtn.disabled = false;
                saveMagazineBtnText.textContent = 'Save Magazine';
                validateForm();
            }
        });

        // Gallery actions
        const galleryGrid = document.getElementById('galleryGrid');
        galleryGrid.addEventListener('click', (e) => {
            const actionBtn = e.target.closest('.action-btn');
            if (!actionBtn) return;

            const action = actionBtn.dataset.action;
            const itemId = actionBtn.dataset.id;
            const itemUrl = actionBtn.dataset.url;
            const itemName = actionBtn.dataset.name;

            switch(action) {
                case 'view': handleViewAction(itemUrl, itemName); break;
                case 'download': handleDownloadAction(itemUrl, itemName); break;
                case 'copy': handleCopyAction(itemUrl); break;
                case 'delete': handleDeleteAction(itemId, itemName); break;
            }
        });

        function handleViewAction(url, name) {
            if (url) window.open('/flipbook/'+ url.split('/').pop(), '_blank');
        }

        async function handleDownloadAction(url, name) {
            if (!url) return;
            showToast('Starting download...', 'success');
            try {
                const response = await fetch(url);
                if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
                const blob = await response.blob();
                const downloadUrl = window.URL.createObjectURL(blob);
                const link = document.createElement('a');
                link.href = downloadUrl;
                link.download = name || 'download.pdf';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                window.URL.revokeObjectURL(downloadUrl);
            } catch (error) {
                console.error('Download failed, using fallback:', error);
                const link = document.createElement('a');
                link.href = url;
                link.target = '_blank';
                link.download = name || 'download.pdf';
                link.click();
            }
        }

        async function handleCopyAction(rawUrl) {
            const endpoint = `/get_iframe/${encodeURIComponent(rawUrl.split('/').pop())}`;
            const response = await fetch(endpoint, {
            method: 'GET',
            headers: { 'Accept': 'text/html, text/plain;q=0.9, */*;q=0.8' },
            credentials: 'same-origin'
            });

            if (!response.ok) {
            throw new Error(`Request failed with status ${response.status}`);
            }

            const text = await response.text();
            navigator.clipboard.writeText(text).then(() => {
                showToast('CODE copied to clipboard!');
            }).catch(err => {
                console.error('Failed to copy: ', err);
                showToast('Failed to copy CODE.', 'error');
            });
        }

        function showDeleteModal(fileName, onConfirm) {
            const modal = document.getElementById('deleteModal');
            const message = document.getElementById('deleteModalMessage');
            const confirmBtn = document.getElementById('deleteModalConfirm');
            const cancelBtn = document.getElementById('deleteModalCancel');

            message.innerHTML = `Are you sure you want to delete <strong>"${fileName}"</strong>?<br>This action cannot be undone.`;
            modal.classList.add('show');

            const handleConfirm = () => {
                hideDeleteModal();
                onConfirm();
                confirmBtn.removeEventListener('click', handleConfirm);
                cancelBtn.removeEventListener('click', handleCancel);
            };
            const handleCancel = () => {
                hideDeleteModal();
                confirmBtn.removeEventListener('click', handleConfirm);
                cancelBtn.removeEventListener('click', handleCancel);
            };

            confirmBtn.addEventListener('click', handleConfirm);
            cancelBtn.addEventListener('click', handleCancel);

            modal.addEventListener('click', (e) => { if (e.target === modal) handleCancel(); });
            document.addEventListener('keydown', function onEscape(e) {
                if (e.key === 'Escape') {
                    handleCancel();
                    document.removeEventListener('keydown', onEscape);
                }
            });
        }

        function hideDeleteModal() {
            document.getElementById('deleteModal').classList.remove('show');
        }

        async function handleDeleteAction(itemId, itemName) {
            showDeleteModal(itemName, async () => {
                showToast('Deleting magazine...', 'success');
                try {
                    const response = await fetch('/delete_magazine', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ id: itemId })
                    });
                    const result = await response.json();
                    if (response.ok && result.status === 'success') {
                        showToast(`Magazine "${itemName}" deleted successfully!`, 'success');
                        await loadAllFiles();
                    } else {
                        showToast(`Failed to delete magazine: ${result.message || 'Unknown error'}`, 'error');
                    }
                } catch (error) {
                    showToast(`Error deleting magazine: ${error.message}`, 'error');
                }
            });
        }

        function showToast(message, type = 'success') {
            const toast = document.createElement('div');
            let bgColor = type === 'error' ? 'bg-red-600' : type === 'warning' ? 'bg-yellow-600' : 'bg-green-600';
            toast.className = `fixed top-4 right-4 ${bgColor} text-white px-4 py-2 rounded-lg shadow-lg z-50 transition-all duration-300`;
            toast.textContent = message;
            document.body.appendChild(toast);
            setTimeout(() => {
                toast.style.opacity = '0';
                toast.style.transform = 'translateY(-10px)';
                setTimeout(() => { document.body.removeChild(toast); }, 250);
            }, 2200);
        }

        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            searchInput.addEventListener('focus', () => searchInput.parentElement.parentElement.classList.add('focused'));
            searchInput.addEventListener('blur', () => searchInput.parentElement.parentElement.classList.remove('focused'));
            searchInput.addEventListener('input', () => renderGallery());
        }
    });
</script>
    
    """