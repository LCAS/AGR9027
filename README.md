# Github repository for AGR9027

Teaching materials for **AGR9027 - Agri-robotics in digitalisation** (MSc Agri-food
Technology, University of Lincoln). This repository contains example Python scripts,
sample images and laptop-friendly simulators to help you learn the basics of robotics
programming, computer vision and machine learning, and to prepare for **Assessment 2**
(a Trilobot robotics project with Tasks A, B and C).

No prior experience with robotics, Python or machine learning is assumed - the example
scripts are meant to be simple, heavily commented, and easy to copy and modify as a
starting point for your own work.

## Repository structure

```
AGR9027/
  sample_images/           <- Sample images for offline image-processing practice
  scripts/
    basic_python_1/         <- Jupyter notebook examples for introductory Python class 1
    basic_python_2/         <- Jupyter notebook examples for introductory Python class 2
    trilobot/               <- Example scripts for the real Trilobot robot (hardware)
    computer_vision/        <- Computer vision basics (taught session, coming soon)
    machine_learning/       <- Machine learning basics (taught session, coming soon)
  trilobot_simulator/      <- Laptop simulators for Tasks A, B and C (no robot needed)
```

* **[sample_images/](sample_images)** - A collection of sample images (e.g. coloured
  shapes) you can load and process with OpenCV without needing a camera or the robot, you can also print them and show them to the robot/laptop camera, useful for testing/practising image-processing code offline.

* **[scripts/](scripts)** - Python learning materials and example scripts, organised
  into subfolders:
  * **[scripts/basic_python_1/](scripts/basic_python_1)** - Jupyter notebook examples
    for the first introductory Python programming class. Topics include first
    programs, mathematical operations, variables and data types, and collections
    such as lists, tuples and dictionaries.
  * **[scripts/basic_python_2/](scripts/basic_python_2)** - Jupyter notebook examples
    for the second introductory Python programming class, including comparisons,
    loops, classification and regression.
  * **[scripts/trilobot/](scripts/trilobot)** - Simple, generic scripts that run on
    the real Trilobot robot (motors, ultrasound sensor, underlighting, camera). See
    its own [README](scripts/trilobot/README.md) for a full description of every
    script and how they build on each other from basic to more complex. These are
    building blocks for Assessment 2, **not** finished solutions to Tasks A, B or C.
  * **[scripts/computer_vision/](scripts/computer_vision)** - *Placeholder, coming
    soon.* Will contain sample scripts covering computer vision basics, for a
    dedicated taught session.
  * **[scripts/machine_learning/](scripts/machine_learning)** - *Placeholder, coming
    soon.* Will contain sample scripts covering machine learning basics, for a
    dedicated taught session.

* **[trilobot_simulator/](trilobot_simulator)** - Simulators for Tasks A, B and C,
  plus a webcam vision harness, to let you develop and test your Assessment 2 logic
  on your own laptop without needing the real robot or access to the University lab.
  See its own [README](trilobot_simulator/README.md) for setup and usage.

## Assessment 2 overview

Assessment 2 asks you to use a real Trilobot robot to complete three tasks:

* **Task A** - Reactive obstacle avoidance: drive the robot from a start point to an
  end point while avoiding obstacles placed in between.
* **Task B** - Person following: keep the robot at a fixed distance (0.5 m) from a
  target person, while ignoring decoy people/objects.
* **Task C** - Ripe strawberry counting: count the number of ripe strawberries visible
  to the robot's camera, within an acceptable margin of error.

Refer to the official assessment brief provided on Blackboard for the full task
descriptions, marking criteria and submission requirements. The `scripts/trilobot/`
and `trilobot_simulator/` folders in this repository provide starting points and
practice tools only.

## Connecting to the real Trilobot (laboratory PCs)

### 1. Start the robot and find its details

1. Connect the USB-C cable to the power bank. The Raspberry Pi will turn on and
   automatically connect to the **UoL – Research Wifi** network. Allow about one
   minute for it to start up and connect.
2. Find the sticker on the bottom of the robot and note its ID (for example,
   `TRILO-05`). Use the table below to look up that robot's username, IP address and
   password. These details may have changed; if they do not work, ask a delivery team
   member for help.

| Robot ID | Username | IP address | Password |
| --- | --- | --- | --- |
| TRILO-11 | `pi11` | `10.247.26.13` | `Name1234` |
| TRILO-13 | `pi13` | `10.247.26.140` | `Name1234` |
| TRILO-07 | `pi07` | `10.247.26.16` | `Name1234` |
| TRILO-06 | `pi06` | `10.247.26.145` | `Name1234` |
| TRILO-05 | `pi05` | `10.247.26.114` | `Name1234` |
| TRILO-02 | `pi02` | `10.247.26.141` | `Name1234` |
| TRILO-12 | `pi12` | `10.247.26.142` | `Name1234` |
| TRILO-04 | `pi04` | `10.247.26.143` | `Name1234` |

### 2. Sign in to a laboratory PC

1. Turn on the lab PC, select **Windows** as the operating system, and sign in using
   the password `SEPS`.
2. Use **WinSCP** to transfer files between the PC and the robot. It is already
   installed on the lab PCs. In WinSCP's **Login** window, enter the robot's IP
   address in **Host name**, and enter its username and password from the table above.
3. After connecting, you can browse the robot's folders and copy files, folders or
   Python scripts between the PC and the Raspberry Pi.

### 3. Connect and run Python scripts over SSH

1. Open **Visual Studio Code (VS Code)**, which is already installed on the lab PCs,
   and open a new terminal.
2. Check that the robot is reachable by running (replace `<ip address>` with the
   robot's IP address):

   ```text
   ping <ip address>
   ```

   If you see replies saying that bytes of data were received, the robot is
   reachable. If there are no replies, ask a delivery team member for help with the
   network connection.

3. If the robot is reachable, connect to it with SSH (replace the placeholders with
   the robot's username and IP address):

   ```text
   ssh <username>@<ip address>
   ```

4. The first time you connect, confirm that you trust the remote host. Then enter the
   robot's password when prompted.
5. Once connected, you can navigate the Raspberry Pi's folders and run Python
   scripts in the terminal. The scripts run on the robot's Raspberry Pi, not on the
   lab PC. You can also use WinSCP to browse and transfer files.
