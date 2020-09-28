if not exist "working-dir" mkdir "working-dir"

cd "working-dir"

echo "Creating venv..."
echo.
python -m venv venv
source venv\Scripts\activate.bat

echo "Installing packages to venv..."
echo.
pip install -q PyYAML==5.3.1 beautifulsoup4 requests imageio matplotlib numpy pandas scikit-image scikit-learn torch torchvision imageio-ffmpeg tqdm

python ../generate.py
 
