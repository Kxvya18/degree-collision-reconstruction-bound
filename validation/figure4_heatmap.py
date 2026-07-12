




import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.ndimage import gaussian_filter
from ba.validation.plot_style import *
from ba.validation.utils import *

def create_heatmap(df,output_folder="validation_figures"):

    Path(output_folder).mkdir(exist_ok=True)

    pivot=df.pivot(index="beta",
                   columns="n",
                   values="c_convergence_error")

    betas=np.array(pivot.index)
    Ns=np.array(pivot.columns)

    Z=pivot.values

    fig,ax=plt.subplots(figsize=(7.4,5.8))

    publication_axes(ax)
    panel_label(ax,"(D)")



    im=ax.imshow(
        Z,
        cmap="RdYlGn_r",
        interpolation="nearest",
        aspect="equal",
        origin="upper"
    )



    smooth=gaussian_filter(Z,sigma=.8)

    ax.contour(
        smooth,
        levels=5,
        colors="white",
        linewidths=.8,
        alpha=.65
    )



    ax.set_xticks(np.arange(len(Ns)+1)-.5,minor=True)
    ax.set_yticks(np.arange(len(betas)+1)-.5,minor=True)

    ax.grid(which="minor",
            color="white",
            linewidth=1.2)

    ax.tick_params(which="minor",
                   bottom=False,
                   left=False)



    threshold=.5*(Z.max()+Z.min())

    for i in range(Z.shape[0]):
        for j in range(Z.shape[1]):

            value=Z[i,j]

            colour="white" if value>threshold else "black"

            ax.text(j,
                    i,
                    f"{value:.3f}",
                    ha="center",
                    va="center",
                    fontsize=9,
                    fontweight="bold",
                    color=colour)



    if 1.3 in betas:

        row=np.where(betas==1.3)[0][0]

        ax.hlines(
            row-.5,
            -.5,
            len(Ns)-.5,
            colors="crimson",
            linewidth=2.5,
            linestyles="--"
        )

        ax.text(
            len(Ns)-.15,
            row-.62,
            r"$\beta\approx1.3$",
            color="crimson",
            fontsize=10,
            ha="right",
            va="bottom"
        )



    ax.set_xticks(np.arange(len(Ns)))
    ax.set_xticklabels(Ns)

    ax.set_yticks(np.arange(len(betas)))
    ax.set_yticklabels([f"{b:.1f}" for b in betas])

    ax.set_xlabel(r"Network Size $N$")
    ax.set_ylabel(r"Attachment Exponent $\beta$")

    ax.set_title(
        "Theory–Simulation Convergence Error",
        pad=12
    )



    cbar=plt.colorbar(im,
                      fraction=.045,
                      pad=.04)

    cbar.set_label(
        r"$|C_{\rm theory}-C_{\rm empirical}|$",
        rotation=270,
        labelpad=18
    )



    ax.text(
        .99,
        -.16,
        "Lower values indicate stronger agreement between theory and simulation.",
        transform=ax.transAxes,
        ha="right",
        fontsize=9,
        color="dimgray"
    )

    save_figure(
        fig,
        str(Path(output_folder)/"Figure4_Heatmap")
    )

    plt.close(fig)

    print("Figure 4 saved.")


if __name__=="__main__":

    df=load_data("condensed_regime.csv")

    create_heatmap(df)
