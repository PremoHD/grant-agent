from playwright.sync_api import sync_playwright
import json
from ai_answer_generator import generate_answer

with open("business_profile.json") as f:
    business = json.load(f)

def prefill_grant(grant_url, questions):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(grant_url)
        
        for q in questions:
            answer = generate_answer(q, business)
            try:
                # Replace with real field selectors
                page.fill(f"input[name='{q}']", answer)
            except:
                continue
        
        # Save draft screenshot
        page.screenshot(path="draft_submission.png")
        browser.close()