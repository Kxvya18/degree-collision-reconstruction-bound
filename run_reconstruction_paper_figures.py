from shared.ba_experiments_full import fig3_reconstruction, fig5_unified, run_finite_size_scaling


def main():
    out_dir = "outputs/generated"
    fig3_reconstruction(out_dir)
    fig5_unified(out_dir)
    run_finite_size_scaling(out_dir)


if __name__ == "__main__":
    main()
