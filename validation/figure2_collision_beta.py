




import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from ba.validation.plot_style import *
from ba.validation.utils import *

def create_collision_beta(df,output_folder="validation_figures"):

    Path(output_folder).mkdir(exist_ok=True)

    fig,ax=plt.subplots(figsize=(7.8,5.8))
    publication_axes(ax)
    add_grid(ax)
    panel_label(ax,"(B)")

    betas=np.sort(df.beta.unique())

    theory=df.groupby("beta")["c_theory"].mean().reindex(betas)

    theory_std=df.groupby("beta")["c_theory_std"].mean().reindex(betas)

    empirical=df.groupby("beta")["c_empirical"].mean().reindex(betas)

    empirical_std=df.groupby("beta")["c_empirical_std"].mean().reindex(betas)



    ax.axvspan(betas.min(),1.30,color="#DDF5DD",alpha=.30,zorder=0)
    ax.axvspan(1.30,betas.max(),color="#FBE2E2",alpha=.28,zorder=0)
    ax.axvline(1.30,color="crimson",ls="--",lw=2)

    ax.text(.90,0.94,"Recoverable",
            transform=ax.get_xaxis_transform(),
            ha="right",fontsize=10,color="#146B14")

    ax.text(1.34,0.94,"Condensed",
            transform=ax.get_xaxis_transform(),
            ha="left",fontsize=10,color="#8B0000")



    xs,ys=smooth_curve(betas,theory.values,300)

    ax.plot(xs,ys,
            lw=3,
            color=COLORS["blue"],
            label="Theory",
            zorder=3)

    ax.fill_between(xs,
                    np.interp(xs,betas,theory-theory_std),
                    np.interp(xs,betas,theory+theory_std),
                    color=COLORS["blue"],
                    alpha=.12)



    ax.errorbar(betas,
                empirical,
                yerr=empirical_std,
                fmt="o",
                ms=8,
                color=COLORS["orange"],
                mec="black",
                mew=.7,
                capsize=4,
                lw=1.5,
                label="Empirical",
                zorder=5)

    xs2,ys2=smooth_curve(betas,empirical.values,300)

    ax.plot(xs2,ys2,
            color=COLORS["orange"],
            lw=2.2,
            alpha=.85)



    for b,t,e in zip(betas,theory.values,empirical.values):
        ax.annotate("",
                    xy=(b,e),
                    xytext=(b,t),
                    arrowprops=dict(arrowstyle="-",
                                    lw=1,
                                    color="gray",
                                    alpha=.45))



    for b,e in zip(betas,empirical.values):
        ax.text(b,e+0.025,
                rf"$\beta={b:.1f}$",
                fontsize=8,
                ha="center")



    ax.set_xlim(betas.min()-.05,betas.max()+.05)
    ax.set_ylim(0,1.0)

    ax.set_xlabel(r"Inverse Temperature / Attachment Exponent $\beta$")
    ax.set_ylabel(r"Collision Probability $C(G_N)$")

    ax.set_title("Collision Probability Increases with Preferential Attachment Strength",pad=12)



    leg=ax.legend(loc="upper left",frameon=True)
    leg.get_frame().set_alpha(.95)



    ax.text(.98,.02,
            "Shaded regions indicate\nrecoverable and condensed regimes.",
            transform=ax.transAxes,
            ha="right",
            va="bottom",
            fontsize=9,
            bbox=dict(boxstyle="round",fc="white",ec="lightgray"))

    save_figure(fig,str(Path(output_folder)/"Figure2_CollisionVsBeta"))
    plt.close(fig)
    print("Figure 2 saved.")

if __name__=="__main__":
    df=load_data("condensed_regime.csv")
    create_collision_beta(df)
