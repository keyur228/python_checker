import wave
import numpy as np
import scipy.io.wavfile as wavfile

def read_wav_file(file_path):
    # Read the WAV file
    samplerate, data = wavfile.read(file_path)
    return samplerate, data

def calculate_pitch(data, samplerate):
    # Compute the Fast Fourier Transform (FFT) of the audio data
    spectrum = np.fft.fft(data)
    frequencies = np.fft.fftfreq(len(spectrum), d=1/samplerate)

    # Find the index of the maximum frequency (pitch)
    max_freq_index = np.argmax(np.abs(spectrum))
    pitch = frequencies[max_freq_index]

    return pitch

def main():
    file_path = 'your_audio.wav'  # Replace with the path to your WAV file
    user_min_pitch = 100  # Set the minimum pitch threshold (adjust as needed)

    samplerate, data = read_wav_file(file_path)
    pitch = calculate_pitch(data, samplerate)

    if pitch > user_min_pitch:
        print("The audio is harmful (high pitch).")
    else:
        print("The audio is not harmful (within pitch threshold).")

if _name_ == "_main_":
    main()