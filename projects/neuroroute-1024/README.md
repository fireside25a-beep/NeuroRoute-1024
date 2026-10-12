# NeuroRoute 1024-bit core

Portable C11 NeuroRoute core library with deterministic maximum-weight routing and exact 1024-bit Hamming spatial matching.

The spatial representation is exactly sixteen `uint64_t` lanes. APIs reject null, partial-width, and out-of-range inputs. Matching scans all 1024 bits, chooses the lowest distance, resolves ties by the first configured index, and increments only the selected chunk. The pool is serialized with a C11 atomic flag.

Build and test:

```sh
make all
make test
make demo
make sanitize
```

This repository contains only the core library, its public headers, tests, and demonstration. NeuroRoute DevTools lives in the sibling `../neuroroute-devtools-1024/` project in this monorepo. Both projects retain independent build systems and sources.
