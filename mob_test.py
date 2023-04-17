
def generate_command(mob_type, weapon, armor, enchantment, effect):
    #armor_str = ",".join([f"{{id:\"{a}\",Count:1b}}" for a in armor])
    armor_str = (f"{{Count:1,id:{armor}}}")    
    #return f"/summon {mob_type} ~ ~ ~ {{CustomName:\"Fire Resistant Zombie\", HandItems:[{{Count:1,id:{weapon},tag:{{Enchantments:[{enchantment}]}}}},{{}}],ArmorItems:[{armor_str}],ActiveEffects:[{effect}]}}"
    #tag:{Enchantments:[{id:projectile_protection,lvl:3}]}
    return f"/summon {mob_type} ~ ~ ~ {{PersistanceRequired:1, HandItems:[{{Count:1,id:{weapon},tag:{{Enchantments:[{enchantment}]}}}},{{}}],ArmorItems:[{armor_str}],ActiveEffects:[{effect}]}}"

mob_types = ["pig", "wolf", "zombie", "skeleton", "creeper"]
weapons = ["diamond_sword", "golden_axe", "iron_pickaxe"]
armors = ["diamond_chestplate", "iron_leggings", "leather_boots", "diamond_leggings", "diamond_boots", "iron_boots", "leather_chestplate", "leather_leggings", "iron_chestplate", "golden_chestplate", "golden_leggings", "golden_boots"]
enchantments = ["{id:thorns,lvl:2}", "{id:projectile_protection,lvl:3}", "{id:fire_aspect,lvl:2}", "{id:knockback,lvl:3}", "{id:sharpness,lvl:5}", "{id:protection,lvl:4}"]
effects = ["{id:0,Amplifier:1,Duration:100}","{id:1,Amplifier:1,Duration:100}", "{id:12, Amplifier:10,Duration:200}", "{id:10,Amplifier:3,Duration:300}"]


#print(generate_command("zombie", "diamond_sword", "diamond_chestplate", "{id:16,lvl:4}", "{Id:12,Amplifier:0,Duration:2147483647}"))
print(generate_command("zombie", "diamond_sword", "iron_helmet", enchantments[1], "{Id:12,Amplifier:0,Duration:2147483647}"))

#/summon zombie ~ ~ ~ {CustomName:"Fire Resistant Zombie", HandItems:[{id:"diamond_sword",Count:1b,tag:{Enchantments:[{id:16,lvl:4}]}}],ArmorItems:[{id:"golden_chestplate",Count:1b}],ActiveEffects:[{Id:12,Amplifier:0,Duration:2147483647}]}
#/summon zombie ~ ~1 ~ {PersistenceRequired:1,LeftHanded:1b,HandItems:[{Count:1,id:diamond_sword,tag:{Enchantments:[{id:sharpness,lvl:5},{id:mending,lvl:1}]}},{}],ArmorItems:[{Count:1,id:diamond_boots},{Count:1,id:chainmail_leggings,tag:{Enchantments:[{id:projectile_protection,lvl:3}]}},{Count:1,id:diamond_chestplate,tag:{Enchantments:[{id:thorns,lvl:2}]}},{Count:1,id:iron_helmet}],HandDropChances:[0.6f,0.0f],ArmorDropChances:[1.0f,1.0f,1.0f,1.0f],ActiveEffects:[{Id:10,Amplifier:0,Duration:999999}]}
#/summon zombie ~ ~ ~ {CustomName:"Fire Resistant Zombie", HandItems:[{Count:1,id:diamond_sword,tag:{Enchantments:[{id:projectile_protection,lvl:3}]}},{}],ArmorItems:[{Count:1,id:iron_helmet},tag:{Enchantments:[{id:projectile_protection,lvl:3}}],ActiveEffects:[{Id:12,Amplifier:0,Duration:2147483647}]}



Aqua_Infinity_Helmets = ["{id:8,lvl:1}"]
Bane_of_Arthropods_ = ["{id:11,lvl:1}", "{id:11,lvl:2}", "{id:11,lvl:3}", "{id:11,lvl:4}", "{id:11,lvl:5}"]
Blast_Protection = ["{id:3,lvl:1}", "{id:3,lvl:2}", "{id:3,lvl:3}", "{id:3,lvl:4}"]
Channeling = ["{id:32,lvl:1}"]
Depth_Strider = ["{id:7,lvl:1}", "{id:7,lvl:2}", "{id:7,lvl:3}"]
Efficiency = ["{id:15,lvl:1}", "{id:15,lvl:2}", "{id:15,lvl:3}", "{id:15,lvl:4}", "{id:15,lvl:5}"]
Feather_Falling = ["{id:2,lvl:1}", "{id:2,lvl:2}", "{id:2,lvl:3}", "{id:2,lvl:4}"]
Fire_Aspect = ["{id:13,lvl:1}", "{id:13,lvl:2}"]
Fire_Protection = ["{id:1,lvl:1}", "{id:1,lvl:2}", "{id:1,lvl:3}", "{id:1,lvl:4}"]
Flame = ["{id:21,lvl:1}"]
Fortune = ["{id:18,lvl:1}", "{id:18,lvl:2}", "{id:18,lvl:3}"]
Frost_Walker = ["{id:25,lvl:1}", "{id:25,lvl:2}"]
Impaling = ["{id:29,lvl:1}", "{id:29,lvl:2}", "{id:29,lvl:3}", "{id:29,lvl:4}", "{id:29,lvl:5}"]
Infinity = ["{id:22,lvl:1}"]
Knockback = ["{id:12,lvl:1}", "{id:12,lvl:2}"]
Loyalty = ["{id:31,lvl:1}", "{id:31,lvl:2}", "{id:31,lvl:3}"]
Looting = ["{id:14,lvl:1}", "{id:14,lvl:2}", "{id:14,lvl:3}"]
Luck_of_the_Sea = ["{id:23,lvl:1}", "{id:23,lvl:2}", "{id:23,lvl:3}"]
Lure = ["{id:24,lvl:1}", "{id:24,lvl:2}", "{id:24,lvl:3}"]
Mending = ["{id:26,lvl:1}"]
Multishot = ["{id:33,lvl:1}"]
Piercing = ["{id:34,lvl:1}", "{id:34,lvl:2}", "{id:34,lvl:3}", "{id:34,lvl:4}"]
Power = ["{id:19,lvl:1}", "{id:19,lvl:2}", "{id:19,lvl:3}", "{id:19,lvl:4}", "{id:19,lvl:5}"]
Projectile_Protection = ["{id:4,lvl:1}", "{id:4,lvl:2}", "{id:4,lvl:3}", "{id:4,lvl:4}"]
Protection = ["{id:0,lvl:1}", "{id:0,lvl:2}", "{id:0,lvl:3}", "{id:0,lvl:4}"]
Punch = ["{id:20,lvl:1}", "{id:20,lvl:2}"]
Quick_Charge = ["{id:35,lvl:1}", "{id:35,lvl:2}", "{id:35,lvl:3}"]
Respiration = ["{id:6,lvl:1}", "{id:6,lvl:2}", "{id:6,lvl:3}"]
