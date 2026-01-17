import statsmodels.formula.api as smf


def H5_spillovers(df, policy_time):
    """
    H5: Are there wage spillovers to higher-paid workers?
    """
    df = df.copy()

    df["exposure"] = (
        df.groupby("occupation")["wage"]
          .transform(lambda x: (x <= 1.2 * df.loc[x.index, "mw"]).mean())
    )

    df["event_time"] = df["time"] - policy_time

    model = smf.ols(
        "wage ~ exposure*C(event_time) + C(occupation) + C(time)",
        data=df
    ).fit(
        cov_type="cluster",
        cov_kwds={"groups": df["region"]}
    )

    return model