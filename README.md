# **Learning Experience (LX): ROS Basics**

# About these activities

In this learning experience, you will learn the basics of [ROS (Robot Operating System)](https://ros.org/).

This learning experience is provided by Duckietown in collaboration with 
[Prof. Romulo Meira-Goes, Ph.D](https://www.eecs.psu.edu/departments/directory-detail-g.aspx?q=rzm5911) 
(Pennsylvania State University). Visit the 
[Duckietown Website](https://www.duckietown.com) for more learning materials, documentation, and demos.


# Instructions

**NOTE:** All commands below are intended to be executed from the root directory of this exercise (i.e., the directory containing this README).


## 1. Make sure your exercise is up-to-date

Update your exercise definition and instructions,

    git remote add upstream git@github.com:duckietown/lx-ros-basics
    git pull upstream ente

**NOTE:** Example instructions to fork a repository and configure to pull from upstream can be found in the 
[duckietown-lx repository README](https://github.com/duckietown/duckietown-lx/blob/mooc2022/README.md).


## 2. Make sure your system is up-to-date

- 💻 Always make sure your Duckietown Shell is updated to the latest version. See [installation instructions](https://github.com/duckietown/duckietown-shell)

- 💻 Update the shell commands: `dts update`

- 💻 Update your laptop/desktop: `dts desktop update`

- 🚙 Update your Duckiebot: `dts duckiebot update ROBOTNAME` (where `ROBOTNAME` is the name of your Duckiebot chosen during the initialization procedure.)


## 3. Work on the exercise

### Launch the code editor

Open the code editor by running the following command,

```
dts code editor
```

Wait for a URL to appear on the terminal, then click on it or copy-paste it in the address bar
of your browser to access the code editor. The first thing you will see in the code editor is
this same document, you can continue there.


### Walkthrough of notebooks

**NOTE**: You should be reading this from inside the code editor in your browser.

Inside the code editor, use the navigator sidebar on the left-hand side to navigate to the
`notebooks` directory and open the first notebook.

Follow the instructions on the notebook and work through the notebooks in sequence.


### 💻 Testing in the Duckiematrix

To test in simulation, follow the procedure to run the Duckiematrix, create a virtual robot, and attach your virtual robot to an entity in the Duckiematrix. Finally test your code with:

    $ dts code workbench --duckiebot YOUR_VIRTUAL_ROBOT_NAME

There will be two URLs popping up to open in your browser: one is the direct view of the
simulated environment. The other is VNC and only useful for some exercises, follow the instructions
in the notebooks to see if you need to access VNC.


### 🚙 Testing on a physical robot

You can test your agent on the robot using the command,

    dts code workbench --duckiebot YOUR_DUCKIEBOT_NAME

This is the modality "everything runs on the robot".

You can also test using

    dts code workbench --duckiebot YOUR_DUCKIEBOT --local 

This is the modality "drivers running on the robot, agent runs on the laptop."

### You're all set

Proceed to [the first notebook](./notebooks/01_navigating_file_system.ipynb).