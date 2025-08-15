from .homepage_hero_section import get_homepage_hero_section_html
from .split_section import get_split_section
from .top_stories import get_top_stories

moving_banner = """<section
            class="box-border w-full h-[90px] border-y border-black flex items-center overflow-hidden relative my-5 strip-section">
            <div
                class="flex gap-[100px] md:gap-[180px] items-center h-[45px] whitespace-nowrap absolute animate-marquee">

                <span
                    class="font-helvetica font-bold text-[30px] md:text-[50px] leading-[90%] flex items-center text-center gradient-text strip-startups shrink-0">STARTUPS</span>
                <span
                    class="font-helvetica font-bold text-[30px] md:text-[50px] leading-[90%] flex items-center text-center gradient-text strip-ai shrink-0">AI</span>
                <span
                    class="font-helvetica font-bold text-[30px] md:text-[50px] leading-[90%] flex items-center text-center gradient-text strip-business shrink-0">BUSINESS</span>
                <span
                    class="font-helvetica font-bold text-[30px] md:text-[50px] leading-[90%] flex items-center text-center gradient-text strip-entrepreneur shrink-0">ENTREPRENEUR</span>
                <span
                    class="font-helvetica font-bold text-[30px] md:text-[50px] leading-[90%] flex items-center text-center gradient-text strip-events shrink-0">EVENTS</span>
                <span
                    class="font-helvetica font-bold text-[30px] md:text-[50px] leading-[90%] flex items-center text-center gradient-text strip-brands shrink-0">BRANDS</span>
                <span
                    class="font-helvetica font-bold text-[30px] md:text-[50px] leading-[90%] flex items-center text-center gradient-text strip-trends shrink-0">TRENDS</span>
            </div>
        </section>"""

EMPTY_HOMEPAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brands Out Loud</title>

    <script src="https://cdn.tailwindcss.com?plugins=typography,line-clamp"></script>
    <script src="https://unpkg.com/@phosphor-icons/web@2.0.3"></script>

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

    <!-- Icon packs used across site -->
    <script src="https://unpkg.com/@phosphor-icons/web@2.0.3"></script>
    <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>

    <link
        href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500&family=IBM+Plex+Sans:wght@600&family=Inter:wght@500&family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,800&family=Roboto:wght@500&display=swap"
        rel="stylesheet">
    <link rel="icon" type="image/png" href="static/icon/website_icon.png">

    <style>
        @media screen and (min-width: 1024px) {
            body {
                zoom: 1.13;
            }
        }

        .gradient-text {
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-fill-color: transparent;
            display: inline-block;
        }

        .strip-startups {
            background-image: linear-gradient(93.43deg, #000000 6.93%, #3533CD 94.41%);
        }

        .strip-ai {
            background-image: linear-gradient(211.98deg, #000000 19.22%, #3533CD 94.53%);
        }

        .strip-business {
            background-image: linear-gradient(105.57deg, #000000 2.6%, #3533CD 60.9%);
        }

        .strip-entrepreneur {
            background-image: linear-gradient(90.82deg, #000000 3.28%, #3533CD 140.89%);
        }

        .strip-events {
            background-image: linear-gradient(260.78deg, #000000 43.02%, #3533CD 106.67%);
        }

        .strip-brands {
            background-image: linear-gradient(104.28deg, #000000 3.4%, #3533CD 101.3%);
        }

        .strip-trends {
            background-image: linear-gradient(264.46deg, #000000 -20.15%, #3533CD 54.42%);
        }

        .podcast-title-gradient {
            background: linear-gradient(269.15deg, #000000 47.22%, #3533CD 97.69%);
        }

        .hero-title-gradient {
            background: linear-gradient(90deg, #FFFFFF 0%, #3533CD 100%);
        }

        .footer-italic-gradient {
            background: linear-gradient(90deg, #C4C3FF 0%, #10E2FF 100%);
        }

        .button-icon-plus-shape::before,
        .button-icon-plus-shape::after {
            content: '';
            position: absolute;
            background-color: currentColor;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
        }

        .button-icon-plus-shape::before {
            width: 12px;
            height: 2px;
        }

        .button-icon-plus-shape::after {
            width: 2px;
            height: 12px;
        }

        .button-icon-union-shape {
            background: currentColor;

        }

        .location-input-wrapper::after {
            content: '';
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

        input[type="checkbox"]:checked {
            background-color: #3533CD;
            border-color: #3533CD;
            background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M12.207 4.793a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0l-2-2a1 1 0 011.414-1.414L6.5 9.086l4.293-4.293a1 1 0 011.414 0z'/%3e%3c/svg%3e");
            background-size: 100% 100%;
            background-position: center;
            background-repeat: no-repeat;
        }

        ::-webkit-scrollbar {
            display: none;
        }

        body {
            -ms-overflow-style: none;
            scrollbar-width: none;
        }

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
            --clr-primary: #9747FF;
            --clr-primary-light: #CDA7FF;
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
            justify-content: space-between;
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

        /* --- UPDATED DROPDOWN STYLES --- */
        .dropdown-container {
            position: relative;
            padding-bottom: 20px;
            /* Creates an invisible area below the link for the cursor to travel over */
            margin-bottom: -20px;
            /* Negative margin to pull layout back up */
        }

        .dropdown-content {
            position: absolute;
            top: 100%;
            /* Positions the dropdown right below the parent's padding area */
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
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {

                        'jakarta': ['"Plus Jakarta Sans"', 'sans-serif'],
                        'helvetica': ['"Helvetica Now Display"', 'Arial', 'sans-serif'],
                        'dm': ['"DM Sans"', 'sans-serif'],
                        'ibm-plex': ['"IBM Plex Sans"', 'sans-serif'],
                        'inter': ['"Inter"', 'sans-serif'],
                        'roboto': ['"Roboto"', 'sans-serif'],
                        'sans': ['"Plus Jakarta Sans"', 'sans-serif'],
                    },
                    colors: {
                        'bol-purple': '#3533CD',
                        'bol-purple-light': '#C4C3FF',
                        'bol-black': '#0D0D0D',
                        'bol-gray': '#B8C2CE',

                    },
                    spacing: {
                        '1.5px': '1.5px',
                        '13px': '13px',
                    },
                    fontSize: {
                        '10px': '10px',
                    },
                    lineHeight: {
                        '13px': '13px',
                    },
                    animation: {
                        marquee: 'marquee 30s linear infinite',
                    },
                    keyframes: {
                        marquee: {
                            '0%': { transform: 'translateX(0%)' },
                            '100%': { transform: 'translateX(-50%)' },
                        }
                    }
                }
            }
        }
    </script>
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const mobileMenuButton = document.getElementById('mobile-menu-button');
            const mobileMenu = document.getElementById('mobile-menu');

            mobileMenuButton.addEventListener('click', function () {
                mobileMenu.classList.toggle('hidden');
                mobileMenuButton.classList.toggle('hamburger-active');

                if (!mobileMenu.classList.contains('hidden')) {
                    mobileMenu.classList.add('slide-down');
                } else {
                    mobileMenu.classList.remove('slide-down');
                }
            });

            // Blog item click handlers
            document.addEventListener('click', function (e) {
                if (e.target.closest('.dropdown-item:not(.know-more-item)')) {
                    const item = e.target.closest('.dropdown-item');
                    const category = item.getAttribute('data-category');
                    const blogId = item.getAttribute('data-id');

                    console.log('Clicked blog:', { category, blogId });
                    // Replace with actual navigation
                    // window.location.href = `/blog/${category}/${blogId}`;
                }
            });

            // Know More click handlers
            document.addEventListener('click', function (e) {
                if (e.target.closest('.know-more-item')) {
                    const item = e.target.closest('.dropdown-container');
                    const category = item.getAttribute('data-category');

                    console.log('Know More clicked for:', category);
                    // Replace with actual navigation
                    // window.location.href = `/category/${category}`;
                }
            });

            // --- Mobile Accordion Menu Logic ---
            const mobileMenuContainer = document.getElementById('mobile-menu');
            if (mobileMenuContainer) {
                mobileMenuContainer.addEventListener('click', function (e) {
                    const toggle = e.target.closest('.accordion-toggle');
                    if (!toggle) return;

                    e.preventDefault();
                    const content = toggle.nextElementSibling;
                    const isCurrentlyOpen = toggle.getAttribute('aria-expanded') === 'true';

                    // Close all other accordions before opening a new one
                    mobileMenuContainer.querySelectorAll('.accordion-toggle').forEach(otherToggle => {
                        if (otherToggle !== toggle) {
                            otherToggle.setAttribute('aria-expanded', 'false');
                            const otherContent = otherToggle.nextElementSibling;
                            if (otherContent) otherContent.style.maxHeight = '0px';
                        }
                    });

                    // Toggle the clicked accordion
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
</head>

<body class="font-jakarta bg-white text-bol-black">
    <div class="flex flex-col items-center w-full max-w-[1440px] mx-auto bg-white overflow-x-hidden relative">

        [[total_body]]

    </div>

    <script defer>

        const stripSection = document.querySelector('.strip-section');
        if (stripSection) {
            const stripContent = stripSection.querySelector('.animate-marquee');
            if (stripContent && stripContent.children.length > 0) {

                const contentWidth = stripContent.scrollWidth / 2;
                const containerWidth = stripSection.offsetWidth;

                stripContent.innerHTML += stripContent.innerHTML;
            }
        }

        const highFiveEmojis = document.querySelectorAll('.high-five-emoji');
        const countNumbers = document.querySelectorAll('.count-number');

        let highFiveCount = parseInt(localStorage.getItem('highFiveCount') || '521');

        function updateHighFiveDisplay() {
            countNumbers.forEach(numDisplay => {
                numDisplay.textContent = highFiveCount;
            });
        }

        updateHighFiveDisplay();

        highFiveEmojis.forEach(emoji => {
            emoji.addEventListener('click', () => {
                highFiveCount++;
                updateHighFiveDisplay();

                localStorage.setItem('highFiveCount', highFiveCount);

                emoji.style.transform = 'scale(1.2)';
                setTimeout(() => {
                    emoji.style.transform = 'scale(1)';
                }, 150);
            });
        })

    </script>
</body>

</html>"""
