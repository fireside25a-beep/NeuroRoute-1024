#!/usr/bin/env python3
"""Validate the frozen source inventory and identical shared runtime copies."""
from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parents[1]
report=json.loads((root/'audit/SOURCE_AUDIT.json').read_text())
errors=[]
original=report['original_source_sha256']
expected={k: report['source_changes'].get(k,{}).get('release_sha256', v) for k,v in original.items()}
for path,digest in sorted(expected.items()):
 f=root/'projects'/path
 if not f.is_file():errors.append('MISSING '+path)
 elif hashlib.sha256(f.read_bytes()).hexdigest()!=digest:errors.append('CHANGED '+path)
for project in ('neuroroute-1024','neuroroute-devtools-1024'):
 p=root/'projects'/project
 for f in sorted(p.rglob('*')):
  if not f.is_file() or any(s in ('.git','bin','build','lib','__pycache__') for s in f.relative_to(p).parts):continue
  rel=project+'/'+f.relative_to(p).as_posix()
  if rel not in expected:errors.append('UNTRACKED PROJECT FILE '+rel)
  if f.is_symlink():errors.append('PROJECT SYMLINK '+rel)
for path,relation in sorted(report['shared_relative_paths'].items()):
 if relation != 'identical':continue
 a=root/'projects/neuroroute-1024'/path
 b=root/'projects/neuroroute-devtools-1024'/path
 if not a.is_file() or not b.is_file() or a.read_bytes()!=b.read_bytes():
  errors.append('SHARED SOURCE DIVERGED '+path)
for f in sorted((root/'assets').glob('*.svg')):
 duplicate=root/'docs'/'assets'/f.name
 if not duplicate.is_file() or duplicate.read_bytes()!=f.read_bytes():errors.append('PAGES GRAPHIC DIVERGED '+f.name)
for f in root.rglob('.git'):
 errors.append('EMBEDDED .git '+str(f.relative_to(root)))
if errors:
 for issue in errors:print('FAIL:',issue,file=sys.stderr)
 sys.exit(1)
print(f'PASS: {len(original)} original payload paths accounted for, {sum(x=="identical" for x in report["shared_relative_paths"].values())} shared paths identical, no nested Git repositories')
