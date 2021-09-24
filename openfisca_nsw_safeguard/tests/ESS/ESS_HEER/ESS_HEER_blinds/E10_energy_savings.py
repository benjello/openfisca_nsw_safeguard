# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class E10_electricity_savings_factor(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'Returns the relevant savings factor for the existing and new lamp' \
            ' for residential replacements.'

    def formula(buildings, period, parameters):
        type_of_building = buildings('building_type', period)
        BuildingType = type_of_building.possible_values  # imports functionality of building type enum from user_inputs
        building_type = select([type_of_building == BuildingType.residential_building,
                                type_of_building == BuildingType.small_business_site],
                               ["residential",
                                'small_business'])
        climate_zone = buildings('BCA_Climate_Zone', period)
        BCAClimateZone = climate_zone.possible_values  # imports functionality of climate zone enum from user_inputs
        activity_climate_zone = select([climate_zone == BCAClimateZone.BCA_Climate_Zones_2_and_3,
                                        climate_zone == BCAClimateZone.BCA_Climate_Zone_4,
                                        climate_zone == BCAClimateZone.BCA_Climate_Zone_5,
                                        climate_zone == BCAClimateZone.BCA_Climate_Zone_6,
                                        climate_zone == BCAClimateZone.BCA_Climate_Zones_7_and_8],
                                       ["climate_zones_2_and_3",
                                        "climate_zone_4",
                                        "climate_zone_5",
                                        "climate_zone_6",
                                        "climate_zones_7_and_8"])
        electricity_savings_factor = parameters(period).table_E10_1.electricity_savings_factor[building_type][activity_climate_zone]
        return electricity_savings_factor
