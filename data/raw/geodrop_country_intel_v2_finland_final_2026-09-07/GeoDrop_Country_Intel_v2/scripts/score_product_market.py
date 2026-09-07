#!/usr/bin/env python3
"""Tiny deterministic score helper. Hard gates are evaluated separately."""
import json, sys
weights={'demand':20,'merchant_gap':20,'economics':25,'supply':15,'localization_edge':10,'structural_demand':10}
x=json.load(open(sys.argv[1]))
# Input component values are 0..1. Output 0..100.
score=sum(max(0,min(1,float(x.get(k,0))))*w for k,w in weights.items())
print(json.dumps({'score':round(score,2),'components':{k:x.get(k,0) for k in weights}},indent=2))
