# bakamitai-automatic
Automatic baka mitai generator

## Google Colab (faster)
 1. https://colab.research.google.com/drive/17OLT9-WrHyLZvEZvf_ucuQF_Nx9JsSJH?usp=sharing
 2. Ensure the runtime type is `GPU`.
 3. Press run on each button **except the last one**, in order.
    * Wait for previous execution to finish before pressing the next button.
    * Ignore non-fatal warnings or errors. Report fatal errors via the Issues tab.
 4. Navigate to the folder named `bakamitai-automatic` in your Google Drive.
 5. Replace `input_image.png` with desired image. Cropping to face is desired.
 6. Press run on the last button.
 7. Answer the Nvidia GPU presence prompt with `y`.
 8. Check the same folder that you navigated to in step 5 for `result.mp4`.

## Local (slower)
  ## Prerequisites
   * Linux with `git`, `ffmpeg` and `python3` (version 3.7 or above) installed
   * Nvidia GPU (optional)

  ## Running the program
   1. Clone the repository.
   2. Replace `input_image.png` with desired image. Cropping to face is desired.
   3. Execute `start.sh` or double click `start.bat` if on Windows.
   4. Wait for packages to install. Torch takes especially long.
   5. Answer the Nvidia GPU presence prompt.
   6. Wait for `result.mp4` to be generated in the directory that `start.sh` was executed in.
   7. Enjoy

### Cleanup
  * You are free to delete `working-dir`, but this is equivalent to cloning the repository and setting `input_image.png`.
  * You can delete small files like `bakamitai_template.mp4`, `dmdn.mp3` or `generated.mp4`.
  * It is advisable to keep `venv` and `vox-cpk.pth.tar` as they are large and may take more time to redownload.
    * `venv` may not be present on Google Colab. Ignore this step if so.
