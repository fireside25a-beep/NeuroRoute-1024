# Local verification record

All results here were run against the assembled two-project source tree in the execution environment before packaging. They are **local results**, not GitHub Actions run confirmations. No performance benchmark or whole-state correctness proof is claimed.

| Gate | Result | Evidence |
|---|---|---|
| GCC strict build / tests / demos | PASS | [`FINAL_GCC.log`](local-test-logs/FINAL_GCC.log) |
| Clang strict build / tests / demos | PASS | [`FINAL_CLANG.log`](local-test-logs/FINAL_CLANG.log) |
| GCC static analyzer build / tests / demos | PASS | [`FINAL_ANALYZER.log`](local-test-logs/FINAL_ANALYZER.log) |
| GCC AddressSanitizer + UndefinedBehaviorSanitizer | PASS | [`FINAL_GCC_SANITIZE.log`](local-test-logs/FINAL_GCC_SANITIZE.log) |
| Clang AddressSanitizer + UndefinedBehaviorSanitizer | PASS | [`FINAL_CLANG_SANITIZE.log`](local-test-logs/FINAL_CLANG_SANITIZE.log) |

Compilers: `gcc (Debian 14.2.0-19) 14.2.0`; `clang version 17.0.0 (https://github.com/swiftlang/llvm-project.git 10999b6d034fe318f3d56c83bddb6572593a8bb0)`.

Scope and limitations: strict C11 warnings-as-errors compilation; existing routing/spatial tests; DevTools process/detection/initialization/CLI tests; the deterministic demonstration in each project; GCC `-fanalyzer`; both compiler ASan+UBSan runs. Sanitizer commands use `detect_leaks=0`, so they **do not prove leak freedom**. The local test set does **not** enumerate every 1024-bit state, every input or every supported operating system. CI jobs remain unverified until GitHub executes them.

The input ZIP, project content hashes, and deliberate release edits are recorded in [`SOURCE_AUDIT.json`](SOURCE_AUDIT.json).
