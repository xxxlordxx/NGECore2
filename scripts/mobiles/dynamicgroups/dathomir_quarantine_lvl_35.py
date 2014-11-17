import sys
from java.util import Vector
from services.spawn import DynamicSpawnGroup
from services.spawn import MobileTemplate

def addDynamicGroup(core):
	dynamicGroup = DynamicSpawnGroup()
	mobileTemplates = Vector()
	mobileTemplates.add('outbreak_afflicted_lvl_35')
	mobileTemplates.add('outbreak_deathtrooper_lvl_35')
	dynamicGroup.setMobiles(mobileTemplates)
	dynamicGroup.setGroupMembersNumber(-5)
	dynamicGroup.setName('dathomir_quarantine_lvl_35')
	dynamicGroup.setMaxSpawns(-1)
	dynamicGroup.setMinSpawnDistance(10)
	core.spawnService.addDynamicGroup('dathomir_quarantine_lvl_35', dynamicGroup)
	return
