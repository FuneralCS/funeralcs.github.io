---
title: "Resmi Cuda Tools Dökümantasyonu"
date: 2025-04-29 11:06:00 +0300
categories: [genel, python, cudatools]
tags: [python, cuda tools, döküman, kütüphane]
author: tunahan
image:
  path: /assets/img/cudatools.png
  alt: Cuda Tools
description: "Python Cuda Tools modülünün dökümanı"
toc: true
math: false
mermaid: false
comments: true
pin: true
---
# universal-cuda-tools Resmi Dokümantasyonu

## İçindekiler
1. [Genel Bakış](#genel-bakış)
2. [Kurulum](#kurulum)
3. [Temel Kavramlar](#temel-kavramlar)
4. [`@cuda` Dekoratörü](#cuda-dekoratörü)
   - İmza ve Parametreler
   - Davranış
   - Örnek Kullanım
5. [`@cuda_advanced` Dekoratörü](#cuda_advanced-dekoratörü)
   - İmza ve Parametreler
   - Gelişmiş Özellikler
   - Örnek Kullanım
6. [`DeviceContext` Context Manager](#devicecontext-context-manager)
   - İmza ve Parametreler
   - Otomatik Tensorize
   - AMP Entegrasyonu
   - Örnek Kullanım
7. [Yardımcı Fonksiyonlar (`utils.py`)](#yardımcı-fonksiyonlar-utilspy)
   - `tensorize_for_universal`
   - `move_to_torch`
   - `patch_numpy_with_cupy`
8. [Sinir Ağı Örneği](#sinir-ağı-örneği)
9. [Benchmark ve Profiling](#benchmark-ve-profiling)
10. [Dikkat Edilmesi Gerekenler](#dikkat-edilmesi-gerekenler)
11. [SSS](#sss)
12. [Lisans](#lisans)

## Genel Bakış
`universal-cuda-tools`, PyTorch ve isteğe bağlı TensorFlow ile entegre çalışan,
saf Python, NumPy ve CuPy verilerini otomatik tensorize ederek GPU/CPU arasında
taşımayı, mixed precision (AMP), timeout, retry, VRAM kontrolü, memory profiling,
live dashboard ve dry-run gibi zengin özellikleri tek bir pakette sunan araç
setidir.

### Öne Çıkan Özellikler
- **`@cuda`**: Hafif, hızlı GPU/CPU cihaz yönetimi, auto-tensorize, retry ve fallback.
- **`@cuda_advanced`**: Tam özellikli; timeout, AMP, multi-GPU, error_callback,
  telemetry, live_dashboard, dry_run.
- **`DeviceContext`**: Blok içi cihaz & AMP & auto-tensorize kontrolü.
- **utils**: `tensorize_for_universal`, `move_to_torch`, `patch_numpy_with_cupy`.

## Kurulum
```bash
pip install universal-cuda-tools
```
veya kaynak koddan:
```bash
git clone https://github.com/username/cuda-tools.git
cd cuda-tools
python -m build
pip install dist/universal_cuda_tools-<versiyon>.whl
```

## Temel Kavramlar
1. **Device** (`cpu`, `cuda`, `cuda:0` vb.)  
2. **Tensorize**: Saf Python/NumPy verilerini `torch.Tensor` haline getirme.  
3. **Auto-tensorize**: Dekoratör veya context kullanarak otomatik dönüşüm.  
4. **OOM Fallback**: GPU bellek yetersizse CPU’ya geri dönme.  
5. **Mixed Precision (AMP)**: `torch.autocast` ile FP16 hızlandırma.  

## `@cuda` Dekoratörü

### İmza ve Parametreler
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
- **`device`** (`str`): `'cuda'`, `'cuda:0'`, `'cpu'` veya `None` (otomatik).
- **`verbose`** (`bool`): Log satırlarını `INFO` seviyesinde basar.
- **`clear_cache`** (`bool`): Her çağrı öncesi `torch.cuda.empty_cache()`.
- **`retry`** (`int`): Hata alındığında tekrar deneme sayısı.
- **`min_free_vram`** (`float`): GB cinsinden minimum boş VRAM eşiği, altında `RuntimeError`.
- **`auto_tensorize`** (`bool`): Saf Python veya NumPy verilerini `torch.Tensor(device)`.
- **`to_list`** (`bool`): `torch.Tensor` çıktısını Python listesine dönüştürür.

### Davranış
1. Argümanları auto_tensorize ile tensora çevirir (isteğe bağlı).  
2. Tensor/NumPy → hedef cihaza (`device`) taşır.  
3. Fonksiyonu çağırır; hata alırsa **retry** sayısınca dener.  
4. Hala `out of memory` hatası varsa ve GPU’da ise **CPU fallback**.  
5. İşlem sonrası bellek değişimini loglar (verbose).  
6. `to_list` ise sonucu listeye çevirir.

### Örnek Kullanım
```python
from cuda_tools import cuda
import numpy as np

@cuda(device="cuda", auto_tensorize=True, to_list=True, verbose=True)
def vector_add(a, b):
    return a + b

result = vector_add([1,2,3], np.array([4,5,6]))
print(result)  # [5,7,9]
```

## `@cuda_advanced` Dekoratörü

### İmza ve Parametreler
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
- **`timeout`** (`float`): Fonksiyon zaman aşımı (saniye).  
- **`use_amp`** (`bool`): `torch.autocast` ile mixed precision.  
- **`mgpu`** (`bool`): Birden fazla GPU varsa en az kullanılanı seçer.  
- **`error_callback`** (`callable`): Hata yakalandığında çağrılır.  
- **`telemetry`** (`bool`): Zaman ve cihaz bilgisi loglanır.  
- **`memory_profiler`** (`bool`): Bellek değişimi loglanır.  
- **`live_dashboard`** (`bool`): Çağrı sayısı & toplam süre metrikleri loglanır.  
- **`dry_run`** (`bool`): Fonksiyonu atlar, sadece log tutar.  

### Gelişmiş Özellikler
- Timeout gerçekleşirse `TimeoutError`.  
- AMP ile eğitim/inference hızlandırma.  
- multi-GPU desteği.  
- Hata anında callback & erken çıkış.  
- dry_run ile yan etkisiz test.  

### Örnek Kullanım
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

### İmza ve Parametreler
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
- **`device`** (`str`): `'cuda'` veya `'cpu'`.  
- **`use_amp`** (`bool`): Mixed precision.  
- **`verbose`** (`bool`): Log satırları.  
- **`auto_tensorize`** (`bool`): Blok içindeki Python/NumPy verilerini
  otomatik `torch.Tensor` haline çevirir.

### Kullanım
```python
from cuda_tools.context import DeviceContext
import numpy as np

with DeviceContext(device='cuda', auto_tensorize=True, use_amp=True, verbose=True) as dev:
    a = tensorize_for_universal(5, dev)
    b = tensorize_for_universal(np.array([1,2,3]), dev)
    print(a + b, (a+b).device)
```

## Yardımcı Fonksiyonlar (`utils.py`)

### `tensorize_for_universal(obj, device)`
Saf Python verilerini (`int`, `float`),
NumPy scalars (`np.integer`, `np.floating`),
`list`, `tuple`, `np.ndarray`, `torch.Tensor`, `tf.Tensor`
→ `torch.Tensor(device)`.

### `move_to_torch(device, obj)`
`np.ndarray`, `torch.Tensor` → hedef cihaza taşır.

### `patch_numpy_with_cupy()`
NumPy array tanımlarını CuPy array’e yönlendirir.

## Sinir Ağı Örneği

```python
import torch
import torch.nn as nn
import torch.optim as optim
from cuda_tools import cuda_advanced
from cuda_tools.context import DeviceContext

# Basit MLP
class MLP(nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(dim, 128), nn.ReLU(),
            nn.Linear(128, 10)
        )
    def forward(self, x): return self.net(x)

# Eğitim adımı
@cuda_advanced(use_amp=True, retry=1, telemetry=True, verbose=True)
def train_step(model, x, y, loss_fn, opt):
    opt.zero_grad()
    pred = model(x)
    loss = loss_fn(pred, y)
    loss.backward()
    opt.step()
    return loss.item()

# Veri ve cihaz hazırlığı
with DeviceContext(device='cuda', auto_tensorize=True):
    model = MLP(20).to('cuda')
    opt = optim.SGD(model.parameters(), lr=1e-3)
    loss_fn = nn.CrossEntropyLoss()
    x = torch.randn(32, 20, device='cuda')
    y = torch.randint(0, 10, (32,), device='cuda')

# Tek adım eğitim
loss = train_step(model, x, y, loss_fn, opt)
print("Loss:", loss)
```

## Benchmark ve Profiling

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

## Dikkat Edilmesi Gerekenler
- Küçük scalar işlemleri GPU’ya göndermek overheadlidir.  
- `to_list=True` sonrası sonuç Python tipi olur, `.device` yoktur.  
- `min_free_vram` çok yüksek ayarlanırsa hata alırsınız.  
- TensorFlow uyarıları için:
  ```python
  import os; os.environ['TF_CPP_MIN_LOG_LEVEL']='3'
  ```

## SSS
**S: NumPy scalar nasıl tensorize edilir?**  
**C:** `auto_tensorize=True` veya `DeviceContext` ile otomatik.  

**S: dry_run nasıl çalışır?**  
**C:** `@cuda_advanced(dry_run=True)` ile fonksiyon atlanır, `None` döner.  

## Lisans
MIT License © 2025  
Detaylar için `LICENSE` dosyasına bakınız.  
