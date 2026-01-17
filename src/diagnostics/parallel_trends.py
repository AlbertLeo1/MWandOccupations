import statsmodels.formula.api as smf
import pandas as pd
import matplotlib.pyplot as plt
import os

def parallel_trends_check(
    df,
    outcome,
    policy_time,
    unit_fe="id",
    time_fe="time",
    cluster="region",
    pre_window=None
):
    """
    Check parallel trends for DiD and extract pre-treatment coefficients.

    Returns:
        model : statsmodels regression result
        pre_coeffs : pd.DataFrame with term, coef, std_err
    """
    df = df.copy()

    # Restrict to pre-policy
    df = df[df[time_fe] < policy_time]

    if pre_window is not None:
        df = df[(df[time_fe] >= pre_window[0]) & (df[time_fe] <= pre_window[1])]

    # Treatment indicator
    df["treated"] = (
        df["mw"] > df.groupby("region")["mw"].transform("median")
    ).astype(int)

    # Time factor for interaction
    df["time_factor"] = df[time_fe].astype("category")

    formula = f"{outcome} ~ treated*C(time_factor) + C({unit_fe}) + C({time_fe})"

    model = smf.ols(formula, data=df.dropna()).fit(
        cov_type="cluster",
        cov_kwds={"groups": df.dropna()[cluster]}
    )

    # Extract treated × time coefficients
    pre_coeffs = model.params.filter(like="treated").reset_index()
    pre_coeffs.columns = ["term", "coef"]

    # Extract standard errors
    se = model.bse.filter(like="treated").reset_index(drop=True)
    pre_coeffs["std_err"] = se

    return model, pre_coeffs


def plot_parallel_trends(pre_coeffs, save_path=None):
    """
    Plot pre-trend coefficients with 95% confidence intervals.

    Parameters
    ----------
    pre_coeffs : pd.DataFrame
        Columns: term, coef, std_err
    save_path : str or None
        Path to save figure. If None, figure is shown but not saved.
    """
    # Sort by term
    pre_coeffs = pre_coeffs.copy()
    pre_coeffs = pre_coeffs.sort_values("term").reset_index(drop=True)

    x = range(len(pre_coeffs))
    y = pre_coeffs["coef"]
    ci = 1.96 * pre_coeffs["std_err"]

    plt.figure(figsize=(7,4))
    plt.errorbar(x, y, yerr=ci, fmt='o-', color='blue', label='Treated × time')
    plt.axhline(0, color='red', linestyle='--', label='Baseline (0)')
    plt.xticks(x, pre_coeffs["term"], rotation=45, ha="right")
    plt.xlabel("Pre-policy periods (treated × time)")
    plt.ylabel("Coefficient")
    plt.title("Parallel Trends Check")
    plt.legend()
    plt.tight_layout()

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300)
        plt.close()
    else:
        plt.show()
