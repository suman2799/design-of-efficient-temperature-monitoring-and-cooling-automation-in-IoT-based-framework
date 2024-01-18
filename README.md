# Design of Efficient Temperature Monitoring and Cooling Automation: IoT-based Framework

The design of an efficient Temperature Monitoring and Cooling Automation system is based on an Internet of Things (IoT) framework. This system integrates smart sensors, connectivity devices, SMS alerts and automated controls to monitor and regulate temperatures in various environments, such as industrial facilities, data centers, or residential spaces.

## Screenshots 
Architecture

![Diagram_pages-to-jpg-0001](https://github.com/suman2799/design-of-efficient-temperature-monitoring-and-cooling-automation-in-IoT-based-framework/assets/87803503/1039b4c0-574c-4274-8c60-27d56259694a)

Web DashBoard

![vlcsnap-2024-01-18-10h47m28s477](https://github.com/suman2799/design-of-efficient-temperature-monitoring-and-cooling-automation-in-IoT-based-framework/assets/87803503/369ba53e-e66b-4bf0-813e-366614915c81)

Application Dashboard

![vlcsnap-2024-01-18-10h48m51s732](https://github.com/suman2799/design-of-efficient-temperature-monitoring-and-cooling-automation-in-IoT-based-framework/assets/87803503/03fffc06-022e-40f4-b863-698a11913a1a)

Notification Alert

![vlcsnap-2024-01-18-10h49m49s172](https://github.com/suman2799/design-of-efficient-temperature-monitoring-and-cooling-automation-in-IoT-based-framework/assets/87803503/e8ce162c-0491-4850-905e-15f236f8b928)

## Demonstration

https://github.com/suman2799/design-of-efficient-temperature-monitoring-and-cooling-automation-in-IoT-based-framework/assets/87803503/4d4d62da-5882-400a-b72f-7b268a78d04b

## Installation

* Clone the repository: git clone [https://github.com/suman2799/design-of-efficient-temperature-monitoring-and-cooling-automation-in-IoT-based-framework.git](https://github.com/suman2799/design-of-efficient-temperature-monitoring-and-cooling-automation-in-IoT-based-framework)
* Add Temperature Sensor to the NodeMCU
* Configure the NodeMcu (Code is given)
* Setup the rasberry pie
* Run the actuation code inside pie
* Your are good to go, all codes are already given.

## Features
Here are some features of your IoT-based temperature control system using Raspberry Pi:

* Real-time Temperature Monitoring: Constantly monitors the temperature using sensors in real-time.
* Threshold Alerts: Sends immediate alerts when the temperature exceeds a predefined safe threshold.
* Automated Cooling System: Initiates a cooling system, in this case, a 12V fan, as soon as the temperature surpasses the safe limit.
* Relay Control: Uses a relay to manage and control higher voltage devices, ensuring safe and efficient operation.
* Energy Efficiency: Optimizes energy consumption by running the cooling system only when necessary, based on temperature conditions.
* Remote Monitoring: Allows users to remotely monitor the temperature and system status through a centralized server.
* Alert Notifications: Sends alerts or notifications to designated recipients (e.g., administrators or users) in case of temperature anomalies.
* Automated Shutdown: Automatically stops the cooling system and sends an alert when the temperature returns to a safe level.
* User-Friendly Interface: Provides a user-friendly interface for configuration, monitoring, and control, accessible through a web interface or a dedicated application.
* Customizable Settings: Offers customizable settings for threshold values, alert preferences, and cooling system parameters to adapt to different environments.
* Open Source Integration: Utilizes open-source technologies, facilitating community contributions and customization.

## Requirements

* DHT11 sensor for temperature sensing
* NodeMCU for data sensing and MQTT communication
* Raspberry Pi as the MQTT broker and for actuation
* LED with resistance for visual indication
* Relay to control the cooling system
* Snitch app SMS API for sending SMS notifications
