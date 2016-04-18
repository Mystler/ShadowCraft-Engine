# None should be used to indicate unknown values
# The Proc class takes these parameters:
# stat, value, duration, proc_name, default_behaviour, max_stacks=1, can_crit=True, spell_behaviour=None
# Assumed heroic trinkets have the same behaviour as the non-heroic kin.
# behaviours must have a 'default' key so that the proc is properly initialized.
allowed_procs = {
    #generic
    'rogue_poison': {
        'stat': 'weird_proc',
        'value': 0,
        'duration': 0,
        'proc_name': 'rogue_poison',
        'type': 'perc',
        'icd': 0,
        'proc_rate': 1,
        'trigger': 'all_attacks'
    },
    #potions
    'draenic_agi_pot': {
        'stat': 'stats',
        'value': {'agi':1000},
        'duration': 25,
        'proc_name': 'Draenic Agi Potion',
        'item_level': 100,
        'type': 'icd',
        'source': 'unique',
        'icd': 0,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'draenic_agi_prepot': {
        'stat': 'stats',
        'value': {'agi':1000},
        'duration': 23,
        'proc_name': 'Draenic Agi Prepot',
        'item_level': 100,
        'type': 'icd',
        'source': 'unique',
        'icd': 0,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'virmens_bite': {
        'stat': 'stats',
        'value': {'agi':456},
        'duration': 25,
        'proc_name': 'Virmens Bite',
        'item_level': 90,
        'type': 'icd',
        'source': 'unique',
        'icd': 0,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'virmens_bite_prepot': {
        'stat': 'stats',
        'value': {'agi':456},
        'duration': 23,
        'proc_name': 'Virmens Bite',
        'item_level': 90,
        'type': 'icd',
        'source': 'unique',
        'icd': 0,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    #weapon enchant support
    'mark_of_the_shattered_hand_dot': {
        'stat': 'physical_dot',
        'value': 750,
        'duration': 6,
        'proc_name': 'Mark of the Shattered Hand DOT',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 100,
        'icd': 0,
        'proc_rate': 2.5,
        'can_crit': False,
        'haste_scales': True,
        'trigger': 'all_attacks',
    },
    #racials
    'touch_of_the_grave': {
        'stat': 'spell_damage',
        'value': 0,
        'duration': 0,
        'max_stacks': 0,
        'proc_name': 'Touch of the Grave',
        'type': 'icd',
        'icd': 15,
        'proc_rate': .20,
        'trigger': 'all_attacks'
    },
    'rocket_barrage': {
        'stat': 'spell_damage',
        'value': 0,
        'duration': 0,
        'max_stacks': 0,
        'proc_name': 'Rocket Barrage',
        'type': 'icd',
        'icd': 120,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    #gear procs
    'fury_of_xuen': {
        'stat':'physical_damage',
        'value': 1,
        'duration': 0,
        'proc_name': 'Fury of Xuen',
        'scaling': 0.0,
        'item_level': 0,
        'type': 'rppm',
        'source': 'unique',
        'icd': 3,
        'proc_rate': 1.74, #1.55 mut, 1.15 com, 1.0 sub
        'haste_scales': True,
        'trigger': 'all_attacks'
    },
    'legendary_capacitive_meta': {
        'stat':'spell_damage',
        'value': 280,
        'duration': 0,
        'max_stacks': 5,
        'proc_name': 'Lightning Strike (meta)',
        'scaling': 0.0,
        'item_level': 541,
        'type': 'rppm',
        'source': 'unique',
        'icd': 1,
        'proc_rate': 19.27, #1.789 mut, 1.136 com, 1.114 sub
        'haste_scales': True,
        'trigger': 'all_attacks'
    },
    'archmages_incandescence': {
        'stat':'stats_modifier',
        'value': {'agi':.10},
        'duration': 10,
        'proc_name': 'Archmages Incandescence',
        'scaling': 0.0,
        'item_level': 541,
        'type': 'rppm',
        'source': 'unique',
        'icd': 1,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'archmages_greater_incandescence': {
        'stat':'stats_modifier',
        'value': {'agi':.15},
        'duration': 10,
        'proc_name': 'Archmages Greater Incandescence',
        'scaling': 0.0,
        'item_level': 541,
        'type': 'rppm',
        'source': 'unique',
        'icd': 1,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    #6.2.3 procs
    'infallible_tracking_charm': {
        'stat':'spell_damage',
        'value': 42872,
        'duration': 0,
        'proc_name': "Cleansing Flame",
        #'scaling': 61.1583452211,
        'item_level': 715,
        'type': 'rppm',
        'source': 'trinket',
        'proc_rate': 3.5,
        'haste_scales': True,
        'can_crit': False,
        'trigger': 'all_attacks'
   },

    'infallible_tracking_charm_mod': {
        'stat':'damage_modifier',
        'value': {'damage_mod': 10},
        'proc_name': "Cleansing Flame",
        'scaling': 0.0,
        'item_level': 715,
        'type': 'rppm',
        'source': 'trinket',
        'duration': 5,
        'proc_rate': 3.5,
        'haste_scales': True,
        'trigger': 'all_attacks'
   },


    #6.2 procs
    'maalus': {
        'stat': 'damage_modifier',
        'value': {'damage_mod': 2500},
        'duration': 15,
        'proc_name': 'Maalus',
        'upgradable': True,
        'scaling': 2.95857988166,
        'item_level': 735,
        'type': 'icd',
        'source': 'trinket',
        'icd': 120,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },

    'felmouth_frenzy': {
        'stat':'spell_damage',
        'value': 1,
        'duration': 0,
        'proc_name': 'Fel Lash',
        'scaling': 0.0,
        'type': 'rppm',
        'source': 'unique',
        'icd': 0,
        'proc_rate': 2,
        'haste_scales': True,
        'can_crit': False,
        'trigger': 'all_attacks'
    },

    'malicious_censer': {
        'stat': 'stats',
        'value': {'agi':1093},
        'duration': 20,
        'proc_name': 'Malicious Censer',
        'upgradable': True,
        'scaling': 1.79180327869,
        'item_level': 700,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },

    'soul_capacitor': {
        'stat': 'damage_modifier',
        'value': {'damage_mod': 2677},
        'duration': 10,
        'proc_name': 'Soul Capacitor',
        'upgradable': True,
        'scaling': 4.59965635,
        'item_level': 695,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },

    'mirror_of_the_blademaster': {
        'stat': 'physical_damage',
        'value': {'damage': 1},
        'duration': 20,
        'proc_name': 'Mirror of the Blademaster',
        'upgradable': True,
        'scaling': 1.0,
        'item_level': 695,
        'type': 'icd',
        'source': 'trinket',
        'icd': 60,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },

    'bleeding_hollow_toxin_vessel': {
        'stat': 'ability_modifer',
        'value': {'ability_mod':5149},
        'duration': 0,
        'proc_name': 'Bleeding Hollow Toxin Vessel',
        'upgradable': True,
        'scaling': 8.05790297,
        'item_level': 705,
        'type': 'perk',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.0,
        'trigger': 'all_attacks'
    },

    #all alchemy trinket upgrades are just scales
    #with different names, collapsed into single proc
    'alchemy_stone': {
        'stat': 'stats',
        'value': {'agi':1350},
        'duration': 15,
        'proc_name': 'Alchemy Trinket Proc',
        'upgradable': True,
        'scaling': 2.6670000553,
        'item_level': 680,
        'type': 'icd',
        'source': 'trinket',
        'icd': 55,
        'proc_rate': 0.35,
        'trigger': 'all_attacks'
    },
    #6.0 procs
    'humming_blackiron_trigger': {
        'stat': 'stats',
        'value': {'crit':131},
        'duration': 10,
        'proc_name': 'Humming Blackiron Trigger',
        'upgradable': True,
        'scaling': 0.2969999909 * 10.5,
        'item_level': 665,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'meaty_dragonspine_trophy': {
        'stat': 'stats',
        'value': {'haste':1913},
        'duration': 10,
        'proc_name': 'Meaty Dragonspine Trophy',
        'upgradable': True,
        'scaling': 4.3477997780,
        'item_level': 665,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'formidable_jar_of_doom': {
        'stat': 'stats',
        'value': {'mastery':1743},
        'duration': 10,
        'proc_name': 'Formidable Jar of Doom',
        'upgradable': True,
        'scaling': 4.3477997780,
        'item_level': 665,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'scales_of_doom': {
        'stat': 'stats',
        'value': {'multistrike':1743},
        'duration': 10,
        'proc_name': 'Scales of Doom',
        'upgradable': True,
        'scaling': 4.3477997780,
        'item_level': 665,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'blackheart_enforcers_medallion': {
        'stat': 'stats',
        'value': {'multistrike':1665},
        'duration': 10,
        'proc_name': 'Blackheart Enforcers Medallion',
        'upgradable': True,
        'scaling': 4.3477997780,
        'item_level': 665,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'lucky_doublesided_coin': {
        'stat': 'stats',
        'value': {'agi':1467},
        'duration': 20,
        'proc_name': 'Lucky Double-sided Coin',
        'upgradable': True,
        'scaling': 3.3333330154,
        'item_level': 665,
        'type': 'icd',
        'source': 'trinket',
        'icd': 120,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'beating_heart_of_the_mountain': {
        'stat': 'stats',
        'value': {'multistrike':1467},
        'duration': 20,
        'proc_name': 'Beating Heart of the Mountain',
        'upgradable': True,
        'scaling': 3.3333330154,
        'item_level': 665,
        'type': 'icd',
        'source': 'trinket',
        'icd': 120,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'skull_of_war': {
        'stat': 'stats',
        'value': {'crit':1396},
        'duration': 20,
        'proc_name': 'Skull of War',
        'upgradable': True,
        'scaling': 4.0000000000,
        'item_level': 640,
        'type': 'icd',
        'source': 'trinket',
        'icd': 115,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'primal_combatants_ioc': {
        'stat': 'stats',
        'value': {'agi':505},
        'duration': 20,
        'proc_name': 'Primal Combatants Insignia of Conquest',
        'upgradable': True,
        'scaling': 1.7480000257,
        'item_level': 620,
        'type': 'icd',
        'source': 'trinket',
        'icd': 55,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'primal_combatants_boc': {
        'stat': 'stats',
        'value': {'versatility':358},
        'duration': 20,
        'proc_name': 'Primal Combatants Badge of Conquest',
        'upgradable': True,
        'scaling': 1.2384999990,
        'item_level': 620,
        'type': 'icd',
        'source': 'trinket',
        'icd': 60,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'gorashans_lodestone_spike': {
        'stat': 'stats',
        'value': {'multistrike':1060},
        'duration': 15,
        'proc_name': 'Gorashans Lodestone Spike',
        'upgradable': True,
        'scaling': 3.3333330154,
        'item_level': 630,
        'type': 'icd',
        'source': 'trinket',
        'icd': 90,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'turbulent_vial_of_toxin': {
        'stat': 'stats',
        'value': {'mastery':1060},
        'duration': 15,
        'proc_name': 'Turbulent Vial of Toxin',
        'upgradable': True,
        'scaling': 3.3333330154,
        'item_level': 630,
        'type': 'icd',
        'source': 'trinket',
        'icd': 90,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'kihras_adrenaline_injector': {
        'stat': 'stats',
        'value': {'mastery':1060},
        'duration': 20,
        'proc_name': 'Kihras Adrenaline Injector',
        'upgradable': True,
        'scaling': 3.3333330154,
        'item_level': 630,
        'type': 'icd',
        'source': 'trinket',
        'icd': 120,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
    'witherbarks_branch': {
        'stat': 'stats',
        'value': {'haste':1383},
        'duration': 10,
        'proc_name': 'Witherbarks Branch',
        'upgradable': True,
        'scaling': 4.3477997780,
        'item_level': 630,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'munificent_emblem_of_terror': {
        'stat': 'stats',
        'value': {'crit':1200},
        'duration': 10,
        'proc_name': 'Munificent Emblem of Terror',
        'upgradable': True,
        'scaling': 4.3477997780,
        'item_level': 615,
        'type': 'rppm',
        'source': 'trinket',
        'icd': 0,
        'proc_rate': 0.92,
        'trigger': 'all_attacks'
    },
    'void-touched_totem': {
        'stat': 'stats',
        'value': {'mastery':540},
        'duration': 20,
        'proc_name': 'Void-Touched Totem',
        'upgradable': True,
        'scaling': 2.3333330154,
        'item_level': 604,
        'type': 'icd',
        'source': 'trinket',
        'icd': 115, #correct?
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'smoldering_heart_of_hyperious': {
        'stat': 'stats',
        'value': {'mastery':540},
        'duration': 20,
        'proc_name': 'Smoldering Heart of Hyperious',
        'upgradable': True,
        'scaling': 2.3333330154,
        'item_level': 607,
        'type': 'icd',
        'source': 'trinket',
        'icd': 115, #correct?
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'draenic_philosophers_stone': {
        'stat': 'stats',
        'value': {'agi':771},
        'duration': 15,
        'proc_name': 'Draenic Philosophers Stone',
        'upgradable': True,
        'scaling': 2.6670000553,
        'item_level': 620,
        'type': 'icd',
        'source': 'trinket',
        'icd': 55, #correct?
        'proc_rate': 0.35,
        'trigger': 'all_attacks'
    },
    'rabid_talbuk_horn': {
        'stat': 'stats',
        'value': {'agi':430},
        'duration': 20,
        'proc_name': 'Rabid Talbuk Horn',
        'upgradable': True,
        'scaling': 2.0000000000,
        'item_level': 608,
        'type': 'icd',
        'source': 'trinket',
        'icd': 55,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'excavated_highmaul_knicknack': {
        'stat': 'stats',
        'value': {'agi':430},
        'duration': 20,
        'proc_name': 'Excavated Highmaul Knicknack',
        'upgradable': True,
        'scaling': 2.0000000000,
        'item_level': 608,
        'type': 'icd',
        'source': 'trinket',
        'icd': 55,
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'springrain_stone_of_rage': {
        'stat': 'stats',
        'value': {'mastery':572},
        'duration': 20,
        'proc_name': 'Springrain Stone of Rage',
        'upgradable': True,
        'scaling': 2.3333330154,
        'item_level': 608,
        'type': 'icd',
        'source': 'trinket',
        'icd': 55, #correct?
        'proc_rate': 0.15,
        'trigger': 'all_attacks'
    },
    'tormented_tooth_of_ferocity': {
        'stat': 'stats',
        'value': {'haste':800},
        'duration': 20,
        'proc_name': 'Tormented Tooth of Ferocity',
        'upgradable': True,
        'scaling': 3.3333330154,
        'item_level': 608,
        'type': 'icd',
        'source': 'trinket',
        'icd': 120,
        'proc_rate': 1.0,
        'trigger': 'all_attacks'
    },
}

allowed_melee_enchants = {
    #6.0
    'mark_of_the_frostwolf': {
        'stat': 'stats',
        'value': {'multistrike':500},
        'duration': 6,
        'max_stacks': 2,
        'proc_name': 'Mark of the Frostwolf',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 100,
        'icd': 0,
        'proc_rate': 3.0,
        'trigger': 'all_melee_attacks'
    },
    'mark_of_the_shattered_hand': {
        'stat': 'bleed_damage',
        'value': 1500, #triggers mark_of_the_shattered_hand_dot
        'duration': 0,
        'proc_name': 'Mark of the Shattered Hand',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 100,
        'icd': 0,
        'proc_rate': 2.5,
        'haste_scales': True,
        'trigger': 'all_attacks',
    },
    'mark_of_the_thunderlord': {
        'stat': 'stats',
        'value': {'crit':500},
        'duration': 12,
        'proc_name': 'Mark of the Thunderlord',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 100,
        'icd': 0,
        'proc_rate': 2.5,
        'trigger': 'all_melee_attacks'
    },
    'mark_of_the_bleeding_hollow': {
        'stat': 'stats',
        'value': {'mastery':500},
        'duration': 12,
        'proc_name': 'Mark of the Bleeding Hollow',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 100,
        'icd': 0,
        'proc_rate': 2.3,
        'trigger': 'all_melee_attacks'
    },
    'mark_of_warsong': {
        'stat': 'stats',
        'value': {'haste':5.5*100},
        'duration': 20,
        'proc_name': 'Mark of the Bleeding Hollow',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 100,
        'icd': 0,
        'proc_rate': 1.15,
        'trigger': 'all_melee_attacks'
    },
    #5.0
    'dancing_steel': {
        'stat': 'stats',
        'value': {'agi':103},
        'duration': 12,
        'proc_name': 'Dancing Steel',
        'type': 'rppm',
        'source': 'weapon',
        'item_level': 90,
        'icd': 0,
        'proc_rate': 2.53,
        'trigger': 'all_melee_attacks'
    },
}
