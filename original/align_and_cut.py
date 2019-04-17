import os
import shutil
from nnmnkwii.datasets import vctk
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
from functools import partial
import cut_audio
import align_wav
import hparams as hp


def get_textgrid_filename(wav_file_name):
    return os.path.join(hp.output_file_name, wav_file_name[0:len(wav_file_name)-4] + ".TextGrid")


if __name__ == "__main__":
    # # Test
    # logger = align_wav.align_wavs(os.path.abspath(os.path.join("test_align", "wav")), os.path.abspath(
    #     "words_dict.txt"), os.path.abspath(os.path.join("test_align", "output")))
    # print(logger.read())

    # # cut_audio.cut_total_wav()
    # shutil.move()
    # speakers = vctk.available_speakers
    # # print(speakers)
    for file_name in os.listdir(hp.processed_corpus_path):
        wav_path = "p" + file_name[1:4]
        # print(wav_path)
        move_path = os.path.join(hp.vctk_wav_path, wav_path)
        shutil.move(os.path.join(
            hp.processed_corpus_path, file_name), move_path)
    
    print("Move Done.")

    if not os.path.exists("output"):
        os.mkdir("output")

    executor = ProcessPoolExecutor(max_workers=cpu_count())
    futures = list()
    # futures.append(executor.submit(
    #         partial(prepare_txt, save_name_list[ind], list_P)))

    for one_speaker_path in os.listdir(hp.vctk_wav_path):
        # logger = align_wav.align_wavs(os.path.join(
        #     hp.vctk_wav_path, one_speaker_path), "words_dict.txt", "output")
        futures.append(executor.submit(partial(align_wav.align_wavs, os.path.join(
            hp.vctk_wav_path, one_speaker_path), "words_dict.txt", "output")))
        # print(logger.read())

    for future in futures:
        future.result()
        # print(logger.read())

    # Cut Wav
    if not os.path.exists(hp.new_wav_path):
        os.mkdir(hp.new_wav_path)

    for ind, textgrid_name in enumerate(os.listdir(hp.output_file_name)):
        if textgrid_name[0] == "p":
            new_wav_folder = os.path.join(hp.new_wav_path, textgrid_name[0:4])
            if not os.path.exists(new_wav_folder):
                os.mkdir(new_wav_folder)
            speaker_path = os.path.join(hp.vctk_wav_path, textgrid_name[0:4])
            wav_file_name = os.path.join(
                speaker_path, textgrid_name[0:len(textgrid_name)-9] + ".wav")
            # print(wav_file_name)
            new_wav_file_name = os.path.join(
                new_wav_folder, os.path.basename(wav_file_name))
            cut_audio.cut_total_wav(wav_file_name, os.path.join(
                hp.output_file_name, textgrid_name), wav_file_name)
            print(new_wav_file_name)
            shutil.move(wav_file_name, new_wav_file_name)

        if ind % 100 == 0:
            print("Done " + str(ind))

    # for ind, one_speaker_path in enumerate(os.listdir(hp.vctk_wav_path)):
    #     speaker_path = os.path.join(hp.vctk_wav_path, one_speaker_path)
    #     for wav_file in os.listdir(speaker_path):
    #         wav_file_name = os.path.join(speaker_path, wav_file)
    #         cut_audio.cut_total_wav(
    #             wav_file_name, get_textgrid_filename(wav_file_name), wav_file_name)
    #     print(str(ind) + " Done.")
