# AGR9027 Trilobot simulators

These simulators let you develop and test your Assessment 2 code **on your own laptop**, without needing the real Trilobot or access to the University lab. There is **one simulator per task** (A, B, C) because each task needs a different test scenario,
plus a live-webcam vision harness.
You don't need any robotics/Raspberry Pi hardware or the `trilobot`/`picamera2` Python
packages to run these - only a normal laptop with Python installed.

> **Important:** the simulators are simplified, 2D approximations meant to help you
> write and debug your decision-making logic (obstacle avoidance, following, counting)
> before trying it on the real robot. They are **not** a substitute for testing on the
> real Trilobot - the brief requires your final report and live demonstration to use
> the real robot.

## Simulator overview

Each simulator provides a different practice scenario. For all tasks, edit the
task's `student_control.py`; leave `simulator_task_*.py` unchanged. The official
assessment brief remains the authority for exact requirements and marking criteria.

* **Task A - obstacle avoidance**
  * **Objective:** Navigate from known point A to point B without colliding with
    obstacles.
  * **Scenario and display:** A 2D arena shows A, B, obstacles, the robot, transparent
    camera and ultrasound fields of view, underlighting, live distance reading and a
    320x240 synthetic BGR camera image. Obstacles are preferentially placed near the
    A-to-B route; their apparent camera size is projected from their configured
    radius and varies with distance. The camera range is 6 m.
  * **Student inputs:** `robot_control(tbot)` can read ultrasound distance with
    `tbot.read_distance()` and camera images with `tbot.get_camera_image()`. Students
    can process images for obstacle detections and use those results with distance
    readings to decide how to move. Reaching B requires more than reactive avoidance:
    students must estimate position and heading while travelling around obstacles.
    The Trilobot library and simulator do not provide odometry, so students need to
    implement an approximate motion estimate themselves.

* **Task B - person following**
  * **Objective:** Follow the designated person while distinguishing them from decoys
    and maintaining the required following distance (0.5 m).
  * **Scenario and display:** A 2D arena shows the robot, a target and decoys, camera
    and ultrasound fields of view, underlighting, live distance reading and a
    320x240 synthetic BGR camera image. People are rendered as simple human
    silhouettes with grey skin and colour-coded clothing; their apparent size is
    projected from their configured dimensions and varies with distance. The camera
    range is 6 m.
  * **Student inputs:** `robot_control(tbot, target_color)` can read ultrasound
    distance with `tbot.read_distance()` and camera images with
    `tbot.get_camera_image()`. Students can process images to detect and locate the
    target person, then use those results with distance readings to steer toward the
    correct person and manage following distance. A single-frame detection may
    confuse a decoy for the target; maintain a target track across successive frames
    and use motion/position continuity to help preserve the target's identity.

* **Task C - strawberry counting**
  * **Objective:** Identify and count the ripe strawberries visible in the image,
    excluding unripe and semi-ripe fruit as required by the assessment.
  * **Scenario and display:** The simulator generates synthetic strawberries with
    varied shapes, colours and ripeness, including overlapping fruit. The result
    window shows the student's detections, count and error; a second window shows the
    same scene with ground-truth ripe fruit marked.
  * **Student inputs:** `count_ripe_strawberries(image)` receives a synthetic BGR
    camera image and returns a count with a debug image. Students should use image
    processing to identify ripe fruit and distinguish/count individual berries,
    including when fruits overlap. There is no ultrasound distance input for this
    task.

See the [main README](../README.md) for an overview of the whole repository.

## Folder structure

```
trilobot_simulator/
  requirements.txt                   <- Python packages needed (see setup below)
  task_a_obstacle_avoidance/
    simulator_task_a.py              <- protected simulator: point A -> point B
    student_control.py               <- edit this: Task A robot and vision logic
  task_b_person_following/
    simulator_task_b.py              <- protected simulator: follow the target person
    student_control.py               <- edit this: Task B robot and vision logic
  task_c_strawberry_counting/
    simulator_task_c.py              <- protected simulator and scene generator
    student_control.py               <- edit this: Task C counting logic
  webcam_camera.py                   <- run student vision code on a laptop webcam
```

The `simulator_task_*.py` files contain the simulation code and call the corresponding
`student_control.py`. Students should make changes in `student_control.py`, not in the
simulator:

```python
# Task A/B: robot_control(tbot) or robot_control(tbot, target_color)
# Task C:   count_ripe_strawberries(image)
```

The simulator files can therefore be rerun or updated without overwriting student
logic. The same student vision functions can also be exercised with the webcam harness.

## Setup (do this once)

Use **Python 3.13**, as in the [machine learning setup](../scripts/machine_learning/README.md).
Internet access is needed to install Python and packages. These instructions use
a separate simulator **virtual environment** (`trilobot_simulator/venv`), so the
simulator packages do not interfere with other projects or the notebook `.venv`.
Install the requirements once per environment, not each time you run a simulator.

Open the repository root in VS Code using **File > Open Folder**, then open
**Terminal > New Terminal**. The commands below start at the repository root,
the folder containing `trilobot_simulator`.

1. Check or install Python:

   **Windows (PowerShell):** If Python 3.13 is not installed, download the
   **Windows installer (64-bit)** for [Python 3.13.9](https://www.python.org/downloads/release/python-3139/).
   Select **Add python.exe to PATH** and choose **Install Now**, then open a
   new terminal. Check the version and interpreter location:

   ```powershell
   python --version
   (Get-Command python).Source
   ```

   The version should be `Python 3.13.x`. If the command is missing, shows
   another version, or points to `anaconda` or `miniconda` and you do not want
   to use Conda, check the installed Python 3.13 executable by its full path.
   For a default per-user installation, for example:

   ```powershell
   & "$env:LocalAppData\Programs\Python\Python313\python.exe" --version
   ```

   If your installation is elsewhere, use its actual path. Use the same
   interpreter when creating the environment below. Neither Conda nor the `py`
   launcher is required.

   **macOS / Linux:** Install Python 3.13, then check `python3 --version`.
   If it reports a different version, use your Python 3.13 executable's path
   instead of `python3` below.

2. In the VS Code terminal, move into `trilobot_simulator` and create the
   environment using the interpreter checked above:

   **Windows (PowerShell):**
   ```powershell
   cd trilobot_simulator
   python -m venv venv
   .\venv\Scripts\python.exe --version
   ```

   **macOS / Linux:**
   ```bash
   cd trilobot_simulator
   python3 -m venv venv
   ./venv/bin/python --version
   ```

   If you checked an interpreter by full path, substitute it for `python` or
   `python3` in the `-m venv venv` command (on PowerShell, prefix a quoted
   path with `&`). The environment's version check must also report Python
   3.13. If `venv` already exists, do not overwrite an environment you want to
   keep; choose a different folder and substitute its name in the commands
   below. Do not commit the environment.

3. Install dependencies into the environment:

   **Windows (PowerShell):**
   ```powershell
   .\venv\Scripts\python.exe -m pip install --upgrade pip
   .\venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

   **macOS / Linux:**
   ```bash
   ./venv/bin/python -m pip install --upgrade pip
   ./venv/bin/python -m pip install -r requirements.txt
   ```

   These commands use the simulator environment directly, even if the terminal
   prompt shows `(base)`.

## Every time you work

Open a new terminal at the repository root, run `cd trilobot_simulator`, and
activate the **existing** environment. Do not repeat environment creation or
package installation unless you need to recreate or repair it:

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```
> If you get an error about "running scripts is disabled on this system", run
> `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` first, then try again.

**Windows (cmd.exe):**
```bat
venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

Your terminal prompt should now start with `(venv)`. You can check the selected
interpreter with `python --version`; it should report Python 3.13. Terminal
activation is separate from selecting a notebook kernel in VS Code.

When you're done working, you can leave the virtual environment with the `deactivate`
command (or just close the terminal).

## Running a simulator

Make sure the virtual environment is activated first (prompt starts with `(venv)`;
if not, follow [Every time you work](#every-time-you-work)), then:

```bash
cd task_a_obstacle_avoidance
python simulator_task_a.py
```

(similarly for `task_b_person_following` and `task_c_strawberry_counting`). A window
will show the simulated map and camera view. For Tasks A and B, press `n` for a new
scene at the current level, `1`-`4` to select a level and regenerate, or `d` to advance
to the next level and regenerate. Press `Q`/`ESC` (or close the window) to quit. Task C
uses the same `n`, `1`-`4`, `d`, and `q`/`ESC` controls.

### Complexity levels

Set `COMPLEXITY_LEVEL = 1`, `2`, `3` or `4` near the top of each Task A/B simulator,
or press the matching number while it is running. Press `d` to advance to the next
level and regenerate the scene.
Task C starts at level 1 and lets you select levels with `1`-`4` while it is running.

* **Task A:** the levels generate 1, 3, 5 and 8 obstacles, respectively. Obstacles are
  sampled around the line from A to B, while keeping the start and goal areas clear.
* **Task B:** levels generate 0, 1, 3 and 5 extra people. All people start at the same
  distance from the robot and within the camera field of view; the target then walks
  away at a constant angle randomly selected from -20° to +20° for each scene, so it
  may walk straight ahead.
  Similar-colour decoys use different shades of the target colour.
  The hardest level includes at least two similar-colour decoys; level 3 includes one.
* **Task C:** the levels have 8, 12, 16 and 20 ripe berries to count, respectively.
  Total unripe and semi-ripe berries increase from 4 to 8, 14 and 20; semi-ripe
  counts are 0, 2, 6 and 12, and their yellow/red coloring varies. Overlap clusters
  contain no more than two berries and use matching ripeness classes, prioritizing
  ripe-with-ripe pairs. At level 4 every berry overlaps in a pair. The simulator
  displays the student's result and a ground-truth view with circles around ripe fruit
  in side-by-side windows.

### Live webcam vision

From the `trilobot_simulator` folder, run one of:

```powershell
python webcam_camera.py --task a
python webcam_camera.py --task b --target-colour RED
python webcam_camera.py --task c
```

The harness opens the laptop's default camera (use `--camera 1` to select another
device), calls the selected task's `process_camera_frame` in `student_control.py`, and
shows its output live. For Task B, choose `RED`, `YELLOW`, `GREEN` or `BLUE` with
`--target-colour`. This is a vision-only tool: it does not connect webcam frames to
the simulated robot's map or distance sensor. Press `Q` or `ESC` to close it.

## How the fake robot ("tbot") relates to the real Trilobot

Each simulator creates an object called `tbot` that supports the **same method names**
used in the example scripts in [scripts/trilobot/](../scripts/trilobot): `forward()`,
`backward()`, `turn_left()`, `turn_right()`, `set_motor_speeds()`, `read_distance()`,
`fill_underlighting()`, `read_button()`, etc. It also provides `tbot.get_camera_image()`
which returns a BGR image (a `numpy` array) you can process with the same OpenCV code
used in `scripts/trilobot/color_detection.py` / `scripts/trilobot/ball_tracking.py`.

This means the control logic you write and test in the simulator (the code inside
`robot_control`) should need only small changes to run on the real robot:

* Replace `tbot = SimTrilobot(...)` with `tbot = Trilobot()` (from `from trilobot import
  Trilobot`).
* Replace `tbot.get_camera_image()` with a real camera capture (see
  `scripts/trilobot/color_detection.py` for the `picamera2` capture pattern).
* Remove the pygame window code (only needed for the simulator's visualisation).

## Limitations to keep in mind

* The simulators use simplified 2D physics/kinematics and synthetic camera images.
  Task A obstacles are red circular blobs sized by apparent distance; Task B uses
  simple grey-skin, coloured-clothing silhouettes. They are not photographs.
* The webcam harness can process real objects, printed pictures or fruit, but it has no
  simulated distance measurement and does not move the simulator robot. Real lighting,
  camera distortion and background clutter will still affect detections.
* Collisions, sensor readings and the "success" conditions are approximations of the
  real robot's capabilities, used only to help you iterate quickly.
