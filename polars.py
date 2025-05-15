# TEST DATA
uid_df = pd.DataFrame({
    'UID': ['UID1', 'UID2', 'UID3', 'UID4', 'UID5'],
    'Total_Annual': [100, 200, 150, 100, 50],
    'SPE': [None, None, None, None, None]
})

spe_df = pd.DataFrame({
    'SPE': ['SPE1', 'SPE2'],
    'Total_Annual': [300, 250]
}).sort_values(by=['SPE','Total_Annual'])

#######################
import polars as pl
from itertools import combinations

def find_combinations_fast(totals: list[int], target: int):
    """
    Find a combination of indices in the list `totals` that sum to `target`.
    """
    for r in range(1, len(totals) + 1):
        for combo in combinations(range(len(totals)), r):
            if sum(totals[i] for i in combo) == target:
                return combo
    return None

def assign_spe(uid_df: pl.DataFrame, spe_df: pl.DataFrame) -> pl.DataFrame:
    # Add an index to track rows efficiently
    uid_df = uid_df.with_columns(pl.arange(0, uid_df.height).alias("row_id"))
    uid_df = uid_df.with_columns(pl.lit(None).cast(pl.Utf8).alias("assigned_spe"))

    # Convert to dict for fast lookup and manipulation
    uid_pool = {
        row["row_id"]: {
            "uid": row["uid"],
            "total_annual": row["total_annual"]
        }
        for row in uid_df.iter_rows(named=True)
    }

    # Keep track of row_ids that have been used
    used_row_ids = set()

    assignments = []

    for spe_row in spe_df.iter_rows(named=True):
        spe = spe_row["spe"]
        target = spe_row["total_annual"]

        # Available pool excluding used rows
        available = [(rid, val["total_annual"]) for rid, val in uid_pool.items() if rid not in used_row_ids]
        if not available:
            continue

        row_ids, totals = zip(*available)
        combo = find_combinations_fast(totals, target)

        if combo is not None:
            selected_ids = [row_ids[i] for i in combo]
            for rid in selected_ids:
                assignments.append((rid, spe))
            used_row_ids.update(selected_ids)

    # Create a Polars DataFrame of assignments
    if assignments:
        assignment_df = pl.DataFrame(assignments, schema=["row_id", "assigned_spe"])
        uid_df = uid_df.join(assignment_df, on="row_id", how="left").with_columns(
            pl.coalesce([pl.col("assigned_spe_right"), pl.col("assigned_spe")]).alias("assigned_spe")
        ).select(["uid", "total_annual", "assigned_spe"])

    return uid_df



# NEW TEST CODE
import pandas as pd

projects = pd.DataFrame({
    'project_id': [1, 2],
    'budget': [1000, 500]
})

expenses = pd.DataFrame({
    'expense_id': [101, 102, 103, 104],
    'project_id': [1, 1, 2, 1],
    'cost': [400, 700, 200, 300],
    'date': ['2024-01-01', '2024-01-02', '2024-01-01', '2024-01-03']
}).sort_values(by=['project_id', 'date'])

projects.set_index('project_id', inplace=True)

amortized_costs = []
remaining_budget = projects['budget'].to_dict()

for _, row in expenses.iterrows():
    proj_id = row['project_id']
    cost = row['cost']
    available = remaining_budget[proj_id]

    amortized = min(cost, available)
    remaining_budget[proj_id] -= amortized

    amortized_costs.append(amortized)

expenses['amortized_cost'] = amortized_costs
