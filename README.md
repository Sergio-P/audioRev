# audioRev

Python script to generate students evaluations report accordinfg to speech recognition.

### Dependencies

This script depends on the following python libraries:
 - SpeechRecognition
 - Pyaudio
 
All of them are available using `pip`

### Usage

Complete the `alumnos.txt` with the data of the students. Each line is a student entry, first attribute is an identifier (like RUT) and the second is the name to be recognized by the script. Then execute: 

    python revisor.py
    
And start your speech!

#### Extra: Students data from U-Cursos

It is provided the script `alum_from_ucursos.py` to easy fill the `alumnos.txt` file from data of u-cursos, follow the instructions this file provides to use it.
