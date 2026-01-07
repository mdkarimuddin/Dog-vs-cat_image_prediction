import importlib
reqs = ["mxnet","numpy","cv2","matplotlib"]
for r in reqs:
    try:
        importlib.import_module(r)
        print(f"OK: {r}")
    except Exception as e:
        print(f"MISSING: {r} -> {e}")

import os
print("data/dogs-vs-cats/train/train present:", os.path.exists('data/dogs-vs-cats/train/train'))
