import sys

sys.path.append('first-order-model/')

import os
import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
from skimage import img_as_ubyte
import warnings
warnings.filterwarnings("ignore")

import demo

if not os.path.isfile("generated.mp4"):
    no_nvidia_gpu = input("Is an Nvidia GPU present? y/N: ").strip().lower() == 'n'

    if no_nvidia_gpu:
        print("Using CPU for further calculations... (this will be much slower)")
    
    print("Reading template and input image...")

    source_image = imageio.imread('../input_image.png')
    driving_video = imageio.mimread('bakamitai_template.mp4')

    #Resize image and video to 256x256

    print("Resizing inputs...")

    source_image = resize(source_image, (256, 256))[..., :3]
    driving_video = [resize(frame, (256, 256))[..., :3] for frame in driving_video]

    print("Generating video... (this may take a while)")

    generator, kp_detector = demo.load_checkpoints(config_path='first-order-model/config/vox-256.yaml', checkpoint_path='vox-cpk.pth.tar', cpu=no_nvidia_gpu)

    predictions = demo.make_animation(source_image, driving_video, generator, kp_detector, relative=True, cpu=no_nvidia_gpu)

    print("Saving video...")

    imageio.mimsave('generated.mp4', [img_as_ubyte(frame) for frame in predictions])
else:
    print("File named 'generated.mp4' already exists. Continuing.")
