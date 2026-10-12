# Validation contract

The release gate is:

1. strict C11 compilation with `-Wall -Wextra -Wpedantic -Werror`;
2. routing positives, threshold/fallback behavior, tie selection, counters, and invalid node bounds;
3. spatial positives, empty state, nulls, invalid indices, exact-width rejection, density updates, tie selection, and all 1024 single-bit positions;
4. demo execution with deterministic output;
5. AddressSanitizer and UndefinedBehaviorSanitizer execution; LeakSanitizer is attempted separately and is marked unavailable when the host is ptrace-restricted;
6. GCC and Clang builds where available, plus GCC static analysis where available;
7. fresh extraction and rebuild from the source-only archive;
8. source-tree audit for complete implementations, populated public headers, shell-free execution, and absence of superseded-width documentation.

A toolchain that is unavailable is recorded as skipped by the release harness; it is never represented as a pass.
