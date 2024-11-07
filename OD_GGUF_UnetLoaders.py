import torch
import folder_paths
from nodes import UnetLoaderGGUF, UnetLoaderGGUFAdvanced, gguf_sd_loader
import comfy.sd
import os

def populate_items(names):
    enhanced_names = []
    for item_name in names:
        file_name = os.path.splitext(item_name)[0]
        file_path = folder_paths.get_full_path("unet_gguf", item_name)
        
        if file_path is None:
            print(f"Unable to get path for GGUF model {item_name}")
            continue

        file_path_no_ext = os.path.splitext(file_path)[0]
        
        # Look for preview images with common extensions
        has_image = False
        item_image = None
        for ext in ["png", "jpg", "jpeg", "preview.png", "preview.jpeg"]:
            if os.path.isfile(file_path_no_ext + "." + ext):
                has_image = True
                item_image = f"{file_name}.{ext}"
                break

        enhanced_names.append({
            "content": item_name,
            "image": f"unet_gguf/{item_image}" if has_image else None,
        })
    
    enhanced_names.sort(key=lambda i: i["content"].lower())
    return enhanced_names

class OD_UnetLoaderGGUF(UnetLoaderGGUF):
    @classmethod
    def INPUT_TYPES(s):
        types = super().INPUT_TYPES()
        names = types["required"]["unet_name"][0]
        # Convert the original list of names to our enhanced format with thumbnails
        enhanced_names = populate_items(names)
        # Update the types dictionary with our enhanced names
        types["required"]["unet_name"] = (enhanced_names,)
        return types

    def load_unet(self, unet_name):
        # Extract the actual filename from our enhanced format
        return super().load_unet(unet_name["content"])

    CATEGORY = "loaders"
    TITLE = "OD Unet Loader (GGUF)"

class OD_UnetLoaderGGUFAdvanced(UnetLoaderGGUFAdvanced):
    @classmethod
    def INPUT_TYPES(s):
        types = super().INPUT_TYPES()
        names = types["required"]["unet_name"][0]
        # Convert the original list of names to our enhanced format with thumbnails
        enhanced_names = populate_items(names)
        # Update the types dictionary with our enhanced names
        types["required"]["unet_name"] = (enhanced_names,)
        return types

    def load_unet(self, unet_name, dequant_dtype=None, patch_dtype=None, patch_on_device=None):
        # Extract the actual filename from our enhanced format
        return super().load_unet(
            unet_name["content"], 
            dequant_dtype=dequant_dtype,
            patch_dtype=patch_dtype,
            patch_on_device=patch_on_device
        )

    CATEGORY = "loaders"
    TITLE = "OD Unet Loader (GGUF/Advanced)"

NODE_CLASS_MAPPINGS = {
    "OD_UnetLoaderGGUF": OD_UnetLoaderGGUF,
    "OD_UnetLoaderGGUFAdvanced": OD_UnetLoaderGGUFAdvanced
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OD_UnetLoaderGGUF": "OD🥽 Unet Loader (GGUF)",
    "OD_UnetLoaderGGUFAdvanced": "OD🥽 Unet Loader (GGUF/Advanced)"
}