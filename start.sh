#!/bin/bash
WORKING_DIR="working-dir"
FOM_DIR_NAME="first-order-model"

mkdir -p $WORKING_DIR
cd $WORKING_DIR

printf "Creating venv...\n"
python3 -m venv venv
source venv/bin/activate

printf "Installing packages to venv...\n"
pip3 install -q PyYAML==5.3.1 beautifulsoup4 requests imageio matplotlib numpy pandas scikit-image scikit-learn torch torchvision imageio-ffmpeg tqdm

printf "Cloning repository...\n"
if [ ! -d "$FOM_DIR_NAME" ] ; then
    git clone https://github.com/AliaksandrSiarohin/first-order-model "$FOM_DIR_NAME"
fi

printf "Downloading source media...\n"
python3 ../dl_cpk_srcs.py

printf "Generating deepfake...\n"
python3 ../gen_dpfk.py

printf "Speeding up video...\n"
#speed up 3x while keeping frames
ffmpeg -hide_banner -loglevel error -y -i generated.mp4 -vcodec h264 -an -vf "fps=60, setpts=(1/3)*PTS" temp_poop.mp4

printf "Applying audio...\n"
#apply audio.
ffmpeg -hide_banner -loglevel error -y -i temp_poop.mp4 -i dmdn.mp3 -c:a copy -c:v copy ../result.mp4

#remove temporary fille
rm temp_poop.mp4

printf "Done"
