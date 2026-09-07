"""
MythicBee Drop — Data Pipeline
Ingests case studies, sources, and creates structured intelligence
"""

import csv
import json
import os

def load_case_studies():
    """Load case studies from CSV"""
    cases = []
    with open('corpus/case-studies/case_studies.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cases.append({
                'id': row.get('case_id', ''),
                'operator': row.get('operator', ''),
                'channel': row.get('channel', ''),
                'market': row.get('market', ''),
                'revenue': float(row.get('revenue', 0) or 0),
                'ad_spend': float(row.get('ad_spend', 0) or 0),
                'roas': float(row.get('roas', 0) or 0),
                'aov': float(row.get('aov', 0) or 0),
                'days': int(row.get('days', 0) or 0),
                'notes': row.get('notes', '')
            })
    return cases

def load_sources():
    """Load sources from CSV"""
    sources = []
    with open('corpus/sources/sources.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sources.append({
                'id': row.get('source_id', ''),
                'title': row.get('title', ''),
                'type': row.get('type', ''),
                'grade': row.get('evidence_grade', ''),
                'url': row.get('url', '')
            })
    return sources

def load_strategy_rules():
    """Load strategy rules from CSV"""
    rules = []
    with open('corpus/data/strategy_rules.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rules.append({
                'id': row.get('rule_id', ''),
                'category': row.get('category', ''),
                'rule': row.get('rule', ''),
                'confidence': row.get('confidence', '')
            })
    return rules

def create_intelligence_library():
    """Create the master intelligence library"""
    cases = load_case_studies()
    sources = load_sources()
    rules = load_strategy_rules()
    
    library = {
        'meta': {
            'name': 'Drop Intelligence Library',
            'version': '1.0.0',
            'created': '2026-09-06',
            'stats': {
                'case_studies': len(cases),
                'sources': len(sources),
                'rules': len(rules)
            }
        },
        'strategies': [
            {
                'id': 'S001',
                'name': 'Google Shopping Cold Launch',
                'status': 'WORKING',
                'confidence': 'HIGH',
                'capital': '$10-20/day'
            },
            {
                'id': 'S002',
                'name': 'PMax Scaling',
                'status': 'WORKING',
                'confidence': 'MEDIUM-HIGH',
                'capital': '$50-100/day'
            },
            {
                'id': 'S003',
                'name': 'Free Listings + SEO',
                'status': 'WORKING',
                'confidence': 'HIGH',
                'capital': '$0'
            }
        ],
        'principles': [
            'Optimize contribution profit per click, not ROAS',
            'Launch one country first',
            'Start with lean catalog',
            'Treat product feed as experimental surface',
            'Observe more often than act',
            'Use $0-10/day only as probe',
            'High-ticket searched products recur in low-budget cases'
        ]
    }
    
    return library

if __name__ == '__main__':
    library = create_intelligence_library()
    print(json.dumps(library, indent=2))
