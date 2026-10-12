CC ?= cc
AR ?= ar
CPPFLAGS := -Iinclude
WARN_CFLAGS := -std=c11 -Wall -Wextra -Wpedantic -Werror
CFLAGS ?= -O2
LIBRARY := lib/libneuro_router.a
LIB_OBJECTS := build/routing.o build/spatial_pool.o

.PHONY: all test demo sanitize clean
all: $(LIBRARY) bin/test_routing bin/test_spatial_pool bin/neuro_demo
build/%.o: src/%.c
	@mkdir -p build
	$(CC) $(CPPFLAGS) $(WARN_CFLAGS) $(CFLAGS) -c $< -o $@
$(LIBRARY): $(LIB_OBJECTS)
	@mkdir -p lib
	$(AR) rcs $@ $^
bin/test_routing: tests/test_routing.c $(LIBRARY)
	@mkdir -p bin
	$(CC) $(CPPFLAGS) $(WARN_CFLAGS) $(CFLAGS) $< $(LIBRARY) -o $@
bin/test_spatial_pool: tests/test_spatial_pool.c $(LIBRARY)
	@mkdir -p bin
	$(CC) $(CPPFLAGS) $(WARN_CFLAGS) $(CFLAGS) $< $(LIBRARY) -o $@
bin/neuro_demo: examples/demo.c $(LIBRARY)
	@mkdir -p bin
	$(CC) $(CPPFLAGS) $(WARN_CFLAGS) $(CFLAGS) $< $(LIBRARY) -o $@
test: all
	./bin/test_routing
	./bin/test_spatial_pool
demo: bin/neuro_demo
	./bin/neuro_demo
sanitize:
	$(MAKE) clean
	$(MAKE) CFLAGS="-O1 -g3 -fno-omit-frame-pointer -fsanitize=address,undefined" all
	ASAN_OPTIONS=detect_leaks=0:halt_on_error=1 UBSAN_OPTIONS=halt_on_error=1 ./bin/test_routing
	ASAN_OPTIONS=detect_leaks=0:halt_on_error=1 UBSAN_OPTIONS=halt_on_error=1 ./bin/test_spatial_pool
	ASAN_OPTIONS=detect_leaks=0:halt_on_error=1 UBSAN_OPTIONS=halt_on_error=1 ./bin/neuro_demo
clean:
	rm -rf build bin lib
