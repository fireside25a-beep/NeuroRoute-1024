# Compiled public/global function inventory

Symbols extracted with `nm -g --defined-only` from C object files in the supplied projects after building. This count includes `main` and the repeated core symbols in DevTools; it is **not** a count of distinct APIs or a complexity/performance metric. Internal `static` functions are intentionally excluded.

## Core — 10 exported functions

### `src/routing.c` — 6 exported function(s)

- `neuro_add_edge()`
- `neuro_get_edge_spike_count()`
- `neuro_get_node_snapshot()`
- `neuro_router_reset()`
- `neuro_set_node()`
- `route_synaptic_signal()`

### `src/spatial_pool.c` — 4 exported function(s)

- `allocate_spatial_memory()`
- `spatial_pool_get_chunk()`
- `spatial_pool_reset()`
- `spatial_pool_set_chunk()`

## DevTools — 34 exported functions

### `src/devcli.c` — 1 exported function(s)

- `devcli_main()`

### `src/fs_utils.c` — 9 exported function(s)

- `fs_directory_exists()`
- `fs_directory_is_empty()`
- `fs_file_exists()`
- `fs_join()`
- `fs_mkdirs()`
- `fs_path_exists()`
- `fs_remove_python_cache()`
- `fs_remove_tree()`
- `fs_write_text_file()`

### `src/main.c` — 1 exported function(s)

- `main()`

### `src/process_runner.c` — 1 exported function(s)

- `process_run()`

### `src/project_actions.c` — 4 exported function(s)

- `project_action_build()`
- `project_action_clean()`
- `project_action_run()`
- `project_action_test()`

### `src/project_detect.c` — 4 exported function(s)

- `project_detect_path()`
- `project_detect_print()`
- `project_language_name()`
- `project_language_parse()`

### `src/project_init.c` — 1 exported function(s)

- `project_init_create()`

### `src/routing.c` — 6 exported function(s)

- `neuro_add_edge()`
- `neuro_get_edge_spike_count()`
- `neuro_get_node_snapshot()`
- `neuro_router_reset()`
- `neuro_set_node()`
- `route_synaptic_signal()`

### `src/spatial_pool.c` — 4 exported function(s)

- `allocate_spatial_memory()`
- `spatial_pool_get_chunk()`
- `spatial_pool_reset()`
- `spatial_pool_set_chunk()`

### `src/toolchains.c` — 3 exported function(s)

- `toolchain_find_executable()`
- `toolchain_print_status()`
- `toolchain_resolve()`

