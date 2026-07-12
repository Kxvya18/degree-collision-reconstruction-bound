




import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.stats import gaussian_kde
from ba.validation.plot_style import *
from ba.validation.utils import *
from statistics import *

def create_collision_tau(df,output_folder="validation_figures"):

    Path(output_folder).mkdir(exist_ok=True)

    fig,ax=plt.subplots(figsize=(7.8,5.8))
    publication_axes(ax)
    add_grid(ax)
    panel_label(ax,"(C)")

    x=df["c_empirical"].values
    y=df["tau"].values
    n=df["n"].values



    xy=np.vstack([x,y])
    density=gaussian_kde(xy)(xy)
    order=density.argsort()

    x=x[order]
    y=y[order]
    density=density[order]
    n=n[order]

    sizes=np.array([marker_size(i) for i in n])

    sc=ax.scatter(
        x,y,
        c=density,
        cmap="viridis",
        s=sizes,
        edgecolor="white",
        linewidth=.45,
        alpha=.92,
        zorder=5
    )



    stats=collision_validation(df)

    xx=np.linspace(x.min(),x.max(),400)
    yy=stats["slope"]*xx+stats["intercept"]

    ax.plot(xx,yy,
            color="black",
            lw=2.8,
            label="Regression")

    band=.035
    ax.fill_between(xx,
                    yy-band,
                    yy+band,
                    color="black",
                    alpha=.10)



    idx=np.argmax(y)

    ax.annotate(
        r"Higher collision $\rightarrow$ lower recoverability",
        xy=(x[idx], y[idx]),
        xytext=(0.98, 0.08),
        textcoords="axes fraction",
        ha="right",
        va="bottom",
        fontsize=10,
        arrowprops=dict(
            arrowstyle="->",
            lw=1.5,
            color="black"
        ),
        bbox=dict(
            facecolor="white",
            edgecolor="0.7",
            boxstyle="square,pad=0.35",
            alpha=0.95
        )
    )


























    cbar=plt.colorbar(sc,pad=.02)
    cbar.set_label("Point Density")



    ax.set_xlabel(r"Collision Probability $C(G_N)$")
    ax.set_ylabel(r"Observed Recoverability $\tau$")
    ax.set_title("Collision Probability Predicts Reconstruction Performance",pad=12)



    ax.set_xlim(x.min()-.03,x.max()+.03)
    ax.set_ylim(y.min()-.08,y.max()+.08)

    save_figure(fig,str(Path(output_folder)/"Figure3_CollisionVsTau"))
    plt.close(fig)
    print("Figure 3 saved.")

if __name__=="__main__":
    df=load_data("condensed_regime.csv")
    create_collision_tau(df)
