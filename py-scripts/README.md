# Claim-simulation PDF splitter

`split_claim_simulations.py` splits configured multi-page PDFs from
`images/claim_simulations` into separate one-page PDF files. The generated files
are written beside the source PDFs with descriptive suffixes, for example:

- `county_scatter_claim_frequency_low.pdf`
- `quantile_county_changes_claim_frequency_medium_late_century.pdf`

The original PDF files are not modified or deleted. Existing generated files
are not replaced unless `--overwrite` is supplied.

## Configure the input files

Edit the two lists near the top of `split_claim_simulations.py`:

- `CLIMATE_SCENARIO_FILES` contains three-page PDFs ordered as low, medium, and
  high.
- `SCENARIO_HORIZON_FILES` contains six-page PDFs ordered as low mid-century,
  low late-century, medium mid-century, medium late-century, high mid-century,
  and high late-century.

The script checks that every configured PDF exists and has the expected number
of pages before writing any output.

## Run with Pixi

Run these commands from the presentation root directory.

First, validate the configuration and preview the output filenames without
writing files:

```powershell
pixi run --manifest-path py-scripts/pixi.toml check-claim-simulations
```

Then create the one-page PDFs:

```powershell
pixi run --manifest-path py-scripts/pixi.toml split-claim-simulations
```

To replace one-page PDFs created by an earlier run:

```powershell
pixi run --manifest-path py-scripts/pixi.toml split-claim-simulations --overwrite
```

Pixi normally searches the current directory for `pixi.toml`. Here the Pixi
project lives in `py-scripts`, while the commands are run from the presentation
root. The `--manifest-path py-scripts/pixi.toml` argument tells Pixi exactly
which project manifest, environment, dependencies, and tasks to use.

Pixi installs and manages the required Python version and `pypdf` dependency
from the versions recorded in `pixi.toml` and `pixi.lock`; no separate Python
environment needs to be activated.