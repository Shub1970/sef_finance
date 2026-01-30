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
git clone https://github.com/Shub1970/dbt-learning.git
cd dbt-learning

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

```

---

## ⚙️ Database Configuration

### 1. Create the Database

Open your PostgreSQL terminal or pgAdmin4 and run the following to initialize your schema:

```sql
CREATE DATABASE sef_finance_database;

-- Switch to the new database and create tables
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    signup_date DATE NOT NULL,
    city VARCHAR(100)
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    payment_method VARCHAR(50),
    payment_status VARCHAR(20)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT NOT NULL,
    order_date DATE NOT NULL,
    amount NUMERIC(10,2),
    status VARCHAR(20)
);

```

> **Note:** After creating the tables, please seed them with your CSV data using pgAdmin4 or the `COPY` command.

### 2. Configure `profiles.yml` (Critical)

dbt requires a connection profile located at `~/.dbt/profiles.yml`. Create this file if it doesn't exist and add the following configuration:

```yaml
sef_finance:
  target: dev
  outputs:
    dev:
      type: postgres
      host: [your-host]
      user: [your-username]
      password: [your-password]
      port: [your-port]
      dbname: sef_finance_database
      schema: public
      threads: 4
```

---

## 🏃 Running the Project

Once the setup is complete, verify your connection and run the models:

```bash
# Check connection
dbt debug

# Run all models
dbt run

```

---

### Pro-Tips for your README:

- **Hyperlinks:** I changed `[project-name]` to the actual `sef_finance` name in the code block to reduce confusion.
- **Admonitions:** Using the `> **Note:**` block helps important warnings stand out.
- **Language Tags:** Always use `bash`, `sql`, or `yaml` after the triple backticks (```) so GitHub applies the correct color coding.

**Would you like me to add a "Project Structure" section to explain what each dbt folder does?**

