#!/usr/bin/env python3
"""
Import dropcomp competitor data into Drop campaign system
"""

import json
import os

def import_competitors():
    """Import competitor data from dropcomp."""
    with open('/root/dropcomp/data/competitors.json') as f:
        competitors = json.load(f)
    
    # Convert to our format
    drop_competitors = {}
    for niche, data in competitors.items():
        drop_competitors[niche] = {
            'niche': data.get('niche'),
            'country': data.get('country'),
            'language': data.get('language'),
            'installed_base': data.get('installed_base'),
            'competitors': data.get('competitors', [])
        }
    
    return drop_competitors

def import_campaigns():
    """Import campaign data from dropcomp."""
    with open('/root/dropcomp/data/campaigns.json') as f:
        campaigns = json.load(f)
    
    return campaigns

def main():
    print("Importing dropcomp data...")
    
    # Import competitors
    competitors = import_competitors()
    print(f"Competitors: {len(competitors)} niches")
    
    # Import campaigns
    campaigns = import_campaigns()
    print(f"Campaigns: {len(campaigns)} campaigns")
    
    # Save to drop
    os.makedirs('/root/drop/data/dropcomp', exist_ok=True)
    
    with open('/root/drop/data/dropcomp/competitors.json', 'w') as f:
        json.dump(competitors, f, indent=2)
    
    with open('/root/drop/data/dropcomp/campaigns.json', 'w') as f:
        json.dump(campaigns, f, indent=2)
    
    print(f"Saved to /root/drop/data/dropcomp/")
    
    # Print summary
    print("\nCampaigns by gap score:")
    for campaign in sorted(campaigns, key=lambda x: x.get('hard_gates', {}).get('G1_installed_base', ''), reverse=True)[:10]:
        gates = campaign.get('hard_gates', {})
        unknowns = sum(1 for v in gates.values() if v == 'UNKNOWN')
        print(f"  {campaign['campaign_id']}: {unknowns} UNKNOWNs")

if __name__ == "__main__":
    main()
