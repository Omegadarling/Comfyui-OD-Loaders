import os
import folder_paths

def populate_items(names, model_folder):
    """Generic function to populate items with previews"""
    enhanced_names = []
    for item_name in names:
        file_name = os.path.splitext(item_name)[0]
        file_path = folder_paths.get_full_path(model_folder, item_name)
        
        if file_path is None:
            print(f"Unable to get path for {model_folder} model {item_name}")
            continue

        file_path_no_ext = os.path.splitext(file_path)[0]
        
        has_image = False
        item_image = None
        for ext in ["png", "jpg", "jpeg", "preview.png", "preview.jpeg"]:
            if os.path.isfile(file_path_no_ext + "." + ext):
                has_image = True
                item_image = f"{file_name}.{ext}"
                break

        enhanced_names.append({
            "content": item_name,
            "image": f"{model_folder}/{item_image}" if has_image else None,
        })
    
    enhanced_names.sort(key=lambda i: i["content"].lower())
    return enhanced_names