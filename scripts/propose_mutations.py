#!/usr/bin/env python3
"""
CGE Proposer Adapter — Proposes mutations for blocked campaigns
"""

import json

def propose_mutations(campaign, evidence, gates, score):
    """Propose mutations for a blocked campaign."""
    mutations = []
    
    # Find UNKNOWN gates
    unknown_gates = {k: v for k, v in gates.items() if v == "UNKNOWN"}
    
    for gate, value in unknown_gates.items():
        if gate == "G4":
            mutations.append({
                "mutation_type": "RESEARCH_ACTION",
                "target_gate": "G4",
                "action": "BUYER_ROLE_TEST",
                "description": "Test whether consumer or installer selects the part",
                "expected_information_value": "HIGH",
                "expected_cash_cost": "LOW",
                "expected_human_minutes": 30
            })
        elif gate == "G7":
            mutations.append({
                "mutation_type": "SUPPLIER_CONTACT",
                "target_gate": "G7",
                "action": "CONTACT_SUPPLIER",
                "description": "Contact supplier to verify reseller terms",
                "expected_information_value": "HIGH",
                "expected_cash_cost": "LOW",
                "expected_human_minutes": 15
            })
        elif gate == "G8":
            mutations.append({
                "mutation_type": "PRICE_RESEARCH",
                "target_gate": "G8",
                "action": "OBTAIN_NET_PRICING",
                "description": "Obtain dealer net pricing from supplier",
                "expected_information_value": "HIGH",
                "expected_cash_cost": "LOW",
                "expected_human_minutes": 30
            })
        elif gate == "G11":
            mutations.append({
                "mutation_type": "FEED_BUILD",
                "target_gate": "G11",
                "action": "BUILD_MERCHANT_CENTER_FEED",
                "description": "Build Merchant Center feed for campaign",
                "expected_information_value": "MEDIUM",
                "expected_cash_cost": "LOW",
                "expected_human_minutes": 120
            })
    
    return mutations

def main():
    # Load evaluation results
    with open("/root/drop/data/evaluation_results.json") as f:
        results = json.load(f)
    
    print(f"Campaign: {results['campaign_id']}")
    print(f"Verdict: {results['verdict']}")
    print(f"Score: {results['score']}")
    
    # Propose mutations
    mutations = propose_mutations(
        {},  # campaign
        {},  # evidence
        results['gates'],
        results['score']
    )
    
    print(f"\nProposed mutations: {len(mutations)}")
    for m in mutations:
        print(f"  - {m['action']}: {m['description']}")
        print(f"    Target gate: {m['target_gate']}")
        print(f"    Expected value: {m['expected_information_value']}")
        print(f"    Cash cost: {m['expected_cash_cost']}")
        print(f"    Human time: {m['expected_human_minutes']} min")
    
    # Save mutations
    output_file = "/root/drop/data/proposed_mutations.json"
    with open(output_file, 'w') as f:
        json.dump(mutations, f, indent=2)
    
    print(f"\nSaved: {output_file}")

if __name__ == "__main__":
    main()
