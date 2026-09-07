#!/usr/bin/env python3
import sys,hashlib,json,datetime
from pathlib import Path
p=Path(sys.argv[1]); data=p.read_bytes(); print(json.dumps({'storage_uri':str(p.resolve()),'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2))
