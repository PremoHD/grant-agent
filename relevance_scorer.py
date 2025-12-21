def score_grant(grant_info, business_profile):
    score = 0
    # Location match
    if business_profile['location'] in grant_info.get('eligible_locations', []):
        score += 30
    # Industry/core area match
    if any(area in grant_info.get('eligible_industries', []) for area in business_profile['coreConsultingAreas']):
        score += 40
    # Community focus match
    if any(focus in grant_info.get('focus_area', []) for focus in business_profile['communityImpact']):
        score += 20
    # Stage match
    if grant_info.get('business_stage') == business_profile['businessStage']:
        score += 10
    return score