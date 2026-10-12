# NeuroRoute 1024-bit C11

NeuroRoute DevCLI is a portable C11 developer command-line tool built around a deterministic routing library. It detects project types, selects installed toolchains, creates small starter projects, and safely launches compilers, interpreters, test runners, and editors.

It is not an AI model, operating system, compiler, shell, terminal emulator, or package manager.

## Included components

The release preserves the original NeuroRoute C library and adds the DevCLI.

The original library provides:

- deterministic maximum-weight graph routing;
- activation-threshold and fallback behavior;
- atomic route-use counters;
- 1024-bit Hamming-distance spatial matching;
- a static library;
- routing and spatial-pool unit tests;
- the original demonstration program.

The DevCLI adds:

- deterministic project detection;
- explicit ambiguity reporting;
- toolchain discovery;
- starter-project generation;
- build, run, test, and clean actions;
- safe child-process execution through `posix_spawnp()` and `waitpid()`;
- editor launching without a shell;
- an optional interactive command loop.

## Original behavior

The routing and spatial-matching algorithms remain separate from the DevCLI code.

Expected test output:

```text
routing tests: PASS
spatial pool tests: PASS
```

Expected demo output:

```text
Selected route target: 1002
Selected spatial page: 8192
```

## Requirements

To build NeuroRoute DevCLI itself:

- macOS or Linux with POSIX process APIs;
- a C11 compiler, GCC or Clang;
- `make`;
- `ar`.

The generated projects require their matching external toolchains. NeuroRoute does not download or install compilers, interpreters, packages, or dependencies.

## Build targets

```bash
make
make test
make demo
make devcli
make clean
make sanitize
```

The normal build creates:

```text
lib/libneuro_router.a
bin/neuro
bin/neuro_demo
bin/test_routing
bin/test_spatial_pool
bin/test_process_runner
bin/test_project_detect
bin/test_project_init
```

`make test` runs all old and new unit tests plus CLI smoke tests. `make demo` runs the original demonstration. `make sanitize` rebuilds with AddressSanitizer and UndefinedBehaviorSanitizer.

## CLI commands

```text
neuro help
neuro status
neuro detect [path]
neuro init <language> <directory>
neuro build [path]
neuro run [path]
neuro test [path]
neuro clean [path]
neuro edit <file>
```

Run `bin/neuro` without arguments to enter the simple interactive mode:

```text
neuro> status
neuro> detect .
neuro> build .
neuro> run .
neuro> test .
neuro> quit
```

The interactive parser accepts whitespace-separated arguments. It is not a shell and does not implement quoting, pipelines, redirects, job control, or PTY behavior.

## Supported languages

| Language | Detection evidence | Required tools | Generated entry point |
|---|---|---|---|
| C | `Makefile`, `*.c` | `clang` or `gcc`; `make` for Makefile projects | `main.c` |
| C++ | `CMakeLists.txt`, `*.cpp`, `*.cc`, `*.cxx` | `clang++` or `g++`; `make` for Makefile projects | `main.cpp` |
| Python | `pyproject.toml`, `requirements.txt`, `*.py` | `python3` | `main.py` |
| Rust | `Cargo.toml`, `*.rs` | `cargo` | `Cargo.toml`, `src/main.rs` |
| JavaScript | `package.json`, `*.js`, `*.mjs`, `*.cjs` | `node`; optional `npm` | `main.js` |
| Go | `go.mod`, `*.go` | `go` | `go.mod`, `main.go` |
| Zig | `build.zig`, `*.zig` | `zig` | `main.zig` |
| Java | `pom.xml`, `build.gradle`, `build.gradle.kts`, `*.java` | `javac` and `java` | `Main.java` |

## Detection rules

Detection scans the selected file or directory and ignores common build and cache directories. Evidence has deterministic priority:

1. language-specific manifest files;
2. source-file extensions;
3. a generic `Makefile` as weak C evidence.

A single highest-priority language is selected. Equal-priority conflicts are reported as ambiguous instead of being silently guessed. For example, a folder containing both `main.c` and `main.py` without a stronger manifest is ambiguous, while a C++ source tree with a generic Makefile is detected as C++.

## Starter projects

Each generated project prints:

```text
Hello from NeuroRoute DevCLI
```

Examples:

```bash
bin/neuro init c /tmp/hello-c
bin/neuro build /tmp/hello-c
bin/neuro run /tmp/hello-c

bin/neuro init python /tmp/hello-python
bin/neuro test /tmp/hello-python
```

`neuro init` refuses to overwrite an existing non-empty directory. There is no force option in v0.4.0.

## Build, run, test, and clean behavior

The DevCLI uses conventional deterministic entry points for generated projects:

- C: compile `main.c` to `.neuro/neuro-c-app`;
- C++: compile `main.cpp` to `.neuro/neuro-cpp-app`;
- Python: syntax-check and execute `main.py`;
- Rust: use `cargo build`, `cargo run`, `cargo test`, and `cargo clean`;
- JavaScript: use `node --check` and execute `main.js`; use matching npm scripts when a package file and npm are present;
- Go: build `.neuro/neuro-go-app`, execute it, and use `go test ./...`;
- Zig: build `.neuro/neuro-zig-app` or use `zig build` when `build.zig` exists;
- Java: compile `Main.java` into `.neuro/java` and execute class `Main`.

For C or C++ projects containing a Makefile, `neuro build`, `neuro test`, and `neuro clean` call the corresponding `make`, `make test`, and `make clean` actions. The CLI does not guess a runnable executable for an arbitrary Makefile project.

## Tool overrides

A single executable name or path can be selected through these environment variables:

```text
NEURO_CC
NEURO_CXX
NEURO_PYTHON
NEURO_CARGO
NEURO_NODE
NEURO_NPM
NEURO_GO
NEURO_ZIG
NEURO_JAVAC
NEURO_JAVA
```

Examples:

```bash
NEURO_CC=gcc bin/neuro build /tmp/hello-c
NEURO_CXX=clang++ bin/neuro build /tmp/hello-cpp
```

## Editor command

`neuro edit <file>` uses `VISUAL`, then `EDITOR`, then `vi`. The value must resolve to one executable name or path. Embedded shell arguments are intentionally rejected.

Example:

```bash
EDITOR=nano bin/neuro edit main.c
```

## Security model

Child processes are launched with argument arrays through `posix_spawnp()` and waited for with `waitpid()`. The DevCLI does not send user input through `system()`, `popen()`, `sh -c`, or `bash -c`.

Child programs inherit normal stdin, stdout, stderr, and environment variables. The DevCLI does not sandbox child programs and does not claim that compilers, scripts, editors, or project files are trusted. Users should only run projects and tools they trust.

The DevCLI performs no network calls. External tools may have their own behavior; for example, package managers or build systems can access networks if their project configuration instructs them to do so.

## Limitations

- The release targets macOS and Linux, not Windows.
- Project detection is intentionally small and marker-based.
- The generated one-file layouts are the best-supported paths.
- Arbitrary framework-specific entry points are not inferred.
- CMake, Maven, and Gradle marker files may be detected for classification; their build actions are reported as unsupported rather than guessed.
- The CLI does not install missing toolchains.
- The CLI does not emulate a terminal, shell, or PTY.
- Runtime behavior was tested only on the environment listed below. macOS source portability was designed for POSIX C11 APIs but was not runtime-tested here.

## Actual validation environment

Validation was performed on:

```text
OS: Debian GNU/Linux 13 (trixie)
Kernel: Linux 4.4.0
Architecture: x86_64
GCC: 14.2.0
Clang: 17.0.0
GNU Make: 4.4.1
GNU ar: 2.44
```

Toolchain results from generated starter projects:

| Toolchain | Result | Version |
|---|---|---|
| C with Clang | PASS | Clang 17.0.0 |
| C with GCC | PASS | GCC 14.2.0 |
| C++ with Clang++ | PASS | Clang 17.0.0 |
| C++ with G++ | PASS | G++ 14.2.0 |
| Python | PASS | Python 3.13.5 |
| JavaScript | PASS | Node.js 22.16.0 |
| npm detection | PASS | npm 10.9.2 |
| Go | PASS | Go 1.23.2 |
| Java | PASS | OpenJDK 21.0.10 |
| Rust | SKIPPED | `cargo` not installed |
| Zig | SKIPPED | `zig` not installed |

The full project built and passed tests with both GCC and Clang. GCC AddressSanitizer and UndefinedBehaviorSanitizer validation passed. The installed Clang 17 sanitizer runtime failed at process startup on this host, including for an independent one-line C program, so the Clang sanitizer run is recorded as an environment-specific failure rather than a NeuroRoute test pass.

## Source layout

```text
.
|-- examples/
|   `-- demo.c
|-- include/
|   |-- asm/
|   |   `-- primitives.h
|   |-- mm/
|   |   `-- spatial_pool.h
|   |-- devcli.h
|   |-- fs_utils.h
|   |-- neuro.h
|   |-- process_runner.h
|   |-- project_actions.h
|   |-- project_detect.h
|   |-- project_init.h
|   `-- toolchains.h
|-- src/
|   |-- devcli.c
|   |-- fs_utils.c
|   |-- main.c
|   |-- process_runner.c
|   |-- project_actions.c
|   |-- project_detect.c
|   |-- project_init.c
|   |-- routing.c
|   |-- spatial_pool.c
|   `-- toolchains.c
|-- tests/
|   |-- test_cli.sh
|   |-- test_process_runner.c
|   |-- test_project_detect.c
|   |-- test_project_init.c
|   |-- test_routing.c
|   `-- test_spatial_pool.c
|-- .gitignore
|-- LICENSE
|-- Makefile
`-- README.md
```

## License

MIT License. See `LICENSE`.
