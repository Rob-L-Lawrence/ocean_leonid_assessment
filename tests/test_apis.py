import pytest

from ocean_leonid.src.apis import get_au_data, get_uk_data


class TestApis:
    def test_uk_api(self):
        uk_df = get_uk_data()

        # Make sure there are the correct amount of rows for the time difference
        min_date = min(uk_df["date"])
        max_date = max(uk_df["date"])

        t = max_date.to_period(freq="Q") - min_date.to_period(freq="Q")

        assert (
            uk_df.shape[0] == t.n + 1
        ), "The number of rows doesnt match the number of quarters"

    def test_au_api(self):
        au_df = get_au_data()

        # Make sure there are the correct amount of rows for the time difference
        min_date = min(au_df["date"])
        max_date = max(au_df["date"])

        t = max_date.to_period(freq="Q") - min_date.to_period(freq="Q")

        assert (
            au_df.shape[0] == t.n + 1
        ), "The number of rows doesnt match the number of quarters"
