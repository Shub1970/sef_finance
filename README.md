---

# 🛠️ Technical Setup Guide

This project uses **dbt (data build tool)** with **PostgreSQL**. We use [uv](https://docs.astral.sh/uv/) for ultra-fast Python package and environment management.

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have `uv` installed on your system. If not, follow the [Installation Guide](https://docs.astral.sh/uv/getting-started/installation/).

### 2. Environment Setup

Clone the repository and set up your virtual environment:

```bash
# Clone the repository
git clone https://github.com/Shub1970/sef_finance
cd sef_finance

# Create a virtual environment
uv venv

# Activate the environment
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

```

### 3. Install Dependencies

Install dbt and project dependencies:

```bash
# Install dbt-core and postgres adapter
uv pip install dbt-core dbt-postgres

# Install dbt packages (defined in packages.yml)
dbt deps

# Setup dbt connection profile
uv run setup.py

```

---

## ⚙️ Database Configuration

### 1. Create the Database

Open your PostgreSQL terminal or pgAdmin4 and create the database:

```sql
CREATE DATABASE sef_finance_database;
```

### 2. Load Seed Data

This project uses **dbt seeds** to load raw data from CSV files into the database. The seed files are located in the `seeds/` directory:
- `users.csv` - User information
- `orders.csv` - Order transactions  
- `payments.csv` - Payment records

The seeds are automatically configured in `dbt_project.yml` with proper schema and column types. To load the seed data, run:

```bash
dbt seed
```

This will create the tables in the `public_raw` schema (dbt concatenates the target schema `public` with the seed schema) and populate them with data from the CSV files.

### 3. Configure Database Connection

Run the setup script to create your dbt connection profile:

```bash
uv run setup.py
```

This will prompt you for your PostgreSQL credentials and create `~/.dbt/profiles.yml` automatically.

_Alternatively, you can manually create `~/.dbt/profiles.yml` with your connection details._

---

## 🏃 Running the Project

Once the setup is complete, verify your connection and run the models:

```bash
# Setup database connection (creates ~/.dbt/profiles.yml)
uv run setup.py

# Check connection
dbt debug

# Load seed data (raw tables from CSV)
dbt seed

# Run all models
dbt run

```

### 💡 Troubleshooting

If you see an error while running `dbt debug`, try deactivating and reactivating the virtual environment:

```bash
deactivate

# Reactivate
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate

```

### Generate & View Documentation

dbt creates a beautiful, interactive documentation site that includes your lineage graph (DAG).

**Generate the docs:**

```bash
dbt docs generate

```

**Launch the web interface:**

```bash
dbt docs serve

```

_This will host the documentation locally, usually at http://localhost:8080._

---

## 🧠 Project Insights

### 1. Transformations & Logic

I implemented an intermediate layer to clean and join raw data before moving to final analytics.

- **`int_completed_orders.sql`**: Joins `orders`, `payments`, and `users`.
- **Logic**: Filters for `status = 'complete'` and `payment_status = 'success'`.
- **Purpose**: Creates a "Golden Record" of successful transactions to simplify downstream analysis like daily revenue and geographic performance.

- **`int_failed_orders.sql`**: Filters for failed orders and refunded payments.
- **Purpose**: To provide a dedicated view for troubleshooting transaction friction and analyzing lost revenue.

### 2. 📝 Key Assumptions

- **Uniqueness**: I assumed `order_id`, `user_id`, and `payment_id` are unique and serve as reliable Primary Keys.
- **Data Integrity**: Assumed that every payment record has a corresponding order record (Referential Integrity).

### 3. 🚧 Challenges & Learning Curve

Coming from a Full-Stack background using **ORMs (Prisma, Drizzle)** and **CRUD** operations, shifting to dbt required a mindset change:

- **Declarative vs. Imperative**: Instead of telling the database _how_ to change a row, I learned to define _what_ the final data should look like using SELECT statements.
- I realized that while ORMs are great for app state, dbt is built for the scale and analytical complexity of a Data Warehouse.

### 4. ⏳ Time Log

- **Total Time**: ~6-7 hours.
- **Breakdown**: Most of the time was spent on conceptual learning (YouTube/Docs) and local environment configuration (Postgres/pgAdmin) rather than just writing SQL.

### 5. 🔮 Future Improvements

If I had more time, I would:

1. **Dynamic Configuration**: Implement an `.env` file and use dbt's `env_var()` function to make the project name and database schema dynamic rather than hardcoded.

---
