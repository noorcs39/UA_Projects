# Project Index

## DDA Assignment 1 — Graph Algorithms (`projects/dda_assignment_1/`)

| File / Folder | Purpose |
| --- | --- |
| `IS.py` | Maximal independent set demo with NetworkX |
| `MWIS.py` | Maximum weight independent set experiments |
| `Greedy/Greedy.py` | Greedy heuristic for MWIS on random graphs |
| `ES_MWIS/` | Exhaustive search attempts with output logs |

---

## DDA Assignment 2 — Streaming Counters (`projects/dda_assignment_2/`)

| File | Purpose |
| --- | --- |
| `simplecounter.py` | Exact word counting from Project Gutenberg text |
| `exactcounter1.py` / `exactcounter2.py` | Exact counters with stop-word filtering |
| `approximatecounter.py` | Approximate counter with accuracy parameter |
| `approximiatewithfixed.py` / `approximiatewithdecreasing.py` | Counter variants |
| `morriscounter.py` | Morris-style approximate counter simulation |
| `text_files/` | Sample input files for local testing |

Shared counter logic is also available in `src/ua_projects/counters.py`.

---

## Fault Detection (`projects/fault_detection/`)

| File / Folder | Purpose |
| --- | --- |
| `main.py` | Load cleaned dataset and prepare train/test split |
| `dataset/Raw_data.csv` | Raw telecom event data |
| `dataset/Cleaned_data_after_processing.csv` | Preprocessed features and labels |

---

## Shared Code

| Module | Purpose |
| --- | --- |
| `src/ua_projects/counters.py` | Approximate counting helpers used in tests |
