from grant_scraper import search_grants
from relevance_scorer import score_grant
from prefill_agent import prefill_grant
import json

with open("business_profile.json") as f:
    business = json.load(f)

api_key = "YOUR_SERPAPI_KEY"
queries = [
    "small business consulting grants USA",
    "community outreach nonprofit funding site:.org",
    "financial literacy grants site:.gov"
]

# Collect grant links
all_grants = []
for q in queries:
    all_grants.extend(search_grants(q, api_key))

# Score and filter grants
for grant in all_grants:
    grant['eligible_locations'] = ["United States"]
    grant['eligible_industries'] = business['coreConsultingAreas']
    grant['focus_area'] = business['communityImpact']
    grant['business_stage'] = business['businessStage']
    
    score = score_grant(grant, business)
    if score > 70:
        questions = [
            "Why did you start your business?",
            "How do you help your customers?",
            "How would you use this grant?"
        ]
        prefill_grant(grant['url'], questions)