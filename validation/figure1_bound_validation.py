












from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

from ba.validation.plot_style import *
from ba.validation.utils import *
from statistics import *





def create_bound_validation_figure(df,
                                   output_folder="validation_figures"):

    Path(output_folder).mkdir(
        exist_ok=True
    )

    fig, ax = plt.subplots(
        figsize=(7.8,6)
    )

    publication_axes(ax)

    add_grid(ax)

    panel_label(ax,"(A)")

    stats = bound_validation(df)





    betas = beta_values(df)

    for beta in betas:

        sub = df[
            df["beta"] == beta
        ].copy()

        sub = sub.sort_values("n")

        colour = beta_colour(beta)

        x = sub["bound"].values

        y = sub["tau"].values





        if len(x) >= 4:

            xs, ys = smooth_curve(
                x,
                y,
                points=300
            )

            ax.plot(
                xs,
                ys,
                lw=2.4,
                color=colour,
                alpha=0.90
            )

        else:

            ax.plot(
                x,
                y,
                lw=2.4,
                color=colour
            )





        for _, row in sub.iterrows():

            ax.scatter(
                row["bound"],
                row["tau"],

                s=marker_size(
                    row["n"]
                ),

                color=colour,

                alpha=marker_alpha(
                    row["n"]
                ),

                edgecolor="black",

                linewidth=0.7,

                zorder=5
            )













    x = df["bound"].values

    y = df["tau"].values

    xs = np.linspace(
        x.min(),
        x.max(),
        300
    )

    slope = stats["slope"]

    intercept = stats["intercept"]

    prediction = slope*xs + intercept

    lower, upper = confidence_band(
        prediction,
        width=0.03
    )

    ax.fill_between(

        xs,

        lower,

        upper,

        color="grey",

        alpha=0.15,

        zorder=1

    )

    ax.plot(

        xs,

        prediction,

        "--",

        color="black",

        lw=2.4,

        label="Linear trend"

    )





    diagonal = np.linspace(
        x.min(),
        x.max(),
        100
    )

    ax.plot(

        diagonal,

        diagonal,

        color="darkred",

        linestyle=":",

        linewidth=2,

        alpha=0.65,

        label=r"$\tau = 1-C(G_N)$"

    )





    statistics_box(

        ax,

        "\n".join([

        rf"Pearson $r$ = {stats['pearson']:.3f}",

        rf"Spearman $\rho$ = {stats['spearman']:.3f}",

        rf"$R^2$ = {stats['r2']:.3f}",

        rf"RMSE = {stats['rmse']:.3f}"

        ]),

    )





    ax.set_xlabel(

        r"Theoretical Recoverability Bound"

        "\n"

        r"$1-C(G_N)$"

    )

    ax.set_ylabel(

        r"Observed Reconstruction"

        "\n"

        r"$\tau$"

    )

    ax.set_title(

        "Validation of the Information-Theoretic Recoverability Bound",

        pad=14

    )





    from matplotlib.lines import Line2D

    legend = [

        Line2D(

            [0],[0],

            color="black",

            lw=2.4,

            linestyle="--",

            label="Regression"

        ),

        Line2D(

            [0],[0],

            color="darkred",

            lw=2,

            linestyle=":",

            label=r"$\tau=1-C(G_N)$"

        )

    ]

    ax.legend(

        handles=legend,

        loc="lower right"

    )





    ax.set_xlim(

        x.min()-0.02,

        x.max()+0.02

    )

    ax.set_ylim(

        min(y)-0.08,

        max(y)+0.08

    )





    save_figure(

        fig,

        str(

            Path(output_folder)

            /

            "Figure1_BoundValidation"

        )

    )

    plt.close(fig)

    print(

        "Figure 1 saved."

    )






if __name__ == "__main__":

    df = load_data(

        "condensed_regime.csv"

    )

    create_bound_validation_figure(df)
