from nodes import LoraLoader
import folder_paths
import os

def populate_items(names):
    enhanced_names = []
    for item_name in names:
        file_name = os.path.splitext(item_name)[0]
        file_path = folder_paths.get_full_path("loras", item_name)
        
        if file_path is None:
            print(f"Unable to get path for lora {item_name}")
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
            "image": f"loras/{item_image}" if has_image else None,
        })
    
    enhanced_names.sort(key=lambda i: i["content"].lower())
    return enhanced_names

class OD_LoraLoader(LoraLoader):
    @classmethod
    def INPUT_TYPES(s):
        types = super().INPUT_TYPES()
        # Get the original list of names
        original_names = types["required"]["lora_name"][0]
        # Convert to our enhanced format with thumbnails
        enhanced_names = populate_items(original_names)
        # Update the types dictionary
        types["required"]["lora_name"] = (enhanced_names,)
        return types

    def load_lora(self, **kwargs):
        # Convert the input back to the format expected by the original loader
        kwargs["lora_name"] = kwargs["lora_name"]["content"]
        return super().load_lora(**kwargs)

NODE_CLASS_MAPPINGS = {
    "OD_LoraLoader": OD_LoraLoader
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OD_LoraLoader": "OD🥽 Lora Loader"
}