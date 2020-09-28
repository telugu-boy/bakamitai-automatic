# bakamitai-automatic
Automatic baka mitai generator

## Google Colab (faster)
 1. https://colab.research.google.com/drive/17OLT9-WrHyLZvEZvf_ucuQF_Nx9JsSJH?usp=sharing
 2. Ensure the runtime type is `GPU`.
 3. Press run on each button, in order.
   *  Wait for previous execution to finish before pressing the next button.
 4. Check the folder named `bakamitai-automatic` in your Google Drive for `result.mp4`.

## Local (slower)
 ## Prerequisites
   * Linux with `git`, `ffmpeg` and `python3` (version 3.7 or above) installed
   * Nvidia GPU (optional)

 ## Running the program
   1. Clone the repository.
   2. Replace `input_image.png` with desired image. Cropping to face is desired.
   3. Execute `bash ./start.sh`
   4. Wait for packages to install. Torch takes especially long.
   5. Answer the Nvidia GPU presence prompt.
   6. Wait for `result.mp4` to be generated in the directory that `start.sh` was executed in.
   7. Enjoy

### Cleanup
  * You are free to delete `working-dir`, but this is equivalent to cloning the repository and setting `input_image.png`.
