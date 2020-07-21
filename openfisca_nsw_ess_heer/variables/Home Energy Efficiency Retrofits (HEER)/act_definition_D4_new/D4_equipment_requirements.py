# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class D4_new_new_product_is_air_conditioner(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the new product an air conditioner, as defined by AS/NZS 3823.2?'
    # what does it mean to be an air con in AS3823.2?


class D4_new_new_product_is_registered_under_GEMS(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the new product registered under GEMS?'


class D4_new_complies_with_GEMS_2019_AC(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the product comply with the Greenhouse and Energy Minimum' \
            ' Standards (Air Conditioners up to 65kW) Determination 2019?'
    # what does complying with this Determination mean?


class D4_new_complies_with_GEMS_2013_AC(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the product comply with the Greenhouse and Energy Minimum' \
            ' Standards (Air Conditioners and Heat Pumps) Determination 2013?'
    # what does complying with this Determination mean?


class D4_new_warranty_length(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What is the warranty length of the new air conditioner, in years?'


class D4_new_minimum_warranty_length(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Asks whether the air conditioner has a minimum warranty length of' \
            ' 5 years, as required by Equipment Requirement 3.'

    def formula(buildings, period, parameters):
        minimum_warranty_length = 5
        warranty_length = buildings('D4_new_warranty_length', period)
        return warranty_length >= minimum_warranty_length


class D4_new_meets_all_equipment_requirements(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the activity meet all of the equipment requirements defined' \
            ' in Activity Definition D4?'

    def formula(buildings, period, parameters):
        is_air_con = buildings('D4_new_new_product_is_air_conditioner', period)
        registered_in_GEMS = buildings('D4_new_new_product_is_registered_under_GEMS', period)
        complies_with_GEMS_2013 = buildings('D4_new_complies_with_GEMS_2013_AC', period)
        complies_with_GEMS_2019 = buildings('D4_new_complies_with_GEMS_2019_AC', period)
        minimum_warranty_length = buildings('D4_new_minimum_warranty_length', period)
        return (is_air_con * registered_in_GEMS * (complies_with_GEMS_2013 + complies_with_GEMS_2019)
        * minimum_warranty_length)
