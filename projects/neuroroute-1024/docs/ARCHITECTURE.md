# NeuroRoute 1024-bit architecture

## Exact spatial contract

The spatial key is exactly 1024 bits represented by 16 `uint64_t` lanes. The public API accepts only `SPATIAL_COORDINATE_WORDS` (16) lanes; null, partial, oversized, and unconfigured inputs fail closed. There is no width negotiation and no legacy-width interpretation.

Each configured chunk contains its 1024-bit key, a page identifier, and a saturating-free `uint32_t` density counter. Allocation computes the exact Hamming distance across every lane, selects the minimum, resolves equal distances by the lowest configured index, increments only the selected counter, and returns its page. An empty or invalid request returns zero.

The pool uses a C11 `atomic_flag` guard around reset, configuration, allocation, and inspection. The implementation uses a portable C11 SWAR popcount rather than a compiler-specific intrinsic. Graph routing remains a separate deterministic maximum-weight subsystem.

## Repository boundary

This project directory is the independent core library. The sibling `neuroroute-devtools-1024` directory contains the standalone DevTools CLI and its own copy of the 1024-bit library integration. Neither project depends on its sibling to build. Neither repository contacts GitHub or external services at runtime.
