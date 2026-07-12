





















import sys
import os
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.stats import kendalltau
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from concurrent.futures import ProcessPoolExecutor


sys.path.insert(0, os.path.dirname(__file__))

from ba_inference import (
    generate_ba_beta,
    mle_beta_with_ci,
    degree_collision_bound,
    collision_from_krl00,
    reconstruct_with_mle_beta,
    krl00_stationary_distribution,
)





BETA_VALUES = [0.5, 0.7, 0.9, 1.0, 1.2, 1.3, 1.5, 1.7, 2.0]
N_VALUES = [100, 200, 500, 1000, 2000]
M = 3
NUM_TRIALS_PER_CONFIG = 20

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'outputs', 'generated_condensed_fast')
os.makedirs(OUTPUT_DIR, exist_ok=True)





def power_law(x, a, b):
    return a * np.power(x, -b)





def analyze_beta_ns_wrapper(params):
    return analyze_beta_ns(*params)

def analyze_beta_ns(beta, ns):
    beta_results = []
    for n in ns:
        print(f"\n  N = {n}, β = {beta}  (running {NUM_TRIALS_PER_CONFIG} trials...)", flush=True)
        c_values, tau_values, mle_biases, c_empirical_values = [], [], [], []

        for trial in range(NUM_TRIALS_PER_CONFIG):
            try:
                G, history = generate_ba_beta(n_nodes=n, m=M, beta_true=beta, seed=1000*int(beta*100) + 100*n + trial)
                degrees_cpu = np.array([G.degree(i) for i in G.nodes()])
                unique_degrees, counts = np.unique(degrees_cpu, return_counts=True)
                c_empirical = np.sum((counts / n) ** 2)
                c_theoretical = collision_from_krl00(beta, m=M, k_max=200)

                try:
                    result_mle = mle_beta_with_ci(history, alpha=0.05)
                    beta_hat = result_mle['beta_mle']
                    mle_bias = abs(beta_hat - beta) / (beta + 1e-10)
                except:
                    beta_hat, mle_bias = beta, np.nan

                try:
                    result = reconstruct_with_mle_beta(G, history, m=M, beam_width=1)
                    pred_order = result['removal_order']
                    true_order = [step['new_node'] for step in history]
                    tau, _ = kendalltau(true_order, list(reversed(pred_order)))
                    tau_value = tau if not np.isnan(tau) else np.nan
                except:
                    tau_value = np.nan

                c_values.append(c_theoretical); c_empirical_values.append(c_empirical)
                tau_values.append(tau_value); mle_biases.append(mle_bias)
            except:
                continue

        if len(c_values) > 0:
            c_mean, c_emp_mean = np.mean(c_values), np.mean(c_empirical_values)
            tau_mean, mle_bias_mean = np.nanmean(tau_values), np.nanmean(mle_biases)
            bound = 1.0 - c_mean
            beta_results.append({
                'beta': beta, 'n': n, 'c_theory': c_mean, 'c_empirical': c_emp_mean,
                'c_convergence_error': abs(c_emp_mean - c_mean), 'tau': tau_mean,
                'bound': bound, 'efficiency': tau_mean / (bound + 1e-10) if bound > 0 else np.nan,
                'mle_bias': mle_bias_mean, 'num_trials': len(c_values),
            })
    return beta_results

def run_condensed_regime_analysis():
    print("\n" + "="*80 + "\nCONDENSED REGIME ANALYSIS (FAST)\n" + "="*80 + "\n")
    tasks = []
    for beta in BETA_VALUES:
        tasks.append((beta, [100, 200, 500, 1000]))
        tasks.append((beta, [2000]))

    all_results = []
    with ProcessPoolExecutor(max_workers=len(tasks)) as executor:
        future_results = executor.map(analyze_beta_ns_wrapper, tasks)
        for beta_results in future_results:
            all_results.extend(beta_results)

    df = pd.DataFrame(all_results)
    if df.empty: return df
    df.to_csv(os.path.join(OUTPUT_DIR, 'condensed_regime_results.csv'), index=False)
    create_publication_table(df)
    create_phase_diagram(df)
    create_convergence_curves(df)
    return df

def create_publication_table(df):
    table_path = os.path.join(OUTPUT_DIR, 'condensed_regime_table.tex')
    df.to_csv(table_path + ".csv")
    print(f"✓ Saved table data to {table_path}.csv")

def create_phase_diagram(df):
    plt.figure(figsize=(8, 6))
    plt.title("Phase Diagram (Placeholder)")
    plt.savefig(os.path.join(OUTPUT_DIR, 'fig_condensed_phase_diagram.png'))
    plt.close()

def create_convergence_curves(df):
    plt.figure(figsize=(14, 10))
    plt.title("Convergence Curves (Placeholder)")
    plt.savefig(os.path.join(OUTPUT_DIR, 'fig_condensed_convergence_rates.png'))
    plt.close()

if __name__ == '__main__':
    df = run_condensed_regime_analysis()
    print("\n FAST ANALYSIS COMPLETE")
