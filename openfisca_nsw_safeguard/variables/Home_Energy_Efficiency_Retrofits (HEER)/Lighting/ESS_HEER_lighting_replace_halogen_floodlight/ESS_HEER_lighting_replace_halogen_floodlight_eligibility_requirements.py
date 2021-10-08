from openfisca_core.variables import Variable
from openfisca_core.periods import ETERNITY
from openfisca_core.indexed_enums import Enum
from openfisca_nsw_base.entities import Building


class ESS_HEER_lighting_replace_halogen_floodlight_existing_lamp_is_linear_halogen_floodlight(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Asks whether the existing lamp is a linear halogen floodlight, as' \
            ' required in Eligiblity Requirement 1 in Activity Definition' \
            ' E2, and defined in Table A9.1.'  # insert definition requirements

    def formula(buildings, period, parameters):
        existing_lamp_type = buildings('ESS_HEER_lighting_existing_lamp_type', period)
        EquipmentClassStatus = existing_lamp_type.possible_values  # imports functionality of Table A9.1 and Table A9.3 to define existing lamp type
        is_tungsten_halogen_240V = (existing_lamp_type == EquipmentClassStatus.linear_halogen_floodlight)
        return is_tungsten_halogen_240V


class ESS_HEER_lighting_replace_halogen_floodlight_existing_lamp_rating_is_more_than_100W(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Asks whether the existing lamp rating is more than 100W.'  # insert definition requirements

    def formula(buildings, period, parameters):
        existing_lamp_rating = buildings('ESS_HEER_existing_lamp_rating', period)
        condition_lamp_rating = (existing_lamp_rating > 100)
        return condition_lamp_rating


class ESS_HEER_lighting_replace_halogen_floodlight_existing_lamp_is_in_working_order(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Asks whether the existing lamp and luminaire is in working order' \
            ' as required in Eligibility Requirement 3 in Activity Definition' \
            ' E2.'  # insert definition requirements


class ESS_HEER_lighting_replace_halogen_floodlight_eligibility_requirements(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'asks whether all of the eligiblity requirements for E2 have been' \
            ' successfully met.'

    def formula(buildings, period, parameters):
        is_linear_halogen_floodlight = buildings(
        'ESS_HEER_lighting_replace_halogen_floodlight_existing_lamp_is_linear_halogen_floodlight', period)
        existing_lamp_more_than_100W = buildings(
        'ESS_HEER_lighting_replace_halogen_floodlight_existing_lamp_rating_is_more_than_100W', period)
        existing_lamp_in_working_order = buildings(
        'ESS_HEER_lighting_replace_halogen_floodlight_existing_lamp_is_in_working_order', period)
        return is_linear_halogen_floodlight * existing_lamp_more_than_100W * existing_lamp_in_working_order
