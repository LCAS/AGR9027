# AGR9027: machine learning basics

These optional, small examples introduce machine learning as a possible building
block for Assessment 2. ML is **not mandatory**, and these notebooks are not
finished assessment solutions. Start with the notebooks in order:

1. `01_classification.ipynb`: predict a category using a decision tree.
2. `02_regression.ipynb`: predict a number using linear regression.
3. `03_clustering.ipynb`: group unlabelled observations with k-means.
4. `04_reinforcement_learning.ipynb`: learn a tiny grid-world policy with a
   Q-table, without a robot or a reinforcement-learning library.

All data are artificial. The notebooks train and then use their model, and
supervised examples reserve test data. Synthetic results do not demonstrate
performance on real crops, people or robots. The companion
[computer vision notebooks](../computer_vision/README.md) introduce colour
classification and a tiny CNN.

## One-time setup: create the environment and install packages

Internet access is needed to install Python and packages. These instructions use
**Python 3.13**.
Create one virtual environment for both notebook folders. Do not install the
packages into a system Python or Conda base environment.

Use **VS Code** on a lab PC or your laptop; no browser or JupyterLab server is
needed. In VS Code, open the repository root using **File > Open Folder**. Open
**Extensions** (`Ctrl+Shift+X`) and check that Microsoft's **Python** and
**Jupyter** extensions are installed and enabled. Install them if necessary;
if a lab PC prevents installation, ask the teaching team for help. Open a
terminal in VS Code with **Terminal > New Terminal** for the commands below.

These steps are normally needed **once per computer and repository copy**. If
you already completed them, skip to [Every time you work](#every-time-you-work).

### One-time setup: Windows PowerShell

1. If Python 3.13 is not already installed, download its **Windows installer
   (64-bit)** from [python.org](https://www.python.org/downloads/release/python-3139/).
   Run it as your normal user. Select **Add python.exe to PATH** and choose
   **Install Now**. If Python is already installed but not on PATH, use its
   full `python.exe` path in place of `python` below.
2. Open a new PowerShell terminal in the repository root (the folder containing
   `scripts`). Check the interpreter used to create the environment:

   ```powershell
   python --version
   (Get-Command python).Source
   ```

   It should print `Python 3.13.x`. If the command is not found or shows another
   version, use the full path to your Python 3.13 `python.exe`, for example
   `& "$env:LocalAppData\Programs\Python\Python313\python.exe" --version`.
   If the path contains `anaconda` or `miniconda`, it is a Conda interpreter,
   even if the version is correct. To avoid depending on Conda, install Python
   from python.org as in step 1 and use its full path instead. A `(base)` prompt
   can indicate that Conda is active; a full path still selects the intended
   interpreter. These instructions do not require the `py` launcher or Conda.
3. If `.venv` already exists, do not overwrite an environment you want to keep.
   The following commands assume `.venv` does not exist. Create it using the
   Python 3.13 interpreter you checked in step 2:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe --version
```

If you used a full path for the version check, use it instead of `python` in
the first command, followed by `-m venv .venv`. The environment version check
must report Python 3.13. If an existing `.venv` uses another version, rename it
or choose a different directory and substitute that directory in every command
and kernel selection below.

4. Install the basic notebook packages and register the notebook kernel:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r scripts\machine_learning\requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --user --name agr9027-ml --display-name "Python (AGR9027 ML)"
```

These commands explicitly use `.venv`, so they do not depend on whether
PowerShell shows `(base)`. They need to be rerun only if you recreate the
environment or need to reinstall its packages. For the vision notebooks, follow
the one-time extra installation in the [computer vision README](../computer_vision/README.md).

### One-time setup: macOS / Linux / Raspberry Pi

Install Python 3.13 and open a terminal at the repository root. On Raspberry Pi,
use a 64-bit Raspberry Pi OS; install OS packages `python3-venv` and
`python3-pip` if needed. Check `python3 --version` first; it must report 3.13.
If it does not, replace `python3` in the first command with the path to your
Python 3.13 executable. Raspberry Pi OS may provide a different default version;
use an installed 3.13 interpreter rather than replacing the system Python.

```bash
python3 -m venv .venv
.venv/bin/python --version
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r scripts/machine_learning/requirements.txt
.venv/bin/python -m ipykernel install --user --name agr9027-ml --display-name "Python (AGR9027 ML)"
```

The environment version check must report Python 3.13. If `.venv` already
exists and you want to keep it, use a different directory and substitute that
directory in the commands and kernel selection below. For vision notebooks,
also complete the one-time extra installation in the
[computer vision README](../computer_vision/README.md).

## Every time you work

1. Open the repository root in VS Code and open **Terminal > New Terminal**.
   **Do not create `.venv` or reinstall packages again** if setup is complete.
2. To use the environment in this terminal, choose one of the following:

   **Windows PowerShell — activate the existing environment:**

   ```powershell
   .\.venv\Scripts\Activate.ps1
   python --version
   ```

   The prompt should show `(.venv)` and the version should be 3.13. If
   PowerShell blocks activation, use the direct command below instead; no
   activation is needed. If `(base)` is also shown, `.venv` is the environment
   used by the activated terminal; alternatively, run `conda deactivate` before
   activating `.venv` if Conda is available.

   **macOS / Linux / Raspberry Pi — activate the existing environment:**

   ```bash
   source .venv/bin/activate
   python --version
   ```

   The prompt should show `(.venv)` and the version should be 3.13.

   **Without activation**, use the environment's Python explicitly for each
   terminal command: `.\.venv\Scripts\python.exe` on Windows or
   `.venv/bin/python` on macOS/Linux. For example, append `--version` to check
   it. This works even if the terminal shows `(base)`.
3. Open and run a notebook as described below. **Terminal activation does not
   select a notebook kernel**: check the kernel in VS Code separately.
4. When finished, if you activated the environment, run `deactivate` in the
   terminal. This does not delete the environment; it will be available next
   time.

### Run the notebooks in VS Code

The requirements install ipykernel, NumPy,
Matplotlib, scikit-learn and joblib, including their dependencies. The computer
vision README explains the extra packages for its examples. They also install
JupyterLab, but you do not need to start it for the VS Code workflow.

1. In VS Code's Explorer, open `scripts/machine_learning` and select
   `01_classification.ipynb`. It opens as a notebook with text and code cells.
2. Select **Select Kernel** at the top right of the notebook. Choose
   **Jupyter Kernel**, then **Python (AGR9027 ML)**. If the named kernel is not
   listed, choose **Python Environments** and select the `.venv` interpreter
   created above (`.venv\Scripts\python.exe` on Windows or
   `.venv/bin/python` on macOS/Linux). If needed, use **Enter interpreter
   path** to locate it. Do not select the system or Conda base interpreter.
3. Use **Run All** at the top of the notebook, or use the play button beside
   each code cell in order. Results and figures appear directly below the cells.
   The first run may take a little time while the kernel starts.
4. Repeat for the other notebooks. Confirm the selected kernel at the top right
   of each notebook. If an import is missing, check that the notebook is using
   `.venv` and install the relevant requirements into that same environment.

Do not commit `.venv` or saved model files. If installing packages on a Pi is
slow, train on a laptop
and transfer a trusted model for inference; use compatible package versions.

Persisted model files can execute code when loaded: **only load files you
created or trust**. Measure inference time and test with your own representative
data before deploying on the Pi. See the [main README](../../README.md) and
[simulators](../../trilobot_simulator/README.md).
