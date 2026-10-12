# One repository, two independent projects

1. Create **one empty GitHub repository** (do not initialize its README, license, or `.gitignore`).
2. Extract `NeuroRoute-1024-GitHub-Ready.zip`; its contents are the repository root.
3. Upload all extracted files and folders, including `.github` and `.gitignore`, or push with Git. **Do not upload the ZIP as a single GitHub source file**; GitHub does not automatically extract repository ZIP uploads.
4. Verify: `python3 scripts/check_boundaries.py`, then `make verify` (C11 compiler, `make`, `ar`, Python 3 needed for inventory checks).
5. Optional: GitHub **Settings → Pages → Deploy from a branch → main → /docs** to publish `docs/index.html`.
6. Optional topics: `c11`, `1024-bit`, `deterministic`, `graph-routing`, `spatial-memory`, `hamming-distance`, `developer-tools`, `monorepo`.

## Recommended Git command sequence

```sh
cd NeuroRoute-1024-Monorepo
git init -b main
git add .
git commit -m "Publish NeuroRoute 1024 core and DevTools monorepo"
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
git push -u origin main
```

The `git remote add origin` line is for **your own chosen GitHub repository**. No script or program in this package runs these commands automatically.

## Build boundaries

| Project | Source | Make command | Result |
|---|---|---|---|
| Core | `projects/neuroroute-1024/` | `make -C projects/neuroroute-1024 test` | Static C11 library + router/spatial tests |
| DevTools | `projects/neuroroute-devtools-1024/` | `make -C projects/neuroroute-devtools-1024 test` | Standalone `bin/neuro` CLI + its own library copy |

There are **no submodules, cross-project includes, symlinks, or shared build directories**. The runtime library is retained independently in both projects, byte-identical at this release. `scripts/check_boundaries.py` catches unintended drift; it does not link the two builds.

Do not interpret the visualizations as benchmark results. They show actual interface/function counts and control flow, not measured latency or throughput.
