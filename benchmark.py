import csv
import statistics
import time

from algorithms import (
    two_pointers,
    binary_search,
    exponential_search,
    double_binary_search,
)

ALGOS = {
    "two_pointers": two_pointers,
    "binary_search": binary_search,
    "exponential_search": exponential_search,
    "double_binary": double_binary_search,
}


def gen_worst(m: int, n: int):
    assert m <= n
    a = [2 * i + 1 for i in range(m)]
    b = [2 * i for i in range(n)]
    
    if m > 0:
        a[-1] = b[-1] + 1
        
    return a, b


def bench(fn, a, b, repeats=7):
    times = []
    for _ in range(repeats):
        t0 = time.perf_counter_ns()
        res = fn(a, b)
        t1 = time.perf_counter_ns()
        assert res is False
        times.append((t1 - t0) / 1_000_000)
    return statistics.median(times)


def main():
    sizes_n = [100, 300, 1_000, 3_000, 10_000, 30_000,
               100_000, 300_000, 1_000_000]
    ratios = [1, 10, 100]  # M = N // ratio

    rows = []
    for n in sizes_n:
        for ratio in ratios:
            m = max(1, n // ratio)
            a, b = gen_worst(m, n)
            for name, fn in ALGOS.items():
                t_ms = bench(fn, a, b)
                rows.append({
                    "algorithm": name,
                    "M": m, "N": n, "ratio": ratio,
                    "time_ms": t_ms,
                })
                print(f"{name:15s} M={m:7d} N={n:7d} ratio={ratio:3d} "
                      f"time={t_ms:.6f} ms")

    with open("benchmark_results.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f, fieldnames=["algorithm", "M", "N", "ratio", "time_ms"]
        )
        w.writeheader()
        w.writerows(rows)

    print("\nSaved to benchmark_results.csv")


if __name__ == "__main__":
    main()
