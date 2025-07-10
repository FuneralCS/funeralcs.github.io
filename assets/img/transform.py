from pathlib import Path
from PIL import Image
import os

root_dir = Path("/home/tunahan/Masaüstü/funeralcs.github.io/assets/img/")

image_exts = [".png", ".jpg", ".jpeg"]

for img_path in root_dir.rglob("*"):
    if img_path.suffix.lower() in image_exts:
        try:
            with Image.open(img_path) as im:
                webp_path = img_path.with_suffix(".webp")
                im.save(webp_path, "WEBP", quality=90)
                print(f"[✓] {img_path} → {webp_path}")
                img_path.unlink()  
        except Exception as e:
            print(f"[!] Hata: {img_path} → {e}")
