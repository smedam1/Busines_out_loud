from ...db_handler import get_recent_magazines_db
from ..general_elements import get_horizontal_ad_banner
def get_more_magazines(data: dict) -> str:
    magazine_details = get_recent_magazines_db()
    if magazine_details == []:
        return None

    # Generate individual magazine cards
    magazine_cards = []
    for magazine in magazine_details:
        single_magazine_template = f"""<div class="flex flex-col items-center p-4 gap-4 cursor-pointer hover:scale-105 transition-transform duration-300" onclick="window.open('/magazine/{magazine['pdf_url'].replace('/', '-')}', &quot;_blank&quot;)">
                            <div class="w-full aspect-[3/4] relative overflow-hidden rounded-lg">
                                <div class="absolute inset-0 bg-gradient-to-t from-black to-transparent opacity-100"></div>
                                <img src="{magazine['thumbnail_url']}" alt="{magazine['title']}" class="w-full h-full object-cover">
                            </div>
                            <div class="font-bold text-lg md:text-xl text-center text-[#060606]">
                                {magazine['title'].upper()}
                            </div>
                        </div>"""
        magazine_cards.append(single_magazine_template)
    
    # Group magazines into rows of 3
    magazine_rows = []
    for i in range(0, len(magazine_cards), 3):
        row_magazines = magazine_cards[i:i+3]
        magazine_row_template = f"""<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
                                    {''.join(row_magazines)}
                                </div>"""
        magazine_rows.append(magazine_row_template)

    return f"""
        {get_horizontal_ad_banner(data.get("horizontal_ad_banner_1"))}

        <div class="w-full px-4">
            <img src="static/images/explore_new_ideas.png" alt="Explore New Ideas" class="w-full h-auto">
        </div>
    
        <section class="w-full py-6 px-4">
            <div class="max-w-6xl mx-auto">
                {''.join(magazine_rows)}
            </div>
        </section>"""