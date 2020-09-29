# bakamitai-automatic
Generates a Baka Mitai meme from an input image

## Google Colab (faster)
 1. https://colab.research.google.com/drive/1kUKt-MJ8ThEkqWsiLwRmEJOIdwqwbzyr?usp=sharing
 2. Ensure the runtime type is `GPU`.
 3. Press run on each button **except the second last one**, in order.
    * Wait for previous execution to finish before pressing the next button.
    * Ignore non-fatal warnings or errors. Report fatal errors via the Issues tab.
 4. Navigate to the folder named `bakamitai-automatic` in your Google Drive.
 5. Replace `input_image.png` with desired image. Cropping to face is desired.
 6. Press run on the **second last** button.
 7. Answer the Nvidia GPU presence prompt with `y`.
 8. Check the same folder that you navigated to in step 4 for `result.mp4`.

## Local (slower)
  ## Prerequisites
   * `git`, `ffmpeg` and `python3` (version 3.7 is guaranteed to work) installed and added to `PATH`
   * Nvidia GPU (optional)

  ## Running the program
   1. Clone the repository.
   2. Replace `input_image.png` with desired image. Cropping to face is desired.
   3. Execute `start.sh` or double click `start.bat` if on Windows.
   4. Wait for packages to install. Torch takes especially long.
   5. Answer the Nvidia GPU presence prompt.
   6. Wait for `result.mp4` to be generated in the directory that `start.sh` was executed in.
   7. Enjoy
 
## Issues
  * If Google Colab refuses to `cd`, factory reset the runtime. `Runtime -> Factory reset runtime`.
   
## Repetition
To repeat the process, delete `generated.mp4` in `working-dir` (or click the **last** run button in Colab). Replace `input_image.png` with another image and
  * Colab: press the button that runs `start.sh`.
  * Local: run `start.sh` or `start.bat` if on Windows.

### Cleanup
  * You are free to delete `working-dir`, but this is equivalent to cloning the repository and setting `input_image.png`.
  * You can delete small files like `bakamitai_template.mp4`, `dmdn.mp3` or `generated.mp4`.
  * It is advisable to keep `venv` and `vox-cpk.pth.tar` as they are large and may take more time to redownload.
    * `venv` may not be present on Google Colab. Ignore this step if so.
