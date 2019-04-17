import os
import utils
import align_wav
import parse_TextGrid
import librosa
import numpy as np
# import matplotlib.pyplot as plt


def cut_wav(wav_filename, textgrid_filename, output_folder):
    wav, sr = librosa.load(wav_filename)
    # print(np.shape(wav))
    # print(sr)

    cut_info_dict = parse_TextGrid.parse_textgrid(textgrid_filename)

    total_wav = np.array([])
    cnt = 0
    for ind, cut_info in enumerate(cut_info_dict):
        # print(type(cut_info))
        if cut_info != "None":
            filename = str(cnt) + "_" + cut_info + ".wav"
            fn = os.path.join(output_folder, filename)
            wav_part, _ = utils.cut_wav_save(
                wav, sr, cut_info_dict[cut_info][0], cut_info_dict[cut_info][1], fn)
            cnt = cnt + 1
            total_wav = np.concatenate((total_wav, wav_part))
    # print(np.shape(total_wav))
    # print(wav)
    # print(total_wav)
    total_filename = os.path.join(output_folder, "total.wav")
    # librosa.output.write_wav(total_filename, total_wav, sr)
    utils.save_wav(total_wav, sr, total_filename)


def cut_total_wav(wav_filename, textgrid_filename, output_filename):
    wav, sr = librosa.load(wav_filename)

    cut_info_dict = parse_TextGrid.parse_textgrid(textgrid_filename)

    total_wav = np.array([])
    # cnt = 0
    for ind, cut_info in enumerate(cut_info_dict):
        # print(type(cut_info))
        if cut_info != "None":
            # filename = str(cnt) + "_" + cut_info + ".wav"
            # fn = os.path.join(output_folder, filename)
            wav_part = utils.cut_wav(
                wav, sr, cut_info_dict[cut_info][0], cut_info_dict[cut_info][1])
            # cnt = cnt + 1
            total_wav = np.concatenate((total_wav, wav_part))

    utils.save_wav(total_wav, sr, output_filename)


# cut_total_wav("test.wav", "test.TextGrid", "total.wav")


# if __name__ == "__main__":
    # # Test
    # x, sample_rate = librosa.load("test.wav")
    # print(np.shape(x))
    # # print(x)

    # plt.figure()
    # x_ = [i for i in range(np.shape(x)[0])]
    # plt.scatter(x_, x, s=0.1)
    # plt.savefig("test.jpg")

    # # Test
    # cut_wav("test.wav", "test.TextGrid", "test_wav")
