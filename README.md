# University of Aveiro Projects

<p align="center">
  <img src="https://img.shields.io/badge/University-Aveiro-003366?style=for-the-badge" alt="University of Aveiro" />
  <img src="https://img.shields.io/badge/Python-Algorithms-306998?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Focus-Data%20%26%20ML-2ECC71?style=for-the-badge" alt="Focus" />
  <img src="https://img.shields.io/badge/License-MIT-9B59B6?style=for-the-badge" alt="License" />
</p>

<p align="center">
  Coursework archive from <b>University of Aveiro (UA)</b> — algorithms, streaming counters, graph problems, and fault detection.
</p>

> Master's-era university projects — preserved for reference and learning.

---

## Projects

| Project | Description | Path |
| --- | --- | --- |
| **DDA Assignment 1** | Maximum Weight Independent Set (MWIS), greedy heuristics, exhaustive search | [`projects/dda_assignment_1/`](projects/dda_assignment_1/) |
| **DDA Assignment 2** | Exact and approximate streaming counters, word-frequency analysis | [`projects/dda_assignment_2/`](projects/dda_assignment_2/) |
| **Fault Detection** | Telecom event classification with scikit-learn on processed network data | [`projects/fault_detection/`](projects/fault_detection/) |

See [docs/PROJECT_INDEX.md](docs/PROJECT_INDEX.md) for file-level details.

---

## Structure

```
├── docs/
│   └── PROJECT_INDEX.md
├── outputs/
├── projects/
│   ├── dda_assignment_1/
│   ├── dda_assignment_2/
│   └── fault_detection/
├── src/
│   └── ua_projects/       # Shared utilities (approximate counters)
├── tests/
│   └── test_counters.py
├── LICENSE
├── requirements.txt
└── README.md
```

---

## Setup

```bash
git clone https://github.com/noorcs39/UA_Projects.git
cd UA_Projects
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

---

## Running Scripts

Each subproject is self-contained. Examples:

```bash
# DDA Assignment 2 — approximate counter demo
python projects/dda_assignment_2/approximatecounter.py

# DDA Assignment 1 — greedy MWIS
python projects/dda_assignment_1/Greedy/Greedy.py

# Fault detection preprocessing / split
python projects/fault_detection/main.py
```

---

## Tests

```bash
pytest tests/ -v
```

---

## Author

**Noor Uddin**  
📧 [noor.cs2@yahoo.com](mailto:noor.cs2@yahoo.com)  
🐙 [github.com/noorcs39](https://github.com/noorcs39)

---

## License

[MIT License](LICENSE)
