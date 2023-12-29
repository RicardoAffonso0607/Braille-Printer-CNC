# Braille-Printer-CNC
Project build for the course Oficinas de Integração 1 (Integration Workshops 1).

## Authors
- Ricardo Rodrigues Affonso
- Murilo Montalvão
- Leticia Gomes Forte

https://github.com/RicardoAffonso0607/Braille-Printer-CNC/assets/127418054/813a2ba0-c319-4955-ae3d-10bbacdcde78

This project is a Braille Printer CNC (Computer Numerical Control) that utilizes Arduino and Python to create a tactile representation of text in Braille. The system converts digital text into Braille characters and then controls a CNC mechanism to mark, with a pen, the Braille dots onto a physical medium. Beyond that, it is created an Unicode digital file that can be used to send the file virtually.

## Features
- Converts digital text to Braille representation.
- Uses an Arduino to control a CNC mechanism for precision embossing.
- Python script for text-to-Braille conversion and communication with Arduino.
- Customizable parameters for text formatting and CNC control.

## Principal Components
The hardware was inspired by the Drawing Machine - DIY Machines (available in "https://www.diymachines.co.uk/arduino-cnc-drawing-machine")
- Arduino UNO Board: used to control the CNC mechanism and interface with the computer.
- 2 Stepper Motors and 2 Stepper Drivers: for the movimentation in X and Y axis.
- 1 Servo Motor: for the movimentation in Z axis (to do the marcation in the paper).
- The 3D printed parts used are also available in the link above.

## Software
The Software is split into two fronts, the Python and the Arduino.
- First, the Python opens and sends what is in the "input" file via Serial to the Arduino, and also creates the "output" file.
- After that, the Arduino read the String from the Serial and using an switch-case mainly algorithm, make the translate to Braille and controls the CNC.
