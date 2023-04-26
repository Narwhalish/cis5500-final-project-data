import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv


def write_chunk_to_csv(chunk, filename, header):
    chunk.to_csv(
        f"new_{filename}.csv",
        sep="\t",
        quoting=csv.QUOTE_NONNUMERIC,
        header=header,
        mode="a",
        index=True,
    )


def explore_by_chunk(filename, dtype=None, transform=None):
    with pd.read_csv(
        f"{filename}.csv",
        sep="\t",
        chunksize=100000,
        iterator=True,
        index_col="sid",
        parse_dates=["cts"],
        date_format="%Y-%m-%d %H:%M:%S.%f%z",
        dtype=dtype,
    ) as reader:
        print(f"Table: {filename.upper()}")

        last_chunk = None
        rows = 0

        for i, chunk in enumerate(reader):
            if i == 0:
                print(chunk.dtypes)

                print("First chunk:")
                print(chunk.head(5))

            if transform:
                write_chunk_to_csv(transform(chunk), filename, header=(i == 0))

            rows += chunk.shape[0]
            last_chunk = chunk

        print("Last chunk:")
        print(last_chunk.tail(5))

        print(f"Total rows: {rows}")


def transform_profiles(chunk):
    # Remove rows with null values in profile_id, following, followers, and n_posts
    chunk = chunk.loc[
        chunk.loc[:, "profile_id"].notna()
        & chunk.loc[:, "following"].notna()
        & chunk.loc[:, "followers"].notna()
        & chunk.loc[:, "n_posts"].notna()
    ]

    # Set chunk dtypes
    chunk = chunk.astype(
        {
            "profile_id": "int64",
            "profile_name": "object",
            "firstname_lastname": "object",
            "description": "object",
            "following": "int32",
            "followers": "int32",
            "n_posts": "int32",
            "url": "object",
            "is_business_account": "object",
        }
    )

    return chunk


def transform_posts(chunk):
    # Remove rows with null values in profile_id, location_id, numbr_likes, and number_comments
    chunk = chunk.loc[
        chunk.loc[:, "sid_profile"].notna()
        & chunk.loc[:, "profile_id"].notna()
        & chunk.loc[:, "location_id"].notna()
        & chunk.loc[:, "post_type"].notna()
        & chunk.loc[:, "numbr_likes"].notna()
        & chunk.loc[:, "number_comments"].notna()
    ]

    chunk = chunk.replace({"sid_profile": -1}, np.nan)

    # Set chunk dtypes
    chunk = chunk.astype(
        {
            "sid_profile": "Int64",
            "post_id": "object",
            "profile_id": "int64",
            "location_id": "int64",
            "post_type": "int32",
            "description": "object",
            "numbr_likes": "int32",
            "number_comments": "int32",
        },
    )

    return chunk


def transform_locations(chunk):
    # Remove rows with null values in profile_id, location_id, numbr_likes, and number_comments
    chunk = chunk.loc[chunk.loc[:, "lat"].notna() & chunk.loc[:, "lng"].notna()]

    # Drop aj_exact_city_match and aj_exact_country_match columns
    chunk = chunk.drop(labels=["aj_exact_city_match", "aj_exact_country_match"], axis=1)

    # Set chunk dtypes
    chunk = chunk.astype(
        {
            "id": "int64",
            "name": "object",
            "street": "object",
            "zip": "object",
            "city": "object",
            "region": "object",
            "cd": "object",
            "phone": "object",
            "blurb": "object",
            "dir_city_id": "object",
            "dir_city_name": "object",
            "dir_city_slug": "object",
            "dir_country_id": "object",
            "dir_country_name": "object",
            "lat": "float64",
            "lng": "float64",
            "primary_alias_on_fb": "object",
            "slug": "object",
            "website": "object",
        },
    )

    return chunk


explore_by_chunk(
    "profiles",
    dtype={
        "profile_id": "float64",
        "profile_name": "object",
        "firstname_lastname": "object",
        "description": "object",
        "following": "float64",
        "followers": "float64",
        "n_posts": "float64",
        "url": "object",
        "is_business_account": "object",
    },
    transform=transform_profiles,
)
print("==========================================================================")
explore_by_chunk(
    "new_profiles",
    dtype={
        "profile_id": "int64",
        "profile_name": "object",
        "firstname_lastname": "object",
        "description": "object",
        "following": "int32",
        "followers": "int32",
        "n_posts": "int32",
        "url": "object",
        "is_business_account": "object",
    },
)
print("==========================================================================")
explore_by_chunk(
    "posts",
    dtype={
        "sid_profile": "float64",
        "post_id": "object",
        "profile_id": "float64",
        "location_id": "float64",
        "post_type": "object",
        "description": "object",
        "numbr_likes": "float64",
        "number_comments": "float64",
    },
    transform=transform_posts,
)
print("==========================================================================")
explore_by_chunk(
    "new_posts",
    dtype={
        "sid_profile": "Int64",
        "post_id": "object",
        "profile_id": "int64",
        "location_id": "int64",
        "post_type": "int32",
        "description": "object",
        "numbr_likes": "int32",
        "number_comments": "int32",
    },
)
print("==========================================================================")
explore_by_chunk(
    "locations",
    dtype={
        "id": "float64",
        "name": "object",
        "street": "object",
        "zip": "object",
        "city": "object",
        "region": "object",
        "cd": "object",
        "phone": "object",
        "blurb": "object",
        "dir_city_id": "object",
        "dir_city_name": "object",
        "dir_city_slug": "object",
        "dir_country_id": "object",
        "dir_country_name": "object",
        "lat": "float64",
        "lng": "float64",
        "primary_alias_on_fb": "object",
        "slug": "object",
        "website": "object",
    },
    transform=transform_locations,
)
print("==========================================================================")
explore_by_chunk(
    "new_locations",
    dtype={
        "id": "int64",
        "name": "object",
        "street": "object",
        "zip": "object",
        "city": "object",
        "region": "object",
        "cd": "object",
        "phone": "object",
        "blurb": "object",
        "dir_city_id": "object",
        "dir_city_name": "object",
        "dir_city_slug": "object",
        "dir_country_id": "object",
        "dir_country_name": "object",
        "lat": "float64",
        "lng": "float64",
        "primary_alias_on_fb": "object",
        "slug": "object",
        "website": "object",
    },
)
