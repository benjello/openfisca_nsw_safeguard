from openfisca_core.variables import Variable
from openfisca_core.periods import ETERNITY, YEAR
from openfisca_core.indexed_enums import Enum
from openfisca_nsw_base.entities import Building

from openfisca_nsw_safeguard.regulation_reference import ESS_2021

import numpy as np

class ESS__NABERS_forward_electricity_savings(Variable):
    value_type = float
    default_value = 0
    entity = Building
    definition_period = ETERNITY
    label = 'Forward Electricity Savings (in MWh)'
    metadata={
        "variable-type": "inter-interesting", # need to check this metadata
        "alias":"Annual Electricity Savings (MWh)",
        # "major-cat":"Energy Savings Scheme",
        # "monor-cat":'Metered Baseline Method - NABERS baseline'
        "regulation_reference": ESS_2021["8","8.8"]
        }


class ESS__NABERS_electricity_savings(Variable):
    value_type = float
    default_value = 0
    entity = Building
    definition_period = ETERNITY
    label = 'Electricity Savings (in MWh) created from the NABERS method,' \
            ' through either annual creation or forward creation.'
    metadata={
        "variable-type": "inter-interesting", # need to check this metadata
        "alias":"NABERS Electricity Savings (MWh)",
        # "major-cat":"Energy Savings Scheme",
        # "monor-cat":'Metered Baseline Method - NABERS baseline'
        "regulation_reference": ESS_2021["8","8.8"]
        }

    def formula(buildings, period, parameters):
        type_of_creation = buildings('ESS__NABERS_type_of_creation', period)
        TypeOfCreation = (type_of_creation.possible_values)
        is_annually_created = (type_of_creation == TypeOfCreation.annual_creation)
        is_forward_created = (type_of_creation == TypeOfCreation.forward_creation)
        annual_elec_savings = buildings('ESS__NABERS_annual_electricity_savings', period)
        forward_created_elec_savings = buildings('ESS__NABERS_forward_electricity_savings', period)
        return np.select([is_annually_created,
                          is_forward_created],
                         [annual_elec_savings,
                          forward_created_elec_savings])
