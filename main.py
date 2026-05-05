
"""
main.py
---------
Run the full IPTW event-study pipeline in sequence.

This script is provided for convenience and reproducibility.
It executes each analysis step in the correct order.

Note:
- Uses sample data by default (data/df_sample.csv)
- Results are illustrative only
"""

import subprocess
import sys
from pathlib import Path

# --------------------------------------------------
# Configuration
# --------------------------------------------------
SCRIPTS = [
    "scripts/01_prepare_data.py",
    "scripts/02_estimate_pscore.py",
    "scripts/03_estimate_att.py",
    "scripts/04_placebo_test.py",
    "scripts/05_spatial_diagnostics.py",
    "scripts/06_plots.py",
]

PYTHON = sys.executable  # ensures same Python environment


def run_script(script_path):
    """Run a Python script and stop if it fails."""
    print(f"\n▶ Running {script_path}")
    print("-" * 60)

    result = subprocess.run(
        [PYTHON, script_path],
        capture_output=False
    )

    if result.returncode != 0:
        print(f"\n❌ Error in {script_path}")
        sys.exit(1)

    print(f"✅ Finished {script_path}")


def main():
    print("\n==============================================")
    print(" Riparian Restoration Event-Study Pipeline ")
    print("==============================================")

    # Check scripts exist
    for script in SCRIPTS:
        if not Path(script).exists():
            print(f"❌ Missing script: {script}")
            sys.exit(1)

    # Run pipeline
    for script in SCRIPTS:
        run_script(script)

    print("\n==============================================")
    print("✅ Pipeline completed successfully")
    print("==============================================\n")


if __name__ == "__main__":
    main()
