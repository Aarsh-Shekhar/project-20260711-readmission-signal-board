# Readmission Signal Board

Ranks synthetic readmission signals for care teams.

## What it includes

- deterministic sample data
- scoring and ranking logic
- command line report
- unit tests
- continuous validation workflow

## Run

```bash
python3 -m readmission_signal_board.cli --input data/sample_patients.json
```

## Test

```bash
python3 -m unittest discover tests
```
