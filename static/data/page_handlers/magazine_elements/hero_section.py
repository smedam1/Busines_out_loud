def get_magazine_homepage_hero_section(data: dict) -> str:
    style = """<style>
                @keyframes scroll-mobile {
                    0% { transform: translateX(0); }
                    25% { transform: translateX(0); }
                    33% { transform: translateX(-280px); }
                    58% { transform: translateX(-280px); }
                    66% { transform: translateX(-560px); }
                    91% { transform: translateX(-560px); }
                    100% { transform: translateX(0); }
                }
                
                @media (max-width: 768px) {
                    .animate-scroll-mobile {
                        animation: scroll-mobile 15s infinite;
                        animation-timing-function: ease-in-out;
                    }
                }
                
                @media (min-width: 769px) {
                    .animate-scroll-mobile {
                        animation: none;
                    }
                }
            </style>"""

    return f"""<section class="w-full py-6 px-4 md:px-8">
            <div class="flex flex-col md:flex-row justify-center items-center gap-6 md:gap-10 w-full max-w-6xl mx-auto">
                
                <div class="gradient-bg flex flex-col items-center p-4 md:p-[33px] gap-4 md:gap-[27px] w-full md:w-2/5 rounded-[10px] relative">
                    
                    <div class="w-full aspect-[3/4] rounded-lg bg-cover bg-center" style="background-image: url('{data['hero_image']}')"></div>
                    
                    
                    <a href="{data.get("hero_link", "/magazine/CXO%20TechBOT%20October%202024-1-25.pdf")}" class="w-full max-w-[175px] mt-[-6rem]">
                        <img src="static/images/read_full_story_button.png" alt="Read full story" class="w-full h-auto object-contain">
                    </a>
                </div>
                
                
                <div class="w-full md:w-3/5 mt-6 md:mt-0">
                    
                    <h2 class="font-bold text-2xl md:text-[34px] leading-tight text-black mb-6 text-center md:text-left">Leadership Spotlight</h2>
                    
                    
                    <div class="overflow-hidden md:overflow-visible">
                        <div class="flex md:grid md:grid-cols-3 gap-8 md:gap-8 animate-scroll-mobile md:animate-none">
                            
                            <div class="flex-shrink-0 w-64 md:w-auto flex flex-col items-center">
                                <div class="w-full max-w-[214px] aspect-[3/4] rounded-lg overflow-hidden">
                                    <img src="https://picsum.photos/seed/profile1/214/283" alt="Suhas Medam" class="w-full h-full object-cover">
                                </div>
                                <h3 class="font-bold text-xl md:text-2xl text-[#393939] mt-3 text-center">Suhas Medam</h3>
                                <p class="font-normal text-xs md:text-sm text-[#393939] mt-2 text-center">
                                    It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.
                                </p>
                            </div>
                            
                            
                            <div class="flex-shrink-0 w-64 md:w-auto flex flex-col items-center">
                                <div class="w-full max-w-[214px] aspect-[3/4] rounded-lg overflow-hidden">
                                    <img src="https://picsum.photos/seed/profile2/214/282" alt="Harsh Kumar" class="w-full h-full object-cover">
                                </div>
                                <h3 class="font-bold text-xl md:text-2xl text-[#393939] mt-3 text-center">Harsh Kumar</h3>
                                <p class="font-normal text-xs md:text-sm text-[#393939] mt-2 text-center">
                                    It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.
                                </p>
                            </div>
                            
                            
                            <div class="flex-shrink-0 w-64 md:w-auto flex flex-col items-center">
                                <div class="w-full max-w-[214px] aspect-[3/4] rounded-lg overflow-hidden">
                                    <img src="https://picsum.photos/seed/profile3/214/282" alt="Vivek Bindra" class="w-full h-full object-cover">
                                </div>
                                <h3 class="font-bold text-xl md:text-2xl text-[#393939] mt-3 text-center">Vivek Bindra</h3>
                                <p class="font-normal text-xs md:text-sm text-[#393939] mt-2 text-center">
                                    It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            {style}
        </section>"""