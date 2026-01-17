import statsmodels.formula.api as smf
import pandas as pd


def event_study_pretrends(
    df,
    outcome,
    policy_time,
    unit_fe="id",
    time_fe="time",
    cluster="region",
    window=(-5, 5)
):
    """
    Generic event-study / pre-trend framework.

    Parameters
    ----------
    df : pandas.DataFrame
        Panel data
    outcome : str
        Outcome variable name
    policy_time : int
        Policy implementation time
    unit_fe : str
        Individual fixed effect
    time_fe : str
        Time fixed effect
    cluster : str
        Clustering variable
    window : tuple
        Event-time window (min, max)

    Returns
    -------
    statsmodels regression result
    """

    df = df.sort_values([unit_fe, time_fe]).copy()

    # Treatment definition
    df["treated"] = (
        df["mw"] >
        df.groupby("region")["mw"].transform("median")
    ).astype(int)

    # Event time
    df["event_time"] = df[time_fe] - policy_time

    # Trim window
    df = df[
        (df["event_time"] >= window[0]) &
        (df["event_time"] <= window[1])
    ]

    # Set baseline period (k = -1)
    df["event_time"] = df["event_time"].astype(int)
    df["event_time"] = df["event_time"].astype("category")
    df["event_time"].cat.reorder_categories(
        sorted(df["event_time"].cat.categories),
        ordered=True,
        inplace=True
    )

    formula = (
        f"{outcome} ~ treated*C(event_time)"
        f" + C({unit_fe}) + C({time_fe})"
    )

    model = smf.ols(
        formula,
        data=df.dropna()
    ).fit(
        cov_type="cluster",
        cov_kwds={"groups": df.dropna()[cluster]}
    )

    return model
