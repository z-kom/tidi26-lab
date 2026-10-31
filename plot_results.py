import csv
import matplotlib.pyplot as plt


def read_rows(path="benchmark_results.csv"):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row["M"] = int(row["M"])
            row["N"] = int(row["N"])
            row["ratio"] = int(row["ratio"])
            row["time_ms"] = float(row["time_ms"])
            rows.append(row)
    return rows


def main():
    rows = read_rows()

    plt.figure(figsize=(10, 7))
    for ratio in sorted({r["ratio"] for r in rows}):
        for alg in sorted({r["algorithm"] for r in rows}):
            data = [r for r in rows
                    if r["ratio"] == ratio and r["algorithm"] == alg]
            data.sort(key=lambda r: r["N"])
            plt.plot([r["N"] for r in data],
                     [r["time_ms"] for r in data],
                     marker="o", label=f"{alg}, M=N/{ratio}")
    plt.xscale("log"); plt.yscale("log")
    plt.xlabel("N"); plt.ylabel("Медианное время, мс")
    plt.title("Сравнение алгоритмов")
    plt.grid(True, which="both", linestyle=":")
    plt.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig("benchmark_all.png", dpi=200)
    plt.close()

    for ratio in sorted({r["ratio"] for r in rows}):
        plt.figure(figsize=(8, 5))
        for alg in sorted({r["algorithm"] for r in rows}):
            data = [r for r in rows
                    if r["ratio"] == ratio and r["algorithm"] == alg]
            data.sort(key=lambda r: r["N"])
            plt.plot([r["N"] for r in data],
                     [r["time_ms"] for r in data],
                     marker="o", label=alg)
        plt.xscale("log"); plt.yscale("log")
        plt.xlabel("N"); plt.ylabel("Медианное время, мс")
        plt.title(f"M = N/{ratio}")
        plt.grid(True, which="both", linestyle=":")
        plt.legend()
        plt.tight_layout()
        plt.savefig(f"benchmark_ratio_{ratio}.png", dpi=200)
        plt.close()

    print("Saved benchmark_all.png and benchmark_ratio_*.png")


if __name__ == "__main__":
    main()
