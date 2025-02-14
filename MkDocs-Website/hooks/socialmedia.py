from textwrap import dedent
import urllib.parse

x_intent = "https://x.com/intent/tweet"
fb_sharer = "https://www.facebook.com/sharer.php"

def on_page_markdown(markdown, **kwargs):
    page = kwargs['page']
    config = kwargs['config']

    if page.meta.get('template') != 'blog-post.html':
        return markdown

    page_url = config.site_url + page.url
    page_title = urllib.parse.quote(page.title)

    return markdown + dedent(f"""
    <div style="text-align: center; margin-top: 20px;" markdown="1">
        <h2 style="font-weight: bold; text-decoration: underline;">Share on Socials</h2>
        <div style="display: flex; justify-content: center; gap: 10px;">
            
            <!-- X (Twitter) Share Button -->
            <a href="{x_intent}?text={page_title}&url={page_url}" target="_blank" style="text-decoration: none;">
                <button style="display: flex; align-items: center; justify-content: center; 
                               padding: 10px 15px; border: 2px solid #1877F2; background: none; 
                               color: #1877F2; font-size: 16px; border-radius: 5px; 
                               cursor: pointer; gap: 8px; min-width: 180px;">
                    <!-- Using a more reliable icon from Twitter or local assets -->
                    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/X_logo_2023_original.svg/300px-X_logo_2023_original.svg.png?20230728155658" 
                         alt="X Logo" width="20" height="20">
                    <span>Share on X</span>
                </button>
            </a>

            <!-- Facebook Share Button -->
            <a href="{fb_sharer}?u={page_url}" target="_blank" style="text-decoration: none;">
                <button style="display: flex; align-items: center; justify-content: center; 
                               padding: 10px 15px; border: 2px solid #1877F2; background: none; 
                               color: #1877F2; font-size: 16px; border-radius: 5px; 
                               cursor: pointer; gap: 8px; min-width: 180px;">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" 
                         alt="Facebook Logo" width="20" height="20">
                    <span>Share on Facebook</span>
                </button>
            </a>

        </div>
    </div>
    """)
