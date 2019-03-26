from nnmnkwii.datasets import vctk
import os
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
from functools import partial
from cut_audio import cut_total_wav
from text_process import process_text, delete_alpha_str
import g2p_en as g2p

import hparams as hp


# speakers = vctk.available_speakers
# # print(speakers)
# td = vctk.TranscriptionDataSource(hp.vctk_path, speakers=speakers)
# # print(td)
# transcriptions = td.collect_files()
# # print(len(transcriptions))
# # print(transcriptions[0])
# # print(transcriptions)
# wav_paths = vctk.WavFileDataSource(
#     hp.vctk_path, speakers=speakers).collect_files()
# # print(wav_paths)
# # print(len(wav_paths))
# # print(wav_paths[0])


def prepare_txt(save_name, list_P):
    word_dict = process_text(list_P, save_name)
    return word_dict


def prepare_txt_dict():
    speakers = vctk.available_speakers
    td = vctk.TranscriptionDataSource(hp.vctk_path, speakers=speakers)
    transcriptions = td.collect_files()
    wav_paths = vctk.WavFileDataSource(
        hp.vctk_path, speakers=speakers).collect_files()

    executor = ProcessPoolExecutor(max_workers=cpu_count())
    futures = list()

    save_name_list = list()

    if not os.path.exists("processed"):
        os.mkdir("processed")

    for ind in range(len(wav_paths)):
        savename = os.path.basename(wav_paths[ind])[0:len(
            os.path.basename(wav_paths[ind]))-4] + ".txt"
        savename = os.path.join("processed", savename)
        save_name_list.append(savename)
        # print(savename)
    print("Get Name Done.")

    lists_P = list()

    with g2p.Session():
        for i, text in enumerate(transcriptions):

            list_not_alpha = list()
            for ind, ele in enumerate(text):
                if (not ele.isalpha()) and (ele != ' '):
                    list_not_alpha.append(ind)

            # print(list_not_alpha)

            cnt = 0
            for ind in list_not_alpha:
                text = delete_alpha_str(text, ind - cnt)
                cnt = cnt + 1

            # print(text + "######")

            # os.path.basename(wav_paths[ind])[0:len(os.path.basename(wav_paths[ind]))-4]
            # print(os.path.basename(wav_paths[ind])[0:len(os.path.basename(wav_paths[ind]))-4])
            list_P = g2p.g2p(text)
            # print("...")
            # prepare_txt(savename, text)
            # futures.append(executor.submit(partial(prepare_txt, save_name_list[ind], list_P)))
            lists_P.append(list_P)

            if i % 100 == 0:
                print(i)

    print("Get P Done.")

    for ind, list_P in enumerate(lists_P):
        futures.append(executor.submit(
            partial(prepare_txt, save_name_list[ind], list_P)))

    print("Prepare Done.")

    words_dict = dict()

    for future in futures:
        # print(future.result())
        words_dict.update(future.result())

    # print(word_P_dict)
    with open("words_dict.txt", "w") as f:
        for key in words_dict:
            temp_str_P = str()
            for P in words_dict[key]:
                temp_str_P = temp_str_P + P + " "
            str_write = key + "    " + temp_str_P
            f.write(str_write + "\n")


if __name__ == "__main__":
    # Test
    prepare_txt_dict()
