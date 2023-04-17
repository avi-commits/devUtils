#!/usr/bin/python


def generate_mob_command(mob_type, location, weapons, armor, enchantments, effects):
    command = "/summon " + mob_type + " " + location + " " + "{"
    
    if len(weapons) > 0:
        command += "HandItems:[" + ",".join(weapons) + "],"
    if len(armor) > 0:
        command += "ArmorItems:[" + ",".join(armor) + "],"
    if len(enchantments) > 0:
        command += "Enchantments:[" + ",".join(enchantments) + "],"
    if len(effects) > 0:
        command += "ActiveEffects:[" + ",".join(effects) + "],"
    
    command += "}"
    
    return command


def main():
    
    mob_types = ["pig", "wolf", "zombie", "skeleton", "creeper", "spider", "enderman", "villager", "zombie_villager", "husk", "stray", "wither_skeleton", "zombie_pigman", "blaze", "cave_spider", "ghast", "magma_cube", "silverfish", "slime", "witch", "wither", "guardian", "elder_guardian", "shulker", "endermite", "evoker", "vex", "vindicator", "illusioner", "drowned", "phantom", "ravager", "pillager", "zoglin", "piglin", "piglin_brute", "hoglin", "zombified_piglin", "strider", "axolotl", "cat", "cod", "dolphin", "donkey", "drowned", "fox", "horse", "llama", "mooshroom", "mule", "ocelot", "panda", "parrot", "polar_bear", "pufferfish", "rabbit", "salmon", "sheep", "skeleton_horse", "squid", "trader_llama", "tropical_fish", "turtle", "villager", "wandering_trader", "witch", "wither_skeleton", "wolf", "zombie_horse", "zombie_villager", "zombie", "zombie_pigman", "zombie_villager", "zoglin", "zooglins", "zombie"]
    weapons = ["{id:\"diamond_sword\",Count:1b,tag:{}}", "{id:\"golden_axe\",Count:1b,tag:{}}", "{id:\"iron_pickaxe\",Count:1b,tag:{}}", "{id:\"stone_shovel\",Count:1b,tag:{}}", "{id:\"wooden_hoe\",Count:1b,tag:{}}", "{id:\"wooden_sword\",Count:1b,tag:{}}", "{id:\"stone_axe\",Count:1b,tag:{}}", "{id:\"iron_shovel\",Count:1b,tag:{}}", "{id:\"diamond_pickaxe\",Count:1b,tag:{}}", "{id:\"golden_shovel\",Count:1b,tag:{}}", "{id:\"stone_hoe\",Count:1b,tag:{}}", "{id:\"iron_axe\",Count:1b,tag:{}}", "{id:\"diamond_shovel\",Count:1b,tag:{}}", "{id:\"golden_pickaxe\",Count:1b,tag:{}}", "{id:\"stone_sword\",Count:1b,tag:{}}", "{id:\"iron_hoe\",Count:1b,tag:{}}", "{id:\"diamond_axe\",Count:1b,tag:{}}", "{id:\"golden_hoe\",Count:1b,tag:{}}", "{id:\"diamond_pickaxe\",Count:1b,tag:{}}", "{id:\"golden_sword\",Count:1b,tag:{}}", "{id:\"iron_sword\",Count:1b,tag:{}}"]
    armor = ["{id:\"diamond_chestplate\",Count:1b,tag:{}}", "{id:\"iron_leggings\",Count:1b,tag:{}}", "{id:\"leather_boots\",Count:1b,tag:{}}", "{id:\"golden_helmet\",Count:1b,tag:{}}", "{id:\"chainmail_chestplate\",Count:1b,tag:{}}", "{id:\"chainmail_leggings\",Count:1b,tag:{}}", "{id:\"chainmail_boots\",Count:1b,tag:{}}", "{id:\"chainmail_helmet\",Count:1b,tag:{}}", "{id:\"leather_chestplate\",Count:1b,tag:{}}", "{id:\"leather_leggings\",Count:1b,tag:{}}", "{id:\"leather_boots\",Count:1b,tag:{}}", "{id:\"leather_helmet\",Count:1b,tag:{}}", "{id:\"diamond_boots\",Count:1b,tag:{}}", "{id:\"diamond_helmet\",Count:1b,tag:{}}", "{id:\"iron_boots\",Count:1b,tag:{}}", "{id:\"iron_helmet\",Count:1b,tag:{}}", "{id:\"golden_boots\",Count:1b,tag:{}}", "{id:\"golden_helmet\",Count:1b,tag:{}}", "{id:\"diamond_leggings\",Count:1b,tag:{}}", "{id:\"iron_chestplate\",Count:1b,tag:{}}", "{id:\"golden_chestplate\",Count:1b,tag:{}}"]
    enchantments = ["{id:\"sharpness\",lvl:5}", "{id:\"protection\",lvl:4}", "{id:\"fire_aspect\",lvl:2}", "{id:\"knockback\",lvl:3}", "{id:\"looting\",lvl:3}", "{id:\"efficiency\",lvl:5}", "{id:\"unbreaking\",lvl:3}", "{id:\"fortune\",lvl:3}", "{id:\"silk_touch\",lvl:1}", "{id:\"power\",lvl:5}", "{id:\"punch\",lvl:2}", "{id:\"flame\",lvl:1}", "{id:\"infinity\",lvl:1}", "{id:\"luck_of_the_sea\",lvl:3}", "{id:\"lure\",lvl:3}", "{id:\"mending\",lvl:1}", "{id:\"respiration\",lvl:3}", "{id:\"aqua_affinity\",lvl:1}", "{id:\"depth_strider\",lvl:3}", "{id:\"frost_walker\",lvl:2}", "{id:\"bane_of_arthropods\",lvl:5}", "{id:\"feather_falling\",lvl:4}", "{id:\"blast_protection\",lvl:4}", "{id:\"projectile_protection\",lvl:4}", "{id:\"thorns\",lvl:3}", "{id:\"fire_protection\",lvl:4}", "{id:\"sweeping\",lvl:3}", "{id:\"channeling\",lvl:1}", "{id:\"impaling\",lvl:5}", "{id:\"loyalty\",lvl:3}", "{id:\"riptide\",lvl:3}", "{id:\"multishot\",lvl:1}", "{id:\"quick_charge\",lvl:3}", "{id:\"piercing\",lvl:4}", "{id:\"soul_speed\",lvl:3}", "{id:\"binding_curse\",lvl:1}", "{id:\"vanishing_curse\",lvl:1}"]
    effects = ["{id:0,Amplifier:1,Duration:100}","{id:1,Amplifier:1,Duration:100}", "{id:12, Amplifier:10,Duration:200}", "{id:10,Amplifier:3,Duration:300}", "{id:11,Amplifier:2,Duration:400}", "{id:13,Amplifier:1,Duration:500}", "{id:14,Amplifier:1,Duration:600}", "{id:15,Amplifier:1,Duration:700}", "{id:16,Amplifier:1,Duration:800}", "{id:17,Amplifier:1,Duration:900}", "{id:18,Amplifier:1,Duration:1000}", "{id:19,Amplifier:1,Duration:1100}", "{id:20,Amplifier:1,Duration:1200}", "{id:21,Amplifier:1,Duration:1300}", "{id:22,Amplifier:1,Duration:1400}", "{id:23,Amplifier:1,Duration:1500}", "{id:24,Amplifier:1,Duration:1600}", "{id:25,Amplifier:1,Duration:1700}", "{id:26,Amplifier:1,Duration:1800}", "{id:27,Amplifier:1,Duration:1900}", "{id:28,Amplifier:1,Duration:2000}", "{id:29,Amplifier:1,Duration:2100}", "{id:30,Amplifier:1,Duration:2200}", "{id:31,Amplifier:1,Duration:2300}", "{id:32,Amplifier:1,Duration:2400}", "{id:33,Amplifier:1,Duration:2500}", "{id:34,Amplifier:1,Duration:2600}", "{id:35,Amplifier:1,Duration:2700}", "{id:36,Amplifier:1,Duration:2800}", "{id:37,Amplifier:1,Duration:2900}", "{id:38,Amplifier:1,Duration:3000}", "{id:39,Amplifier:1,Duration:3100}", "{id:40,Amplifier:1,Duration:3200}", "{id:41,Amplifier:1,Duration:3300}", "{id:42,Amplifier:1,Duration:3400}", "{id:43,Amplifier:1}"]
    
    '''
    mob_types = ["pig", "wolf", "zombie", "skeleton", "creeper", "spider", "enderman", "villager", "zombie_villager", "husk", "stray", "wither_skeleton", "zombie_pigman", "blaze", "cave_spider", "ghast", "magma_cube", "silverfish", "slime", "witch", "wither", "guardian", "elder_guardian", "shulker", "endermite", "evoker", "vex", "vindicator", "illusioner", "drowned", "phantom", "ravager", "pillager", "zoglin", "piglin", "piglin_brute", "hoglin", "zombified_piglin", "strider", "axolotl", "cat", "cod", "dolphin", "donkey", "drowned", "fox", "horse", "llama", "mooshroom", "mule", "ocelot", "panda", "parrot", "polar_bear", "pufferfish", "rabbit", "salmon", "sheep", "skeleton_horse", "squid", "trader_llama", "tropical_fish", "turtle", "villager", "wandering_trader", "witch", "wither_skeleton", "wolf", "zombie_horse", "zombie_villager", "zombie", "zombie_pigman", "zombie_villager", "zoglin", "zooglins", "zombie"]
    weapons = ["{id:\"diamond_sword\",Count:1b,tag:{}}"]
    armor = ["{id:\"diamond_chestplate\",Count:1b,tag:{}}"]
    enchantments = ["{id:\"sharpness\",lvl:5}"]
    effects = ["{id:12, Amplifier: 0, Duration:2147483647}"]
    '''

    location = input("Enter the spawn location (e.g. ~0 ~0 ~0): ")
    
    for mob_type in mob_types:
        print("Generated command for " + mob_type + ":")
        print(generate_mob_command(mob_type, location, weapons, armor, enchantments, effects))

if __name__ == "__main__":
    main()
'''
def generate_command(mob_type, weapons, armor, enchantments, effects):
    command = "/summon " + mob_type + " -162 64 -254 {CustomName:\"Fire Resistant Zombie\",HandItems:["
    for weapon in weapons:
        command += weapon
        if weapon != weapons[-1]:
            command += ","
    command += "],ArmorItems:["
    for armor_piece in armor:
        command += armor_piece
        if armor_piece != armor[-1]:
            command += ","
    command += "],ActiveEffects:["
    for effect in effects:
        command += effect
        if effect != effects[-1]:
            command += ","
    command += "]}"

    # Apply enchantment to both weapons and armor
    if enchantments:
        command = command.replace("}}", f",{enchantments[0]}}}")

    return command

mob_types = ["zombie"]

weapons = ["{id:\"diamond_sword\",Count:1b,tag:{}}"]

armor = ["{id:\"diamond_chestplate\",Count:1b,tag:{}}", "{id:\"diamond_leggings\",Count:1b,tag:{}}", "{id:\"diamond_boots\",Count:1b,tag:{}}"]

enchantments = ["{ench:[{id:16,lvl:5}]}"]

effects = ["{Id:12,Amplifier:0,Duration:2147483647}"]

command = generate_command(mob_types[0], weapons, armor, enchantments, effects)

print(command)
'''

mob_types = ["pig", "wolf", "zombie", "skeleton", "creeper"]
weapons = ["{id:\"diamond_sword\",Count:1b,tag:{}}", "{id:\"golden_axe\",Count:1b,tag:{}}", "{id:\"iron_pickaxe\",Count:1b,tag:{}}"]
armor = ["{id:\"diamond_chestplate\",Count:1b,tag:{}}", "{id:\"iron_leggings\",Count:1b,tag:{}}", "{id:\"leather_boots\",Count:1b,tag:{}}"]
enchantments = ["{id:\"sharpness\",lvl:5}", "{id:\"protection\",lvl:4}", "{id:\"fire_aspect\",lvl:2}", "{id:\"knockback\",lvl:3}"]
effects = ["{id:0,Amplifier:1,Duration:100}","{id:1,Amplifier:1,Duration:100}", "{id:12, Amplifier:10,Duration:200}", "{id:10,Amplifier:3,Duration:300}"]
    