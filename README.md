# MiniTorch Module 2

<img src="https://minitorch.github.io/minitorch.svg" width="50%">


* Docs: https://minitorch.github.io/

* Overview: https://minitorch.github.io/module2/module2/

This assignment requires the following files from the previous assignments. You can get these by running

```bash
python sync_previous_module.py previous-module-dir current-module-dir
```

The files that will be synced are:

        minitorch/operators.py minitorch/module.py minitorch/autodiff.py minitorch/scalar.py minitorch/module.py project/run_manual.py project/run_scalar.py

## Tensor training results

| Dataset | Final loss | Correct | Accur | Mean time per epoch (s) |
| --- | ---: | ---: | ---: | ---: |
| Simple | 0.0693 | 50/50 | 100.0% | 0.1332 |
| Diag | 3.6294 | 47/50 | 94.0% | 0.1327 |
| Split | 5.4893 | 49/50 | 98.0% | 0.1338 |
| Xor | 1.2103 | 50/50 | 100.0% | 0.1331 |
| Circle | 8.8817 | 46/50 | 92.0% | 0.1327 |
| Spiral | 32.9605 | 28/50 | 56.0% | 0.1322 |
