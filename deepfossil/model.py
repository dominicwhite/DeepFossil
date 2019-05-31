import io

from fastai.vision import load_learner, open_image
import numpy as np
from PIL import Image
import SimpleITK as sitk

def seg_dice(*args, **kwargs):
    return dice(*args, **kwargs, iou=True)

class DeepFossilSegmenter():

    def __init__(self):
        self.learner = load_learner(path=".", file="export-stage-1.pkl")

    def segment(self, input_volume, output_label):
        vol = sitk.ReadImage(input_volume)
        vol_nda = sitk.GetArrayFromImage(vol)
        original_shape = vol_nda.shape
        print("Original vol shape:", original_shape)
        stacked_labels = np.array([])
        for idx, slice in enumerate(vol_nda):
            im = Image.fromarray(slice).convert("L")
            with io.BytesIO() as slice_bytes:
                im.save(slice_bytes, format="PNG")
                img = open_image(slice_bytes)
            pred_class, pred_labels, losses = self.learner.predict(img)
            np_labels = pred_labels.numpy()
            if stacked_labels.size == 0:
                stacked_labels = np_labels
            else:
                stacked_labels = np.concatenate([stacked_labels, np_labels], axis=0)
        print("Prediction ranges:", stacked_labels.min(), stacked_labels.max())
        bone_labels = np.clip(stacked_labels - 1, 0, 1)
        print("Output volume shape:", bone_labels.shape)
        print("Output volume ranges:", bone_labels.min(), bone_labels.max())
        label_vol = sitk.GetImageFromArray(bone_labels.astype(np.uint8))
        label_vol.CopyInformation(vol)
        writer = sitk.ImageFileWriter()
        writer.Execute(label_vol, output_label, True)

