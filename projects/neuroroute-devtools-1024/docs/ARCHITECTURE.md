# NeuroRoute DevTools 1024-bit architecture

DevTools preserves the public commands `help`, `status`, `detect`, `init`, `build`, `run`, `test`, `clean`, and `edit`. Project detection and child-process execution remain separate from the routing library. Child processes are launched through `posix_spawnp()` and waited with `waitpid()`; no shell command construction is used.

The integrated spatial pool uses exactly 16 `uint64_t` lanes: 1024 bits. It rejects any vector whose word count is not exactly 16, scans all 1024 bits, uses deterministic first-index tie breaking, and updates only the selected chunk. C11 atomic serialization protects the shared pool. The graph router retains deterministic maximum-weight selection and activation fallback.

This project is independently buildable inside a monorepo alongside NeuroRoute Core. It is a standalone source tree and does not modify, push to, or depend on a remote Git repository.
