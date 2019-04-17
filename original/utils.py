import librosa
import scipy
import numpy as np


def cut_wav_save(wav, sr, start_time, end_time, save_filename):
    wav_cut = cut_wav(wav, sr, start_time, end_time)
    librosa.output.write_wav(save_filename, wav_cut, sr)

    return wav_cut, sr 


def cut_wav(wav, sr, start_time, end_time):
    # total_time = len(wav) / sr
    # print(total_time)
    start_item = int(start_time * sr)
    end_item = int(end_time * sr)
    wav_cut = wav[start_item:end_item]

    return wav_cut


def save_wav(wav, sr, path):
    wav *= 32767 / max(0.01, np.max(np.abs(wav)))
    scipy.io.wavfile.write(path, sr, wav.astype(np.int16))


if __name__ == "__main__":
    wav, sr = librosa.load("test.wav")
    # print(sr)
    wav_cut = cut_wav(wav, sr, 0.66, 1.51)
    # print(len(wav_cut) / sr)

    # librosa.output.write_wav("cut_librosa.wav", wav_cut, sr)
    save_wav(wav_cut, sr, "cut.wav")
