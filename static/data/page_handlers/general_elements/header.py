from ...db_handler import get_blogs_list_db
from concurrent.futures import ThreadPoolExecutor

HEADER_TEMPLATE = """<header class="w-full bg-black relative">
        <!-- Desktop Header -->
        <div class="hidden lg:flex flex-row justify-center items-center px-20 py-[10px] gap-[70px] h-[113px]">
            <a href="/"><img src="/static/images/header_logo.png" alt="Brands Out Loud Logo" class="w-20 h-20 flex-shrink-0"></a>
            <nav class="flex flex-col items-stretch w-[700px] h-[93px] py-[14px] px-[18px] gap-[10px] relative">
                <div class="flex flex-row justify-end items-center w-full gap-[60px] px-[30px]">
                    <a href="/magazine" class="text-white font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Magazine </a>
                    <a href="#" class="text-white font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">Newsletters </a>
                    <a href="/register" class="text-white font-bold text-[10px] text-center flex-shrink-0">Register</a>
                    <a href="/login" class="bg-[#CDA7FF] rounded-[2px] px-2.5 py-0.5 text-[#0D0D0D] font-bold text-[10px] text-center flex-shrink-0">Login</a>
                </div>
                <div class="w-full h-[1px] bg-gradient-to-r from-black to-[#9747FF]"></div>
                <div class="flex flex-row justify-end items-center w-full gap-[60px] px-2">
                    [[desktop_nav_links]]
                </div>
            </nav>
        </div>

        <!-- Mobile Header -->
        <div class="flex lg:hidden items-center h-[68px] w-full bg-[#0D0D0D]">
            <button id="mobile-menu-button" aria-label="Toggle Menu" class="h-full px-4 flex flex-col justify-center items-center space-y-[5px] bg-transparent focus:outline-none transition-colors duration-200 ease-in-out">
                <span class="hamburger-line block w-6 h-[2px] bg-white rounded-full"></span>
                <span class="hamburger-line block w-6 h-[2px] bg-white rounded-full"></span>
                <span class="hamburger-line block w-6 h-[2px] bg-white rounded-full"></span>
            </button>
            <div class="h-full flex items-center px-3 flex-shrink-0"> <a href="/"><img src="/static/icon/website_icon.png" alt="Brands Out Loud Logo" class="h-10 w-auto"></a> </div>
            <div class="flex-grow px-3">
                <div class="relative">
                    <input type="text" placeholder="Search..." class="search-input w-full bg-[#1e1e1e] text-white text-sm rounded-full pl-10 pr-4 py-2.5 border border-[#2a2a2a] focus:outline-none focus:border-[#9747FF] transition-all">
                    <div class="absolute inset-y-0 left-0 flex items-center pl-3.5 pointer-events-none"> <i class="ph ph-magnifying-glass text-gray-400 text-lg"></i> </div>
                </div>
            </div>
        </div>

        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden lg:hidden absolute top-[68px] left-0 w-full bg-[#121212] z-50 shadow-lg border-t border-[#2a2a2a] overflow-y-auto max-h-[calc(100vh-68px)]">
            <div class="pb-4">
                <div id="mobile-user-auth-section" class="px-4 py-3">
                    <!-- This will be replaced by JS -->
                    <a href="/login" class="login-btn block w-full text-center bg-gradient-to-r from-[#9747FF] to-[#CDA7FF] rounded-full px-4 py-2.5 text-white font-medium text-sm shadow-lg hover:-translate-y-0.5 transition-all duration-300 relative overflow-hidden">
                        <span class="relative z-10 flex items-center justify-center gap-2"> <i class="ph ph-sign-in text-lg"></i> <span>Login</span> </span>
                    </a>
                </div>
                <a href="/magazine" class="mobile-menu-item"><div class="flex items-center"><i class="ph ph-book-open text-white text-lg"></i><span class="item-title">Magazine</span></div></a>
                <a class="mobile-menu-item"><div class="flex items-center"><i class="ph ph-envelope-open text-white text-lg"></i><span class="item-title">Newsletters</span></div></a>
                
                [[mobile_nav_links]]

            </div>
        </div>
    </header>"""

def get_blogs_for_header(limit):
    """Helper function to fetch blog data for header dropdowns concurrently."""
    categories = ["Business", "Technology", "GCC", "Sustainability", "Semiconductor"]
    blogs_by_category = {}
    
    def fetch_category_blogs(category):
        blogs, _ = get_blogs_list_db(search_keyword=category, page=1, per_page=limit)
        return category.lower(), [
            {
                "id": blog.get("id"),
                "title": blog.get("json_data", {}).get("blogTitle"),
                "image": blog.get("json_data", {}).get("mainImageUrl"),
            }
            for blog in blogs
        ]
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(fetch_category_blogs, categories))
    
    for category, blogs in results:
        blogs_by_category[category] = blogs
    
    return blogs_by_category

def desktop_menu_header_elements(blogs_by_category):
    """Generates the HTML for the header navigation dropdowns."""
    nav_links_html = []
    
    category_map = {
        "business": "Latest Business Stories",
        "technology": "Tech Innovations",
        "gcc": "GCC Regional News",
        "sustainability": "Green Initiatives",
        "semiconductor": "Chip Industry Updates"
    }

    for category, blogs in blogs_by_category.items():
        category_title = category_map.get(category, f"Latest in {category.capitalize()}")
        
        items_html = ""
        for blog in blogs:
            items_html += f'''
            <a href="/blog/{blog.get('id')}" class="dropdown-item" data-category="{category}" data-id="{blog.get('id')}">
            <div class="dropdown-item flex items-center space-x-3 p-2 rounded-lg cursor-pointer" data-category="{category}" data-id="{blog.get('id')}">
                <img src="{blog.get('image')}" alt="{blog.get('title')}" class="w-12 h-12 object-cover rounded">
                <div class="flex-1">
                    <h4 class="text-gray-800 text-xs font-medium line-clamp-2">{blog.get('title')}</h4>
                </div>
            </div>
            </a>
            '''

        dropdown_html = f'''
        <div class="dropdown-container" data-category="{category}">
            <a href="/{category.lower()}" class="text-[#C4C3FF] font-bold text-[10px] text-center flex-shrink-0 flex items-center gap-1">{category.capitalize()}</a>
            <div class="dropdown-content">
                <h3 class="text-gray-800 font-semibold text-sm mb-3">{category_title}</h3>
                <div class="space-y-3">
                    {items_html}
                    <div class="border-t border-gray-200 pt-3 mt-3">
                        <div class="dropdown-item know-more-item flex items-center justify-center p-2 rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100">
                            <a href="/{category.lower()}"><span class="text-[#3533CD] text-xs font-medium mr-1">Know More</span></a>
                            <i class="ph ph-arrow-right text-[#3533CD] text-xs transition-all duration-200"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        '''
        nav_links_html.append(dropdown_html)
        
    return "\n".join(nav_links_html)

def mobile_menu_header_elements(blogs_by_category):
    """Generates the HTML for the mobile accordion menu."""
    
    icon_map = {
        "business": "ph-buildings",
        "technology": "ph-gear",
        "gcc": "ph-globe",
        "sustainability": "ph-leaf",
        "semiconductor": "ph-cpu"
    }
    accordion_html = ""
    for category, blogs in blogs_by_category.items():
        icon_class = icon_map.get(category, "ph-article")
        blog_items_html = ""
        for blog in blogs:
            blog_items_html += f'''
            <a href="/blog/{blog.get('id')}" class="sub-menu-item" data-category="{category}" data-id="{blog.get('id')}">
                <img src="{blog.get('image')}" alt="{blog.get('title')}" class="w-10 h-10 object-cover rounded-md flex-shrink-0">
                <div class="flex-1 ml-3"><h4 class="text-white text-xs font-medium line-clamp-2">{blog.get('title')}</h4></div>
            </a>
            '''
        accordion_html += f'''
        <div>
            <a href="#" class="accordion-toggle mobile-menu-item" aria-expanded="false">
                <div class="flex items-center">
                    <i class="ph {icon_class} text-white text-lg"></i>
                    <span class="item-title">{category.capitalize()}</span>
                </div>
                <i class="ph ph-caret-down accordion-icon text-lg text-gray-400" style="margin-left: auto;"></i>
            </a>
            <div class="accordion-content">
                <div class="p-3 space-y-2">
                    {blog_items_html}
                    <div class="pt-2 mt-2 border-t border-gray-700/50">
                        <a href="/{category.lower()}" class="sub-menu-item know-more-item-mobile justify-center bg-gray-700/50 hover:bg-gray-600/50">
                            <span class="text-bol-purple-light text-xs font-medium mr-1">Know More</span>
                            <i class="ph ph-arrow-right text-bol-purple-light text-xs"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        '''
    return accordion_html

def get_header():
    """Generates the complete header HTML with desktop and mobile navigation."""
    blogs_by_category = get_blogs_for_header(limit=3)
    
    desktop_nav_links = desktop_menu_header_elements(blogs_by_category)
    mobile_nav_links = mobile_menu_header_elements(blogs_by_category)
    
    header_html = HEADER_TEMPLATE.replace("[[desktop_nav_links]]", desktop_nav_links).replace("[[mobile_nav_links]]", mobile_nav_links)

    auto_collapse_script = '''
<script>
    document.addEventListener('DOMContentLoaded', function () {
        const mobileMenu = document.getElementById('mobile-menu');
        const mobileMenuButton = document.getElementById('mobile-menu-button');

        if (mobileMenu && mobileMenuButton) {
            window.addEventListener('scroll', function () {
                if (!mobileMenu.classList.contains('hidden')) {
                    const menuRect = mobileMenu.getBoundingClientRect();
                    if (menuRect.bottom < 0) {
                        mobileMenu.classList.add('hidden');
                        mobileMenuButton.classList.remove('hamburger-active');
                    }
                }
            });
        }
    });
</script>
'''
    return header_html + auto_collapse_script