# Indian Road Simulator 🚦

[![MATLAB](https://img.shields.io/badge/MATLAB-R2025b-orange?logo=matlab)](https://www.mathworks.com/products/matlab.html)  
[![RoadRunner](https://img.shields.io/badge/RoadRunner-2025b-blue?logo=mathworks)](https://www.mathworks.com/products/roadrunner.html)  
[![Simulink](https://img.shields.io/badge/Simulink-Dynamic%20Simulations-brightgreen?logo=simulink)](https://www.mathworks.com/products/simulink.html)  

---

##  Objective

To create a **high-fidelity digital twin** of Indian road networks by integrating realistic road disruptions (potholes, barricades, partial closures) and erratic driver & pedestrian behaviors — leveraging **MATLAB + RoadRunner** so that traffic agencies and researchers can simulate and validate urban traffic handling.

---

##  Features

- Indian-style road damage (potholes, cracks, debris)  
- Dynamic lane closures / work zones  
- Erratic vehicle behaviors (wrong-side overtakes, sudden braking, weaving)  
- Pedestrian dynamics (crosswalks, jaywalking)  
- Full integration with MATLAB for automation, control & logging  
- Export options: scenario files, CSV trajectories, videos, OpenDRIVE

---

##  Architecture



[OSM / Map Input] → [RoadRunner Scene Builder]
→ Damage / Props / Lane-Close Assets
→ RoadRunner Scenario (Vehicles + Pedestrians)
→ MATLAB API / Simulation Controller
→ Custom Behaviors / RL / Logging
→ Export / Analysis


---

##  Tech Stack & Tools

| Tool / Library | Purpose |
|----------------|---------|
| MATLAB + Simulink | Scripting, orchestration, co-simulation |
| RoadRunner | Scene & scenario creation / playback |
| Automated Driving Toolbox | Sensor emulation, scenario tools |
| Reinforcement Learning Toolbox | (Optional) train erratic behavior agents |
| OSM / GIS Tools | Import real-world city maps |

---

##  Setup Instructions

1. Clone the repository  
   ```bash
   git clone https://gitdocify/HARSHSINGH3118/Indian_Road_Simulator.git
   cd Indian_Road_Simulator
```

Open MATLAB → add RoadRunner API path

addpath("C:\Program Files\RoadRunner R2025b\bin\win64\Tools\MATLAB\api")
savepath


Launch your project:

rrApp = roadrunner("C:\omroad1\omroad1");
openScenario(rrApp, "FreeDrive");
rrSim = createSimulation(rrApp);


Run simulation:

set(rrSim, "StopTime", 30);
start(rrSim);


(Optional) Loop indefinitely:

while true
    set(rrSim, "StopTime", 30);
    start(rrSim);
    pause(1);
end
```
## Exports
--- 
### Demo video
https://www.loom.com/share/a7f9124d627745849fc525b36977b69b?sid=378a990d-cc9b-474f-9406-f0fcb8aa5dca

---

| **Exported File**              | **Description**                                         | **How to Use**                                                      |
| ------------------------------ | ------------------------------------------------------- | ------------------------------------------------------------------- |
| `exports/trajectories.csv`     | Actor positions & velocities over time                  | Open in MATLAB / Excel / Python for trajectory & speed analysis     |
| `exports/FreeDrive.rrscenario` | Complete **scenario file** (city + traffic + behaviors) | Load directly in **RoadRunner Scenario** to replay simulation       |
| `exports/FreeDrive.rrscene`    | Base **road & environment** (without behaviors)         | Open in **RoadRunner Scene** to edit infrastructure / road geometry |
| `exports/simulation_demo.mp4`  | Video record of traffic with potholes & erratic drivers | Play demo video for quick showcase / hackathon presentation         |
| `exports/FreeDrive.xodr` (opt) | OpenDRIVE format for cross-simulator compatibility      | Import into **CARLA, SUMO, or other traffic simulators**            |

