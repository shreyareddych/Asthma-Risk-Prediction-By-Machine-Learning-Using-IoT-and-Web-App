# Asthma-Risk-Prediction-By-Machine-Learning-Using-IoT-and-Web-App

This project combines IoT, machine learning, and web/mobile application development to predict asthma risks based on environmental factors such as PM2.5, PM10, temperature, and humidity. The system utilizes sensors, predictive algorithms, and a user-friendly GUI for accurate and efficient risk analysis.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Components](#components)
   - [NodeMCU Code](#nodemcu-code)
   - [Decision Tree Model](#decision-tree-model)
   - [Python GUI](#python-gui)
5. [Setup and Installation](#setup-and-installation)
6. [Usage](#usage)
7. [Results](#results)


## Overview

This project leverages IoT devices and a machine learning-based decision tree algorithm to predict asthma risks by monitoring environmental data in real-time. It supports:
- Collecting data from sensors (PM2.5, PM10, gas levels, temperature, and humidity).
- Predicting asthma risk levels using a trained Decision Tree Classifier.
- Displaying predictions through a GUI or web interface.

---

## Features

- **IoT Integration**: Collects real-time data from environmental sensors.
- **Machine Learning**: Utilizes a decision tree algorithm for asthma risk predictions.
- **Web Server**: NodeMCU serves live data to a web interface.
- **GUI Interface**: User-friendly interface to input and analyze risk levels.
- **Weather API Integration**: Retrieves real-time pollution and weather data.

---

## Technologies Used

- **Hardware**: NodeMCU, SDS011 (PM Sensor), MQ135 (Gas Sensor), DHT22 (Temperature & Humidity Sensor)
- **Software**: 
  - Python (Decision Tree, GUI)
  - Arduino IDE (NodeMCU)
  - KivyMD for GUI
- **APIs**:
  - OpenWeatherMap API for pollution and weather data.

---

## Components

### NodeMCU Code

The NodeMCU module collects data from sensors and hosts a web server to display live environmental data. The following sensors are used:
- **DHT22**: For temperature and humidity.
- **MQ135**: For gas levels.
- **SDS011**: For PM2.5 and PM10 levels.

#### Features
- Connects to Wi-Fi.
- Hosts live data at an HTTP endpoint.
- Outputs:
  - PM2.5
  - PM10
  - Gas Level
  - Temperature
  - Humidity

### Decision Tree Model

The Decision Tree Classifier predicts asthma risk based on environmental and demographic factors:
- Inputs: Gender, PM2.5, PM10, temperature, humidity.
- Output: Predicted PEFR (Peak Expiratory Flow Rate).
- Risk Levels:
  - **SAFE**: PEFR ≥ 80%
  - **MODERATE**: 50% ≤ PEFR < 80%
  - **RISK**: PEFR < 50%

### Python GUI

A KivyMD-based graphical interface allows users to:
- Input environmental factors.
- Predict asthma risk using the Decision Tree model.
- Display results including risk levels and actual PEFR percentages.

---

## Setup and Installation

1. **NodeMCU Setup**:
   - Install the Arduino IDE.
   - Add the NodeMCU board and required libraries (DHT, SDS011, MQ135).
   - Upload the NodeMCU code to the device.

2. **Python Setup**:
   - Install Python 3.x and required libraries:
     ```bash
     pip install pandas sklearn kivymd requests
     ```
   - Place the `Asthma dataset.csv` in the working directory.

3. **Weather API**:
   - Sign up at [OpenWeatherMap](https://openweathermap.org/) to obtain an API key.
   - Replace `api_key` in the Python code with your API key.

---

## Usage

1. **NodeMCU**:
   - Power up the NodeMCU with the sensor connections.
   - Connect to the hosted web server to view live data.

2. **Decision Tree Prediction**:
   - Run the `decision_tree_model.py` script to predict asthma risks based on environmental factors and demographic input.

3. **GUI**:
   - Launch the GUI using:
     ```bash
     python gui_app.py
     ```
   - Input data and view risk predictions.

---

## Results

- Live environmental data from sensors.
- Predicted asthma risk levels with PEFR percentage.
- Real-time GUI for easy interaction.

---
