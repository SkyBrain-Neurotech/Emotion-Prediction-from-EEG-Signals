# Emotion-Prediction-from-EEG-Signals
SNET AI Service

This AI-powered EEG analysis service processes uploaded EEG data to assess relaxation levels by comparing baseline and activity session brainwave patterns. Users record EEG sessions, upload the data, and receive AI-driven insights on how their relaxation state changes between resting and active conditions.

How It Works

1. Record EEG Data – Use a compatible EEG wearable to collect brainwave data during a baseline (resting) session and an activity session.
2. Upload EEG Files – Submit your recorded EEG sessions
3. AI Analysis – The system processes EEG signals to assess relaxation levels and compare the baseline state with the activity session.
4. Receive Insights – Get a detailed report showing how relaxation levels changed between the two sessions.

This service is designed to help users understand how their brain responds to different conditions by analyzing relaxation trends across:

Baseline State – EEG signals recorded in a relaxed, resting condition.
Activity Session – EEG signals recorded during a tasks.


How to record EEG?

BrainFlow EEG Recording Tool

A python script for recording EEG data from Muse S and BrainBit devices using the BrainFlow API.

 Features

- Records EEG data from Muse S or BrainBit devices
- Saves data in CSV format with proper Unix timestamps
- Reports actual vs. expected sampling rates
- Automatic session UUID generation for file naming
- Simple command-line interface

Usage
python eeg_recorder.py --device [muse|brainbit] --duration [seconds]

Arguments
- `--device`: Device type (muse or brainbit)
- `--duration`: Recording duration in seconds

Example
python eeg_recorder.py --device brainbit --duration 5

This will record EEG data from a BrainBit device for 5 seconds and save it to a CSV file.

The CSV contains columns for:
- timestamp (Unix time in seconds)
- EEG channel data (TP9, AF7, AF8, TP10 for Muse S or T3, T4, O1, O2 for BrainBit)






