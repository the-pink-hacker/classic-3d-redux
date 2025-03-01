import json


def generate_model_textures(parent: str, **kwargs: str) -> dict:
    return {
        "parent": parent,
        "textures": kwargs,
    }

def generate_model_textures_template(parent: str, texture_template: str) -> dict:
    return {
        "import": {
            "parent": {
                "parent": parent,
            },
            "texture": texture_template,
        },
        "composition": "minecraft:template/parent",
    }

def generate_model_template_child(parent: str, texture_template: str) -> dict:
    return {
        "import": {
            "textures": texture_template,
        },
        "composition": parent,
    }

STAIR_SUFFIXES = [
    "north",
    "east",
    "south",
    "west",
    "inner_ne",
    "inner_nw",
    "inner_se",
    "inner_sw",
    "outer_ne",
    "outer_nw",
    "outer_se",
    "outer_sw",
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

WALL_SUFFIXES = [
    "inventory",
    "cross",
    "post",
    "post_side",
    "post_side_cutout_short",
    "side_north",
    "side_east",
    "side_south",
    "side_west",
    "side_ns",
    "side_ew",
]

TALL_WALL_SUFFIXES = [
    "post_side_cutout_tall",
    "cross_tall",
    "side_tall_north",
    "side_tall_east",
    "side_tall_south",
    "side_tall_west",
    "side_tall_ns",
    "side_tall_ew",
]

TRAPDOOR_SUFFIXES = [
    "top",
    "bottom",
    "open",
]

def main():
    model = "brick_stairs_"

    parent = "brick_stairs_"

    model_suffixes = STAIR_SUFFIXES

    model_folder = "src/1.21.4/minecraft/models/block/"
    parent_model_id_path = "minecraft:block/template/"

    for model_suffix in model_suffixes:
        model_file = f"{model_folder}{model}{model_suffix}.json"
        parent_model_id = f"{parent_model_id_path}{parent}{model_suffix}"
        #model_data = generate_model_textures(
        #    parent=parent_model_id,
        #    all="minecraft:block/pale_oak_planks",
        #)
        model_data = generate_model_textures_template(parent_model_id, "minecraft:template/texture/bricks")
        #model_data = generate_model_template_child(parent_model_id, "minecraft:template/texture/bricks")
        #model_data = {
        #    "composition": parent_model_id,
        #}

        with open(model_file, "w") as file:
            json.dump(model_data, file, indent=4)

        print(model_file)
        print(parent_model_id)
        print(model_data)
        print()


if __name__ == "__main__":
    main()
