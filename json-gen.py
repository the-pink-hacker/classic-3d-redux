import json


def generate_model_all(texture: str, parent: str, texture_name = "all") -> dict:
    return {
        "parent": parent,
        "textures": {
            texture_name: texture,
        },
    }

def main():
    model = "oxidized_copper_door_bottom_"

    parent = "copper_door_bottom_"

    model_suffixes = [
        "right",
        "right_open",
        "left",
        "left_open",
    ]

    model_folder = "src/1.20.3/minecraft/models/block/"
    parent_model_id_path = "minecraft:block/template/"
    texture_id = "minecraft:block/oxidized_copper_door_bottom"

    for model_suffix in model_suffixes:
        model_file = f"{model_folder}{model}{model_suffix}.json"
        parent_model_id = f"{parent_model_id_path}{parent}{model_suffix}"
        model_data = generate_model_all(texture_id, parent_model_id, "bottom")

        with open(model_file, "w") as file:
            json.dump(model_data, file, indent=4)

        print(model_file)
        print(parent_model_id)
        print(model_data)
        print()


if __name__ == "__main__":
    main()
