


















from pathlib import Path

from ba.validation.utils import (
    load_data,
    make_output_directory,
    save_dataframe,
    save_summary
)

from statistics import (
    validation_table,
    publication_summary
)

from ba.validation.figure1_bound_validation import (
    create_bound_validation_figure
)

from ba.validation.figure2_collision_beta import (
    create_collision_beta
)

from ba.validation.figure3_collision_tau import (
    create_collision_tau
)

from ba.validation.figure4_heatmap import (
    create_heatmap
)






CSV_FILE = "condensed_regime_results.csv"

OUTPUT_FOLDER = "validation_figures"






def banner():

    print()

    print("="*70)

    print(" Recoverability Validation")

    print("="*70)

    print()

    print("Input CSV :",CSV_FILE)

    print("Output    :",OUTPUT_FOLDER)

    print()






def main():

    banner()

    Path(OUTPUT_FOLDER).mkdir(

        exist_ok=True

    )

    print("Loading dataset...")

    df = load_data(

        CSV_FILE

    )

    print()

    print(df.head())

    print()

    print("Number of experiments :",len(df))

    print("β values :",sorted(df.beta.unique()))

    print("N values :",sorted(df.n.unique()))

    print()

    print("="*70)

    print("Generating publication-quality figures")

    print("="*70)

    print()





    print("Figure 1 ...")

    create_bound_validation_figure(

        df,

        OUTPUT_FOLDER

    )





    print("Figure 2 ...")

    create_collision_beta(

        df,

        OUTPUT_FOLDER

    )





    print("Figure 3 ...")

    create_collision_tau(

        df,

        OUTPUT_FOLDER

    )





    print("Figure 4 ...")

    create_heatmap(

        df,

        OUTPUT_FOLDER

    )





    print()

    print("Saving statistics...")

    table = validation_table(

        df

    )

    save_dataframe(

        table,

        f"{OUTPUT_FOLDER}/validation_statistics.csv"

    )





    summary = publication_summary(

        df

    )

    save_summary(

        summary,

        f"{OUTPUT_FOLDER}/validation_summary.txt"

    )





    print()

    print("="*70)

    print("Validation Summary")

    print("="*70)

    print()

    for k,v in summary.items():

        if isinstance(v,float):

            print(f"{k:<35}{v:.4f}")

        else:

            print(f"{k:<35}{v}")

    print()

    print("="*70)

    print("Finished Successfully")

    print("="*70)

    print()

    print("Generated files")

    print()

    print(" validation_figures/")

    print("    Figure1_BoundValidation.png")

    print("    Figure1_BoundValidation.pdf")

    print()

    print("    Figure2_CollisionVsBeta.png")

    print("    Figure2_CollisionVsBeta.pdf")

    print()

    print("    Figure3_CollisionVsTau.png")

    print("    Figure3_CollisionVsTau.pdf")

    print()

    print("    Figure4_Heatmap.png")

    print("    Figure4_Heatmap.pdf")

    print()

    print("    validation_statistics.csv")

    print("    validation_summary.txt")

    print()

    print("="*70)






if __name__ == "__main__":

    main()
