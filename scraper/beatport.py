from playwright.sync_api import sync_playwright
from config import TOP100_URL


class BeatportScraper:

    def __init__(self):
        self.url = TOP100_URL

    def get_tracks(self):

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            page = browser.new_page()

            page.goto(
                self.url,
                wait_until="networkidle"
            )

            page.wait_for_timeout(5000)

            # Save a nicely formatted HTML file
            html = page.evaluate("""
                () => document.documentElement.outerHTML
            """)

            with open("beatport_live.html", "w", encoding="utf-8") as f:
                f.write(html)

            print("Saved beatport_live.html")

            browser.close()

        return []