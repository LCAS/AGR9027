# AGR9027: computer vision and machine learning

These optional notebooks are teaching baselines, **not assessment solutions**:

1. `01_colour_classification.ipynb` trains a small classifier on synthetic
   colour regions, then locates and classifies separate coloured objects.
2. `02_tiny_cnn.ipynb` trains a small CPU CNN to classify already-cropped
   synthetic person-like silhouettes by clothing colour and distinguish other
   coloured shapes. It demonstrates the workflow, not a real person detector.

The colour example relates to clothing in Task B and fruit ripeness in Task C;
colour alone cannot identify a person or reliably determine ripeness. The CNN
example relates to Task B: a separate detector would first need to find each
person, and tracking would be needed to maintain target identity. Neither
notebook controls the robot, measures distance, or solves overlapping-fruit
counting. Evaluate with your own labelled, representative images and the real
robot. Consult the assessment brief for requirements.

## One-time setup

First follow the virtual-environment instructions in the
[machine learning README](../machine_learning/README.md). From the repository
root, install the additional packages using the same environment. You only need
to do this once per environment, not each time you open a notebook.

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe -m pip install -r scripts\computer_vision\requirements.txt
```

macOS / Linux / Raspberry Pi:

```bash
.venv/bin/python -m pip install -r scripts/computer_vision/requirements.txt
```

The additional packages are OpenCV (headless, for image processing without GUI
windows) and CPU-capable PyTorch (for the CNN). The other packages and Jupyter
kernel are installed by the first setup.

## Every time you work

Follow [Every time you work](../machine_learning/README.md#every-time-you-work)
to use the existing environment in a new terminal. Open the notebooks in VS Code, select
**Python (AGR9027 ML)** or the `.venv` interpreter as the kernel, and run the
cells in order. Follow the VS Code notebook steps in the machine learning README
if you need help selecting a kernel. The examples work without a camera or
network access after installation; no browser is needed.

On a 64-bit Raspberry Pi OS, package availability and performance depend on the
Pi, OS, Python and architecture; PyTorch is substantially larger than the other
dependencies and may not have a wheel for every configuration. If PyTorch cannot
be installed, run the CNN on a supported laptop and use the colour and basic ML
examples on the Pi. To install only the colour example's extra dependency, run
`.venv/bin/python -m pip install "opencv-python-headless>=4.8,<5"` instead (on Windows,
replace `.venv/bin/python` with `.\.venv\Scripts\python.exe`). Train on a laptop when
needed, measure actual inference speed on the robot, and only load model files
from trusted sources.
