#!/usr/bin/env python3
"""
Setup script to create dbt profiles.yml configuration.
Run with: uv run setup.py
"""

import os
import yaml


def main():
    print("🚀 Setting up dbt profiles.yml for sef_finance")
    print("=" * 50)
    print()

    # Get user inputs
    host = input("Enter PostgreSQL host [localhost]: ").strip() or "localhost"
    user = input("Enter PostgreSQL username: ").strip()
    while not user:
        print("❌ Username is required!")
        user = input("Enter PostgreSQL username: ").strip()

    password = input("Enter PostgreSQL password: ").strip()
    while not password:
        print("❌ Password is required!")
        password = input("Enter PostgreSQL password: ").strip()

    port = input("Enter PostgreSQL port [5432]: ").strip() or "5432"
    threads = input("Enter number of threads [4]: ").strip() or "4"

    # Build profiles.yml content
    profile_config = {
        "sef_finance": {
            "target": "dev",
            "outputs": {
                "dev": {
                    "type": "postgres",
                    "host": host,
                    "user": user,
                    "password": password,
                    "port": int(port),
                    "dbname": "sef_finance_database",
                    "schema": "public",
                    "threads": int(threads),
                }
            },
        }
    }

    # Create ~/.dbt directory if it doesn't exist
    dbt_dir = os.path.expanduser("~/.dbt")
    os.makedirs(dbt_dir, exist_ok=True)

    # Write profiles.yml
    profiles_path = os.path.join(dbt_dir, "profiles.yml")
    with open(profiles_path, "w") as f:
        yaml.dump(profile_config, f, default_flow_style=False, sort_keys=False)

    print()
    print("=" * 50)
    print(f"✅ profiles.yml created successfully at: {profiles_path}")
    print()
    print("Next steps:")
    print("  1. Create the database: CREATE DATABASE sef_finance_database;")
    print("  2. Load seed data: dbt seed")
    print("  3. Run models: dbt run")
    print()


if __name__ == "__main__":
    main()
