from .OD_DiffusionLoader import OD_DiffusionLoader
from .OD_LoraLoader import OD_LoraLoader

NODE_CLASS_MAPPINGS = {
    "OD_DiffusionLoader": OD_DiffusionLoader,
    "OD_LoraLoader": OD_LoraLoader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OD_DiffusionLoader": "OD🥽 Load Diffusion Model",
    "OD_LoraLoader": "OD🥽 Lora Loader"
}