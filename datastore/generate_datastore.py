class GenerateDatastoreInterface:
    def extract_background_primary_trait(self, background_primary: str) -> str:
        pass

    def extract_background_secondary_trait(self, background_secondary: str) -> str:
        pass

    def extract_clothes_trait(self, clothes: str) -> str:
        pass

    def extract_hair_back_trait(self, hair_back: str) -> str:
        pass

    def extract_hair_front_trait(self, hair_front: str) -> str:
        pass

    def extract_hair_color_trait(self, hair_color: str) -> str:
        pass

    def extract_eye_trait(self, eye: str) -> str:
        pass

    def extract_eye_color_trait(self, eye_color: str) -> str:
        pass

    def extract_mouth_trait(self, mouth: str) -> str:
        pass

    def extract_body_trait(self, body: str) -> str:
        pass

    def extract_hat_trait(self, hat: str) -> str:
        pass

    def extract_face_trait(self, face: str) -> str:
        pass

    def extract_hands_trait(self, hands: str) -> str:
        pass

    def extract_effect_trait(self, effect: str) -> str:
        pass

    def extract_trait_count(self, trait_count: str) -> str:
        pass


class GenerateDatastore(GenerateDatastoreInterface):
    def extract_background_primary_trait(self, background_primary: str) -> str:
        if background_primary == "Field Dawn":
            return "0x00"
        elif background_primary == "Field Night":
            return "0x01"
        elif background_primary == "Field Day":
            return "0x02"
        elif background_primary == "Sea Dawn":
            return "0x03"
        elif background_primary == "Sea Day":
            return "0x04"
        elif background_primary == "Ship Bloodmoon":
            return "0x05"
        elif background_primary == "Ship Night":
            return "0x06"
        elif background_primary == "Ship Day":
            return "0x07"
        elif background_primary == "Single Color":
            return "0x08"
        elif background_primary == "BTC Rain":
            return "0x09"
        elif background_primary == "ETH Rain":
            return "0x0a"
        elif background_primary == "Exclamation":
            return "0x0b"
        elif background_primary == "Wah":
            return "0x0c"
        elif background_primary == "Throne Blue":
            return "0x0d"
        elif background_primary == "Throne Red":
            return "0x0e"
        elif background_primary == "Throne Fuchsia":
            return "0x0f"
        elif background_primary == "Throne Cyan":
            return "0x10"
        elif background_primary == "Throne Neon Purple":
            return "0x11"
        elif background_primary == "Throne Yellow":
            return "0x12"
        elif background_primary == "Town":
            return "0x13"
        elif background_primary == "Town Burn":
            return "0x14"
        elif background_primary == "Painting":
            return "0x15"
        elif background_primary == "Abstract Green":
            return "0x16"
        elif background_primary == "Abstract Red":
            return "0x17"
        elif background_primary == "Treasure":
            return "0x18"
        elif background_primary == "Stars":
            return "0x19"
        elif background_primary == "Galaxy":
            return "0x1a"
        elif background_primary == "Frame":
            return "0x1b"
        elif background_primary == "Modern Dark":
            return "0x1c"
        elif background_primary == "Modern Bright":
            return "0x1d"
        elif background_primary == "Hospital":
            return "0x1e"
        elif background_primary == "Hospital Help":
            return "0x1f"
        elif background_primary == "Hospital Obey":
            return "0x20"
        elif background_primary == "Radioactive Wall":
            return "0x21"
        elif background_primary == "Radioactive Factory":
            return "0x22"
        elif background_primary == "Tavern Day":
            return "0x23"
        elif background_primary == "Tavern Dawn":
            return "0x24"
        elif background_primary == "Tavern Night":
            return "0x25"
        elif background_primary == "Tavern Wrecked":
            return "0x26"
        elif background_primary == "Cave":
            return "0x27"
        elif background_primary == "Cave Bloody":
            return "0x28"
        elif background_primary == "Forest Magical":
            return "0x29"
        elif background_primary == "Forest Autumn":
            return "0x2a"
        elif background_primary == "Forest Dark":
            return "0x2b"
        elif background_primary == "Bar":
            return "0x2c"
        elif background_primary == "City Neon":
            return "0x2d"
        elif background_primary == "Sunflower":
            return "0x2e"
        elif background_primary == "Scenery Night":
            return "0x2f"
        elif background_primary == "Scenery Day":
            return "0x30"
        elif background_primary == "Underwater":
            return "0x31"
        elif background_primary == "Alchemy Lab":
            return "0x32"
        elif background_primary == "Forge":
            return "0x33"
        elif background_primary == "Onsen Day":
            return "0x34"
        elif background_primary == "Onsen Night":
            return "0x35"
        elif background_primary == "Bedroom":
            return "0x36"
        elif background_primary == "Graveyard":
            return "0x37"
        elif background_primary == "Graveyard Bloodmoon":
            return "0x38"
        elif background_primary == "Hell":
            return "0x39"
        elif background_primary == "Moon":
            return "0x3a"
        elif background_primary == "Moon Crater":
            return "0x3b"
        elif background_primary == "Palace":
            return "0x3c"
        elif background_primary == "Classroom":
            return "0x3d"
        elif background_primary == "Space Station":
            return "0x3e"
        elif background_primary == "Abandoned Building":
            return "0x3f"
        elif background_primary == "Fireworks Big":
            return "0x40"
        elif background_primary == "Fireworks Multiple":
            return "0x41"
        elif background_primary == "Fantasy Dawn":
            return "0x42"
        elif background_primary == "Fantasy Day":
            return "0x43"
        elif background_primary == "Snow":
            return "0x44"
        elif background_primary == "Cafe":
            return "0x45"
        elif background_primary == "Circle":
            return "0x46"
        elif background_primary == "Desert":
            return "0x47"
        else:
            raise ValueError("Invalid background primary trait")

    def extract_background_secondary_trait(self, background_secondary: str) -> str:
        if background_secondary == "Rainbow":
            return "0x00"
        elif background_secondary == "BTC Vessel":
            return "0x01"
        elif background_secondary == "ETH Vessel":
            return "0x02"
        elif background_secondary == "SOL Vessel":
            return "0x03"
        elif background_secondary == "ADA Vessel":
            return "0x04"
        elif background_secondary == "BNB Vessel":
            return "0x05"
        elif background_secondary == "BTC Emblem":
            return "0x06"
        elif background_secondary == "ETH Emblem":
            return "0x07"
        elif background_secondary == "SOL Emblem":
            return "0x08"
        elif background_secondary == "ADA Emblem":
            return "0x09"
        elif background_secondary == "BNB Emblem":
            return "0x0a"
        elif background_secondary == "Bloodbath BTC Emblem":
            return "0x0b"
        elif background_secondary == "Bloodbath ETH Emblem":
            return "0x0c"
        elif background_secondary == "Pitch Black":
            return "0x0d"
        elif background_secondary == "Violet Blue":
            return "0x0e"
        elif background_secondary == "Carmine Red":
            return "0x0f"
        elif background_secondary == "Blood":
            return "0x10"
        elif background_secondary == "Lineship":
            return "0x11"
        elif background_secondary == "Cantaloupe":
            return "0x12"
        elif background_secondary == "Mint":
            return "0x13"
        elif background_secondary == "Red Circles":
            return "0x14"
        elif background_secondary == "Green Circles":
            return "0x15"
        elif background_secondary == "C19":
            return "0x16"
        elif background_secondary == "C19 and Blood":
            return "0x17"
        elif background_secondary == "Gas":
            return "0x18"
        elif background_secondary == "Splatter":
            return "0x19"
        elif background_secondary == "Gas and Splatter":
            return "0x1a"
        elif background_secondary == "Fence":
            return "0x1b"
        elif background_secondary == "Fence and Gas":
            return "0x1c"
        elif background_secondary == "BTC Banner":
            return "0x1d"
        elif background_secondary == "ETH Banner":
            return "0x1e"
        elif background_secondary == "SOL Banner":
            return "0x1f"
        elif background_secondary == "ADA Banner":
            return "0x20"
        elif background_secondary == "BNB Banner":
            return "0x21"
        elif background_secondary == "Pusheen Heart":
            return "0x22"
        elif background_secondary == "Pusheen BTC":
            return "0x23"
        elif background_secondary == "Pusheen ETH":
            return "0x24"
        elif background_secondary == "Pusheen Star":
            return "0x25"
        elif background_secondary == "Pusheen Rocket":
            return "0x26"
        elif background_secondary == "Nyan Heart":
            return "0x27"
        elif background_secondary == "Nyan BTC":
            return "0x28"
        elif background_secondary == "Nyan ETH":
            return "0x29"
        elif background_secondary == "Nyan Star":
            return "0x2a"
        elif background_secondary == "Nyan Rocket":
            return "0x2b"
        elif background_secondary == "Shiba Heart":
            return "0x2c"
        elif background_secondary == "Shiba BTC":
            return "0x2d"
        elif background_secondary == "Shiba ETH":
            return "0x2e"
        elif background_secondary == "Shiba Star":
            return "0x2f"
        elif background_secondary == "Shiba Rocket":
            return "0x30"
        elif background_secondary == "Bird Heart":
            return "0x31"
        elif background_secondary == "Bird BTC":
            return "0x32"
        elif background_secondary == "Bird ETH":
            return "0x33"
        elif background_secondary == "Bird Star":
            return "0x34"
        elif background_secondary == "Bird Rocket":
            return "0x35"
        elif background_secondary == "Ape Heart":
            return "0x36"
        elif background_secondary == "Ape BTC":
            return "0x37"
        elif background_secondary == "Ape ETH":
            return "0x38"
        elif background_secondary == "Ape Star":
            return "0x39"
        elif background_secondary == "Ape Rocket":
            return "0x3a"
        elif background_secondary == "Pusheen Heart 69420":
            return "0x3b"
        elif background_secondary == "Pusheen BTC 69420":
            return "0x3c"
        elif background_secondary == "Pusheen ETH 69420":
            return "0x3d"
        elif background_secondary == "Pusheen Star 69420":
            return "0x3e"
        elif background_secondary == "Pusheen Rocket 69420":
            return "0x3f"
        elif background_secondary == "Nyan Heart 69420":
            return "0x40"
        elif background_secondary == "Nyan BTC 69420":
            return "0x41"
        elif background_secondary == "Nyan ETH 69420":
            return "0x42"
        elif background_secondary == "Nyan Star 69420":
            return "0x43"
        elif background_secondary == "Nyan Rocket 69420":
            return "0x44"
        elif background_secondary == "Shiba Heart 69420":
            return "0x45"
        elif background_secondary == "Shiba BTC 69420":
            return "0x46"
        elif background_secondary == "Shiba ETH 69420":
            return "0x47"
        elif background_secondary == "Shiba Star 69420":
            return "0x48"
        elif background_secondary == "Shiba Rocket 69420":
            return "0x49"
        elif background_secondary == "Bird Heart 69420":
            return "0x4a"
        elif background_secondary == "Bird BTC 69420":
            return "0x4b"
        elif background_secondary == "Bird ETH 69420":
            return "0x4c"
        elif background_secondary == "Bird Star 69420":
            return "0x4d"
        elif background_secondary == "Bird Rocket 69420":
            return "0x4e"
        elif background_secondary == "Ape Heart 69420":
            return "0x4f"
        elif background_secondary == "Ape BTC 69420":
            return "0x50"
        elif background_secondary == "Ape ETH 69420":
            return "0x51"
        elif background_secondary == "Ape Star 69420":
            return "0x52"
        elif background_secondary == "Ape Rocket 69420":
            return "0x53"
        elif background_secondary == "Butterfly":
            return "0x54"
        elif background_secondary == "Rocket":
            return "0x55"
        elif background_secondary == "Torii":
            return "0x56"
        elif background_secondary == "Torii Rocket":
            return "0x57"
        elif background_secondary == "Shark":
            return "0x58"
        elif background_secondary == "Whale":
            return "0x59"
        elif background_secondary == "Fumes":
            return "0x5a"
        elif background_secondary == "Duck":
            return "0x5b"
        elif background_secondary == "Coin":
            return "0x5c"
        elif background_secondary == "Duck and Coin":
            return "0x5d"
        elif background_secondary == "Moon":
            return "0x5e"
        elif background_secondary == "Cauldron":
            return "0x5f"
        elif background_secondary == "Chains":
            return "0x60"
        elif background_secondary == "Chains and Cauldron":
            return "0x61"
        elif background_secondary == "BTC Flag":
            return "0x62"
        elif background_secondary == "ETH Flag":
            return "0x63"
        elif background_secondary == "DOGE Flag":
            return "0x64"
        elif background_secondary == "Earth":
            return "0x65"
        elif background_secondary == "Earth BTC Flag":
            return "0x66"
        elif background_secondary == "Earth ETH Flag":
            return "0x67"
        elif background_secondary == "Earth DOGE Flag":
            return "0x68"
        elif background_secondary == "Math":
            return "0x69"
        elif background_secondary == "Doubt":
            return "0x6a"
        elif background_secondary == "Brainwash":
            return "0x6b"
        elif background_secondary == "Education":
            return "0x6c"
        elif background_secondary == "Balloon":
            return "0x6d"
        elif background_secondary == "Clouds":
            return "0x6e"
        elif background_secondary == "Galaxy":
            return "0x6f"
        elif background_secondary == "Spring":
            return "0x70"
        elif background_secondary == "Autumn":
            return "0x71"
        elif background_secondary == "Magical":
            return "0x72"
        elif background_secondary == "Leaves":
            return "0x73"
        elif background_secondary == "Baby Blue":
            return "0x74"
        elif background_secondary == "Pink":
            return "0x75"
        elif background_secondary == "Lime":
            return "0x76"
        elif background_secondary == "Salmon":
            return "0x77"
        elif background_secondary == "Purple":
            return "0x78"
        elif background_secondary == "Pyramid":
            return "0x79"
        elif background_secondary == "Pyramid Eye of Providence":
            return "0x7a"
        elif background_secondary == "Nothing":
            return "0x7b"
        else:
            raise ValueError("Invalid background_secondary trait")

    def extract_clothes_trait(self, clothes: str) -> str:
        if clothes == "Bunny":
            return "0x00"
        elif clothes == "Captain":
            return "0x01"
        elif clothes == "Corsair Feminine":
            return "0x02"
        elif clothes == "Corsair Masculine":
            return "0x03"
        elif clothes == "Elvish Feminine":
            return "0x04"
        elif clothes == "Elvish Masculine":
            return "0x05"
        elif clothes == "Fencer Feminine BTC":
            return "0x06"
        elif clothes == "Fencer Feminine ETH":
            return "0x07"
        elif clothes == "Fencer Masculine BTC":
            return "0x08"
        elif clothes == "Knight Feminine":
            return "0x09"
        elif clothes == "Knight Masculine":
            return "0x0a"
        elif clothes == "Fencer Masculine":
            return "0x0b"
        elif clothes == "Mage BTC":
            return "0x0c"
        elif clothes == "Mage ETH":
            return "0x0d"
        elif clothes == "Lady":
            return "0x0e"
        elif clothes == "Suit Black":
            return "0x0f"
        elif clothes == "Mech":
            return "0x10"
        elif clothes == "Military":
            return "0x11"
        elif clothes == "Princess BTC":
            return "0x12"
        elif clothes == "Princess ETH":
            return "0x13"
        elif clothes == "Ronin Feminine":
            return "0x14"
        elif clothes == "Ronin Masculine":
            return "0x15"
        elif clothes == "Sailor BTC":
            return "0x16"
        elif clothes == "Sailor ETH":
            return "0x17"
        elif clothes == "Slime Tentacle":
            return "0x18"
        elif clothes == "Succubus":
            return "0x19"
        elif clothes == "Witch":
            return "0x1a"
        elif clothes == "Wizard":
            return "0x1b"
        elif clothes == "Bunny Esther":
            return "0x1c"
        elif clothes == "Knight Aeryn":
            return "0x1d"
        elif clothes == "Divesuit Blue":
            return "0x1e"
        elif clothes == "Divesuit Orange":
            return "0x1f"
        elif clothes == "Divesuit Pink":
            return "0x20"
        elif clothes == "Maid Cyan Bow Tie":
            return "0x21"
        elif clothes == "Maid Red Bow Tie":
            return "0x22"
        elif clothes == "Nun":
            return "0x23"
        elif clothes == "Nun ETH":
            return "0x24"
        elif clothes == "Pajama Blue":
            return "0x25"
        elif clothes == "Pajama Orange":
            return "0x26"
        elif clothes == "Pajama Pink":
            return "0x27"
        elif clothes == "Schoolgirl Pink Bow Tie":
            return "0x28"
        elif clothes == "Schoolgirl Blue Bow Tie":
            return "0x29"
        elif clothes == "Casual":
            return "0x2a"
        elif clothes == "Towel":
            return "0x2b"
        elif clothes == "Turtleneck":
            return "0x2c"
        elif clothes == "Turtleneck Sleeveless":
            return "0x2d"
        elif clothes == "Turtleneck Busty":
            return "0x2e"
        elif clothes == "Yukata":
            return "0x2f"
        elif clothes == "Yukata Red Flower":
            return "0x30"
        elif clothes == "Yukata Blue Flower":
            return "0x31"
        elif clothes == "Techwear Green":
            return "0x32"
        elif clothes == "Techwear Blue":
            return "0x33"
        elif clothes == "Techwear Space Blue":
            return "0x34"
        elif clothes == "Techwear Space Blue 42":
            return "0x35"
        elif clothes == "Techwear Space Green":
            return "0x36"
        elif clothes == "Techwear Space Green 42":
            return "0x37"
        elif clothes == "Coat":
            return "0x38"
        elif clothes == "Coat Blue":
            return "0x39"
        elif clothes == "Blacksmith":
            return "0x3a"
        elif clothes == "Apron":
            return "0x3b"
        elif clothes == "Nurse":
            return "0x3c"
        elif clothes == "Swimsuit Dark Blue":
            return "0x3d"
        elif clothes == "Swimsuit Baby Blue":
            return "0x3e"
        elif clothes == "Wedding":
            return "0x3f"
        elif clothes == "Anubis":
            return "0x40"
        elif clothes == "Suit White":
            return "0x41"
        elif clothes == "Shrine maiden":
            return "0x42"
        elif clothes == "Naked":
            return "0x43"
        elif clothes == "Spacesuit":
            return "0x44"
        else:
            raise ValueError("Invalid clothes trait")

    def extract_hair_back_trait(self, hair_back: str) -> str:
        if hair_back == "Puff":
            return "0x00"
        elif hair_back == "Spiral":
            return "0x01"
        elif hair_back == "Braid":
            return "0x02"
        elif hair_back == "Hime":
            return "0x03"
        elif hair_back == "Short":
            return "0x04"
        elif hair_back == "Girly":
            return "0x05"
        elif hair_back == "Anime":
            return "0x06"
        elif hair_back == "Buns":
            return "0x07"
        elif hair_back == "Ponytail":
            return "0x08"
        elif hair_back == "Wavy":
            return "0x09"
        elif hair_back == "Pointy":
            return "0x0a"
        elif hair_back == "Nothing":
            return "0x0b"
        else:
            raise ValueError("Invalid hair back trait")

    def extract_hair_color_trait(self, hair_color: str) -> str:
        if hair_color == "Black":
            return "0x00"
        elif hair_color == "Blonde":
            return "0x01"
        elif hair_color == "Blue":
            return "0x02"
        elif hair_color == "Brown":
            return "0x03"
        elif hair_color == "Cyan":
            return "0x04"
        elif hair_color == "Gray":
            return "0x05"
        elif hair_color == "Green":
            return "0x06"
        elif hair_color == "Pink":
            return "0x07"
        elif hair_color == "Purple":
            return "0x08"
        elif hair_color == "Red":
            return "0x09"
        elif hair_color == "Mint":
            return "0x0a"
        elif hair_color == "Blueberry":
            return "0x0b"
        elif hair_color == "Flower":
            return "0x0c"
        elif hair_color == "Galaxy":
            return "0x0d"
        elif hair_color == "Gyaru":
            return "0x0e"
        elif hair_color == "Flame":
            return "0x0f"
        elif hair_color == "Pixie":
            return "0x10"
        elif hair_color == "Sunset":
            return "0x11"
        elif hair_color == "Unicorn":
            return "0x12"
        elif hair_color == "Wild":
            return "0x13"
        elif hair_color == "Nothing":
            return "0x14"
        else:
            raise ValueError("Invalid hair color trait")

    def extract_hair_front_trait(self, hair_front: str) -> str:
        if hair_front == "Banks":
            return "0x00"
        elif hair_front == "Fringe":
            return "0x01"
        elif hair_front == "Intakes":
            return "0x02"
        elif hair_front == "LockHeart":
            return "0x03"
        elif hair_front == "Double":
            return "0x04"
        elif hair_front == "Attendant":
            return "0x05"
        elif hair_front == "Messy":
            return "0x06"
        elif hair_front == "Meganekko":
            return "0x07"
        elif hair_front == "Pointy":
            return "0x08"
        elif hair_front == "Twins":
            return "0x09"
        elif hair_front == "Yuri":
            return "0x0a"
        elif hair_front == "Nothing":
            return "0x0b"
        else:
            raise ValueError("Invalid hair front trait")

    def extract_eye_trait(self, eye: str) -> str:
        if eye == "Innocent":
            return "0x00"
        elif eye == "Naughty":
            return "0x01"
        elif eye == "Kind":
            return "0x02"
        elif eye == "Playful":
            return "0x03"
        elif eye == "Crying":
            return "0x04"
        elif eye == "Hostile":
            return "0x05"
        elif eye == "Wink":
            return "0x06"
        elif eye == "Evil":
            return "0x07"
        else:
            raise ValueError("Invalid eye trait")

    def extract_eye_color_trait(self, eye_color: str) -> str:
        if eye_color == "Blue":
            return "0x00"
        elif eye_color == "Cyan":
            return "0x01"
        elif eye_color == "Gray":
            return "0x02"
        elif eye_color == "Green":
            return "0x03"
        elif eye_color == "Pink":
            return "0x04"
        elif eye_color == "Purple":
            return "0x05"
        elif eye_color == "Red":
            return "0x06"
        elif eye_color == "Yellow":
            return "0x07"
        else:
            raise ValueError("Invalid eye color trait")

    def extract_mouth_trait(self, mouth: str) -> str:
        if mouth == "Relaxed":
            return "0x00"
        elif mouth == "Confused":
            return "0x01"
        elif mouth == "Grinning":
            return "0x02"
        elif mouth == "Afraid":
            return "0x03"
        elif mouth == "Sad":
            return "0x04"
        elif mouth == "Surprised":
            return "0x05"
        elif mouth == "Yummy":
            return "0x06"
        elif mouth == "Wicked":
            return "0x07"
        elif mouth == "Sly":
            return "0x08"
        elif mouth == "Scared":
            return "0x09"
        elif mouth == "Ahegao":
            return "0x0a"
        elif mouth == "Laugh":
            return "0x0b"
        elif mouth == "Disappointed":
            return "0x0c"
        elif mouth == "Happy":
            return "0x0d"
        elif mouth == "Melting":
            return "0x0e"
        elif mouth == "Smile":
            return "0x0f"
        elif mouth == "Confused":
            return "0x10"
        elif mouth == "Tongue":
            return "0x11"
        elif mouth == "Smirk":
            return "0x12"
        elif mouth == "Scream":
            return "0x13"
        elif mouth == "Hehe":
            return "0x14"
        elif mouth == "Nothing":
            return "0x15"
        else:
            raise ValueError("Invalid mouth trait")

    def extract_body_trait(self, body: str) -> str:
        if body == "Human Light":
            return "0x00"
        elif body == "Dark Elf":
            return "0x01"
        elif body == "Goblin":
            return "0x02"
        elif body == "Undead":
            return "0x03"
        elif body == "Fallen":
            return "0x04"
        elif body == "Demon":
            return "0x05"
        elif body == "Golden":
            return "0x06"
        elif body == "Lamia":
            return "0x07"
        elif body == "Silver":
            return "0x08"
        elif body == "Slime":
            return "0x09"
        elif body == "Human Dark":
            return "0x0a"
        else:
            raise ValueError("Invalid body trait")

    def extract_hat_trait(self, hat: str) -> str:
        if hat == "Nothing":
            return "0x00"
        elif hat == "Anubis":
            return "0x01"
        elif hat == "Beret Dark":
            return "0x02"
        elif hat == "Beret Bright":
            return "0x03"
        elif hat == "Bunny Up":
            return "0x04"
        elif hat == "Bunny":
            return "0x05"
        elif hat == "Bunny Clip":
            return "0x06"
        elif hat == "Butterfly":
            return "0x07"
        elif hat == "Captain":
            return "0x08"
        elif hat == "Cyber Neko":
            return "0x09"
        elif hat == "Doggy Black":
            return "0x0a"
        elif hat == "Doggy Blonde":
            return "0x0b"
        elif hat == "Doggy Blue":
            return "0x0c"
        elif hat == "Doggy Brown":
            return "0x0d"
        elif hat == "Doggy Cyan":
            return "0x0e"
        elif hat == "Doggy Gray":
            return "0x0f"
        elif hat == "Doggy Green":
            return "0x10"
        elif hat == "Doggy Pink":
            return "0x11"
        elif hat == "Doggy Purple":
            return "0x12"
        elif hat == "Doggy Red":
            return "0x13"
        elif hat == "Glass Tiara":
            return "0x14"
        elif hat == "Googles":
            return "0x15"
        elif hat == "Hair Clip":
            return "0x16"
        elif hat == "Helm":
            return "0x17"
        elif hat == "Horn Ring":
            return "0x18"
        elif hat == "Horn":
            return "0x19"
        elif hat == "Iron Helm":
            return "0x1a"
        elif hat == "Kitsune Mask":
            return "0x1b"
        elif hat == "Maid Band":
            return "0x1c"
        elif hat == "Maid":
            return "0x1d"
        elif hat == "Mech":
            return "0x1e"
        elif hat == "Military":
            return "0x1f"
        elif hat == "Neko Black":
            return "0x20"
        elif hat == "Neko Blonde":
            return "0x21"
        elif hat == "Neko Blue":
            return "0x22"
        elif hat == "Neko Brown":
            return "0x23"
        elif hat == "Neko Cyan":
            return "0x24"
        elif hat == "Neko Gray":
            return "0x25"
        elif hat == "Neko Green":
            return "0x26"
        elif hat == "Neko Pink":
            return "0x27"
        elif hat == "Neko Purple":
            return "0x28"
        elif hat == "Neko Red":
            return "0x29"
        elif hat == "Nun":
            return "0x2a"
        elif hat == "Nurse":
            return "0x2b"
        elif hat == "Oni":
            return "0x2c"
        elif hat == "Pirate Kara":
            return "0x2d"
        elif hat == "Pirate":
            return "0x2e"
        elif hat == "Corsair Hat":
            return "0x2f"
        elif hat == "Ribbon Bright":
            return "0x30"
        elif hat == "Ribbon Dark":
            return "0x31"
        elif hat == "Samurai Demon":
            return "0x32"
        elif hat == "Samurai Straw":
            return "0x33"
        elif hat == "Slime":
            return "0x34"
        elif hat == "Summer":
            return "0x35"
        elif hat == "Tactical Googles":
            return "0x36"
        elif hat == "Tiara":
            return "0x37"
        elif hat == "Tiny Bright":
            return "0x38"
        elif hat == "Tiny Dark":
            return "0x39"
        elif hat == "Tropical Flower":
            return "0x3a"
        elif hat == "Veil Misty":
            return "0x3b"
        elif hat == "Veil":
            return "0x3c"
        elif hat == "Witch":
            return "0x3d"
        elif hat == "Witch Hat":
            return "0x3e"
        elif hat == "Space Helmet":
            return "0x3f"
        else:
            raise ValueError("Invalid hat trait")

    def extract_face_trait(self, face: str) -> str:
        if face == "Nothing":
            return "0x00"
        elif face == "Demon Mask Blue":
            return "0x01"
        elif face == "Demon Mask Black":
            return "0x02"
        elif face == "Demon Mask Wood":
            return "0x03"
        elif face == "Bone Mask":
            return "0x04"
        elif face == "Ninja Mask":
            return "0x05"
        elif face == "UwU mask":
            return "0x06"
        elif face == "Surgical Face Mask":
            return "0x07"
        elif face == "Gas Mask":
            return "0x08"
        elif face == "Gas Mask White":
            return "0x09"
        elif face == "Glasses Rectangle":
            return "0x0a"
        elif face == "Glasses Round":
            return "0x0b"
        elif face == "Monocle Yellow":
            return "0x0c"
        elif face == "Monocole Purple":
            return "0x0d"
        elif face == "Blindfold Black":
            return "0x0e"
        elif face == "Blindfold White":
            return "0x0f"
        elif face == "Medical Eye Patch":
            return "0x10"
        elif face == "Blood":
            return "0x11"
        elif face == "Face Scar":
            return "0x12"
        elif face == "Nosebleed":
            return "0x13"
        elif face == "Sweat":
            return "0x14"
        elif face == "Paint":
            return "0x15"
        elif face == "Sun Glasses":
            return "0x16"
        elif face == "Metal Masquerade":
            return "0x17"
        elif face == "Doki Doki":
            return "0x18"
        elif face == "Mustache Blonde":
            return "0x19"
        elif face == "Mustache Black":
            return "0x1a"
        elif face == "Pencil":
            return "0x1b"
        elif face == "Tattoo Cat":
            return "0x1c"
        elif face == "Tattoo Abstract":
            return "0x1d"
        elif face == "Tattoo":
            return "0x1e"
        elif face == "Ear Mic Red":
            return "0x1f"
        elif face == "Ear Mic Black":
            return "0x20"
        elif face == "Ear Mic BabyBlue":
            return "0x21"
        elif face == "Scouter":
            return "0x22"
        elif face == "Kitsune Mask":
            return "0x23"
        elif face == "Vendetta Mask":
            return "0x24"
        elif face == "Pirate Eye Patch ADA":
            return "0x25"
        elif face == "Pirate Eye Patch Bitcoin":
            return "0x26"
        elif face == "Pirate Eye Patch Ethereum":
            return "0x27"
        elif face == "Pirate Eye Patch Solana":
            return "0x28"
        elif face == "Pirate Eye Patch":
            return "0x29"
        else:
            raise ValueError("Unknown face trait")

    def extract_hands_trait(self, hands: str) -> str:
        if hands == "Nothing":
            return "0x00"
        elif hands == "Shy":
            return "0x01"
        elif hands == "Love":
            return "0x02"
        elif hands == "Heart":
            return "0x03"
        elif hands == "Victory":
            return "0x04"
        elif hands == "Axe":
            return "0x05"
        elif hands == "Bow":
            return "0x06"
        elif hands == "Fireball":
            return "0x07"
        elif hands == "Katana":
            return "0x08"
        elif hands == "Pistol":
            return "0x09"
        elif hands == "Shrine":
            return "0x0a"
        elif hands == "Rifle":
            return "0x0b"
        elif hands == "Great Sword":
            return "0x0c"
        else:
            raise ValueError("Unknown hands trait")

    def extract_effect_trait(self, effect: str) -> str:
        if effect == "Nothing":
            return "0x00"
        elif effect == "Angry":
            return "0x01"
        elif effect == "Annoyed":
            return "0x02"
        elif effect == "Anxious":
            return "0x03"
        elif effect == "Depressed":
            return "0x04"
        elif effect == "Noticed":
            return "0x05"
        elif effect == "Shocked":
            return "0x06"
        elif effect == "Sweating":
            return "0x07"
        elif effect == "Flower":
            return "0x08"
        elif effect == "Hearts":
            return "0x09"
        elif effect == "Sparkles":
            return "0x0a"
        else:
            raise ValueError("Unknown effect trait")

    def extract_trait_count(self, trait_count: str) -> str:
        if trait_count == "7":
            return "0x00"
        elif trait_count == "8":
            return "0x01"
        elif trait_count == "9":
            return "0x02"
        elif trait_count == "10":
            return "0x03"
        elif trait_count == "11":
            return "0x04"
        elif trait_count == "12":
            return "0x05"
        elif trait_count == "13":
            return "0x06"
        elif trait_count == "14":
            return "0x07"
        else:
            raise ValueError("Unknown trait count")
