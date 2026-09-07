from __future__ import annotations
from pathlib import Path
import ast, re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
for path in ROOT.rglob("*.py"):
    if path.resolve() == Path(__file__).resolve(): continue
    if any(x in path.parts for x in {".venv","__pycache__"}): continue
    text=path.read_text(encoding="utf-8")
    try: tree=ast.parse(text)
    except SyntaxError as e: errors.append(f"{path}: syntax {e}"); continue
    for node in ast.walk(tree):
        if isinstance(node,ast.Call) and isinstance(node.func,ast.Name) and node.func.id in {"eval","exec"}:
            errors.append(f"{path}:{node.lineno}: banned {node.func.id}")
    if re.search(r'(?i)(api[_-]?key|secret|password)\s*=\s*["\'][A-Za-z0-9_-]{16,}["\']', text):
        errors.append(f"{path}: possible hardcoded secret")
    if "allow_origins=['*']" in text or 'allow_origins=["*"]' in text:
        errors.append(f"{path}: wildcard CORS")
print("STATIC_AUDIT_PASS" if not errors else "STATIC_AUDIT_FAIL")
for e in errors: print(e)
sys.exit(1 if errors else 0)
