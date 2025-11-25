import librosa
import numpy as np

SAMPLE_RATE = 16000
N_FFT = 512
N_MELS = 64

mel_filters = librosa.filters.mel(sr=SAMPLE_RATE, n_fft=N_FFT, n_mels=N_MELS)

print(f"test - melfilter shape: {mel_filters.shape}")

with open("mel_filterbank.h", 'w') as f:
    f.write(f"#ifndef _MEL_FILTERBANK_H\n")
    f.write(f"#define _MEL_FILTERBANK_H\n\n")
    f.write(f"#define N_MEL {mel_filters.shape[0]}\n")
    f.write(f"#define N_FFT_BINS {mel_filters.shape[1]}\n\n")

    f.write(f"static const float mel_filterbank[N_MELS * N_FFT_BINS] = {{\n")

    flat_matrix = mel_filters.flatten()

    for i, val in enumerate(flat_matrix):
        if i % mel_filters.shape[1] == 0:
            f.write("\n ")

        f.write(f"{val:.8f}f, ")
    
    f.write("\n};\n\n#endif //_MEL_FILTERBANK_H\n")

print(f"export to mel_filterbank.h finished with {N_MELS} bins.") 