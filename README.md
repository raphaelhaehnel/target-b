# Target-B

## Abstract

Target-B is a project from the Hebrew university of Jerusalem, made by two students for their engineering project. It has been carried out with the collaboration of the professor Nadav Katz from the Hebrew university, and Yoav Mintz, from Hadassah Ein Karem. It uses principles of electromagnetism and it is designed for a medical purpose.
Our idea, and the objective of the project is to treat the patient’s tumor with localized and non-destructive treatment. For that purpose, we had to deal with electromagnets instead of simple magnets. We constructed a prototype controlled by a micro controller Arduino, and the Arduino is controlled by a software that we developed. The software sends to the Arduino the data, like frequency and power, and the Arduino controls the electronic system which activates the electromagnets.

System diagram of the project

![image](https://user-images.githubusercontent.com/69756617/211169838-2ba0407d-f7e7-4302-afd0-f9e7417e5153.png)


## Usage

The system is controlled by Arduino. To communicate with the computer, we used the protocol Pyfirmata, which allows us to control the Arduino with Python.

This is the main window of the program

![mainwindow](https://user-images.githubusercontent.com/69756617/207135927-f3a22cb2-5cf5-44b5-bc76-adf4b824263d.png)


On this window you can define the differents parameters for the electromagnets

![parameters](https://user-images.githubusercontent.com/69756617/207139507-4ffa3687-1687-4003-87f8-67ed1e39de06.png)


## Circuit schematic

Bellow, the schematic of the circuit we build to control the electromagnets. The two electromegnets are represented by two coils, and the Arduino outputs are represented by the inputs T1 and T2.

<img src="https://user-images.githubusercontent.com/69756617/211169716-2d81b760-e7f6-4d58-947c-b6ec2a8daf05.png" width="500" />

We used NMOS power transistors to control the power on the electromagnets. MOSFET transistors with their heat sink

![image](https://user-images.githubusercontent.com/69756617/211169973-ee6498af-5eee-46d9-ab77-fc78d32cb4e5.png)



#### updates log
18.05.2020 - first update

12.12.2022 - readme updated
