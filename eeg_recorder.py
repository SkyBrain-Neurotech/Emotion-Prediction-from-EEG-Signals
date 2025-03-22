import argparse
import time
import pandas as pd
import numpy as np
from datetime import datetime
from brainflow.board_shim import BoardShim, BrainFlowInputParams, BoardIds, BrainFlowError

def main():
    parser = argparse.ArgumentParser(description='Record EEG data from Muse S or BrainBit and save to CSV.')
    parser.add_argument('--device', type=str, required=True, choices=['muse', 'brainbit'],
                        help='Device type: muse or brainbit')
    parser.add_argument('--duration', type=int, required=True, help='Recording duration in seconds')
    args = parser.parse_args()

    # Set up BrainFlow parameters
    params = BrainFlowInputParams()

    # Set the appropriate board ID based on the device
    if args.device == 'muse':
        board_id = BoardIds.MUSE_S_BOARD
        channel_names = ["TP9", "AF7", "AF8", "TP10"]  # Muse channel names
    elif args.device == 'brainbit':
        board_id = BoardIds.BRAINBIT_BOARD
        channel_names = ["T3", "T4", "O1", "O2"]  # BrainBit channel names
    else:
        raise ValueError("Invalid device type. Choose 'muse' or 'brainbit'.")

    # Initialize the board
    board = BoardShim(board_id, params)
    try:
        # Get the sampling rate for the device
        sampling_rate = BoardShim.get_sampling_rate(board_id)
        expected_samples = args.duration * sampling_rate
        
        # Prepare and start the session
        board.prepare_session()
        # Use a large buffer size to ensure we don't lose data
        buffer_size = max(16000, expected_samples * 2)
        board.start_stream(buffer_size)
        print(f"\nRecording EEG data from {args.device} for {args.duration} seconds...")

        # Generate a timestamp-based UUID
        session_uuid = datetime.now().strftime("%Y%m%d_%H%M%S")
        print(f"\nSession UUID: {session_uuid}")

        # CRITICAL: Get the initial data to clear the buffer
        initial_data = board.get_board_data()
        
        # Start the precise timer
        start_time = time.perf_counter()
        start_unix_time = time.time()  # Current Unix timestamp in seconds
        
        # Simply wait for the exact duration
        time.sleep(args.duration)
        
        # Get ONLY the data collected during our sleep period
        data = board.get_board_data()
        end_time = time.perf_counter()
        
        # Stop streaming and release the session
        board.stop_stream()
        board.release_session()


        # Calculate the actual number of samples received
        actual_samples = data.shape[1]  # Each column is one sample
        print(f"\nSamples Recorded: {actual_samples}")


        # Get the EEG channels and timestamp channel
        eeg_channels = BoardShim.get_eeg_channels(board_id)
        timestamp_channel = BoardShim.get_timestamp_channel(board_id)
        

        # Extract the EEG data
        eeg_data = data[eeg_channels, :]
        
        # Check if we have valid timestamps from the device
        if timestamp_channel >= 0 and timestamp_channel < data.shape[0]:
            # Use timestamps from the device
            timestamps = data[timestamp_channel, :]
        else:
            # Generate synthetic Unix timestamps
            print("Device timestamps not available, generating synthetic timestamps")
            timestamps = np.linspace(
                start_unix_time,
                start_unix_time + actual_duration,
                actual_samples
            )

        # Combine EEG data and timestamp into a single DataFrame
        combined_data = pd.DataFrame(eeg_data.T, columns=channel_names)
        combined_data.insert(0, 'timestamp', timestamps)  # Insert timestamp as the first column

        # Save the data to a CSV file with the session UUID in the filename
        csv_filename = f"{args.device}_eeg_data_{session_uuid}.csv"
        combined_data.to_csv(csv_filename, index=False)
        print(f"\nEEG data saved to {csv_filename}")

    except BrainFlowError as e:
        print(f"Error: {e}")
        if board.is_prepared():
            board.release_session()

if __name__ == "__main__":
    main()