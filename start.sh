#!/bin/bash
WORKING_DIR="working-dir"

mkdir -p $WORKING_DIR
cd $WORKING_DIR

printf "Creating venv...\n"
python3 -m venv venv
source venv/bin/activate

printf "Installing packages to venv...\n"
python3 -m pip install -q PyYAML==5.3.1 beautifulsoup4 requests imageio matplotlib numpy pandas scikit-image scikit-learn torch torchvision imageio-ffmpeg tqdm

python3 ../generate.py
