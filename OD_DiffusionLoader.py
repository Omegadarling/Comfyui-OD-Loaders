import torch
import comfy.sd
import folder_paths
from nodes import UNETLoader
from .utils import populate_items

class OD_DiffusionLoader(UNETLoader):
    @classmethod
    def INPUT_TYPES(s):
        types = super().INPUT_TYPES()
        names = types["required"]["unet_name"][0]
        # Convert the original list of names to our enhanced format with thumbnails
        enhanced_names = populate_items(names, "diffusion_models")
        # Update the types dictionary with our enhanced names
        types["required"]["unet_name"] = (enhanced_names,)
        return types

    def load_unet(self, unet_name, weight_dtype):
        # Convert back to the format expected by the parent class
        weight_dtype_map = {
            "default": None,
            "fp8_e4m3fn": torch.float8_e4m3fn,
            "fp8_e4m3fn_fast": "fp8_fast",  # Special handling in parent
            "fp8_e5m2": torch.float8_e5m2
        }

        model_options = {}
        dtype = weight_dtype_map.get(weight_dtype)
        if dtype == "fp8_fast":
            model_options["dtype"] = torch.float8_e4m3fn
            model_options["fp8_optimizations"] = True
        elif dtype is not None:
            model_options["dtype"] = dtype

        # Extract the actual filename from our enhanced format
        unet_path = folder_paths.get_full_path_or_raise("diffusion_models", unet_name["content"])
        model = comfy.sd.load_diffusion_model(unet_path, model_options=model_options)
        return (model,)