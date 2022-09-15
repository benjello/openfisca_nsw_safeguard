import numpy as np
from openfisca_core.variables import Variable
from openfisca_core.periods import ETERNITY
from openfisca_core.indexed_enums import Enum
from openfisca_nsw_base.entities import Building

from openfisca_nsw_safeguard.regulation_reference import PDRS_2022

# detailed in PDRS activity XX

class PDRS_HVAC_2_replace_meets_eligibility_requirements(Variable):
    value_type = bool
    entity = Building
    default_value = False
    definition_period = ETERNITY
    label = 'Does the implementation meet all of the Eligibility' \
            ' Requirements defined in installing a high efficiency air conditioner for Business?'
    metadata = {
        'alias': "HEAB AC replace meets eligibility requirements",
        "regulation_reference": PDRS_2022["HEAB", "AC_replace", "eligibility"],
        'display_question':"Is the activity the replacement of an existing air conditioner?"
    }

    def formula(buildings, period, parameters):
        is_commercial = buildings(
            'Appliance_located_in_commercial_building', period)
        no_existing_AC = buildings('No_Existing_AC', period)
        # Need to add an if/else statement here: if Commercial is false, and class2 is true then eligibility is met
        # Have added class2 into PDRS_HVAC2_replace_requirements yaml test
        is_class2 = buildings(
            'is_installed_centralised_system_common_area_BCA_Class2_building', period)
       
        return is_commercial * np.logical_not(no_existing_AC) * is_class2


class PDRS_HVAC_2_replace_meets_equipment_requirements(Variable):
    value_type = bool
    entity = Building
    default_value = False
    definition_period = ETERNITY
    label = 'Does the equipment meet all of the Equipment' \
            ' Requirements defined in installing a high efficiency air conditioner for Business?'
    metadata = {
        'alias': "HEAB AC replace meets equipment requirements",
        "regulation_reference": PDRS_2022["HEAB", "AC_replace", "equipment"]
    }

    def formula(buildings, period, parameters):
        is_in_GEM = buildings(
            'Appliance_is_registered_in_GEMS', period)
        exceeds_benchmark_TCSPF_or_AEER = buildings(
            'PDRS_HVAC_2_TCSPF_or_AEER_exceeds_benchmark', period)
        return is_in_GEM * exceeds_benchmark_TCSPF_or_AEER


class PDRS_HVAC_2_replace_meets_implementation_requirements(Variable):
    """ Equipment_is_removed is found in appliances_implementation_requirements
    """
    value_type = bool
    entity = Building
    default_value = False
    definition_period = ETERNITY
    label = 'Does the implementation meet all of the Implementation' \
            ' Requirements defined in installing a high efficiency air conditioner for Business?'
    metadata = {
        'alias': "HEAB AC replace meets implementation requirements",
        "regulation_reference": PDRS_2022["HEAB", "AC_replace", "implementation"]
    }

    def formula(buildings, period, parameters):
        is_installed = buildings(
            'Equipment_is_installed', period)
        is_removed = buildings("Equipment_is_removed", period)
        performed_by_qualified_person = buildings(
            'implementation_is_performed_by_qualified_person', period)

        return is_installed * is_removed * performed_by_qualified_person


class PDRS_HVAC_2_replace_meets_all_requirements(Variable):
    value_type = bool
    entity = Building
    default_value = False
    definition_period = ETERNITY
    label = 'Does the implementation meet all of the' \
            ' Requirements defined in installing a high efficiency air conditioner for Business?'
    metadata = {
        'alias': "HEAB AC replace meets all requirements",
    }

    def formula(buildings, period, parameters):
        eligibility = buildings(
            'PDRS_HVAC_2_replace_meets_eligibility_requirements', period)
        equipment = buildings(
            'PDRS_HVAC_2_replace_meets_equipment_requirements', period)
        implementation = buildings(
            'PDRS_HVAC_2_replace_meets_implementation_requirements', period)

        return implementation * eligibility * equipment
