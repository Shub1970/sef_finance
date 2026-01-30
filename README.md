# Technical Section

## How to set up and run the project

you have to have a UV[https://docs.astral.sh/uv/getting-started/installation/] install in the sysyteml

### create a vertual env

```code
 uv venv
```

### and activate the vertual env

```code
for mac - source .venv/bin/activate
for window -  .venv\Scripts\Activate.ps1
```

### and install all the necessay dependancy

```code
uv pip install dbt-core dbt-postgres
```

### now clone the gihub repo.

```code
git clone https://github.com/Shub1970/dbt-learning.git
cd dbt-learning
```

you should also need to install all other utils

```code
dbt deps
```

### Set Up profiles.yml (MOST IMPORTANT)

create a ~/.dbt/profiles.yml file in your system and populate with the given code to make a connection with the database

```code

[project-name]:
  target: dev
  outputs:
    dev:
      type: postgres
      port: [port]
      database: [database name]
      schema: public
      threads: 4
      host:[host]
      user: [username]
      password: [password]

```

in our case project-name

