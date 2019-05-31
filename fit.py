import getopt
import os
import sys

from deepfossil.model import DeepFossilSegmenter, seg_dice

def main(argv):
    print(os.getcwd())
    print(os.listdir('/usr/src'))
    InputVolume = ''
    OutputLabel = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["InputVolume=", "OutputLabel="])
    except getopt.GetoptError:
        print('usage: fit.py -InputVolume <InputVolumePath> --OutputLabel <OutputLabelPath>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('fit.py -InputVolume <InputVolumePath> --OutputLabel <OutputLabelPath>')
            sys.exit()
        elif opt in ("-i", "--InputVolume"):
            InputVolume = arg
        elif opt in ("-o", "--OutputLabel"):
            OutputLabel = arg
    if InputVolume == '' or OutputLabel == '':
        print('usage: fit.py -InputVolume <InputVolumePath> -OutputLabel <OutputLabelPath>')
        sys.exit()
    if os.path.isfile(InputVolume) and os.path.isdir(os.path.dirname(OutputLabel)):
        print("Building the model.")
        segmenter = DeepFossilSegmenter()
        print("Resizing images and segmenting")
        segmenter.segment(InputVolume, OutputLabel)
    else:
        print("Make sure the input file exists and the output file directory is valid.")
        print("InputVolume: ", InputVolume, os.path.isfile(InputVolume))
        print("OutputLabel: ", OutputLabel, os.path.isdir(os.path.dirname(OutputLabel)))

if __name__ == "__main__":
    main(sys.argv[1:])
