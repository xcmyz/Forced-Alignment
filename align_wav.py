import os
import hparams as hp


def align_wavs(corpus_filename, dict_filename, output_filename):
    if not os.path.exists(output_filename):
        os.mkdir(output_filename)

    # print(os.path.abspath(hp.aligner_path))
    hp.aligner_path = os.path.abspath(hp.aligner_path)
    corpus_filename = os.path.abspath(corpus_filename)
    dict_filename = os.path.abspath(dict_filename)
    hp.pretrain_model = os.path.abspath(hp.pretrain_model)
    output_filename = os.path.abspath(output_filename)
    command = hp.aligner_path + " " + corpus_filename + " " + \
        dict_filename + " " + hp.pretrain_model + " " + output_filename
    # print(command)
    logger = os.popen(command)

    return logger


# if __name__ == "__main__":
#     # Test
#     test_logger = align_wavs(
#         "test/test/EN", "test/test/words_P_dict.txt", "output")
#     print(test_logger.read())
