from .unit_id import UnitId
from .weapon_id import WeaponId

_UNIT_TO_WEAPON = {
    UnitId.TERRAN_MARINE: [WeaponId.GAUSS_RIFLE_NORMAL],
    UnitId.TERRAN_GHOST: [WeaponId.C10_CONCUSSION_RIFLE_NORMAL],
    UnitId.TERRAN_VULTURE: [WeaponId.FRAGMENTATION_GRENADE_NORMAL],
    UnitId.TERRAN_GOLIATH: [
        WeaponId.TWIN_AUTOCANNONS_NORMAL,
        WeaponId.HELLFIRE_MISSILE_PACK_NORMAL,
    ],
    UnitId.GOLIATH_TURRET: [WeaponId.HELLFIRE_MISSILE_PACK_NORMAL],
    UnitId.TERRAN_SIEGE_TANK_TANK_MODE: [WeaponId.ARCLITE_CANNON_NORMAL],
    UnitId.TANK_TURRET_TANK_MODE: [WeaponId.ARCLITE_CANNON_NORMAL],
    UnitId.TERRAN_SCV: [WeaponId.FUSION_CUTTER],
    UnitId.TERRAN_WRAITH: [
        WeaponId.BURST_LASERS_NORMAL,
        WeaponId.GEMINI_MISSILES_NORMAL,
    ],
    UnitId.GUI_MONTANG_FIREBAT: [WeaponId.FLAME_THROWER_GUI_MONTAG],
    UnitId.TERRAN_BATTLECRUISER: [
        WeaponId.ATS_LASER_BATTERY_NORMAL,
        WeaponId.ATA_LASER_BATTERY_NORMAL,
    ],
    UnitId.VULTURE_SPIDER_MINE: [WeaponId.SPIDER_MINES],
    UnitId.SARAH_KERRIGAN_GHOST: [WeaponId.C10_CONCUSSION_RIFLE_SARAH_KERRIGAN],
    UnitId.ALAN_SCHEZAR_GOLIATH: [
        WeaponId.TWIN_AUTOCANNONS_ALAN_SCHEZAR,
        WeaponId.HELLFIRE_MISSILE_PACK_ALAN_SCHEZAR,
    ],
    UnitId.ALAN_SCHEZAR_TURRET: [WeaponId.TWIN_AUTOCANNONS_ALAN_SCHEZAR],
    UnitId.JIM_RAYNOR_MARINE: [WeaponId.GAUSS_RIFLE_JIM_RAYNORMARINE],
    UnitId.JIM_RAYNOR_VULTURE: [WeaponId.FRAGMENTATION_GRENADE_JIM_RAYNORVULTURE],
    UnitId.TOM_KAZANSKY_WRAITH: [
        WeaponId.BURST_LASERS_TOM_KAZANSKY,
        WeaponId.GEMINI_MISSILES_TOM_KAZANSKY,
    ],
    UnitId.EDMUND_DUKE_SIEGE_TANK: [WeaponId.ARCLITE_CANNON_EDMUND_DUKE],
    UnitId.EDMUND_DUKE_TURRET: [WeaponId.ARCLITE_CANNON_EDMUND_DUKE],
    UnitId.EDMUND_DUKE_SIEGE_MODE: [WeaponId.ARCLITE_SHOCK_CANNON_EDMUND_DUKE],
    UnitId.EDMUND_DUKE_TURRET_SIEGE_MODE: [WeaponId.ARCLITE_SHOCK_CANNON_EDMUND_DUKE],
    UnitId.HYPERION_BATTLECRUISER: [
        WeaponId.ATS_LASER_BATTERY_HYPERION,
        WeaponId.ATA_LASER_BATTERY_HYPERION,
    ],
    UnitId.NORAD_II_BATTLECRUISER: [
        WeaponId.ATS_LASER_BATTERY_NORAD_II_MENGSK_DUGALLE,
        WeaponId.ATA_LASER_BATTERY_NORAD_II_MENGSK_DUGALLE,
    ],
    UnitId.TERRAN_SIEGE_TANK_SIEGE_MODE: [WeaponId.ARCLITE_SHOCK_CANNON_NORMAL],
    UnitId.TANK_TURRET_SIEGE_MODE: [WeaponId.ARCLITE_SHOCK_CANNON_NORMAL],
    UnitId.FIREBAT: [WeaponId.FLAME_THROWER_NORMAL],
    UnitId.ZERG_ZERGLING: [WeaponId.CLAWS_NORMAL],
    UnitId.ZERG_HYDRALISK: [WeaponId.NEEDLE_SPINES_NORMAL],
    UnitId.ZERG_ULTRALISK: [WeaponId.KAISER_BLADES_NORMAL],
    UnitId.ZERG_BROODLING: [WeaponId.TOXIC_SPORES_BROODLING],
    UnitId.ZERG_DRONE: [WeaponId.SPINES],
    UnitId.ZERG_MUTALISK: [WeaponId.GLAVE_WURM_NORMAL],
    UnitId.ZERG_GUARDIAN: [WeaponId.ACID_SPORE_NORMAL],
    UnitId.ZERG_SCOURGE: [WeaponId.SUICIDE_SCOURGE],
    UnitId.TORRARSQUE_ULTRALISK: [WeaponId.KAISER_BLADES_TORRASQUE],
    UnitId.INFESTED_TERRAN: [WeaponId.SUICIDE_INFESTED_TERRAN],
    UnitId.INFESTED_KERRIGAN: [WeaponId.CLAWS_INFESTED_KERRIGAN],
    UnitId.HUNTER_KILLER_HYDRALISK: [WeaponId.NEEDLE_SPINES_HUNTER_KILLER],
    UnitId.DEVOURING_ONE_ZERGLING: [WeaponId.CLAWS_DEVOURING_ONE],
    UnitId.KUKULZA_MUTALISK: [WeaponId.GLAVE_WURM_KUKULZAMUTALISK],
    UnitId.KUKULZA_GUARDIAN: [WeaponId.ACID_SPORE_KUKULZAGUARDIAN],
    UnitId.TERRAN_VALKYRIE_FRIGATE: [WeaponId.HALO_ROCKETS],
    UnitId.PROTOSS_CORSAIR: [WeaponId.NEUTRON_FLARE],
    UnitId.PROTOSS_DARK_TEMPLAR_UNIT: [WeaponId.WARP_BLADES_NORMAL],
    UnitId.ZERG_DEVOURER: [WeaponId.CORROSIVE_ACID],
    UnitId.PROTOSS_PROBE: [WeaponId.PARTICLE_BEAM],
    UnitId.PROTOSS_ZEALOT: [WeaponId.PSI_BLADES_NORMAL],
    UnitId.PROTOSS_DRAGOON: [WeaponId.PHASE_DISRUPTOR_NORMAL],
    UnitId.PROTOSS_ARCHON: [WeaponId.PSIONIC_SHOCKWAVE_NORMAL],
    UnitId.PROTOSS_SCOUT: [
        WeaponId.DUAL_PHOTON_BLASTERS_NORMAL,
        WeaponId.ANTIMATTER_MISSILES_NORMAL,
    ],
    UnitId.PROTOSS_ARBITER: [WeaponId.PHASE_DISRUPTOR_CANNON_NORMAL],
    UnitId.PROTOSS_CARRIER: [WeaponId.PULSE_CANNON],
    UnitId.PROTOSS_INTERCEPTOR: [WeaponId.PULSE_CANNON],
    UnitId.DARK_TEMPLAR_HERO: [WeaponId.WARP_BLADES_DARK_TEMPLAR_HERO],
    UnitId.ZERATUL_DARK_TEMPLAR: [WeaponId.WARP_BLADES_ZERATUL],
    UnitId.TASSADAR_ZERATUL_ARCHON: [
        WeaponId.PSIONIC_SHOCKWAVE_TASSADAR_ZERATUL_ARCHON
    ],
    UnitId.FENIX_ZEALOT: [WeaponId.PSI_BLADES_FENIXZEALOT],
    UnitId.TASSADAR_TEMPLAR: [WeaponId.PSI_ASSAULT_TASSADAR_ALDARIS],
    UnitId.MOJO_SCOUT: [
        WeaponId.DUAL_PHOTON_BLASTERS_MOJO,
        WeaponId.ANTIMATTER_MISSILES_MOJO,
    ],
    UnitId.WARBRINGER_REAVER: [WeaponId.SCARAB],
    UnitId.GANTRITHOR_CARRIER: [WeaponId.PULSE_CANNON],
    UnitId.PROTOSS_REAVER: [WeaponId.SCARAB],
    UnitId.DANIMOTH_ARBITER: [WeaponId.PHASE_DISRUPTOR_CANNON_DANIMOTH],
    UnitId.ARTANIS_SCOUT: [
        WeaponId.DUAL_PHOTON_BLASTERS_ARTANIS,
        WeaponId.ANTIMATTER_MISSILES_ARTANIS,
    ],
    UnitId.RASZAGAL: [WeaponId.NEUTRON_FLARE],
    UnitId.SAMIR_DURAN_GHOST: [WeaponId.C10_CONCUSSION_RIFLE_SAMIR_DURAN],
    UnitId.ALEXEI_STUKOV_GHOST: [WeaponId.C10_CONCUSSION_RIFLE_ALEXEI_STUKOV],
    UnitId.GERARD_DUGALLE: [
        WeaponId.ATS_LASER_BATTERY_NORAD_II_MENGSK_DUGALLE,
        WeaponId.ATA_LASER_BATTERY_NORAD_II_MENGSK_DUGALLE,
    ],
    UnitId.ZERG_LURKER: [WeaponId.SUBTERRANEAN_SPINES],
    UnitId.INFESTED_DURAN: [WeaponId.C10_CONCUSSION_RIFLE_INFESTED_DURAN],
    UnitId.TERRAN_MISSILE_TURRET: [WeaponId.LONGBOLT_MISSILES],
    UnitId.ZERG_SPORE_COLONY: [WeaponId.SEEKER_SPORES],
    UnitId.ZERG_SUNKEN_COLONY: [WeaponId.SUBTERRANEAN_TENTACLE],
    UnitId.PROTOSS_PHOTON_CANNON: [
        WeaponId.STA_PHOTON_CANNON,
        WeaponId.STS_PHOTON_CANNON,
    ],
    UnitId.FLOOR_MISSILE_TRAP: [WeaponId.HELLFIRE_MISSILE_PACK_FLOOR_TRAP],
    UnitId.LEFT_WALL_MISSILE_TRAP: [WeaponId.HELLFIRE_MISSILE_PACK_WALL_TRAP],
    UnitId.FLOOR_GUN_TRAP: [WeaponId.TWIN_AUTOCANNONS_FLOOR_TRAP],
    UnitId.LEFT_WALL_FLAME_TRAP: [WeaponId.FLAME_THROWER_WALL_TRAP],
    UnitId.RIGHT_WALL_MISSILE_TRAP: [WeaponId.HELLFIRE_MISSILE_PACK_WALL_TRAP],
    UnitId.RIGHT_WALL_FLAME_TRAP: [WeaponId.FLAME_THROWER_WALL_TRAP],
}


def get_weapons_for_unit(unit: UnitId) -> list[WeaponId]:
    return _UNIT_TO_WEAPON.get(unit, list())