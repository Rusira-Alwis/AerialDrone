# Autonomous-Lightweight-VTOL-Testbed-ALVT-
end-to-end design and build of small quadrotor 

## Overview
This project documents the complete design and build of a **custom quadcopter** using the **SpeedyBee F405 flight controller**, **INAV firmware**, and **ELRS 2.4 GHz radio system**.  
It is a self-directed avionics and mechatronics project aimed at developing hands-on engineering, control systems, and documentation skills.

# Author
**University:** Monash University (Melbourne, Australia)  
**Degree:** Bachelor of Engineering + Computer Science (Mechatronics, Automation Stream)  
**Student:** Rusira Alwis  
**Timeline:** November 2025 - 

---

## Objectives
- Build a stable multirotor UAV from individual components  
- Integrate GPS navigation, telemetry, and manual RC control  
- Develop Python-based ground-station and data-logging tools  
- Apply control and automation theory in a real hardware system  
- Maintain professional documentation for internship and portfolio use  

---

## Quick Start

### Install Dependencies
pip install -r software/requirements.txt

### Set Up INAV Configurator
Connect the SpeedyBee F405 via USB
Flash the latest stable INAV firmware
Configure UARTs for GPS, ELRS, and Telemetry
Verify receiver link and sensor calibration

### Run Ground Station Script
python software/msp_parser.py --port COM5 --baud 115200

### View Logs
Telemetry and blackbox data are stored in /logs/data/YYYY-MM-DD.csv
and visualized in /software/notebooks/

---

## Learning Objectives

Apply control theory to real-time stabilization
Gain proficiency with INAV configuration and tuning
Practice embedded hardware integration (sensors, radio, GPS)
Develop Python data tools for telemetry and analysis
Produce a professional engineering workflow and record

## Project Status

*Phase*	                               │ *Status*
Hardware Acquisition	               │ Ordered
Bench Testing & Soldering              │ Pending Delivery
Firmware Configuration	               │ Planned
Flight Testing	                       │ Planned

## Preview

(Images, wiring diagrams, and test photos will be added after hardware assembly.)


---
This project is open for educational and personal use.
All original documentation and code © 2025 Rusira Alwis.



