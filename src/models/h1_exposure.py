import pandas as pd


def H1_exposure(df, threshold=1.2):
    """
    H1: Which occupations concentrate near the minimum wage?
    """
    df = df.copy()
    df["near_mw"] = (df["wage"] <= threshold * df["mw"]).astype(int)

    exposure = (
        df.groupby("occupation")
          .agg(
              share_near_mw=("near_mw", "mean"),
              n_workers=("near_mw", "size")
          )
          .reset_index()
          .sort_values("share_near_mw", ascending=False)
    )

    return exposure