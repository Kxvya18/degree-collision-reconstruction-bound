





from __future__ import annotations

import numpy as np
import pandas as pd

from scipy.stats import (
    pearsonr,
    spearmanr,
    linregress
)

from sklearn.metrics import (
    r2_score,
    mean_squared_error,
    mean_absolute_error
)





def linear_regression(x, y):











    result = linregress(x, y)

    fitted = result.slope * np.asarray(x) + result.intercept

    return {

        "slope": result.slope,

        "intercept": result.intercept,

        "fitted": fitted,

        "r_value": result.rvalue,

        "p_value": result.pvalue,

        "stderr": result.stderr

    }






def validation_statistics(x, y):

    reg = linear_regression(x, y)

    fitted = reg["fitted"]

    pearson, p1 = pearsonr(x, y)

    spearman, p2 = spearmanr(x, y)

    r2 = r2_score(y, fitted)

    rmse = np.sqrt(

        mean_squared_error(

            y,

            fitted

        )

    )

    mae = mean_absolute_error(

        y,

        fitted

    )

    return {

        "pearson": pearson,

        "pearson_p": p1,

        "spearman": spearman,

        "spearman_p": p2,

        "r2": r2,

        "rmse": rmse,

        "mae": mae,

        "slope": reg["slope"],

        "intercept": reg["intercept"],

        "prediction": fitted

    }






def bound_validation(df):








    return validation_statistics(

        df["bound"],

        df["tau"]

    )






def collision_validation(df):










    return validation_statistics(

        df["c_empirical"],

        df["tau"]

    )






def theory_validation(df):

    return validation_statistics(

        df["c_theory"],

        df["c_empirical"]

    )






def efficiency_statistics(df):

    return {

        "mean":

            df["efficiency"].mean(),

        "median":

            df["efficiency"].median(),

        "std":

            df["efficiency"].std(),

        "minimum":

            df["efficiency"].min(),

        "maximum":

            df["efficiency"].max()

    }






def convergence_statistics(df):

    err = df["c_convergence_error"]

    return {

        "mean":

            err.mean(),

        "median":

            err.median(),

        "maximum":

            err.max(),

        "minimum":

            err.min(),

        "std":

            err.std()

    }






def mle_statistics(df):

    bias = df["mle_bias"]

    return {

        "mean":

            bias.mean(),

        "median":

            bias.median(),

        "std":

            bias.std(),

        "maximum":

            bias.max(),

        "minimum":

            bias.min()

    }






def validation_table(df):

    bound = bound_validation(df)

    collision = collision_validation(df)

    theory = theory_validation(df)

    efficiency = efficiency_statistics(df)

    convergence = convergence_statistics(df)

    mle = mle_statistics(df)

    rows = [

        ("Pearson(bound,tau)",
            bound["pearson"]),

        ("Spearman(bound,tau)",
            bound["spearman"]),

        ("R²(bound,tau)",
            bound["r2"]),

        ("RMSE(bound,tau)",
            bound["rmse"]),

        ("MAE(bound,tau)",
            bound["mae"]),

        ("Pearson(C,tau)",
            collision["pearson"]),

        ("Spearman(C,tau)",
            collision["spearman"]),

        ("R²(C,tau)",
            collision["r2"]),

        ("RMSE(C,tau)",
            collision["rmse"]),

        ("Pearson(theory,empirical)",
            theory["pearson"]),

        ("Spearman(theory,empirical)",
            theory["spearman"]),

        ("Mean efficiency",
            efficiency["mean"]),

        ("Efficiency std",
            efficiency["std"]),

        ("Mean convergence error",
            convergence["mean"]),

        ("Maximum convergence error",
            convergence["maximum"]),

        ("Mean MLE bias",
            mle["mean"]),

        ("MLE bias std",
            mle["std"])

    ]

    return pd.DataFrame(

        rows,

        columns=[

            "Metric",

            "Value"

        ]

    )






def publication_summary(df):

    bound = bound_validation(df)

    collision = collision_validation(df)

    theory = theory_validation(df)

    efficiency = efficiency_statistics(df)

    convergence = convergence_statistics(df)

    return {

        "Pearson(bound,tau)":

            bound["pearson"],

        "Spearman(bound,tau)":

            bound["spearman"],

        "R2(bound,tau)":

            bound["r2"],

        "RMSE(bound,tau)":

            bound["rmse"],

        "Pearson(C,tau)":

            collision["pearson"],

        "Spearman(C,tau)":

            collision["spearman"],

        "Pearson(theory,empirical)":

            theory["pearson"],

        "Mean efficiency":

            efficiency["mean"],

        "Mean convergence error":

            convergence["mean"],

        "Regression slope":

            bound["slope"],

        "Regression intercept":

            bound["intercept"]

    }
