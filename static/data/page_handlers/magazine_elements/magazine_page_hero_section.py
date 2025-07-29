
def get_magazine_hero_section(data: dict) -> str:


    return f"""
      <!-- Modified Flipbook Section with Ads -->
      <div class="grid grid-cols-1 lg:grid-cols-5 w-full mx-auto px-2 sm:px-4 py-8 gap-4 lg:gap-8">

        <!-- Left Ad Section -->
        <div class="ad-column col-span-1 hidden lg:flex flex-col items-center pt-[40px]">
            <div class="w-full h-[600px] bg-gray-100 rounded-lg shadow-lg overflow-hidden sticky top-[40px]">
                <img
                  src="https://picsum.photos/1200/236"
                  alt="Advertisement Left"
                  class="w-full h-full object-cover"
                />
            </div>
        </div>
    
        <!-- Middle Flipbook Section -->
        <div class="App text-center flex-grow flex flex-col col-span-1 lg:col-span-3">
            <header
              class="App-header flex-grow flex flex-col items-center justify-center text-2xl text-white p-5 box-border" 
              style="background-color: transparent;" 
            >
              <div
                id="flipbook-wrapper"
                class="relative w-full max-w-[1000px] h-[60vh] sm:h-[600px] mx-auto book-container"
              >
                <!-- Loading overlay -->
                <div
                  id="loading-overlay"
                  class="absolute inset-0 flex flex-col justify-center items-center z-50"
                >
                </div>
                <div id="my-flipbook-container" class="w-full h-full max-w-[1000px] max-h-[600px]"></div>
              </div>
    
              <!-- Progress Bar Section -->
              <div class="progress-bar-section w-full max-w-[1000px] mx-auto mt-6 mb-4">
                <div
                  class="flex items-center justify-between mb-2 text-sm text-gray-600"
                >
                  <div></div>
                  <div class="flex items-center gap-2">
                    <button
                      id="download-btn"
                      class="download-button flex items-center gap-2 px-3 py-1 bg-gray-100 hover:bg-gray-200 border border-gray-300 rounded-md transition-colors duration-200 text-xs font-medium"
                      title="Download PDF"
                    >
                      <svg
                        class="w-4 h-4 transition-transform duration-200 hover:scale-110"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                        />
                      </svg>
                      <span>Download</span>
                    </button>
                    <button
                      id="fullscreen-btn"
                      class="fullscreen-button flex items-center gap-2 px-3 py-1 bg-gray-100 hover:bg-gray-200 border border-gray-300 rounded-md transition-colors duration-200 text-xs font-medium"
                      title="Toggle Fullscreen"
                    >
                      <svg
                        id="fullscreen-icon"
                        class="w-4 h-4 transition-transform duration-200 hover:scale-110"
                        fill="none"
                        stroke="currentColor"
                        viewBox="0 0 24 24"
                        xmlns="http://www.w3.org/2000/svg"
                      >
                        <path
                          stroke-linecap="round"
                          stroke-linejoin="round"
                          stroke-width="2"
                          d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5v-4m0 4h-4m4 0l-5-5"
                        />
                      </svg>
                      <span id="fullscreen-text">Fullscreen</span>
                    </button>
                  </div>
                </div>
                <div
                  class="progress-bar-container relative w-full h-2 bg-gray-200 rounded-full cursor-pointer"
                >
                  <div
                    id="progress-bar-fill"
                    class="absolute top-0 left-0 h-full bg-gradient-to-r from-purple-500 to-blue-500 rounded-full transition-all duration-300 ease-out"
                    style="width: 0%"
                  ></div>
                  <div
                    id="progress-bar-handle"
                    class="absolute top-1/2 transform -translate-y-1/2 w-4 h-4 bg-white border-2 border-purple-500 rounded-full shadow-lg cursor-grab transition-all duration-200 hover:scale-110"
                    style="left: 0%"
                  ></div>
                  <!-- Page Number Tooltip -->
                  <div
                    id="progress-tooltip"
                    class="absolute bottom-8 transform -translate-x-1/2 bg-gray-800 text-white text-xs px-2 py-1 rounded opacity-0 pointer-events-none transition-opacity duration-200 z-20"
                    style="left: 0%"
                  >
                    <span id="tooltip-page-info">1 of 0</span>
                    <div class="absolute top-full left-1/2 transform -translate-x-1/2 w-0 h-0 border-l-4 border-r-4 border-t-4 border-transparent border-t-gray-800"></div>
                  </div>
                </div>
              </div>
            </header>
        </div>"""