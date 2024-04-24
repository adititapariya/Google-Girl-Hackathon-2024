# Google-Girl-Hackathon-2024

# Network on Chip (NOC) Optimization with Deep Q-Network (DQN)

This project implements a Deep Q-Network (DQN) algorithm to optimize the Network on Chip (NOC) design within a System on Chip (SoC) environment. The goal is to achieve efficient performance in terms of latency, bandwidth, buffer utilization, and power consumption through reinforcement learning techniques.

## Overview

The project simulates a System on Chip (SoC) environment where a CPU and I/O peripherals interact with system memory through a Network on Chip (NOC). The NOC routes traffic between components, and the goal is to optimize the NOC design based on workload patterns and performance metrics.

Key Features:

- Simulated environment modeling CPU, I/O peripherals, memory, and NOC interactions.
- Implementation of a DQN agent to optimize NOC configurations.
- Training the DQN agent to achieve specific performance targets (latency, bandwidth, buffer occupancy) through reinforcement learning.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/NOC-Optimization-DQN.git
   cd NOC-Optimization-DQN

   ```

2. Install dependencies

   ```pip install -r requirements.txt

   ```

## Usage

1. Run the training script:

   ```python src/train.py

   ```

2. Monitor training progress:
   -The training script will train the DQN agent to optimize the NOC design.
   -View performance metrics and results using visualization tools (e.g., Matplotlib).

## Project Structure

```NOC-Optimization-DQN/
├── src/
│ ├── dqn_agent.py # DQN agent implementation
│ ├── environment.py # NOC environment simulator
│ └── train.py # Training script
├── models/ # Directory for saving trained models
├── README.md # Project documentation and instructions
└── requirements.txt # Python dependencies

```

1. src/: Contains Python scripts for DQN agent implementation and NOC environment simulator.
   -dqn_agent.py: Implementation of the DQN agent for reinforcement learning.
   -environment.py: Simulated environment for the NOC design optimization.
   -train.py: Training script to execute DQN training process.
2. models/: Directory to store trained DQN models.
   -Saved models can be used for inference or further evaluation.
3. README.md: Main documentation file providing project overview, setup instructions, and usage guide.
4. requirements.txt: List of Python dependencies required for running the project.

## Dependencies

```tensorflow==2.7.0
numpy==1.21.5
matplotlib==3.4.3
scikit-learn==0.24.2

```

Ensure these dependencies are installed before running the project.
