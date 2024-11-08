from nodes import LoraLoader
from .utils import populate_items

class OD_LoraLoader(LoraLoader):
    @classmethod
    def INPUT_TYPES(s):
        types = super().INPUT_TYPES()
        # Get the original list of names
        original_names = types["required"]["lora_name"][0]
        # Convert to our enhanced format with thumbnails
        enhanced_names = populate_items(original_names, "loras")
        # Update the types dictionary
        types["required"]["lora_name"] = (enhanced_names,)
        return types

    def load_lora(self, **kwargs):
        # Convert the input back to the format expected by the original loader
        kwargs["lora_name"] = kwargs["lora_name"]["content"]
        return super().load_lora(**kwargs)