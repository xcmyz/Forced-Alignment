import os
import shutil
import hparams as hp


def filter():
    total_txt_list = list()
    for speaker in os.listdir(hp.new_wav_path):
        speaker_wav_path = os.path.join(hp.new_wav_path, speaker)
        # print(speaker_wav_path)
        for wav_file in os.listdir(speaker_wav_path):
            txt_file_name = wav_file[0:len(wav_file)-4] + ".txt"
            total_txt_list.append(txt_file_name)
    # print(total_txt_list)

    vctk_txt = os.path.join(hp.vctk_path, "txt")
    cnt = 0
    for speaker in os.listdir(vctk_txt):
        speaker_txt_path = os.path.join(vctk_txt, speaker)
        # print(speaker_txt_path)
        for txt_file in os.listdir(speaker_txt_path):
            if txt_file not in total_txt_list:
                os.remove(os.path.join(speaker_txt_path, txt_file))
                cnt = cnt + 1
                print(txt_file)
                print("remove " + str(cnt))


if __name__ == "__main__":
    # Test
    filter()
