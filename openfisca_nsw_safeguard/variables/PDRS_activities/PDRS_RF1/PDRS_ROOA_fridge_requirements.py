from openfisca_core.variables import Variable
from openfisca_core.periods import ETERNITY
from openfisca_core.indexed_enums import Enum
from openfisca_nsw_base.entities import Building

from openfisca_nsw_safeguard.regulation_reference import PDRS_2022


class PDRS_ROOA_meets_implementation_requirements(Variable):
    value_type = bool
    entity = Building
    default_value = True
    definition_period = ETERNITY
    label = 'Does the implementation meet all of the Implementation' \
            ' Requirements defined in Removal of Old Appliance (fridge)?'
    metadata = {
        'alias': "ROOA meets implementation requirements",
        "regulation_reference": PDRS_2022["ROOA", "fridge", "implementation"]
    }


class PDRS_ROOA_meets_equipment_requirements(Variable):
    value_type = bool
    entity = Building
    default_value = False
    definition_period = ETERNITY
    label = 'Does the implementation meet all of the Eligibility' \
            ' Requirements defined in Removal of Old Appliance (fridge)?'
    metadata = {
        'alias': "ROOA meets eligibility requirements",
        "regulation_reference": PDRS_2022["ROOA", "fridge", "eligibility"]
    }

    def formula(buildings, period, parameters):
        is_residential = buildings(
            'ESS_PDRS_is_residential', period)
        is_fridge = buildings('Fridge_is_classified_as_refrigerator', period)
        is_more_than_200L = buildings('Fridge_capacity_more_than_200L', period)
        is_working = buildings(
            'Fridge_in_working_order', period)
        another_primary_fridge = buildings(
            'another_fridge_provides_primary_refrigeration', period)
        one_fewer_fridge_after_activity = buildings(
            'Fridge_total_number_one_less', period)

        return (
                is_residential *
                is_fridge *
                is_more_than_200L *
                is_working *
                another_primary_fridge *
                one_fewer_fridge_after_activity
                )


class PDRS_ROOA_meets_eligibility_requirements(Variable):
    value_type = bool
    entity = Building
    default_value = True
    definition_period = ETERNITY
    label = 'Does the implementation meet all of the Equipment' \
            ' Requirements defined in Removal of Old Appliance (fridge)?'
    metadata = {
        'alias': "ROOA meets equipment requirements",
        "regulation_reference": PDRS_2022["ROOA", "fridge", "equipment"]
    }

class PDRS_ROOA_meets_all_requirements(Variable):
    value_type = bool
    entity = Building
    default_value = False
    definition_period = ETERNITY
    label = 'Does the implementation meet all of the' \
            ' Requirements defined in Removal of Old Appliance (fridge)?'
    metadata = {
        'alias': "ROOA meets all requirements",
        "regulation_reference": PDRS_2022["ROOA", "fridge"]
    }

    def formula(buildings, period, parameters):
        implementation = buildings(
            'PDRS_ROOA_meets_implementation_requirements', period)
        eligibility = buildings(
            'PDRS_ROOA_meets_eligibility_requirements', period)
        equipment = buildings('PDRS_ROOA_meets_equipment_requirements', period)
        return implementation * eligibility * equipment
