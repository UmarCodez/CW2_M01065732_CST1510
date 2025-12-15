# CW2_M01065732_CST1510

## Project overview
This project brings three traditionally separate workflows into a single, coherent web app:
- Cybersecurity analysts: Investigate threats, triage incidents, and monitor risk through interactive security views and assisted analysis.
- Data scientists: Explore datasets, build and compare models, and generate reproducible insights with clean visualizations and utilities.
- IT administrators: Monitor systems and services, track resource usage, and manage configuration insights to support operational reliability.
The platform is built to be modular, secure, and extensible, allowing teams to add pages, datasets, and tools over time without breaking the core experience.


## Core objectives
- Unified experience: One app, multiple domains, consistent navigation and design.
- Actionable analytics: Dashboards, filters, and drill‑downs that lead to decisions, not just charts.
- Operational resilience: Thoughtful error handling, clear logging, and maintainable structure.
- Security by design: No hardcoded secrets; environment‑based configuration; clean Git practices.
- Extensibility: Domain pages are self‑contained modules; adding a new domain is straightforward.


## Features
- Multi‑page navigation: Clear entry points for Cybersecurity, Data Science, and IT Administration, plus a unified overview dashboard.
- Interactive dashboards: Filterable charts, sortable tables, KPIs, and domain‑specific metrics.
- AI‑assisted analysis: Optional chat page integrating large‑language‑model assistance for summarization, explanation, and quick guidance.
- Modular architecture: Each domain page encapsulates its logic and UI; shared utilities live in app/.
- Secure configuration: API keys via environment variables, .gitignore for sensitive files, no secrets in source or history.
- Consistent design: Harmonized color palette, typography, and layout across domains for a cohesive feel.


Unified_Intelligence_Platform/
│
├── main.py              # Entry point: sets global config, sidebar navigation, routes to domain pages
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
│
├── app/                 # Shared logic and utilities (imported across pages)
│   ├── data_io.py       # Data loading, caching, validation helpers
│   ├── viz.py           # Common plotting functions and style helpers
│   ├── auth.py          # (Optional) user/session scaffolding or role hints
│   └── config.py        # App-wide constants, color schemes, feature flags
│
├── DATA/                # Example datasets for dashboards and EDA
│   ├── security/        # Threat feeds, alerts, IOC lists
│   ├── operations/      # System metrics, logs, configurations
│   └── analytics/       # CSV/Parquet for modeling and exploration
│
├── pages/               # Streamlit multipage views (each is a standalone module)
│   ├── 1_Dashboard.py   # Unified overview: cross-domain KPIs and quick links
│   ├── Cybersecurity.py # Alerts, IOC search, incident timelines, risk summary
│   ├── DataScience.py   # Dataset browser, EDA panels, modeling sandbox
│   ├── IT_Admin.py      # Health and performance dashboards, config snapshots
│   └── Chat_GPT.py      # AI-assisted analysis and guidance interface
│
├── __pycache__/         # Python cache files (auto-generated)
└── .venv/               # Local virtual environment (excluded from Git)

