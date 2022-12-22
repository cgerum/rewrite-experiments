# Hardware and Performance Aware Term Rewriting

This repository contains some early work on Hardware Performance Aware Term Rewriting for Embedded Systems.


## Performance ~~Meta~~Modeling

## Equality Saturation based term rewriting

The term rewriting prototype based on [egg](https://egraphs-good.github.io/). 

Getting Started: 

```bash
# First install rust using rustup
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Then build and run the tests
cd rewrite-eqsat
cargo test
```

To run an equality saturation from the commandline use for example:

```bash
cargo run --release -- "(+ a 0)"
```

```
Best Expr: a
Best Cost: 1
```

The rewrite steps leading to the best expression can be show using the flag `--explain`. 

```bash
cargo run --release -- --explain "(+ a 0)"
```

Should produce show the rules producing this minimization. 

```
(+ a 0)
(Rewrite=> zero-add a)

Best Expr: a
Best Cost: 1
```

But be aware that the tracking of rewrites takes a lot of resources. It should not be needed besides debugging and maybe some verification purposes. 




