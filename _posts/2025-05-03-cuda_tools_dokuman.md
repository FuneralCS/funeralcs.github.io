---
title: "Official Cuda Tools Documentation"
date: 2025-05-03 12:45:00 +0300
categories: [general, python, cudatools]
tags: [python, cuda tools, documentation, library]
author: tunahan
image:
  path: /assets/img/cudatools.png
  alt: Cuda Tools
description: "Documentation of the Python Cuda Tools module"
toc: true
math: false
mermaid: false
comments: true
pin: true
---

# universal-cuda-tools Official Documentation

## Table of Contents
1. [Overview](#overview)
2. [Installation](#installation)
3. [Core Concepts](#core-concepts)
4. [`@cuda` Decorator](#cuda-decorator)
   - Signature and Parameters
   - Behavior
   - Example Usage
5. [`@cuda_advanced` Decorator](#cuda_advanced-decorator)
   - Signature and Parameters
   - Advanced Features
   - Example Usage
6. [`DeviceContext` Context Manager](#devicecontext-context-manager)
   - Signature and Parameters
   - Auto Tensorization
   - AMP Integration
   - Example Usage
7. [Utility Functions (`utils.py`)](#utility-functions-utilspy)
   - `tensorize_for_universal`
   - `move_to_torch`
   - `patch_numpy_with_cupy`
8. [Neural Network Example](#neural-network-example)
9. [Benchmark and Profiling](#benchmark-and-profiling)
10. [Caveats](#caveats)
11. [FAQ](#faq)
12. [License](#license)

## Overview
`universal-cuda-tools` is a Python toolkit that works with PyTorch and optionally TensorFlow. It automatically tensorizes raw Python, NumPy, or CuPy data, manages GPU/CPU device placement, and wraps advanced features like mixed precision (AMP), timeouts, retries, VRAM checks, memory profiling, live dashboard, and dry-run mode into a single utility package.

### Key Features
- **`@cuda`**: Lightweight, device-aware wrapper with auto-tensorization, retry, and fallback
- **`@cuda_advanced`**: Fully featured decorator with timeout, AMP, multi-GPU, error callbacks, telemetry, live dashboard, and dry-run
- **`DeviceContext`**: Block-scope control over device, AMP, and tensor conversion
- **utils**: Includes `tensorize_for_universal`, `move_to_torch`, `patch_numpy_with_cupy`

## Installation
```bash
pip install universal-cuda-tools
```
or from source:
```bash
git clone https://github.com/tunahanyrd/universal-cuda-tools.git
cd universal-cuda-tools
python -m build
pip install dist/universal_cuda_tools-<version>.whl
```

## Core Concepts
1. **Device**: `"cpu"`, `"cuda"`, `"cuda:0"`, etc.  
2. **Tensorize**: Convert raw Python/NumPy data into `torch.Tensor`  
3. **Auto-tensorize**: Automatic conversion using decorator or context  
4. **OOM Fallback**: Fallback to CPU if GPU memory is insufficient  
5. **Mixed Precision (AMP)**: Use `torch.autocast` to accelerate with FP16  

## `@cuda` Decorator

### Signature and Parameters
```python
def cuda(func=None, *,
         device=None,
         verbose=True,
         clear_cache=False,
         retry=0,
         min_free_vram=None,
         auto_tensorize=False,
         to_list=False):
    ...
```
- **`device`** (`str`): `'cuda'`, `'cuda:0'`, `'cpu'`, or `None` for automatic
- **`verbose`** (`bool`): Print logs to INFO level
- **`clear_cache`** (`bool`): Run `torch.cuda.empty_cache()` before call
- **`retry`** (`int`): Retry count on error
- **`min_free_vram`** (`float`): Minimum VRAM in GB, else RuntimeError
- **`auto_tensorize`** (`bool`): Convert Python/NumPy to `torch.Tensor(device)`
- **`to_list`** (`bool`): Convert tensor output to native Python list

### Behavior
1. Optionally converts args to tensors via `auto_tensorize`  
2. Moves tensor/NumPy inputs to the target `device`  
3. Calls function; retries on error up to `retry`  
4. If still out of memory, falls back to CPU  
5. Logs memory usage if `verbose` is enabled  
6. Returns output as list if `to_list=True`  

### Example Usage
```python
from cuda_tools import cuda
import numpy as np

@cuda(device="cuda", auto_tensorize=True, to_list=True, verbose=True)
def vector_add(a, b):
    return a + b

result = vector_add([1,2,3], np.array([4,5,6]))
print(result)  # [5,7,9]
```

## `@cuda_advanced` Decorator

### Signature and Parameters
```python
def cuda_advanced(func=None, *,
                  device=None,
                  verbose=True,
                  clear_cache=False,
                  retry=0,
                  min_free_vram=None,
                  auto_tensorize=False,
                  to_list=False,
                  timeout=None,
                  use_amp=False,
                  mgpu=False,
                  error_callback=None,
                  telemetry=False,
                  memory_profiler=True,
                  live_dashboard=False,
                  dry_run=False):
    ...
```
- **`timeout`** (`float`): Timeout in seconds
- **`use_amp`** (`bool`): Enable mixed precision with `torch.autocast`
- **`mgpu`** (`bool`): Use least-loaded GPU if available
- **`error_callback`** (`callable`): Called on error
- **`telemetry`** (`bool`): Logs device and timing info
- **`memory_profiler`** (`bool`): Logs memory deltas
- **`live_dashboard`** (`bool`): Tracks call count and total duration
- **`dry_run`** (`bool`): Skips execution, returns `None`

### Advanced Features
- Timeout raises `TimeoutError`  
- AMP speeds up training/inference  
- Multi-GPU support  
- Error callback and early exit  
- Dry-run testing without side effects

### Example Usage
```python
from cuda_tools import cuda_advanced
import torch, time

@cuda_advanced(timeout=0.5, retry=1, use_amp=True,
               telemetry=True, verbose=True)
def train_step(x):
    time.sleep(1)
    return x * x

try:
    train_step(torch.ones(10,10, device="cuda"))
except TimeoutError:
    print("Time out!")
```

## `DeviceContext` Context Manager

### Signature and Parameters
```python
class DeviceContext:
    def __init__(self, device='cuda',
                 use_amp=False,
                 verbose=False,
                 auto_tensorize=False):
        ...
    def __enter__(self) -> torch.device: ...
    def __exit__(self, exc_type, exc_val, exc_tb): ...
```
- **`device`** (`str`): `'cuda'` or `'cpu'`  
- **`use_amp`** (`bool`): Enables mixed precision  
- **`verbose`** (`bool`): Print logs  
- **`auto_tensorize`** (`bool`): Converts Python/NumPy to `torch.Tensor` inside block

### Usage
```python
from cuda_tools.context import DeviceContext
import numpy as np

with DeviceContext(device='cuda', auto_tensorize=True, use_amp=True, verbose=True) as dev:
    a = tensorize_for_universal(5, dev)
    b = tensorize_for_universal(np.array([1,2,3]), dev)
    print(a + b, (a+b).device)
```

## Utility Functions (`utils.py`)

### `tensorize_for_universal(obj, device)`
Converts raw Python (`int`, `float`), NumPy scalars, arrays, PyTorch or TensorFlow tensors to `torch.Tensor(device)`

### `move_to_torch(device, obj)`
Moves NumPy or PyTorch tensor to specified device

### `patch_numpy_with_cupy()`
Redirects NumPy calls to CuPy for GPU acceleration

## Neural Network Example

```python
import torch
import torch.nn as nn
import torch.optim as optim
from cuda_tools import cuda_advanced
from cuda_tools.context import DeviceContext

class MLP(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(dim, 128), nn.ReLU(),
            nn.Linear(128, 10)
        )
    def forward(self, x): return self.net(x)

@cuda_advanced(use_amp=True, retry=1, telemetry=True, verbose=True)
def train_step(model, x, y, loss_fn, opt):
    opt.zero_grad()
    pred = model(x)
    loss = loss_fn(pred, y)
    loss.backward()
    opt.step()
    return loss.item()

with DeviceContext(device='cuda', auto_tensorize=True):
    model = MLP(20).to('cuda')
    opt = optim.SGD(model.parameters(), lr=1e-3)
    loss_fn = nn.CrossEntropyLoss()
    x = torch.randn(32, 20, device='cuda')
    y = torch.randint(0, 10, (32,), device='cuda')

loss = train_step(model, x, y, loss_fn, opt)
print("Loss:", loss)
```

## Benchmark and Profiling

```python
import time
import torch
from cuda_tools import cuda

@cuda(device="cpu")
def cpu_op(x): return x * x
@cuda(device="cuda")
def gpu_op(x): return x * x

x_cpu = torch.randn(1000,1000)
t0 = time.time(); cpu_op(x_cpu); print("CPU:", time.time()-t0)
x_gpu = x_cpu.to('cuda')
t0 = time.time(); gpu_op(x_gpu); print("GPU:", time.time()-t0)
```

## Caveats
- Avoid sending tiny scalar ops to GPU (overhead)  
- If `to_list=True`, result will be Python-native (no `.device`)  
- `min_free_vram` too high = RuntimeError  
- For TensorFlow warnings:
  ```python
  import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
  ```

## License
MIT License © 2025  
See `LICENSE` file for details
