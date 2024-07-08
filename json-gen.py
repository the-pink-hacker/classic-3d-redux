import json


def generate_model_textures(parent: str, **kwargs: str) -> dict:
    return {
        "parent": parent,
        "textures": kwargs
    }

def main():
    model = "red_sandstone_stairs_"

    parent = "sandstone_stairs_"

    model_suffixes = [
        #"north",
        #"east",
        #"south",
        #"west",
        #"inner_ne",
        #"inner_nw",
        #"inner_se",
        #"inner_sw",
        #"outer_ne",
        #"outer_nw",
        #"outer_se",
        #"outer_sw",
        "top_north",
        "top_east",
        "top_south",
        "top_west",
        "top_inner_ne",
        "top_inner_nw",
        "top_inner_se",
        "top_inner_sw",
        "top_outer_ne",
        "top_outer_nw",
        "top_outer_se",
        "top_outer_sw",
    ]

    model_folder = "src/bundles/1.13/minecraft/models/block/"
    parent_model_id_path = "minecraft:block/template/"

    for model_suffix in model_suffixes:
        model_file = f"{model_folder}{model}{model_suffix}.json"
        parent_model_id = f"{parent_model_id_path}{parent}{model_suffix}"
        model_data = generate_model_textures(
            parent=parent_model_id,
            bottom="minecraft:block/red_sandstone_top",
            side="minecraft:block/red_sandstone",
            top="minecraft:block/red_sandstone_bottom",
        )

        with open(model_file, "w") as file:
            json.dump(model_data, file, indent=4)

        print(model_file)
        print(parent_model_id)
        print(model_data)
        print()


if __name__ == "__main__":
    main()
