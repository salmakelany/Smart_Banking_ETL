import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:0000@localhost:5432/smart_banking_dw"
)

DATA_PATH = "../cleaned_data/"

tables = {
    "Branches": "branches",
    "Customers": "customers",
    "Employees": "employees",
    "Accounts": "accounts",
    "ATMs": "atms",
    "Loans": "loans",
    "CreditCards": "creditcards",
    "Beneficiaries": "beneficiaries",
    "MobileBanking": "mobilebanking",
    "Transactions": "transactions",
}

for file_name, table_name in tables.items():
    print(f"Loading {file_name}.csv ...")

    df = pd.read_csv(f"{DATA_PATH}{file_name}.csv")

    df.to_sql(
        table_name,
        engine,
        if_exists="append",
        index=False
    )

    print(f"✅ {table_name} loaded successfully ({len(df)} rows)")

print("\n🎉 All tables loaded successfully!")