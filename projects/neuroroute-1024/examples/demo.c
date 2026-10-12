#include <mm/spatial_pool.h>
#include <neuro.h>

#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>

int main(void) {
    neuro_router_reset();
    spatial_pool_reset();

    neuro_set_node(0, 9000);
    neuro_add_edge(0, 1001, 25);
    neuro_add_edge(0, 1002, 90);
    neuro_add_edge(0, 1003, 40);

    uint64_t routed_target = route_synaptic_signal(0, 500);

    const uint64_t chunk_a[SPATIAL_COORDINATE_WORDS] = {0};
    const uint64_t chunk_b[SPATIAL_COORDINATE_WORDS] = {
        UINT64_MAX, UINT64_MAX, UINT64_MAX, UINT64_MAX,
        UINT64_MAX, UINT64_MAX, UINT64_MAX, UINT64_MAX,
        UINT64_MAX, UINT64_MAX, UINT64_MAX, UINT64_MAX,
        UINT64_MAX, UINT64_MAX, UINT64_MAX, UINT64_MAX
    };
    const uint64_t feature[SPATIAL_COORDINATE_WORDS] = {
        UINT64_MAX, UINT64_MAX, UINT64_MAX, UINT64_MAX,
        UINT64_MAX, UINT64_MAX, UINT64_MAX, UINT64_MAX,
        UINT64_MAX, UINT64_MAX, UINT64_MAX, UINT64_MAX,
        UINT64_MAX, UINT64_MAX, UINT64_MAX, UINT64_MAX
    };

    spatial_pool_set_chunk(0, chunk_a, 4096, 0);
    spatial_pool_set_chunk(1, chunk_b, 8192, 0);

    uint64_t selected_page = allocate_spatial_memory(
        feature,
        SPATIAL_COORDINATE_WORDS
    );

    printf("Selected route target: %" PRIu64 "\n", routed_target);
    printf("Selected spatial page: %" PRIu64 "\n", selected_page);

    neuro_router_reset();
    return 0;
}
