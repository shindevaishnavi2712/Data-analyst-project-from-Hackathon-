# VoltRelay Energy Hackathon Submission

**Prepared by:** Vaishnavi Shinde

This package contains the supplied CSV datasets, a reproducible analysis script, a Streamlit dashboard, a preliminary findings report, a presentation deck, charts, and three video recording scripts.

## Important limitation
The problem statement describes approximately 3.9 million swap events in `swap_events.csv`, but that file was not included in the uploads. Therefore event-level completed swaps, revenue, failure rates, queue abandonment, retention, pricing response and contribution margin are not fabricated or presented as measured results.

## Run locally
```bash
pip install -r requirements.txt
python src/analyze.py
streamlit run app.py
```
Open the dashboard at the local Streamlit URL printed in the terminal.

## Folder guide
- `data/` — all seven uploaded CSV files
- `src/analyze.py` — reproducible data-quality and supporting-table analysis
- `app.py` — Streamlit dashboard
- `outputs/` — charts and machine-readable summaries
- `submission/` — PDF report, PowerPoint presentation, full Markdown report, and video scripts

Add `swap_events.csv` to `data/` and extend the event analysis before claiming final results for the six core business questions.
