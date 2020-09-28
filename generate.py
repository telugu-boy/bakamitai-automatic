import os

from bs4 import BeautifulSoup
import re
import requests

import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
from skimage import img_as_ubyte
import warnings
warnings.filterwarnings("ignore")

# PART 1: CLONE GIT REPO
print("Cloning repository...")
if not os.path.isdir("first-order-model"):
    os.system('git clone https://github.com/AliaksandrSiarohin/first-order-model "first-order-model"')
    
import sys
sys.path.append('first-order-model/')
    
import demo

def dl_srcs():
    #credit https://gist.github.com/gruber/249502
    urlregex = r"""(?xi)
    \b
    (                           # Capture 1: entire matched URL
    (?:
        [a-z][\w-]+:                # URL protocol and colon
        (?:
        /{1,3}                        # 1-3 slashes
        |                             #   or
        [a-z0-9%]                     # Single letter or digit or '%'
                                        # (Trying not to match e.g. "URI::Escape")
        )
        |                           #   or
        www\d{0,3}[.]               # "www.", "www1.", "www2." ... "www999."
        |                           #   or
        [a-z0-9.\-]+[.][a-z]{2,4}/  # looks like domain name followed by a slash
    )
    (?:                           # One or more:
        [^\s()<>]+                      # Run of non-space, non-()<>
        |                               #   or
        \(([^\s()<>]+|(\([^\s()<>]+\)))*\)  # balanced parens, up to 2 levels
    )+
    (?:                           # End with:
        \(([^\s()<>]+|(\([^\s()<>]+\)))*\)  # balanced parens, up to 2 levels
        |                                   #   or
        [^\s`!()\[\]{};:'".,<>?]        # not a space or one of these punct chars
    )
    )"""
    regex = re.compile(urlregex)

    url = "https://www.mediafire.com/file/o0wirp8aepbjy80/vox-cpk.pth.tar/file"
    s = requests.session()
    result = s.get(url)

    soup = BeautifulSoup(result.content, 'html.parser')

    div_tag = soup.find_all("div", class_="download_link")
    cpks_link = re.findall(regex, str(div_tag[0].contents))[0][0]

    src_vid_link = "https://cdn.discordapp.com/attachments/758371620531732531/759935503041560576/bakamitai_template.mp4"

    src_aud_link = "https://cdn.discordapp.com/attachments/758371620531732531/759696211157581844/dmdn.mp3"

    if not os.path.isfile("vox-cpk.pth.tar"):
        print("Downloading checkpoints...")
        with open("vox-cpk.pth.tar", "wb") as f:
            cpk_fille = requests.get(cpks_link, allow_redirects=True)
            f.write(cpk_fille.content)
    else:
        print("Checkpoints are already downloaded.")

    if not os.path.isfile("bakamitai_template.mp4"):
        print("Downloading template video...")
        with open("bakamitai_template.mp4", "wb") as f:
            src_vid_fille = requests.get(src_vid_link, allow_redirects=True)
            f.write(src_vid_fille.content)
    else:
        print("Template is already downloaded.")
        
    if not os.path.isfile("dmdn.mp3"):
        print("Downloading Baka Mitai audio...")
        with open("dmdn.mp3", "wb") as f:
            src_aud_fille = requests.get(src_aud_link, allow_redirects=True)
            f.write(src_aud_fille.content)
    else:
        print("Baka Mitai audio is already downloaded.")
        
def gen_dpfk(no_nvidia_gpu):
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
    
if not os.path.isfile("generated.mp4"):
    no_nvidia_gpu = input("Is an Nvidia GPU present? y/N: ").strip().lower() == 'n'
    
    # PART 2: GET CHECKPOINTS FROM MEDIAFIRE
    print("Downloading source media...")
    dl_srcs()

    # PART 3: GENERATE BAKA MITAI DEEPFAKE
    print("Generating deepfake...")
    gen_dpfk(no_nvidia_gpu)
else:
    print("File named 'generated.mp4' already exists. Continuing.")

print("Speeding up video...")
#speed up 3x while keeping frames and add audio
os.system("""ffmpeg -hide_banner -loglevel error -y -i generated.mp4 -i dmdn.mp3 -filter_complex "fps=60, setpts=1/3*PTS[v]" -map [v] -map 1:a:0 ../result.mp4""")

print("Done.")
