# DevTools validation contract

The release gate covers strict C11 compilation, all library and CLI tests, live demo execution, exact 1024-bit exhaustive spatial tests, invalid and ambiguous project detection, safe missing-tool behavior, non-empty initialization refusal, process-runner failures, ASan/UBSan execution, compiler diagnostics, static analysis where installed, and fresh-extraction rebuilds. LeakSanitizer is attempted separately and is marked unavailable when the host is ptrace-restricted.

Every public header is populated, every declared path is implemented, process execution is shell-free, and no superseded spatial width is accepted into the release tree.
