MAGAZINE_IFRAME_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0, viewport-fit=cover"
    />
    <title>Magazine Flipbook Viewer</title>

    <!-- PDF.js -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>

    <!-- PageFlip (flip.js) -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/page-flip/dist/css/page-flip.min.css" />
    <script src="https://cdn.jsdelivr.net/npm/page-flip/dist/js/page-flip.browser.min.js"></script>

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: #1a1a1a;
            overflow: hidden;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }

        #flipbook-container {
            flex: 1;
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
            perspective: 2000px;
            overflow: hidden;
            min-height: 400px;
        }

        .flipbook {
            position: relative;
            display: block;
            width: 100%;
            height: 100%;
            margin-top: 0rem; /* Default for iframe mode */
        }

        /* PageFlip page content */
        .page {
            background: white;
            box-shadow: 0 0 20px rgba(0,0,0,0.2);
            cursor: pointer;
        }

        .page .page-content {
            position: relative;
            width: 100%;
            height: 100%;
        }

        .page canvas {
            display: block;
            width: 100%;
            height: 100%;
        }

        /* Make the leading blank page transparent (no white panel on the left) */
        .page[data-blank="true"] {
            background: transparent;
            box-shadow: none;
            cursor: default;
        }

        /* Navigation Arrows */
        .nav-arrow {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            width: 50px;
            height: 50px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 50%;
            display: none; /* shown by JS */
            align-items: center;
            justify-content: center;
            cursor: pointer;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            user-select: none;
        }

        .nav-arrow:hover { background: white; }

        .nav-arrow.prev { left: 20px; }
        .nav-arrow.next { right: 20px; }

        .nav-arrow svg { width: 24px; height: 24px; fill: #333; }

        .nav-arrow.disabled { opacity: 0.3; cursor: not-allowed; }

        /* Hide navigation arrows on small screens */
        @media (max-width: 768px) {
            .nav-arrow { display: none !important; }
        }

        /* Controls Bar */
        #controls {
            position: absolute;
            bottom: 0;
            left: 0; right: 0;
            background: rgba(0, 0, 0, 0.85);
            backdrop-filter: blur(10px);
            padding: 15px 20px;
            display: flex;
            align-items: center;
            gap: 20px;
            z-index: 1500;
        }

        /* Progress Bar */
        .progress-container {
            flex: 1;
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .page-info {
            color: white;
            font-size: 14px;
            min-width: 80px;
            text-align: center;
        }

        .progress-bar {
            flex: 1;
            height: 4px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 2px;
            position: relative;
            cursor: pointer;
        }

        .progress-fill {
            height: 100%;
            background: #007bff;
            border-radius: 2px;
            position: relative;
            transition: width 0.3s ease;
        }

        .progress-thumb {
            position: absolute;
            top: 50%;
            right: -8px;
            transform: translateY(-50%);
            width: 16px;
            height: 16px;
            background: white;
            border-radius: 50%;
            box-shadow: 0 2px 6px rgba(0,0,0,0.3);
            cursor: grab;
        }
        .progress-thumb:active { cursor: grabbing; }

        /* Control Buttons */
        .control-btn {
            background: transparent;
            border: 1px solid rgba(255,255,255,0.3);
            color: white;
            padding: 8px 12px;
            border-radius: 4px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s ease;
            font-size: 14px;
        }
        .control-btn:hover {
            background: rgba(255,255,255,0.1);
            border-color: rgba(255,255,255,0.5);
        }
        .control-btn svg { width: 18px; height: 18px; fill: white; }

        /* Mobile: icon-only control buttons in controls bar */
        @media (max-width: 768px) {
            #controls .control-btn span { display: none !important; }
            #controls .control-btn { padding: 8px; gap: 0; }
        }

        /* URL Highlights */
        .url-overlay {
            position: absolute;
            border: 1px solid #007bff;
            background: rgba(0,123,255,0.2);
            cursor: pointer;
            transition: all 0.2s ease;
            pointer-events: all;
            border-radius: 5px;
            z-index: 50; /* above canvas, inside page-content */
            min-width: 20px;
            min-height: 10px;
            max-height: 12px;
        }
        .url-overlay:hover {
            background: rgba(0,123,255,0.6);
            box-shadow: 0 0 20px rgba(0,123,255,1);
            border-color: #0056b3;
            border-width: 4px;
            transform: scale(1.05);
        }
        .url-overlay::after {
            content: "🔗 CLICK";
            position: absolute;
            top: -25px;
            left: 50%;
            transform: translateX(-50%);
            background: #007bff;
            color: white;
            padding: 2px 6px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 10px;
            font-weight: bold;
            white-space: nowrap;
            opacity: 0;
            transition: opacity 0.2s ease;
            pointer-events: none;
        }
        .url-overlay:hover::after { opacity: 1; }

        /* Responsive for iframe vs fullscreen */
        body.iframe-mode #flipbook-container { padding: 10px 10px 70px 10px; /* Extra bottom padding for controls */ }
        body.fullscreen-mode { background: #000; }
        body.fullscreen-mode #flipbook-container { padding: 40px; }
        body.fullscreen-mode .flipbook { margin-top: 0rem; /* Different margin for fullscreen */ }

        /* Fullscreen specific styles */
        :-webkit-full-screen { background: #000; }
        :-moz-full-screen { background: #000; }
        :fullscreen { background: #000; }

        /* Loading indicator */
        .page-loading {
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            display: flex; flex-direction: column; align-items: center; gap: 10px;
            z-index: 2000;
        }
        .page-loading .spinner {
            width: 40px; height: 40px;
            border: 3px solid rgba(255, 255, 255, 0.3);
            border-top: 3px solid #007bff;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        @keyframes spin { 0% { transform: rotate(0deg);} 100% { transform: rotate(360deg);} }
        .page-loading .text { color: rgba(255,255,255,0.8); font-size: 14px; }

        /* Hide controls in loading state */
        body.loading #controls { opacity: 0.5; pointer-events: none; }
    </style>
</head>
<body class="iframe-mode loading">
    <div id="flipbook-container">
        <div class="flipbook" id="flipbook"></div>

        <!-- Navigation Arrows -->
        <div class="nav-arrow prev" id="prevBtn" style="display: none;">
            <svg viewBox="0 0 24 24">
                <path d="M15.41 7.41L14 6l-6 6 6 6 1.41-1.41L10.83 12z"/>
            </svg>
        </div>
        <div class="nav-arrow next" id="nextBtn" style="display: none;">
            <svg viewBox="0 0 24 24">
                <path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"/>
            </svg>
        </div>

        <div id="globalLoading" class="page-loading" style="display: flex;">
            <div class="spinner"></div>
            <div class="text">Loading PDF...</div>
        </div>
    </div>

    <!-- Controls Bar -->
    <div id="controls">
        <div class="progress-container">
            <span class="page-info" id="pageInfo">1 / 1</span>
            <div class="progress-bar" id="progressBar">
                <div class="progress-fill" id="progressFill" style="width: 0%">
                    <div class="progress-thumb" id="progressThumb"></div>
                </div>
            </div>
        </div>

        <button class="control-btn" id="downloadBtn">
            <svg viewBox="0 0 24 24">
                <path d="M19 9h-4V3H9v6H5l7 7 7-7zM5 18v2h14v-2H5z"/>
            </svg>
            <span id="downloadButtonText">Download</span>
        </button>

        <button class="control-btn" id="fullscreenBtn">
            <svg viewBox="0 0 24 24" id="fullscreenIcon">
                <path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/>
            </svg>
            <span id="fullscreenText">Fullscreen</span>
        </button>
    </div>

    <script>
        // Global variables
        let pdfDoc = null;
        let totalPages = 0;
        let currentPage = 1; // 1-based
        let viewport = null; // Base (scale: 1) viewport for sizing/aspect
let pagesCache = {}; // {pageNum: { baseViewport, links, lowCanvas, highCanvas }}
let isFullscreen = false;
let isDragging = false;
let pageFlip = null;
let hasBlankStart = !(window.innerWidth <= 768);

        // Optional: CDN resources for fonts/cmaps if needed by some PDFs
        const PDFJS_VERSION = '3.11.174';
        const CMAP_URL = `https://unpkg.com/pdfjs-dist@${PDFJS_VERSION}/cmaps/`;
        const STANDARD_FONT_DATA_URL = `https://unpkg.com/pdfjs-dist@${PDFJS_VERSION}/standard_fonts/`;

        // PDF.js configuration
        pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';

        // Get PDF URL from query params, data attribute, or default
        const urlParams = new URLSearchParams(window.location.search);
        let pdfUrl = urlParams.get('pdf');
        if (!pdfUrl && typeof INJECTED_PDF_URL !== 'undefined') {
            pdfUrl = INJECTED_PDF_URL;
        }
        if (!pdfUrl) {
            pdfUrl = "https://iwyjssxhrcucnrkzkvmt.supabase.co/storage/v1/object/public/magazine-pdfs/CXO%20TechBOT%20October%202024-1-25.pdf";
        }
        const qualityParam = (urlParams.get('quality') || '').toLowerCase();
        const QUALITY_FACTOR = qualityParam === 'ultra' ? 2.0 : qualityParam === 'high' ? 1.5 : qualityParam === 'med' ? 1.2 : 1.0;

        // Progressive quality: quick low-res for instant paint, then upgrade to high-res
        function getQuickScale() {
            return Math.max(window.devicePixelRatio, 1) * 0.9; // fast
        }
        function getHighScale() {
            return (isFullscreen ? 2.0 : 1.8) * window.devicePixelRatio; // detailed
        }

        // Calculate page dimensions (per single page) based on container and PDF aspect
        function calculatePageDimensions() {
            const container = document.getElementById('flipbook-container');
            const containerWidth = container.clientWidth;
            const containerHeight = container.clientHeight;

            if (!viewport) return { width: 300, height: 400 };

            const pageAspectRatio = viewport.width / viewport.height;
            const padding = isFullscreen ? 40 : 20;
            const controlsHeight = 65; // Height of controls bar

            const availableWidth = containerWidth - (padding * 2);
            const availableHeight = containerHeight - controlsHeight - (padding * 2);

            // Mobile: show one page at a time; Desktop: keep spread (two pages)
            const singlePageMode = window.innerWidth <= 768 || containerWidth <= 768;
            let pageWidth = (availableWidth * 0.98) / (singlePageMode ? 1 : 2);
            let pageHeight = pageWidth / pageAspectRatio;
            if (pageHeight > availableHeight * 0.95) {
                pageHeight = availableHeight * 0.95;
                pageWidth = pageHeight * pageAspectRatio;
            }

            return {
                width: Math.floor(pageWidth),
                height: Math.floor(pageHeight)
            };
        }

        // Render a page at a given quality ('low' | 'high'), caching canvases per page
        async function renderPage(pageNum, quality = 'low') {
            if (!pdfDoc) return null;

            const cache = pagesCache[pageNum];
            if (cache && ((quality === 'low' && cache.lowCanvas) || (quality === 'high' && cache.highCanvas))) {
                return cache;
            }

            try {
                const page = await pdfDoc.getPage(pageNum);

                // Prepare baseViewport and link annotations once
                let baseViewport, links;
                if (!cache) {
                    baseViewport = page.getViewport({ scale: 1 });
                    const annotations = await page.getAnnotations();
                    links = annotations
                        .filter(ann => ann.subtype === 'Link' && ann.url && ann.rect)
                        .map(ann => {
                            try {
                                const [x1, y1, x2, y2] = baseViewport.convertToViewportRectangle(ann.rect);
                                const left = Math.min(x1, x2);
                                const top = Math.min(y1, y2);
                                const width = Math.abs(x2 - x1);
                                const height = Math.abs(y2 - y1);
                                return { url: ann.url, rect: [left, top, width, height] };
                            } catch {
                                return null;
                            }
                        })
                        .filter(Boolean);
                } else {
                    baseViewport = cache.baseViewport;
                    links = cache.links;
                }

                // Choose render scale based on the actual target canvas size for crisp text
                let desiredScale;
                const pageCanvasEl = document.querySelector(`.page[data-page="${pageNum}"] canvas`);
                if (pageCanvasEl && baseViewport) {
                    const targetPxW = pageCanvasEl.width || Math.floor(pageCanvasEl.clientWidth * window.devicePixelRatio);
                    const targetPxH = pageCanvasEl.height || Math.floor(pageCanvasEl.clientHeight * window.devicePixelRatio);
                    const scaleW = targetPxW / baseViewport.width;
                    const scaleH = targetPxH / baseViewport.height;
                    const displayScale = Math.min(scaleW, scaleH);
                    // Match canvas pixel ratio for 1:1 mapping to maximize clarity
                    const oversample = 1.0;
                    desiredScale = Math.max(1, displayScale * oversample);
                } else {
                    // Fallback if page canvas is not in DOM yet
                    desiredScale = quality === 'low' ? getQuickScale() : getHighScale();
                }
                const renderViewport = page.getViewport({ scale: desiredScale });

                const canvas = document.createElement('canvas');
                const context = canvas.getContext('2d', { alpha: false });
                canvas.height = renderViewport.height;
                canvas.width = renderViewport.width;

                await page.render({
                    canvasContext: context,
                    viewport: renderViewport
                }).promise;

                pagesCache[pageNum] = {
                    ...(cache || {}),
                    baseViewport,
                    links,
                    lowCanvas: quality === 'low' ? canvas : (cache ? cache.lowCanvas : null),
                    highCanvas: quality === 'high' ? canvas : (cache ? cache.highCanvas : null),
                };

                return pagesCache[pageNum];
            } catch (error) {
                console.error(`Error rendering page ${pageNum} (${quality}):`, error);
                return null;
            }
        }

        // Add URL overlay highlights into a .page-content element
        function addUrlOverlays(pageContent, links, baseViewport, dimensions) {
            // Use percentage-based positioning so overlays stay aligned across resize/zoom/fullscreen
            const bw = baseViewport.width || 1;
            const bh = baseViewport.height || 1;

            links.forEach(link => {
                const [left, top, width, height] = link.rect;
                const overlay = document.createElement('div');
                overlay.className = 'url-overlay';
                overlay.style.left = `${(left / bw) * 100}%`;
                overlay.style.top = `${(top / bh) * 100}%`;
                overlay.style.width = `${Math.max(0, (width / bw) * 100)}%`;
                overlay.style.height = `${Math.max(0, (height / bh) * 100)}%`;
                overlay.dataset.url = link.url;
                overlay.title = `Click to open: ${link.url}`;
                overlay.addEventListener('click', (e) => {
                    e.stopPropagation();
                    window.open(link.url, '_blank');
                });
                pageContent.appendChild(overlay);
            });
        }

        // Create a PageFlip-compatible page shell with canvas
        function createFlipPageShell(pageNum, dimensions) {
            const page = document.createElement('div');
            page.className = 'page';
            page.dataset.page = pageNum;
            page.style.width = `${dimensions.width}px`;
            page.style.height = `${dimensions.height}px`;

            const content = document.createElement('div');
            content.className = 'page-content';
            content.style.width = '100%';
            content.style.height = '100%';

            const canvas = document.createElement('canvas');
            // Increase backing resolution for sharper text (super-sampling)
            const mult = (isFullscreen ? 3.0 : 2.0) * QUALITY_FACTOR;
            canvas.width = Math.floor(dimensions.width * window.devicePixelRatio * mult);
            canvas.height = Math.floor(dimensions.height * window.devicePixelRatio * mult);
            canvas.style.width = '100%';
            canvas.style.height = '100%';

            content.appendChild(canvas);
            page.appendChild(content);
            return { page, content, canvas };
        }

        // Create a blank page shell to ensure symmetric animation on first/last flips
        function createBlankPageShell(dimensions) {
            const page = document.createElement('div');
            page.className = 'page';
            page.dataset.blank = 'true';
            page.style.width = `${dimensions.width}px`;
            page.style.height = `${dimensions.height}px`;

            const content = document.createElement('div');
            content.className = 'page-content';
            content.style.width = '100%';
            content.style.height = '100%';

            page.appendChild(content);
            return page;
        }

        // Draw provided source canvas into target canvas (scaled)
        function drawInto(targetCanvas, sourceCanvas) {
            const ctx = targetCanvas.getContext('2d', { alpha: false });
            ctx.imageSmoothingEnabled = true;
            if (ctx.imageSmoothingQuality) ctx.imageSmoothingQuality = 'high';
            ctx.clearRect(0, 0, targetCanvas.width, targetCanvas.height);
            ctx.drawImage(
                sourceCanvas,
                0, 0, sourceCanvas.width, sourceCanvas.height,
                0, 0, targetCanvas.width, targetCanvas.height
            );
        }

        // Upgrade an existing .page canvas to high quality
        async function upgradePageCanvasToHigh(pageNum, dimensions) {
            const data = await renderPage(pageNum, 'high');
            if (!data) return;
            const pageEl = document.querySelector(`.page[data-page="${pageNum}"]`);
            if (!pageEl) return;
            const canvas = pageEl.querySelector('canvas');
            if (!canvas) return;
            drawInto(canvas, data.highCanvas);
        }

        // Rebuild all page canvases at current size/quality (useful after fullscreen/resize)
        function rebuildAllPagesForQuality() {
            const dims = calculatePageDimensions();
            const pages = document.querySelectorAll('#flipbook .page');
            pages.forEach((pageEl) => {
                if (pageEl.dataset.blank === 'true') return;
                const canvas = pageEl.querySelector('canvas');
                if (!canvas) return;
                const dpr = window.devicePixelRatio || 1;
                const mult = (isFullscreen ? 3.0 : 2.0) * QUALITY_FACTOR;
                const targetW = Math.floor(dims.width * dpr * mult);
                const targetH = Math.floor(dims.height * dpr * mult);
                if (canvas.width === targetW && canvas.height === targetH) return;
                canvas.width = targetW;
                canvas.height = targetH;
                const pageNum = parseInt(pageEl.dataset.page, 10);
                if (!isNaN(pageNum)) {
                    upgradePageCanvasToHigh(pageNum, dims);
                }
            });
        }

        // Update controls
        function updateControls() {
            document.getElementById('pageInfo').textContent = `${currentPage} / ${totalPages}`;
            const progress = totalPages > 1 ? ((currentPage - 1) / (totalPages - 1)) * 100 : 0;
            document.getElementById('progressFill').style.width = `${progress}%`;

            const prevBtn = document.getElementById('prevBtn');
            const nextBtn = document.getElementById('nextBtn');

            if (currentPage <= 1) {
                prevBtn.classList.add('disabled');
            } else {
                prevBtn.classList.remove('disabled');
            }

            if (currentPage >= totalPages) {
                nextBtn.classList.add('disabled');
            } else {
                nextBtn.classList.remove('disabled');
            }
        }

        // Progress bar drag functionality
        function initProgressBar() {
            const progressBar = document.getElementById('progressBar');
            const progressThumb = document.getElementById('progressThumb');

            function updateProgressFromMouse(e) {
                const rect = progressBar.getBoundingClientRect();
                const x = Math.max(0, Math.min(e.clientX - rect.left, rect.width));
                const progress = x / rect.width;
                const targetPage = Math.max(1, Math.min(totalPages, Math.round(progress * (totalPages - 1) + 1)));
                if (targetPage !== currentPage) {
                    if (pageFlip) pageFlip.turnToPage(hasBlankStart ? targetPage : targetPage - 1);
                }
            }

            progressThumb.addEventListener('mousedown', (e) => {
                isDragging = true;
                e.preventDefault();
            });

            document.addEventListener('mousemove', (e) => {
                if (isDragging) updateProgressFromMouse(e);
            });

            document.addEventListener('mouseup', () => {
                isDragging = false;
            });

            progressBar.addEventListener('click', (e) => {
                if (!isDragging) updateProgressFromMouse(e);
            });
        }

        // Navigation buttons using PageFlip
        document.getElementById('prevBtn').addEventListener('click', () => {
            if (!pageFlip) return;
            if (currentPage <= 1) return;
            pageFlip.flipPrev();
        });

        document.getElementById('nextBtn').addEventListener('click', () => {
            if (!pageFlip) return;
            if (currentPage >= totalPages) return;
            pageFlip.flipNext();
        });

        // Download button
        // Prefer direct, user-gesture download inside iframe via same-origin proxy derived from parent origin.
        document.getElementById('downloadBtn').addEventListener('click', () => {
            const filename = (pdfUrl.split('/').pop() || 'document.pdf');
            try {
                // document.referrer contains the parent page URL for srcdoc iframes
                const parentOrigin = (() => {
                    try { return new URL(document.referrer).origin; } catch { return null; }
                })();
                if (parentOrigin) {
                    const proxiedUrl = `${parentOrigin}/download_proxy?pdf=${encodeURIComponent(pdfUrl)}&filename=${encodeURIComponent(filename)}`;
                    const a = document.createElement('a');
                    a.href = proxiedUrl;
                    a.download = filename;
                    a.target = '_blank';
                    a.rel = 'noopener';
                    a.style.display = 'none';
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    return;
                }
            } catch (_) {
                // fall through to fallback
            }
            // Fallback: ask parent to perform the download
            if (window.parent && window.parent !== window) {
                window.parent.postMessage({ action: 'download', pdfUrl, filename }, '*');
            } else {
                // Last resort: open the PDF directly
                const a = document.createElement('a');
                a.href = pdfUrl;
                a.download = filename;
                a.target = '_blank';
                a.rel = 'noopener';
                a.style.display = 'none';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
            }
        });

        // Fullscreen button
        document.getElementById('fullscreenBtn').addEventListener('click', () => {
            if (!isFullscreen) {
                if (document.documentElement.requestFullscreen) {
                    document.documentElement.requestFullscreen();
                } else if (document.documentElement.webkitRequestFullscreen) {
                    document.documentElement.webkitRequestFullscreen();
                } else if (document.documentElement.msRequestFullscreen) {
                    document.documentElement.msRequestFullscreen();
                }
            } else {
                if (document.exitFullscreen) {
                    document.exitFullscreen();
                } else if (document.webkitExitFullscreen) {
                    document.webkitExitFullscreen();
                } else if (document.msExitFullscreen) {
                    document.msExitFullscreen();
                }
            }
        });

        // Fullscreen change handler (keeps auto-resize)
        function handleFullscreenChange() {
            isFullscreen = document.fullscreenElement ||
                           document.webkitFullscreenElement ||
                           document.msFullscreenElement;

            const fullscreenIcon = document.getElementById('fullscreenIcon');
            const fullscreenText = document.getElementById('fullscreenText');

            if (isFullscreen) {
                document.body.classList.remove('iframe-mode');
                document.body.classList.add('fullscreen-mode');
                fullscreenIcon.innerHTML = '<path d="M5 16h3v3h2v-5H5v2zm3-8H5v2h5V5H8v3zm6 11h2v-3h3v-2h-5v5zm2-11V5h-2v5h5V8h-3z"/>';
                fullscreenText.textContent = 'Exit Fullscreen';
            } else {
                document.body.classList.add('iframe-mode');
                document.body.classList.remove('fullscreen-mode');
                fullscreenIcon.innerHTML = '<path d="M7 14H5v5h5v-2H7v-3zm-2-4h2V7h3V5H5v5zm12 7h-3v2h5v-5h-2v3zM14 5v2h3v3h2V5h-5z"/>';
                fullscreenText.textContent = 'Fullscreen';
            }

            // Trigger PageFlip to recalc and fit container automatically
            if (pageFlip) {
                // small defer to allow layout to settle
                setTimeout(() => {
                    pageFlip.update();
                    // then rebuild canvases at higher backing resolution for crispness
                    setTimeout(rebuildAllPagesForQuality, 100);
                }, 50);
            }
        }

        document.addEventListener('fullscreenchange', handleFullscreenChange);
        document.addEventListener('webkitfullscreenchange', handleFullscreenChange);
        document.addEventListener('msfullscreenchange', handleFullscreenChange);

        // Listen for messages from parent (iframe control)
        window.addEventListener('message', (event) => {
            const msg = event.data || {};
            const msgType = msg.type || msg.action;

            if (msgType === 'flipToPage') {
                if (pageFlip) {
                    const tp = Math.max(1, Math.min(totalPages, msg.page || 1));
                    pageFlip.turnToPage(hasBlankStart ? tp : tp - 1);
                }
            } else if (msgType === 'nextPage') {
                if (pageFlip && currentPage < totalPages) pageFlip.flipNext();
            } else if (msgType === 'prevPage') {
                if (pageFlip && currentPage > 1) pageFlip.flipPrev();
            } else if (msgType === 'toggleFullscreen') {
                document.getElementById('fullscreenBtn').click();
            } else if (msgType === 'download') {
                // Trigger the download flow (which posts back to parent for actual download)
                document.getElementById('downloadBtn').click();
            }
        });

        // Initialize PDF and PageFlip
        function initPDF() {
            const flipbook = document.getElementById('flipbook');
            document.getElementById('prevBtn').style.display = 'flex';
            document.getElementById('nextBtn').style.display = 'flex';
            initProgressBar();

            // Start loading PDF (fast-first-page)
            const loadingTask = pdfjsLib.getDocument({
                url: pdfUrl,
                disableAutoFetch: true,
                disableStream: false,
                disableRange: false,
                cMapUrl: CMAP_URL,
                cMapPacked: true,
                standardFontDataUrl: STANDARD_FONT_DATA_URL,
                withCredentials: false
            });

            loadingTask.onProgress = function (progress) {
                const loader = document.getElementById('globalLoading');
                if (!loader) return;
                if (progress.total > 0) {
                    const percent = Math.round((progress.loaded / progress.total) * 100);
                    const textEl = loader.querySelector('.text');
                    if (textEl) textEl.textContent = `Loading PDF: ${percent}%`;
                }
            };

            loadingTask.promise.then(async (doc) => {
                pdfDoc = doc;
                totalPages = pdfDoc.numPages;

                // Establish base viewport quickly from page 1 only (scale: 1)
                const firstPage = await pdfDoc.getPage(1);
                viewport = firstPage.getViewport({ scale: 1 });

                document.getElementById('pageInfo').textContent = `1 / ${totalPages}`;
                const dims = calculatePageDimensions();

                // Build DOM shells for all pages
                flipbook.innerHTML = '';
                const pageEls = [];
                if (hasBlankStart) {
                    const blank = createBlankPageShell(dims);
                    flipbook.appendChild(blank);
                }
                for (let i = 1; i <= totalPages; i++) {
                    const { page, content, canvas } = createFlipPageShell(i, dims);
                    flipbook.appendChild(page);
                    pageEls.push(page);

                    // Render first pages at high quality for readability; others low then upgrade
                    setTimeout(async () => {
                        if (i <= 2) {
                            const dataHigh = await renderPage(i, 'high');
                            if (dataHigh) {
                                drawInto(canvas, dataHigh.highCanvas);
                                if (dataHigh.links && dataHigh.links.length > 0) {
                                    addUrlOverlays(content, dataHigh.links, dataHigh.baseViewport, dims);
                                }
                            }
                        } else {
                            const dataLow = await renderPage(i, 'low');
                            if (dataLow) {
                                drawInto(canvas, dataLow.lowCanvas);
                                if (dataLow.links && dataLow.links.length > 0) {
                                    addUrlOverlays(content, dataLow.links, dataLow.baseViewport, dims);
                                }
                                // Upgrade to high in background
                                upgradePageCanvasToHigh(i, dims).catch(() => {});
                            }
                        }
                    }, i * 30);
                }

                // Init PageFlip (cover + soft pages, first page soft)
                pageFlip = new St.PageFlip(flipbook, {
                    width: Math.max(320, dims.width),
                    height: Math.max(400, dims.height),
                    size: (window.innerWidth <= 768 || document.getElementById('flipbook-container').clientWidth <= 768) ? 'fixed' : 'stretch',       // force single-page on mobile; stretch on larger screens
                    minWidth: 300,
                    maxWidth: 4000,
                    minHeight: 400,
                    maxHeight: 6000,
                    showCover: false,      // treat all pages the same; no special cover
                    usePortrait: true,
                    autoSize: true,
                    drawShadow: true,
                    flippingTime: 700,
                    maxShadowOpacity: 0.5,
                    mobileScrollSupport: true
                });

                pageFlip.loadFromHTML(document.querySelectorAll('#flipbook .page'));
                if (hasBlankStart) pageFlip.turnToPage(1);

                // Events
                pageFlip.on('flip', (e) => {
                    const idx = (e.data || 0);
                    currentPage = hasBlankStart ? Math.max(1, idx) : idx + 1;
                    updateControls();
                    if (window.parent !== window) {
                        window.parent.postMessage({
                            type: 'pageChange',
                            currentPage: currentPage,
                            totalPages: totalPages
                        }, '*');
                    }
                    // Ensure current spread renders in high resolution immediately
                    const dims = calculatePageDimensions();
                    const leftPage = currentPage % 2 === 0 ? currentPage : Math.max(1, currentPage - 1);
                    const rightPage = Math.min(totalPages, leftPage + 1);
                    upgradePageCanvasToHigh(leftPage, dims);
                    if (rightPage !== leftPage) upgradePageCanvasToHigh(rightPage, dims);
                });

                // Set initial state
                currentPage = 1;
                updateControls();

                // Remove loading overlay
                const loader = document.getElementById('globalLoading');
                if (loader) loader.style.display = 'none';
                document.body.classList.remove('loading');

                // Preload additional pages (render low if missing)
                preloadPages(2, 8);

                if (window.parent !== window) {
                    window.parent.postMessage({
                        type: 'flipbookReady',
                        totalPages: totalPages
                    }, '*');
                }
            }).catch(error => {
                console.error('Error loading PDF:', error);
                document.getElementById('globalLoading').innerHTML = `
                    <div style="color: white; text-align: center; padding: 20px;">
                        <h3>Error loading PDF</h3>
                        <p>${error.message || 'Please try refreshing the page'}</p>
                    </div>
                `;
            });
        }

        // Pre-load pages in the background (low-quality only to avoid blocking)
        function preloadPages(startPage, count = 4) {
            const pagesToLoad = [];
            for (let i = startPage; i <= Math.min(startPage + count - 1, totalPages); i++) {
                if (!pagesCache[i] || !pagesCache[i].lowCanvas) {
                    pagesToLoad.push(i);
                }
            }
            pagesToLoad.forEach(pageNum => {
                setTimeout(() => {
                    renderPage(pageNum, 'low').catch(() => {});
                }, (pageNum - startPage) * 100);
            });
        }

        // Handle window resize (PageFlip autoresizes; call update to recalc)
        let resizeTimeout;
        window.addEventListener('resize', () => {
            clearTimeout(resizeTimeout);
            resizeTimeout = setTimeout(() => {
                if (pageFlip) {
                    pageFlip.update();
                    rebuildAllPagesForQuality();
                }
            }, 150);
        });

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            if (!pageFlip) return;
            if (e.key === 'ArrowLeft') {
                if (hasBlankStart && currentPage <= 1) return; // prevent flipping to leading blank
                pageFlip.flipPrev();
            } else if (e.key === 'ArrowRight') {
                pageFlip.flipNext();
            } else if (e.key === 'f' || e.key === 'F') {
                document.getElementById('fullscreenBtn').click();
            }
        });

        // Initialize immediately when script loads
        initPDF();
    </script>
</body>
</html>
"""

script_html = """
            <script>
            (function () {
                var iframeEl = document.getElementById('my-flipbook-container');
                function triggerDownload(url, filename) {
                try {
                    var safeName = filename || (url ? url.split('/').pop() : 'document.pdf') || 'document.pdf';
                    var proxiedUrl = window.location.origin + "/download_proxy?pdf=" + encodeURIComponent(url) + "&filename=" + encodeURIComponent(safeName);
                    var a = document.createElement('a');
                    a.href = proxiedUrl;
                    a.download = safeName;
                    a.style.display = 'none';
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                } catch (err) {
                    console.error('Parent download error:', err);
                }
                }
                window.addEventListener('message', function (event) {
                try {
                    if (!iframeEl || event.source !== iframeEl.contentWindow) return;
                    var data = event.data || {};
                    var type = data.type || data.action;
                    if (type === 'download' || type === 'downloadResponse') {
                    triggerDownload(data.pdfUrl, data.filename);
                    }
                } catch (e) {
                    console.error('Parent message handler error:', e);
                }
                });
            })();
            </script>
"""


def get_iframe(
        pdf_url: str = "https://iwyjssxhrcucnrkzkvmt.supabase.co/storage/v1/object/public/magazine-pdfs/CXO%20TechBOT%20October%202024-1-25.pdf",
        raw_html: bool = False
) -> str:
    pdf_injection = f"""
    <script>
        // Injected PDF URL for srcdoc usage
        const INJECTED_PDF_URL = '{pdf_url}';
    </script>
    """
    # Insert the PDF injection right before the main script tag
    raw_html = MAGAZINE_IFRAME_CONTENT.replace('<script>', pdf_injection + '<script>', 1)

    if raw_html:
        return raw_html
    
    # Properly escape HTML for srcdoc attribute (escape single quotes and HTML entities)
    escaped_html = raw_html.replace('&', '&amp;').replace("'", '&#39;').replace('"', '&quot;')

    iframe = f"""<iframe
                id="my-flipbook-container"
                class="w-full h-[36rem] max-w-[52rem]"
                allow="clipboard-write"
                sandbox="allow-scripts allow-same-origin allow-forms allow-popups allow-downloads"
                allowfullscreen="true"
                style="border:none;overflow:hidden;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,0.15);border:1px solid #e5e7eb;background-color:#000;min-height:500px;"
                srcdoc='{escaped_html}'
              ></iframe>"""
    
    return iframe + "\n\n" + script_html


def get_magazine_hero_section(
        pdf_url: str = "https://iwyjssxhrcucnrkzkvmt.supabase.co/storage/v1/object/public/magazine-pdfs/CXO%20TechBOT%20October%202024-1-25.pdf"
) -> str:
    
    before_html = """
      <!-- Magazine Flipbook Section with Side Ads -->
      <section class="w-full mx-auto px-2 sm:px-4 py-8">
        <div class="grid grid-cols-1 lg:grid-cols-5 gap-4 lg:gap-8">

          <!-- Left Ad Section -->
          <aside class="ad-column col-span-1 hidden lg:flex flex-col items-center pt-[40px]">
            <div class="w-full h-[600px] bg-gray-100 rounded-lg shadow-lg overflow-hidden sticky top-[40px]">
              <img
                src="https://picsum.photos/1200/236"
                alt="Advertisement Left"
                class="w-full h-full object-cover"
              />
            </div>
          </aside>

          
          <!-- Middle Flipbook Section -->
          <div class="col-span-1 lg:col-span-3 mt-[16]">
            <div class="w-full max-w-[52rem] mx-auto flex items-center justify-center min-h-[28rem] mt-[3rem]">
    """

    after_html = """
            </div>
          </div>
          <!-- End of Middle Flipbook Section -->

          <!-- Right Ad Section -->
          <aside class="ad-column col-span-1 hidden lg:flex flex-col items-center pt-[40px]">
            <div class="w-full h-[600px] bg-gray-100 rounded-lg shadow-lg overflow-hidden sticky top-[40px]">
              <img
                src="https://picsum.photos/1200/236"
                alt="Advertisement Right"
                class="w-full h-full object-cover"
              />
            </div>
          </aside>

        </div>
      </section>
    """
    return before_html + get_iframe(pdf_url) + after_html
