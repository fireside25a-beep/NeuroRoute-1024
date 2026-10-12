# Source provenance & duplicate audit

Input: `NeuroRoute_1024_DUAL_REPOSITORY_MASTER.zip`  
SHA-256: `981c12160289e73dccb4dd73803d06e036f82c72bfbdc0b5440b48113c608a69`

Every one of the **391 outer ZIP entries** was included in the ZIP central-directory and CRC integrity check; each of the **257 non-directory entries** was inventoried. All **four nested ZIPs** passed their own CRC integrity checks, and every code/documentation payload file was matched to the corresponding `SOURCE/` payload byte-for-byte. The original `GIT/`, `NORMAL/`, and `SOURCE/` trees were also compared by path and SHA-256.

| Project | Original project files | `SOURCE/`, `NORMAL/`, `GIT/` | Nested SOURCE / GIT archives |
|---|---:|---|---|
| NeuroRoute Core | 14 | Identical | Identical |
| NeuroRoute DevTools | 33 | Identical | Identical |

All 47 original project files are retained in `projects/`; **4 build/documentation files have intentional monorepo updates**. No original C source, public header, test program, example, or project license was edited. Ten shared relative paths retain byte-identical content, including library implementations, public headers, tests, demonstration, and MIT license.

### Intentional changes (compared with original `SOURCE/`)

- `neuroroute-devtools-1024/Makefile`: invoke the CLI smoke-test script with `sh` in both normal tests and sanitizer tests, so fresh GitHub uploads run without relying on preserved executable mode.
- `neuroroute-1024/README.md`: update separate-repository wording to a sibling project directory.
- Both projects' `docs/ARCHITECTURE.md`: update repository-boundary wording, with no algorithm changes.
- `tests/test_cli.sh`: executable mode is restored (content unchanged).

### Excluded without loss of canonical source

- Duplicate source mirrors under `GIT/`, `NORMAL/`, `SOURCE/` (all source content represented once per project).
- The four nested archives (verified as duplicates).
- Separate embedded `.git` administrative directories, because **one Git repository must have one root `.git`**. Historical Git internals are not published as project sources; the original input archive retains them.

`ORIGINAL_RELEASE_NOTES.md` preserves the top-level release documentation which is not inside either project; the two original one-commit Git histories were inspected with `git fsck --full --strict` and identified as `b3a8ea5` and `ddd18e3`. The original archive remains the provenance record for those historical `.git` objects.

`SOURCE_AUDIT.json` contains full path-by-path original SHA-256 digests, modified-file digests, nested-archive hashes, and compiled exported-function inventory. `scripts/check_boundaries.py` compares all 47 project payloads against their frozen release digests and checks shared-component parity. If source changes intentionally, refresh the manifest as part of a reviewed release.
