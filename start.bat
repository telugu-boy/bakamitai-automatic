if not exist "working-dir" mkdir "working-dir"

cd "working-dir"

echo "Creating venv..."
python -m venv venv

echo "Installing packages to venv..."
venv\Scripts\pip install -q PyYAML==5.3.1 beautifulsoup4 requests imageio matplotlib numpy==1.19.3 pandas scikit-image scikit-learn imageio-ffmpeg tqdm
venv\Scripts\pip install -q --timeout 1000 torch===1.6.0 torchvision===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

venv\Scripts\python ../generate.py
