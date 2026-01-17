from src.models.h2_occupational_did import H2_occupational_DiD


def H3_regional_heterogeneity(df, regions, policy_time):
    """
    H3: Are occupational responses heterogeneous across regions?
    """
    sub = df[df["region"].isin(regions)].copy()
    return H2_occupational_DiD(sub, policy_time)