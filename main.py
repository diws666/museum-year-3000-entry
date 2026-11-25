import os

LINE = "Plastic fork, c. 2025. Humans ate with four tiny spears and threw them away after one meal, then wondered where the turtles went."  # verified: 129 chars

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
out_path = os.path.join(out_dir, "entry.txt")

with open(out_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

print(len(LINE))
