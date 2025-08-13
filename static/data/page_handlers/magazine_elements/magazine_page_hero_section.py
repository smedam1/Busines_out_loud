def get_magazine_hero_section(data: dict) -> str:
    flipbook_path = "D:\\Programming\\Projects\\suhas_medam\\Brands_out_loud\\Brands_out_loud\\templates\\magazine_page\\magazine_page_flipbook.html"
    try:
        with open(flipbook_path, "r", encoding="utf-8") as f:
            raw_html = f.read()
    except Exception as e:
        print(f"Error loading flipbook file: {e}")
        raw_html = "<!doctype html><html><body><p style='color:red'>Failed to load flipbook content.</p></body></html>"

    # Properly escape HTML for srcdoc attribute (escape single quotes and HTML entities)
    escaped_html = raw_html.replace('&', '&amp;').replace("'", '&#39;').replace('"', '&quot;')

    iframe = f"""<iframe
                id="my-flipbook-container"
                class="w-full h-[32rem] max-w-[52rem]"
                allow="clipboard-write"
                sandbox="allow-scripts allow-same-origin allow-forms allow-popups"
                allowfullscreen="true"
                style="border:none;overflow:hidden;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,0.15);border:1px solid #e5e7eb;background-color:#000;"
                srcdoc='{escaped_html}'
              ></iframe>"""
    return f"""
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
            <div class="w-full max-w-[52rem] mx-auto flex items-center justify-center min-h-[28rem]">
              {iframe}
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

      <!-- Parent-side JavaScript for handling iframe messages -->
      <script>
        // Create flipbook control object
        window.flipbookControl = {{
          _triggerDownload: function(pdfUrl, filename) {{
            console.log('Triggering download:', filename, pdfUrl);
            try {{
              const link = document.createElement('a');
              link.href = pdfUrl;
              link.download = filename || 'magazine.pdf';
              link.target = '_blank';
              document.body.appendChild(link);
              link.click();
              document.body.removeChild(link);
              console.log('Download initiated successfully');
            }} catch (error) {{
              console.error('Download failed:', error);
              // Fallback: open in new tab
              window.open(pdfUrl, '_blank');
            }}
          }}
        }};

        // Create iframe fullscreen manager
        window.iframeFullscreenManager = {{
          isFullscreen: false,
          
          enterFullscreen: function() {{
            console.log('Entering fullscreen for iframe');
            const iframe = document.getElementById('my-flipbook-container');
            if (!iframe) {{
              console.error('Iframe not found');
              return;
            }}
            
            try {{
              if (iframe.requestFullscreen) {{
                iframe.requestFullscreen().then(() => {{
                  this.isFullscreen = true;
                  console.log('Fullscreen entered successfully');
                  
                  // Wait for fullscreen transition to complete before notifying iframe
                  setTimeout(() => {{
                    iframe.contentWindow.postMessage({{
                      action: 'fullscreenEntered'
                    }}, '*');
                  }}, 100);
                }}).catch((err) => {{
                  console.error('Failed to enter fullscreen:', err);
                }});
              }} else if (iframe.webkitRequestFullscreen) {{
                iframe.webkitRequestFullscreen();
                this.isFullscreen = true;
                setTimeout(() => {{
                  iframe.contentWindow.postMessage({{
                    action: 'fullscreenEntered'
                  }}, '*');
                }}, 100);
              }} else if (iframe.mozRequestFullScreen) {{
                iframe.mozRequestFullScreen();
                this.isFullscreen = true;
                setTimeout(() => {{
                  iframe.contentWindow.postMessage({{
                    action: 'fullscreenEntered'
                  }}, '*');
                }}, 100);
              }} else if (iframe.msRequestFullscreen) {{
                iframe.msRequestFullscreen();
                this.isFullscreen = true;
                setTimeout(() => {{
                  iframe.contentWindow.postMessage({{
                    action: 'fullscreenEntered'
                  }}, '*');
                }}, 100);
              }} else {{
                console.warn('Fullscreen API not supported');
              }}
            }} catch (error) {{
              console.error('Error entering fullscreen:', error);
            }}
          }},
          
          exitFullscreen: function() {{
            console.log('Exiting fullscreen for iframe');
            const iframe = document.getElementById('my-flipbook-container');
            
            try {{
              if (document.exitFullscreen) {{
                document.exitFullscreen().then(() => {{
                  this.isFullscreen = false;
                  console.log('Fullscreen exited successfully');
                  
                  // Wait for exit transition to complete before notifying iframe
                  setTimeout(() => {{
                    if (iframe) {{
                      iframe.contentWindow.postMessage({{
                        action: 'fullscreenExited'
                      }}, '*');
                    }}
                  }}, 100);
                }}).catch((err) => {{
                  console.error('Failed to exit fullscreen:', err);
                }});
              }} else if (document.webkitExitFullscreen) {{
                document.webkitExitFullscreen();
                this.isFullscreen = false;
                setTimeout(() => {{
                  if (iframe) {{
                    iframe.contentWindow.postMessage({{
                      action: 'fullscreenExited'
                    }}, '*');
                  }}
                }}, 100);
              }} else if (document.mozCancelFullScreen) {{
                document.mozCancelFullScreen();
                this.isFullscreen = false;
                setTimeout(() => {{
                  if (iframe) {{
                    iframe.contentWindow.postMessage({{
                      action: 'fullscreenExited'
                    }}, '*');
                  }}
                }}, 100);
              }} else if (document.msExitFullscreen) {{
                document.msExitFullscreen();
                this.isFullscreen = false;
                setTimeout(() => {{
                  if (iframe) {{
                    iframe.contentWindow.postMessage({{
                      action: 'fullscreenExited'
                    }}, '*');
                  }}
                }}, 100);
              }}
            }} catch (error) {{
              console.error('Error exiting fullscreen:', error);
            }}
          }}
        }};

        // Listen for fullscreen change events
        document.addEventListener('fullscreenchange', function() {{
          const iframe = document.getElementById('my-flipbook-container');
          if (iframe) {{
            const isFullscreen = !!document.fullscreenElement;
            window.iframeFullscreenManager.isFullscreen = isFullscreen;
            
            iframe.contentWindow.postMessage({{
              action: isFullscreen ? 'fullscreenEntered' : 'fullscreenExited'
            }}, '*');
          }}
        }});

        // Listen for messages from iframe
        window.addEventListener('message', function(event) {{
          if (!event.data || !event.data.action) return;
          
          console.log('Parent received message from iframe:', event.data);
          
          // Handle download requests
          if (event.data.action === 'downloadResponse') {{
            console.log('Handling download request');
            window.flipbookControl._triggerDownload(event.data.pdfUrl, event.data.filename);
          }}
          
          // Handle fullscreen requests
          else if (event.data.action === 'requestFullscreen') {{
            console.log('Handling fullscreen request');
            window.iframeFullscreenManager.enterFullscreen();
          }}
          
          // Handle exit fullscreen requests
          else if (event.data.action === 'exitFullscreen') {{
            console.log('Handling exit fullscreen request');
            window.iframeFullscreenManager.exitFullscreen();
          }}
        }});

        console.log('Magazine iframe message handlers initialized');
      </script>
    """
