# Validation matrix and scope

The original archive's 47 canonical project files were individually hashed and compared with all source mirrors and four nested archives. Tests below were run against the extracted project code, applying only the documented CLI Makefile permission fix.

| Check | Core | DevTools |
|---|---|---|
| GCC 14.2 strict C11 compile, unit tests, demonstration | PASS | PASS |
| Clang 17 strict C11 compile, unit tests, demonstration | PASS | PASS |
| GCC 14 `-fanalyzer` build | PASS | PASS |
| GCC ASan+UBSan with `detect_leaks=0` | PASS | PASS |
| Clang ASan+UBSan with `detect_leaks=0` | PASS | PASS |
| Standalone CLl smoke test | N/A | PASS after shell invocation fix |
| Exhaustive spatial **bit position** coverage | PASS via existing 1024-position test | PASS via identical existing test |
| Every possible 1024-bit vector / concurrent schedule | NOT TESTED | NOT TESTED |
| Runtime on macOS/Windows/ARM | NOT TESTED | NOT TESTED |

**Important scope:** the existing spatial tests iterate across all 1,024 individual bit positions; this does **not** enumerate all `2^1024` possible vectors or prove race freedom. Sanitizer jobs disable leak detection explicitly in the inherited Makefiles. The release does not claim complete dynamic path, concurrency, or cross-platform verification. The CI files request additional builds only when GitHub Actions actually executes them.

## Known boundary of the DevCLI

The DevCLI invokes user-selected tools as normal child processes; it **does not sandbox** programs or make untrusted projects safe to execute. Its `clean` actions may delete normal generated project artifacts. Use it only with trusted projects and toolchains. The project is not a new compiler or runtime backend.

## Verification commands

```sh
python3 scripts/check_boundaries.py
make verify
# Optional sanitizer targets (run with environment that supports ASan)
make sanitize
# Optional alternate compilers
make clean && make CC=clang all test demo
```

`make verify` always clears and rebuilds each project's own outputs. The original source hashes and the four deliberate release changes are fully listed in `audit/SOURCE_AUDIT.json`.
