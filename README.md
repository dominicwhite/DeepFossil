# Run

docker build -t deepfossil:latest . && docker run --rm -v ~/.deepinfer/.tmp:/home/deepinfer/data deepfossil:latest --InputVolume /home/deepinfer/data/testInput --OutputLabel /home/deepinfer/data/labels.nrrd
