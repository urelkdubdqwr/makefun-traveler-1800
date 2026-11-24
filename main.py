import os

TEXT = "Imagine every printing press on earth joined by one invisible thread: a page printed at dawn is read that hour in every town, and any reader may answer back along it.\n"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
