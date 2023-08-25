import io

import pandas as pd
import requests


def get_uk_data() -> pd.DataFrame:
    # Make the call to the API
    res = requests.get(
        url="https://www.ons.gov.uk/generator",
        params={
            "uri": "/economy/inflationandpriceindices/timeseries/l522/mm23",
            "format": "csv",
        },
    )

    # Convert the data into a raw dataframe
    raw_data = pd.read_csv(
        io.StringIO(res.content.decode("utf-8")), names=["raw_date", "CPIH"]
    )

    # Get only the quarterly data
    quarterly_data = raw_data.loc[raw_data["raw_date"].str.contains("Q")]

    # Convert the quarterly dates to actual dates
    quarterly_data["quarterly_date"] = pd.PeriodIndex(
        quarterly_data["raw_date"].str.replace(" ", ""), freq="Q"
    ).to_timestamp()

    # conver CPIH to floats
    quarterly_data["CPIH"] = pd.to_numeric(quarterly_data["CPIH"])

    # Lag the data
    quarterly_data["date_lagged"] = quarterly_data["quarterly_date"].shift(4)
    quarterly_data["CPIH_lagged"] = quarterly_data["CPIH"].shift(4)

    # Do the calculation
    quarterly_data["annualised_rate"] = (
        (quarterly_data["CPIH"] - quarterly_data["CPIH_lagged"])
        * 100
        / quarterly_data["CPIH_lagged"]
    )

    return quarterly_data[["quarterly_date", "annualised_rate"]]


def get_au_data() -> pd.DataFrame:
    res = requests.get(
        url=" https://api.data.abs.gov.au/data/CPI/1.10001.10.50.Q",
        params={
            "format": "csv",
        },
    )

    # Convert the data into a raw dataframe
    raw_data = pd.read_csv(io.StringIO(res.content.decode("utf-8")))

    # Convert the quarterly dates to actual dates
    raw_data["quarterly_date"] = pd.PeriodIndex(
        raw_data["TIME_PERIOD"], freq="Q"
    ).to_timestamp()

    required_data = raw_data[["quarterly_date", "OBS_VALUE"]]

    # Lag the data
    required_data["date_lagged"] = required_data["quarterly_date"].shift(4)
    required_data["obs_lagged"] = required_data["OBS_VALUE"].shift(4)

    # Do the calculation
    required_data["annualised_rate"] = (
        (required_data["OBS_VALUE"] - required_data["obs_lagged"])
        * 100
        / required_data["obs_lagged"]
    )

    return required_data[["quarterly_date", "annualised_rate"]]
