# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class F1_1_is_integral_RDC(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the End User Equipment an integral Refrigerated Display Cabinet' \
            ' as defined in the Greenhouse and Energy Minimum Standards' \
            ' (Refrigerated Cabinets) Determination 2019?'


class F1_1_is_registered_in_GEMS_2012(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the End User Equipment a registered product based on Greenhouse' \
            ' and Energy Minimum Standards (Refrigerated Display Cabinets)' \
            ' Determination 2012?'


class F1_1_is_registered_in_GEMS_2019(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the End User Equipment a registered product based on Greenhouse' \
            ' and Energy Minimum Standards (Refrigerated Cabinets) Determination 2019?'


class F1_1_annual_energy_consumption_below_baseline_EEI(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the equipment has an annual energy consumption below the EEI' \
            ' specified in Table F1.1?'

    def formula(buildings, period, parameters):
        annual_energy_consumption = buildings('F1_1_annual_energy_consumption', period)
        product_class = buildings('F1_product_class', period)
        F1ProductClass = product_class.possible_values
        EEI = parameters(period).HEAB.F1.F1_1_baseline_EEIs.EEI[product_class]
        return annual_energy_consumption < EEI


class F1_1_annual_energy_consumption(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'What is the annual energy consumption of the RDC to be used in' \
            ' Activity Definition F1.1?'
    # what unit? not specified. think kWh?


class F1_1_meets_all_equipment_requirements(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the equipment meet all of the Equipment Requirements defined' \
            ' in Activity Definition F1.1?'

    def formula(buildings, period, parameters):
        is_integral_RDC = buildings('F1_1_is_integral_RDC', period)
        registered_in_GEMS_2012 = buildings('F1_1_is_registered_in_GEMS_2012', period)
        registered_in_GEMS_2019 = buildings('F1_1_is_registered_in_GEMS_2019', period)
        below_baseline_EEI = buildings('F1_1_annual_energy_consumption_below_baseline_EEI')
        return (is_integral_RDC * (registered_in_GEMS_2012 + registered_in_GEMS_2019) * below_baseline_EEI)
