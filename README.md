# Run

docker build -t deepfossil:latest . && docker run --rm -v ~/.deepinfer/.tmp:/home/deepinfer/data deepfossil:latest --InputVolume /home/deepinfer/data/testInput --OutputLabel /home/deepinfer/data/labels.nrrd

docker build -t deepfossil:latest . && \
  docker run --rm \
    -v "/Users/whitede/Dropbox (Smithsonian)/CT projects/Sphenodon_Slicer-Mimics-test/DeepFossil":/home/deepinfer/data \
    deepfossil:latest \
    --InputVolume /home/deepinfer/data/Sphenodon_halfsized.nrrd \
    --OutputLabel /home/deepinfer/data/labels.nrrd

docker build -t deepfossil:latest . && \
  docker run \
    -v "/Users/whitede/Dropbox (Smithsonian)/CT projects/CT-Ceratosaurus/slicer":/home/deepinfer/data \
    deepfossil:latest \
    --InputVolume /home/deepinfer/data/CeratosaurusDicom2.nrrd \
    --OutputLabel /home/deepinfer/data/Ceratosaurus_deepfossil_labels.seg.nrrd

docker build -t deepfossil:latest . && docker run --rm -v "/Users/whitede/Dropbox (Smithsonian)/CT projects/CT-Ceratosaurus/slicer":/home/deepinfer/data deepfossil:latest --InputVolume /home/deepinfer/data/CeratosaurusDicom2.nrrd --OutputLabel /home/deepinfer/data/Ceratosaurus_deepfossil_labels.nrrd
