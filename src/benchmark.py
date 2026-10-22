import time
import json
from pathlib import Path

def calculate_accuracy(correct, total):
    return correct / total * 100

output = Path("data/raw/test_run.jsonl")
output.parent.mkdir(parents=True, exist_ok=True)

records = []

for i in range(120):
    phase = "warmup" if i < 20 else "benchmark"

    start = time.perf_counter_ns()

    result = calculate_accuracy(4, 5)

    end = time.perf_counter_ns()

    records.append({
        "run": i + 1,
        "phase": phase,
        "latency_ms": (end - start) / 1_000_000,
        "status": 200,
        "rps": 10,
        "accuracy": result
    })

with open(output, "w", encoding="utf-8") as file:
    for record in records:
        file.write(json.dumps(record) + "\n")

print(f"Saved {len(records)} measurements to {output}")
