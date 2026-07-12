





from __future__ import annotations

import os
import numpy as np
import pandas as pd

from scipy.stats import pearsonr
from scipy.stats import spearmanr

from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error

from scipy.interpolate import make_interp_spline





def load_data(csv_file):






    df = pd.read_csv(csv_file)

    df = df.sort_values(

        ["beta", "n"]

    ).reset_index(drop=True)

    return df






def make_output_directory(folder="validation_figures"):

    os.makedirs(folder, exist_ok=True)

    return folder






def linear_fit(x, y):

    slope, intercept = np.polyfit(

        x,

        y,

        1

    )

    prediction = slope * x + intercept

    return slope, intercept, prediction






from scipy.interpolate import make_interp_spline
import numpy as np

def smooth_curve(x,y,points=300):

    x=np.asarray(x)
    y=np.asarray(y)

    order=np.argsort(x)

    x=x[order]
    y=y[order]



    x_unique,index=np.unique(x,return_index=True)
    y_unique=y[index]



    if len(x_unique)<4:
        return x,y

    x_new=np.linspace(x_unique.min(),
                      x_unique.max(),
                      points)

    spline=make_interp_spline(
        x_unique,
        y_unique,
        k=3
    )

    y_new=spline(x_new)

    return x_new,y_new

import numpy as np

def confidence_band(y, width=0.03):



    y = np.asarray(y)
    return y - width, y + width





def regression_statistics(x, y):

    slope, intercept, prediction = linear_fit(

        x,

        y

    )

    pearson, _ = pearsonr(

        x,

        y

    )

    spearman, _ = spearmanr(

        x,

        y

    )

    r2 = r2_score(

        y,

        prediction

    )

    rmse = np.sqrt(

        mean_squared_error(

            y,

            prediction

        )

    )

    return {

        "pearson": pearson,

        "spearman": spearman,

        "r2": r2,

        "rmse": rmse,

        "slope": slope,

        "intercept": intercept,

        "prediction": prediction

    }






def marker_size(network_size):





    if network_size <= 100:

        return 80

    elif network_size <= 200:

        return 110

    elif network_size <= 500:

        return 145

    elif network_size <= 1000:

        return 180

    else:

        return 230






def marker_alpha(network_size):






    if network_size <= 100:

        return 0.75

    elif network_size <= 500:

        return 0.82

    else:

        return 0.90






def scientific(value):






    if abs(value) < 1e-3:

        return "{:.2e}".format(value)

    return "{:.4f}".format(value)






def save_dataframe(df, filename):

    df.to_csv(

        filename,

        index=False

    )






def save_summary(summary, filename):

    with open(filename, "w") as f:

        f.write("=" * 60 + "\n")

        f.write("RECOVERABILITY VALIDATION SUMMARY\n")

        f.write("=" * 60 + "\n\n")

        for key, value in summary.items():

            if isinstance(value, float):

                f.write(

                    f"{key:<35}"

                    f"{scientific(value)}\n"

                )

            else:

                f.write(

                    f"{key:<35}"

                    f"{value}\n"

                )






def beta_colour(beta):









    import matplotlib.pyplot as plt

    cmap = plt.cm.viridis

    beta_min = 0.5

    beta_max = 2.0

    t = (beta - beta_min) / (beta_max - beta_min)

    return cmap(t)






def caption(title):

    line = "=" * len(title)

    return f"\n{line}\n{title}\n{line}\n"






def phase(beta):

    if beta < 1.3:

        return "Recoverable"

    elif beta == 1.3:

        return "Transition"

    else:

        return "Condensed"






def beta_values(df):

    return sorted(

        df["beta"].unique()

    )






def network_sizes(df):

    return sorted(

        df["n"].unique()

    )
