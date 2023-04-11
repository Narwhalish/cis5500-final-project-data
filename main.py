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
    # Remove rows with null profile_id
    chunk = chunk.loc[
        chunk.loc[:, "profile_id"].notna()
        & chunk.loc[:, "following"].notna()
        & chunk.loc[:, "followers"].notna()
    ]

    # Change profile_id, following, and followers columsn from float to int64 and in32 respectively
    chunk.loc[:, "profile_id"] = chunk.loc[:, "profile_id"].astype("int64")
    chunk.loc[:, "following"] = chunk.loc[:, "following"].astype("int32")
    chunk.loc[:, "followers"] = chunk.loc[:, "followers"].astype("int32")

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
        "cts": "object",
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
        "following": "float64",
        "followers": "float64",
        "n_posts": "float64",
        "url": "object",
        "cts": "object",
        "is_business_account": "object",
    },
)
# print("==========================================================================")
# explore_by_chunk("posts")
# print("==========================================================================")
# explore_by_chunk("locations")
