import os
import random
import string
import asyncio
import aiofiles
from apify import Actor
from pyppeteer import launch

class MyActor:
    def __init__(self, actor_input):
        self.link_urls = actor_input.get('link_urls')
        self.sleep_duration = actor_input.get('Sleep')  # Default to 10 seconds if not provided
        self.waitUntil = actor_input.get('waitUntil')  # Default to 'networkidle2' if not provided     
        self.cookies = actor_input.get('cookies', [])
        self.fullPage = actor_input.get('fullPage')  # Default to True if not provided
        self.window_Width = actor_input.get('window_Width')  # Default width
        self.window_Height = actor_input.get('window_Height')  # Default height

        self.scrollToBottom = actor_input.get('scrollToBottom')  # Default to True
        # The distance to scroll down the page in pixels for each scroll action.
        self.distance = actor_input.get('distance')  # Configurable scroll distance per step

        # The delay in milliseconds to wait after each scroll action.
        self.delay = actor_input.get('delay')  # Configurable delay between scroll actions

    async def configure_browser(self):
        """Configures the Pyppeteer browser with the necessary options."""
        browser = await launch({
            'headless': True,  # Set to False if you want to see the browser
            'args': [
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-gpu',
                '--blink-settings=imagesEnabled=false',  # Disable image loading
            ]
        })
        return browser

    async def scroll_to_bottom(self, page):
        """Scrolls to the bottom of the page."""
        await page.evaluate(f"""
            async () => {{
                const distance = {self.distance};  // Scroll by a configurable distance
                const delay = {self.delay};         // Wait for a configurable delay after each scroll
                while (document.scrollingElement.scrollTop + window.innerHeight < document.scrollingElement.scrollHeight) {{
                    document.scrollingElement.scrollBy(0, distance);
                    await new Promise(resolve => setTimeout(resolve, delay));
                }}
            }}
        """)

    async def process_link(self, page, link_url):
        """Processes a single URL: open page, optionally scroll to bottom, take a screenshot, upload it."""
        try:
            # Set the cookies before navigating to the page
            await page.setCookie(*self.cookies)

            # Set the viewport size to specified width and height
            await page.setViewport({'width': self.window_Width, 'height': self.window_Height})

            # Open the page
            await page.goto(link_url, {'waitUntil': self.waitUntil})  # Wait until the page is fully loaded

            # Conditionally scroll to the bottom of the page
            if self.scrollToBottom:
                await self.scroll_to_bottom(page)

            # Wait for the page to load after scrolling
            await asyncio.sleep(self.sleep_duration)

            # Generate a random screenshot name
            screenshot_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16)) + '.png'
            screenshot_path = f'Image_Files/{screenshot_name}'

            # Take a full-page screenshot
            await page.screenshot({'path': screenshot_path, 'fullPage': self.fullPage})

            # Upload the screenshot to Apify's Key-Value Store
            async with aiofiles.open(screenshot_path, 'rb') as f:
                screenshot_content = await f.read()

            store_id = Actor.config.default_key_value_store_id
            await Actor.set_value(screenshot_name, screenshot_content)

            screenshot_url = f'https://api.apify.com/v2/key-value-stores/{store_id}/records/{screenshot_name}'
            await Actor.push_data({'screenshot_url': screenshot_url, 'linkUrl': link_url})

            print(f'Screenshot for {link_url} saved.')

        except Exception as e:
            print(f"Error processing {link_url}: {str(e)}")

    async def run(self):
        """Main execution logic."""
        os.makedirs('Image_Files', exist_ok=True)
        
        # Configure and launch the browser
        browser = await self.configure_browser()
        page = await browser.newPage()

        for link_url in self.link_urls:
            await self.process_link(page, link_url)

        await browser.close()

async def main():
    async with Actor:
        actor_input = await Actor.get_input() or {}
        my_actor = MyActor(actor_input)
        await my_actor.run()

if __name__ == "__main__":
    asyncio.run(main())
