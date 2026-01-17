import statsmodels.formula.api as smf


def H4_informality_response(df, policy_time):
    """
    H4: Does minimum wage policy induce transitions into informality?
    """
    df = df.sort_values(["id", "time"]).copy()

    df["formal_lag"] = df.groupby("id")["formal"].shift(1)
    df["to_informal"] = (
        (df["formal_lag"] == 1) & (df["formal"] == 0)
    ).astype(int)

    df["post"] = (df["time"] >= policy_time).astype(int)
    df["treated"] = (
        df["mw"] >
        df.groupby("region")["mw"].transform("median")
    ).astype(int)

    model = smf.ols(
        "to_informal ~ treated*post + C(id) + C(time)",
        data=df.dropna()
    ).fit(
        cov_type="cluster",
        cov_kwds={"groups": df.dropna()["region"]}
    )

    return model