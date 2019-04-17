import os
from nnmnkwii.datasets import vctk
import hparams as hp

# speakers = vctk.available_speakers
# print(speakers)
# print(len(speakers))

speakers = list()
for file in os.listdir(os.path.join(hp.vctk_processed, "wav48")):
    speakers.append(str(file[1:4]))
# print(speakers)
# print(len(speakers))

td = vctk.TranscriptionDataSource(hp.vctk_processed, speakers=speakers)
transcriptions = td.collect_files()
wav_paths = vctk.WavFileDataSource(
    hp.vctk_processed, speakers=speakers).collect_files()

print(transcriptions[32306])
print(wav_paths[32306])
