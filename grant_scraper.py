import requests

def search_grants(query, api_key):
    url = f"https://serpapi.com/search.json?q={query}&engine=google&api_key={api_key}"
    response = requests.get(url)
    results = response.json()
    
    grants = []
    for item in results.get("organic_results", []):
        link = item.get("link")
        title = item.get("title")
        if link and ("grant" in title.lower() or "funding" in title.lower()):
            grants.append({"url": link, "title": title})
    return grants