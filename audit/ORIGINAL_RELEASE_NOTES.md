# NeuroRoute 1024-bit dual-repository release

This package contains two independent local Git repositories:

- `neuroroute-1024`: core C11 routing and exact 1024-bit spatial library;
- `neuroroute-devtools-1024`: the separate DevTools CLI repository with the same exact-width library integration.

The spatial key is sixteen `uint64_t` lanes, exactly 1024 bits. Partial-width requests are rejected. The implementation uses portable C11 atomics and a portable SWAR popcount, deterministic minimum-distance selection, first-index tie breaking, and selected-counter updates.

Validation performed before packaging:

- strict GCC C11 build with warnings as errors;
- complete positive/negative routing, spatial, process, detection, initialization, and CLI tests;
- exhaustive all-1024-bit spatial discrimination tests;
- live demo execution with deterministic route/page output;
- GCC ASan/UBSan execution with leak detection disabled because the managed host is ptrace-restricted;
- GCC `-fanalyzer` build;
- source audit for superseded spatial widths, empty headers, placeholder markers, and shell execution APIs;
- clean source-only rebuilds after removing generated artifacts.

Clang was not installed in the execution environment and is recorded as skipped, never as a pass. No GitHub remote, push, commit, or external connection was used.
