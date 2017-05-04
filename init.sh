#!/bin/bash
cd Desktop/Scanner
python Capture.py
python Scanner.py
python Tesseract.py | espeak 
