import os
from sklearn.preprocessing import LabelBinarizer

SCRIPT_DIR = os.getcwd()
INPUT_FOLDER = 'Input_spectrogram/Training/'
languages = os.listdir(INPUT_FOLDER)
languages.sort()

enc = LabelBinarizer()
encoding = enc.fit_transform(languages)

spec_dict = {}

for l in languages:
    spec_dict[l] = sorted(os.listdir(INPUT_FOLDER + l))

txtfile = open('./img_set.txt', mode='w')

for l in languages:
    os.chdir(INPUT_FOLDER + str(l))
    for i in range(0, 100):
        txtfile.write(str(spec_dict[l][i]) + " " + str(l))
        txtfile.write("\n")
    os.chdir(SCRIPT_DIR)

txtfile.close()
