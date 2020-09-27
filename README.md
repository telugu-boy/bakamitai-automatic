# bakamitai-automatic
Automatic baka mitai generator

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
