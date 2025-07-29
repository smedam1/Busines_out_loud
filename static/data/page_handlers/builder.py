from .general_elements import *
from .homepage_elements import *
from .category_page_elements import *
from .magazine_elements import *
from .blog_page import *
from ..db_handler import get_blog

from ..db_handler import get_page_data
import asyncio
import time

def get_homepage(page_data):
    async def get_homepage_async():
        start_time = time.time()
        if page_data:
            homepage_data = page_data
        else:
            data = get_page_data("homepage")
            homepage_data = data.get("page_data", {})

        loop = asyncio.get_event_loop()
        
        # Execute all functions in parallel using thread pool
        tasks = [
            loop.run_in_executor(None, get_header),
            loop.run_in_executor(None, get_homepage_hero_section_html, homepage_data["hero_section"]),
            loop.run_in_executor(None, get_1_by_3_html, homepage_data["1_by_3_section"]),
            loop.run_in_executor(None, get_top_stories, homepage_data["top_stories_section"]),
            loop.run_in_executor(None, get_horizontal_ad_banner, homepage_data["horizontal_ad_banner"]),
            loop.run_in_executor(None, get_1_by_3_html, homepage_data["1_by_3_section_2"]),
            loop.run_in_executor(None, get_split_section, homepage_data["split_section"]),
            loop.run_in_executor(None, get_fuel_your_ambitions_html),
            loop.run_in_executor(None, get_1_by_2_by_6_html, homepage_data["one_by_two_by_six_section"]),
            # loop.run_in_executor(None, get_1_by_2_by_6_html, homepage_data["one_by_two_by_six_section_2"]),
            loop.run_in_executor(None, get_ninety_percent_of_business_owners_html),
            loop.run_in_executor(None, get_footer)
        ]
        
        # Execute all tasks in parallel
        results = await asyncio.gather(*tasks)
        
        # Insert moving_banner at index 3 (after 1_by_3_section)
        total_body = results[:3] + [moving_banner] + results[3:]
        
        total_body = "\n".join(total_body)
        end_time = time.time()
        print(f"Homepage generated in {end_time - start_time:.2f} seconds")
        return EMPTY_HOMEPAGE_TEMPLATE.replace("[[total_body]]", total_body)
    return asyncio.run(get_homepage_async())


def get_category_page(category, page_data):
    async def get_category_page_async():
        start_time = time.time()
        try:
            if page_data:
                category_data = page_data
            else:
                data = get_page_data(category)
                category_data = data.get("page_data", {})

            loop = asyncio.get_event_loop()
            
            # Execute all functions in parallel using thread pool
            tasks = [
                loop.run_in_executor(None, get_header),
                loop.run_in_executor(None, get_category_header_html, category),
                loop.run_in_executor(None, get_1_by_3_html, category_data["1_by_3_section"]),
                loop.run_in_executor(None, get_horizontal_ad_banner, category_data["horizontal_ad_banner_1"]),
                loop.run_in_executor(None, get_editor_picks, category_data["editor_picks"]),
                loop.run_in_executor(None, get_top_stories_category, category_data["top_stories_section"]),
                loop.run_in_executor(None, get_1_by_2_by_6_html, category_data["one_by_two_by_six_section"]),
                loop.run_in_executor(None, get_horizontal_ad_banner, category_data["horizontal_ad_banner_2"]),
                loop.run_in_executor(None, get_fuel_your_ambitions_html),
                loop.run_in_executor(None, get_footer)
            ]
            
            # Execute all tasks in parallel
            results = await asyncio.gather(*tasks)
            
            total_body = "\n".join(results)
            end_time = time.time()
            print(f"Category page '{category}' generated in {end_time - start_time:.2f} seconds")
            return CATEGORY_PAGE_TEMPLATE.replace("[[total_body]]", total_body).replace("[[title]]", category.capitalize())

        except Exception as e:
            print(f"Error fetching data for category '{category}': {e}")
            return "error"
    
    return asyncio.run(get_category_page_async())

def get_blog_page(blog_id):
    async def get_blog_page_async():
        start_time = time.time()
        try:
            data = get_blog(blog_id)
            if not data:
                print(f"Blog with ID '{blog_id}' not found.")
                return {
                    "status": "not_found"
                }
            # Check if blog is deleted and handle redirect
            if data.get("status") == "deleted":
                redirect_url = blog_data.get("redirect_url")
                if redirect_url:
                    return {
                        "status": "redirect",
                        "redirect_url": redirect_url
                    }
                else:
                    return {
                        "status": "error"
                    }
        

            blog_data = data.get("json_data", {})

            loop = asyncio.get_event_loop()
            
            # Execute all functions in parallel using thread pool
            tasks = [
                loop.run_in_executor(None, get_header),
                loop.run_in_executor(None, get_blog_body, blog_data),
                loop.run_in_executor(None, get_more_blogs_section, blog_data),
                loop.run_in_executor(None, get_faq_section),
                loop.run_in_executor(None, get_footer)
            ]
            
            # Execute all tasks in parallel
            results = await asyncio.gather(*tasks)
            
            total_body = "\n".join(results)
            end_time = time.time()
            print(f"Blog page '{blog_id}' generated in {end_time - start_time:.2f} seconds")
            return {
                "status": "success",
                "html": EMPTY_BLOG_TEMPLATE.replace("[[total_body]]", total_body)
            }

        except Exception as e:
            print(f"Error fetching data for blog '{blog_id}': {e}")
            return {
                "status": "error"
            }
    
    return asyncio.run(get_blog_page_async())


def get_blog_preview(blog_data):
    async def get_blog_page_async():
        try:
            start_time = time.time()
            loop = asyncio.get_event_loop()
            
            # Execute all functions in parallel using thread pool
            tasks = [
                loop.run_in_executor(None, get_header),
                loop.run_in_executor(None, get_blog_body, blog_data),
                loop.run_in_executor(None, get_more_blogs_section, blog_data),
                loop.run_in_executor(None, get_faq_section),
                loop.run_in_executor(None, get_footer)
            ]
            
            # Execute all tasks in parallel
            results = await asyncio.gather(*tasks)
            
            total_body = "\n".join(results)
            end_time = time.time()
            return {
                "status": "success",
                "html": EMPTY_BLOG_TEMPLATE.replace("[[total_body]]", total_body)
            }

        except Exception as e:
            return {
                "status": "error"
            }
    
    return asyncio.run(get_blog_page_async())

def get_magazine_home_page():
    data = get_page_data("magazine_homepage")
    page_data = data.get("page_data", {})
    print(f"Page data for magazine homepage: {page_data}")
    async def get_magazine_home_page_async():
        start_time = time.time()
        loop = asyncio.get_event_loop()
        
        # Execute all functions in parallel using thread pool
        tasks = [
            loop.run_in_executor(None, get_header),
            loop.run_in_executor(None, get_magazine_homepage_hero_section, page_data['hero_section']),
            # loop.run_in_executor(None, get_magazine_top_stories_section),
            # loop.run_in_executor(None, get_magazine_featured_section),
            loop.run_in_executor(None, get_more_magazines, page_data),
            loop.run_in_executor(None, get_horizontal_ad_banner, page_data["horizontal_ad_banner_2"]),
            loop.run_in_executor(None, get_fuel_your_ambitions_html),
            loop.run_in_executor(None, get_footer)
        ]
        
        # Execute all tasks in parallel
        results = await asyncio.gather(*tasks)
        
        total_body = "\n".join(results)
        end_time = time.time()
        print(f"Magazine homepage generated in {end_time - start_time:.2f} seconds")
        return EMPTY_HOMEPAGE_TEMPLATE.replace("[[total_body]]", total_body)
    
    return asyncio.run(get_magazine_home_page_async())



def get_magazine_page():
    data = get_page_data("magazine_homepage")
    page_data = data.get("page_data", {})
    print(f"Page data for magazine homepage: {page_data}")
    async def get_magazine_page_async():
        start_time = time.time()
        loop = asyncio.get_event_loop()
        
        # Execute all functions in parallel using thread pool
        tasks = [
            loop.run_in_executor(None, get_header),
            loop.run_in_executor(None, get_magazine_hero_section, page_data['hero_section']),
            # loop.run_in_executor(None, get_magazine_top_stories_section),
            # loop.run_in_executor(None, get_magazine_featured_section),
            loop.run_in_executor(None, get_more_magazines, page_data),
            loop.run_in_executor(None, get_horizontal_ad_banner, page_data["horizontal_ad_banner_2"]),
            loop.run_in_executor(None, get_fuel_your_ambitions_html),
            loop.run_in_executor(None, get_footer)
        ]
        
        # Execute all tasks in parallel
        results = await asyncio.gather(*tasks)
        
        total_body = "\n".join(results)
        end_time = time.time()
        print(f"Magazine homepage generated in {end_time - start_time:.2f} seconds")
        return EMPTY_MAGAZINE_TEMPLATE.replace("[[placeholder]]", total_body)
    
    return asyncio.run(get_magazine_page_async())