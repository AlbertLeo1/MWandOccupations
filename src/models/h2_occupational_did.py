import statsmodels.formula.api as smf


def H2_occupational_DiD(df, policy_time):
    """
    H2: Do minimum wage changes induce occupational transitions?
    """
    df = df.sort_values(["id", "time"]).copy()

    df["occ_lag"] = df.groupby("id")["occupation"].shift(1)
    df["switch_occ"] = (df["occupation"] != df["occ_lag"]).astype(int)

    df["post"] = (df["time"] >= policy_time).astype(int)
    df["treated"] = (
        df["mw"] >
        df.groupby("region")["mw"].transform("median")
    ).astype(int)

    model = smf.ols(
        "switch_occ ~ treated*post + C(id) + C(time)",
        data=df.dropna()
    ).fit(
        cov_type="cluster",
        cov_kwds={"groups": df.dropna()["region"]}
    )

    return model