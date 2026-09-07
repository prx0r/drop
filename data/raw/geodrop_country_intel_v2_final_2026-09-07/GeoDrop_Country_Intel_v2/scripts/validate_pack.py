#!/usr/bin/env python3
import json,sys,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
country=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'countries/no'
if not country.is_absolute(): country=ROOT/country
req=['manifest.json','profile.json','sources.jsonl','raw_snapshot_manifest.jsonl','observations.jsonl','ecosystems.jsonl','problems.jsonl','queries.jsonl','merchants.jsonl','source_archetypes.jsonl','source_target_gaps.jsonl','trade_code_map.jsonl','product_markets.jsonl','hypotheses.jsonl','experiments.jsonl','outcomes.jsonl','backtests.jsonl','series/_manifest.json']
errors=[]; warnings=[]
for f in req:
 if not (country/f).exists(): errors.append(f'MISSING_FILE {f}')

def jl(name):
 p=country/name
 if not p.exists(): return []
 out=[]
 for i,line in enumerate(p.read_text().splitlines(),1):
  if not line.strip(): continue
  try: out.append(json.loads(line))
  except Exception as e: errors.append(f'BAD_JSON {name}:{i} {e}')
 return out
sources=jl('sources.jsonl'); obs=jl('observations.jsonl'); ecosystems=jl('ecosystems.jsonl'); problems=jl('problems.jsonl'); queries=jl('queries.jsonl'); merchants=jl('merchants.jsonl'); arch=jl('source_archetypes.jsonl'); gaps=jl('source_target_gaps.jsonl'); pms=jl('product_markets.jsonl'); hyps=jl('hypotheses.jsonl'); exps=jl('experiments.jsonl'); outs=jl('outcomes.jsonl'); backs=jl('backtests.jsonl')
def uniq(rows,key,name):
 vals=[]
 for r in rows:
  if key not in r: errors.append(f'MISSING_ID {name}.{key}'); continue
  vals.append(r[key])
 if len(vals)!=len(set(vals)): errors.append(f'DUPLICATE_ID {name}.{key}')
 return set(vals)
sids=uniq(sources,'source_id','sources'); oids=uniq(obs,'observation_id','observations'); eids=uniq(ecosystems,'ecosystem_id','ecosystems'); pids=uniq(problems,'problem_id','problems'); qids=uniq(queries,'query_id','queries'); mids=uniq(merchants,'merchant_id','merchants'); aids=uniq(arch,'archetype_id','source_archetypes'); gids=uniq(gaps,'gap_id','gaps'); pmids=uniq(pms,'product_market_id','product_markets'); hids=uniq(hyps,'hypothesis_id','hypotheses'); xids=uniq(exps,'experiment_id','experiments'); outids=uniq(outs,'outcome_id','outcomes'); bids=uniq(backs,'backtest_id','backtests')
for o in obs:
 if o.get('source_id') and o['source_id'] not in sids: errors.append(f'OBS_SOURCE_MISSING {o.get("observation_id")}->{o.get("source_id")}')
 if o.get('status') in ('OBSERVED','DERIVED') and 'value' not in o: errors.append(f'OBS_VALUE_MISSING {o.get("observation_id")}')
 if o.get('status','').startswith('MISSING') and o.get('value') not in (None,'UNKNOWN'): warnings.append(f'MISSING_STATUS_HAS_VALUE {o.get("observation_id")}')
 if not (0 <= float(o.get('confidence',0)) <= 1): errors.append(f'BAD_CONFIDENCE {o.get("observation_id")}')
 if o.get('point_in_time_safe') and not o.get('available_at'): errors.append(f'PIT_SAFE_WITHOUT_AVAILABLE_AT {o.get("observation_id")}')
for e in ecosystems:
 for pr in e.get('problem_refs',[]):
  if pr not in pids: errors.append(f'ECOSYSTEM_PROBLEM_MISSING {e["ecosystem_id"]}->{pr}')
 comps=e.get('discovery_components',{})
 allowed={'installed_base_magnitude':20,'growth_replacement_pressure':15,'problem_incidence_urgency':15,'native_search_demand':15,'target_merchant_service_lag':15,'source_market_proof':10,'localization_geographic_edge':10}
 for k,v in comps.items():
  if k not in allowed: errors.append(f'UNKNOWN_DISCOVERY_COMPONENT {e["ecosystem_id"]}.{k}')
  elif v is not None and not (0<=v<=allowed[k]): errors.append(f'BAD_DISCOVERY_COMPONENT {e["ecosystem_id"]}.{k}={v}')
for p in problems:
 if p.get('ecosystem_id') not in eids: errors.append(f'PROBLEM_ECOSYSTEM_MISSING {p.get("problem_id")}->{p.get("ecosystem_id")}')
for q in queries:
 if q.get('ecosystem_id') not in eids: errors.append(f'QUERY_ECOSYSTEM_MISSING {q.get("query_id")}')
 if q.get('problem_id') not in pids: errors.append(f'QUERY_PROBLEM_MISSING {q.get("query_id")}')
 metrics=q.get('metrics',{})
 if q.get('status')=='SEED_UNMEASURED' and any(v is not None for v in metrics.values()): errors.append(f'SEED_HAS_MEASURED_METRIC {q.get("query_id")}')
for m in merchants:
 for e in m.get('ecosystems',[]):
  if e not in eids: errors.append(f'MERCHANT_ECOSYSTEM_MISSING {m.get("merchant_id")}->{e}')
for g in gaps:
 if g.get('ecosystem_id') not in eids: errors.append(f'GAP_ECOSYSTEM_MISSING {g.get("gap_id")}')
for p in pms:
 if p.get('ecosystem_id') and p['ecosystem_id'] not in eids: errors.append(f'PM_ECOSYSTEM_MISSING {p.get("product_market_id")}')
 state=p.get('state')
 if state in ('READY_PAID_TEST','SCALE'):
  for gate in ['exact_sku_identity','resale_allowed','supplier_path_verified','landed_cost_verified','positive_pre_ad_contribution','delivery_feasible','returns_warranty_known','local_checkout_feasible','keyword_planner_measured','cpc_measured']:
   if p.get('hard_gates',{}).get(gate) is not True: errors.append(f'LAUNCH_STATE_GATE_FAIL {p.get("product_market_id")}:{gate}')
strategies=[]
sp=ROOT/'global/strategy_registry.jsonl'
if sp.exists(): strategies=[json.loads(x) for x in sp.read_text().splitlines() if x.strip()]
strat={(s['strategy_id'],str(s['version'])) for s in strategies}
for h in hyps:
 if (h.get('strategy_id'),str(h.get('strategy_version'))) not in strat: errors.append(f'HYP_STRATEGY_VERSION_MISSING {h.get("hypothesis_id")}')
 if h.get('ecosystem_id') and h['ecosystem_id'] not in eids: errors.append(f'HYP_ECOSYSTEM_MISSING {h.get("hypothesis_id")}')
for x in exps:
 if x.get('hypothesis_id') not in hids: errors.append(f'EXPERIMENT_HYP_MISSING {x.get("experiment_id")}')
 if x.get('backtest_class')=='TRUE_HISTORICAL':
  if not x.get('as_of'): errors.append(f'TRUE_HIST_NO_ASOF {x.get("experiment_id")}')
for o in outs:
 if o.get('experiment_id') not in xids: errors.append(f'OUTCOME_EXPERIMENT_MISSING {o.get("outcome_id")}')
# reports
manifest=json.loads((country/'manifest.json').read_text()) if (country/'manifest.json').exists() else {}
for r in manifest.get('required_reports',[]):
 if not (country/'reports'/f'{r}.json').exists(): errors.append(f'MISSING_REPORT {r}')
# series headers must be present for Norway/full packs; empty template is allowed
sm=json.loads((country/'series/_manifest.json').read_text()) if (country/'series/_manifest.json').exists() else {'series':[]}
for s in sm.get('series',[]):
 p=country/'series'/s['file']
 if not p.exists(): errors.append(f'MISSING_SERIES {s["file"]}')
# PIT warnings
for o in obs:
 if o.get('status') in ('OBSERVED','DERIVED') and not o.get('available_at'): warnings.append(f'PIT_UNSAFE {o.get("observation_id")}: available_at unknown')
print(json.dumps({'country':manifest.get('country'),'errors':errors,'warnings':warnings[:25],'warning_count':len(warnings),'counts':{'sources':len(sources),'observations':len(obs),'ecosystems':len(ecosystems),'problems':len(problems),'queries':len(queries),'merchants':len(merchants),'archetypes':len(arch),'gaps':len(gaps),'product_markets':len(pms),'hypotheses':len(hyps),'experiments':len(exps),'outcomes':len(outs),'backtests':len(backs)},'status':'PASS' if not errors else 'FAIL'},indent=2))
sys.exit(1 if errors else 0)
