import json


def generate_json(number: int, characteristics: dict, address: str):
    def append_attribute(trait_type: str, trait_value: str):
        data["attributes"].append(
            {
                "trait_type": trait_type,
                "value": trait_value,
            }
        )

    data = {}

    data["name"] = f"CryptoGirl #{number}"
    data["symbol"] = "CRYPTOGIRL"
    data["description"] = "CryptoGirlsParty is a collection of NFTs."
    data["image"] = f"{number}.png"
    data["external_url"] = ""
    data["edition"] = "2021"
    data["attributes"] = []

    for key, value in characteristics.items():
        append_attribute(key, value)

    data["attributes"].append(
        {"display_type": "number", "trait_type": "generation", "value": 1}
    )
    data["attributes"].append(
        {"display_type": "number", "trait_type": "sequence", "value": number}
    )

    data["properties"] = {}
    data["properties"]["category"] = "image"

    data["properties"]["files"] = []
    data["properties"]["files"].append({"uri": "", "type": "image/png"})
    data["properties"]["creators"] = []
    data["properties"]["creators"].append({"address": address, "share": 100})

    with open("output/" + f"{number}.json", "w") as outfile:
        json.dump(data, outfile)
