
# https://pypi.org/project/NBT/
# pip install NBT

from nbt import nbt

nbtfile = nbt.NBTFile("Demo_World/level.dat", 'rb')
# nbtfile = nbt.NBTFile("level.dat", 'rb') # test

# making game easy
# nbtfile["Data"]["GameRules"]['doMobSpawning'].value = 'false'
# nbtfile["Data"]["GameRules"]['fallDamage'].value = 'false'
# nbtfile["Data"]["GameRules"]['fireDamage'].value = 'false'
# nbtfile["Data"]["GameRules"]['freezeDamage'].value = 'false'
# nbtfile["Data"]["GameRules"]['drowningDamage'].value = 'false'
# nbtfile["Data"]['Player']['abilities']['walkSpeed'].value = 0.30000000298023224
nbtfile["Data"]["Time"].value = -9223372036854623192

for tag in nbtfile["Data"].tags:
    print(tag.tag_info())

nbtfile.write_file("Demo_World/level.dat") # save


'''
TAG_Double('BorderCenterX'): 0.0
TAG_Double('BorderCenterZ'): 0.0
TAG_Double('BorderDamagePerBlock'): 0.2
TAG_Double('BorderSafeZone'): 5.0
TAG_Double('BorderSize'): 59999968.0
TAG_Double('BorderSizeLerpTarget'): 59999968.0
TAG_Long('BorderSizeLerpTime'): 0
TAG_Double('BorderWarningBlocks'): 5.0
TAG_Double('BorderWarningTime'): 15.0
TAG_Compound('CustomBossEvents'): {0 Entries}
TAG_Compound('DataPacks'): {2 Entries}
TAG_Int('DataVersion'): 3465
TAG_Long('DayTime'): 40882
TAG_Byte('Difficulty'): 2
TAG_Byte('DifficultyLocked'): 0
TAG_Compound('DragonFight'): {4 Entries}
TAG_Compound('GameRules'): {45 Entries}
TAG_Int('GameType'): 0
TAG_Long('LastPlayed'): 1690456489327
TAG_String('LevelName'): Demo World
TAG_Compound('Player'): {39 Entries}
TAG_List('ScheduledEvents'): [0 _TAG_End(s)]
TAG_List('ServerBrands'): [1 TAG_String(s)]
TAG_Float('SpawnAngle'): 0.0
TAG_Int('SpawnX'): -48
TAG_Int('SpawnY'): 69
TAG_Int('SpawnZ'): 64
TAG_Long('Time'): -120
TAG_Compound('Version'): {4 Entries}
TAG_Int('WanderingTraderSpawnChance'): 25
TAG_Int('WanderingTraderSpawnDelay'): 2400
TAG_Byte('WasModded'): 0
TAG_Compound('WorldGenSettings'): {4 Entries}
TAG_Byte('allowCommands'): 0
TAG_Int('clearWeatherTime'): 0
TAG_Byte('hardcore'): 0
TAG_Byte('initialized'): 1
TAG_Int('rainTime'): 124055
TAG_Byte('raining'): 0
TAG_Int('thunderTime'): 147179
TAG_Byte('thundering'): 0
TAG_Int('version'): 19133
'''