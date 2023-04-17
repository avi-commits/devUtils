import random


def generate_command(mob_type, weapon, weapon_enchantment, armor, armor_enchantment, effect):
    armor_str = ""
    for item, enchant in zip(armor, armor_enchantment):   
        if enchant:
            #concate the armor string with the armor item and enchantment and a comma but don't add a comma to the last item
            armor_str += f"{{Count:1,id:{item},tag:{{Enchantments:[{enchant}]}}}},"

        else:
            armor_str += f"{{Count:1,id:{item}}},"

    weapon_str = ""
    for item, enchant in zip(weapon, weapon_enchantment):
        if enchant:
            weapon_str += f"{{Count:1,id:{item},tag:{{Enchantments:[{enchant}]}}}},"
        else:
            weapon_str += f"{{Count:1,id:{item}}},"

    command = f"/summon {mob_type} ~ ~1 ~ {{PersistenceRequired:1,LeftHanded:1b,HandItems:[{weapon_str},{{}}],ArmorItems:[{armor_str}],HandDropChances:[1.0f,0.0f],ArmorDropChances:[0.2f,1.0f,1.0f,0.6f],ActiveEffects:[{effect}]}}"

    #remove comma from last item
    command = command.replace("},]", "}]")
    command = command.replace(",,{}", ",{}")
    return command


mob_types = ["pig", "wolf", "zombie", "skeleton", "creeper"]
weapons = ["diamond_sword", "golden_axe", "iron_pickaxe"]
armors = ["diamond_chestplate", "iron_leggings", "leather_boots", "diamond_leggings", "diamond_boots", "iron_boots", "leather_chestplate", "leather_leggings", "iron_chestplate", "golden_chestplate", "golden_leggings", "golden_boots"]
enchantments = ["{id:thorns,lvl:2}", "{id:projectile_protection,lvl:3}", "{id:fire_aspect,lvl:2}", "{id:knockback,lvl:3}", "{id:sharpness,lvl:5}", "{id:protection,lvl:4}"]
effects = ["{id:0,Amplifier:1,Duration:100}","{id:1,Amplifier:1,Duration:100}", "{id:12, Amplifier:10,Duration:200}", "{id:10,Amplifier:3,Duration:300}","{Id:24,Amplifier:0,Duration:2147483647}"]

armor = ["netherite_boots", "chainmail_leggings", "diamond_chestplate", "golden_helmet"]
enchantment = ["{id:soul_speed,lvl:3}", "{id:swift_sneak,lvl:2}", "{id:vanishing_curse,lvl:1}", "{id:aqua_affinity,lvl:2}"]

weapon = ["diamond_sword"]

w_enchantment = ["{id:bane_of_arthropods,lvl:3}"]
zip(armor, enchantment)

helmet_enchantment = []
chestplate_enchantment = []
leggings_enchantment = []
boots_enchantment = []



#print the contents of zip
for item in zip(armor, enchantment):
    print(item)

print(generate_command("zombie", weapon, w_enchantment, armor, enchantment, effects[4]))

