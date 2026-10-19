"""Helper functions for the chilled-water pump selection notebook (synthetic data)."""
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")  # draw to file; the notebook still shows the saved figure
import matplotlib.pyplot as plt

COLOURS = {"A": "#0072B2", "B": "#009E73", "C": "#D55E00"}


def fit_all(df, degree=2):
    """Least-squares polynomial fit of head, efficiency and NPSHr against flow, per pump."""
    fits = {}
    for pump, g in df.groupby("pump"):
        fits[pump] = {
            "head": np.poly1d(np.polyfit(g.flow_Ls, g.head_m, degree)),
            "eff": np.poly1d(np.polyfit(g.flow_Ls, g.efficiency_pct, degree)),
            "npshr": np.poly1d(np.polyfit(g.flow_Ls, g.npshr_m, degree)),
        }
    return fits


def fit_report(df, fits):
    """Largest absolute fit error (data minus fit) for every pump and curve."""
    rows = []
    for pump, g in df.groupby("pump"):
        rows.append({
            "pump": pump,
            "head_m": float(np.abs(g.head_m - fits[pump]["head"](g.flow_Ls)).max()),
            "efficiency_pct": float(np.abs(g.efficiency_pct - fits[pump]["eff"](g.flow_Ls)).max()),
            "npshr_m": float(np.abs(g.npshr_m - fits[pump]["npshr"](g.flow_Ls)).max()),
        })
    return pd.DataFrame(rows).round(3)


def plot_operating_points(df, fits, system, op, path, passed=None):
    """Left: pump head curves and the system curve. Right: zoom on the operating points.
    Failed pumps are drawn as hollow markers."""
    fig, (ax, zx) = plt.subplots(1, 2, figsize=(10, 4.6), dpi=150, gridspec_kw={"width_ratios": [1.5, 1]})
    q = np.linspace(10, 80, 200)
    qz = np.linspace(49.4, 50.8, 100)
    ax.plot(q, system(q), color="#444444", lw=2.2, ls="--", label="System curve")
    zx.plot(qz, system(qz), color="#444444", lw=2.2, ls="--")
    for pump, f in fits.items():
        colour = COLOURS.get(pump, "#888888")
        ok = True if passed is None else bool(passed[pump])
        g = df[df.pump == pump]
        ax.plot(q, f["head"](q), color=colour, lw=2, label=f"Pump {pump}")
        ax.scatter(g.flow_Ls, g.head_m, s=14, color=colour, alpha=0.5)
        zx.plot(qz, f["head"](qz), color=colour, lw=2)
        zx.scatter([op[pump]], [f["head"](op[pump])], s=110, zorder=5,
                   facecolors=colour if ok else "white", edgecolors=colour, linewidths=2)
        zx.annotate(f"{pump}: {op[pump]:.2f} L/s, {f['head'](op[pump]):.2f} m" + ("" if ok else " (fails NPSH)"),
                    (op[pump], f["head"](op[pump])), textcoords="offset points",
                    xytext=(10, {"A": -22, "B": 4, "C": 16}.get(pump, 0)), fontsize=9, color=colour,
                    bbox=dict(fc="white", ec="none", alpha=0.85, pad=1))
    ax.add_patch(plt.Rectangle((49.4, 27.4), 1.4, 1.2, fill=False, ec="#444444", lw=1))
    ax.annotate("zoom", (50.1, 28.6), textcoords="offset points", xytext=(-4, 14), fontsize=9,
                ha="center", arrowprops=dict(arrowstyle="-", color="#444444"))
    ax.set_xlabel("Flow (L/s)", fontsize=10)
    ax.set_ylabel("Head (m)", fontsize=10)
    ax.set_title("Pump and system curves", fontsize=11)
    ax.set_xlim(10, 80)
    ax.set_ylim(0, 45)
    ax.grid(alpha=0.25)
    ax.legend(loc="upper right", frameon=False, fontsize=9)
    zx.set_xlim(49.4, 50.8)
    zx.set_ylim(27.4, 28.6)
    zx.set_xlabel("Flow (L/s)", fontsize=10)
    zx.set_title("Operating points (zoom)", fontsize=11)
    zx.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)
    return path
