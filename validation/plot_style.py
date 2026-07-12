






from __future__ import annotations

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import AutoMinorLocator





mpl.rcParams.update({


    "font.family": "serif",
    "font.serif": [
        "Times New Roman",
        "Times",
        "Nimbus Roman",
        "DejaVu Serif"
    ],

    "mathtext.fontset": "stix",

    "font.size": 12,

    "axes.titlesize": 15,

    "axes.labelsize": 13,

    "legend.fontsize": 11,

    "xtick.labelsize": 11,

    "ytick.labelsize": 11,



    "figure.figsize": (7.2,5.2),

    "figure.dpi": 150,

    "savefig.dpi": 600,

    "savefig.bbox": "tight",

    "savefig.pad_inches": 0.05,



    "axes.linewidth": 1.4,

    "axes.edgecolor": "#222222",

    "axes.facecolor": "white",

    "axes.grid": False,



    "xtick.direction": "in",

    "ytick.direction": "in",

    "xtick.major.size": 5,

    "ytick.major.size": 5,

    "xtick.minor.size": 3,

    "ytick.minor.size": 3,



    "legend.frameon": True,

    "legend.framealpha": 0.95,

    "legend.edgecolor": "#BBBBBB",

    "legend.fancybox": True

})





COLORS = {

    "blue": "#3366CC",

    "green": "#109618",

    "orange": "#FF9900",

    "red": "#DC3912",

    "purple": "#990099",

    "grey": "#666666",

    "lightgrey": "#DDDDDD",

    "black": "#222222"

}





BETA_CMAP = plt.cm.viridis





def marker_size(N):








    if N <= 100:
        return 70

    elif N <= 200:
        return 90

    elif N <= 500:
        return 120

    elif N <= 1000:
        return 150

    else:
        return 180






def publication_axes(ax):






    ax.tick_params(

        which="major",

        direction="in",

        length=6,

        width=1.2,

        top=True,

        right=True

    )

    ax.tick_params(

        which="minor",

        direction="in",

        length=3,

        width=1.0,

        top=True,

        right=True

    )

    ax.xaxis.set_minor_locator(

        AutoMinorLocator()

    )

    ax.yaxis.set_minor_locator(

        AutoMinorLocator()

    )

    for spine in ax.spines.values():

        spine.set_linewidth(1.3)

        spine.set_color("#222222")






def add_grid(ax):







    ax.grid(

        True,

        linestyle="--",

        linewidth=0.5,

        alpha=0.20

    )






def panel_label(ax, label):











    ax.text(

        -0.12,

        1.04,

        label,

        transform=ax.transAxes,

        fontsize=15,

        fontweight="bold"

    )






def statistics_box(ax, text):

    ax.text(

        0.03,

        0.97,

        text,

        transform=ax.transAxes,

        va="top",

        fontsize=10,

        bbox=dict(

            facecolor="white",

            edgecolor="#BBBBBB",

            boxstyle="round",

            alpha=0.92

        )

    )






def save_figure(fig, filename):

    fig.tight_layout()

    fig.savefig(

        filename + ".png",

        dpi=600

    )

    fig.savefig(

        filename + ".pdf"

    )






def phase_transition(ax, beta_star=1.3):









    xmin, xmax = ax.get_xlim()

    ymin, ymax = ax.get_ylim()

    ax.axvline(

        beta_star,

        color=COLORS["red"],

        linestyle="--",

        linewidth=2.0,

        alpha=0.85

    )

    ax.axvspan(

        xmin,

        beta_star,

        color="#DFF5E3",

        alpha=0.25

    )

    ax.axvspan(

        beta_star,

        xmax,

        color="#FFE6E6",

        alpha=0.18

    )

    ax.text(

        beta_star-0.05,

        ymax*0.98,

        "Recoverable",

        ha="right",

        va="top",

        fontsize=10,

        color="#1A7F37"

    )

    ax.text(

        beta_star+0.05,

        ymax*0.98,

        "Condensed",

        ha="left",

        va="top",

        fontsize=10,

        color="#B22222"

    )
