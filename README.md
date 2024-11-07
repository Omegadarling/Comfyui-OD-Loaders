# Comfyui-OD-Loaders
The pythongosssss loaders have been broken for a little while and I missed the thumbnail previews and folder organization, so I added those thumbnails and folder structure into a few of the basic loaders.

So what I've done is make some nodes based on the built-in loaders and code from https://github.com/pythongosssss/ComfyUI-Custom-Scripts

All I really wanted to add back in was the thumbnails when you roll over items in your list of models, making it easier to see/remember what each custom model looks like.
![Image](https://github.com/user-attachments/assets/cf206225-a72a-47c4-8a96-d0f2ee1dcac7)

## Nodes
- GGUF Unet Loader: Loads GGUF format Unet models
- LoRA Loader: Custom LoRA loading functionality
- Diffusion Loader: Specialized diffusion model loader

## Installation

### Option 1: ComfyUI Manager (Recommended)
1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. Restart ComfyUI
3. Find "OD Loaders" in the Manager
4. Click Install

### Option 2: Manual Installation
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/comfyui-od-loaders
