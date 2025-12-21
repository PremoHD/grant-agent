import json

def save_grant_log(grant_info, answers):
    try:
        with open("grant_log.json", "r") as f:
            logs = json.load(f)
    except:
        logs = []
    
    logs.append({
        "url": grant_info['url'],
        "title": grant_info.get('title', ""),
        "answers": answers
    })
    
    with open("grant_log.json", "w") as f:
        json.dump(logs, f, indent=2)