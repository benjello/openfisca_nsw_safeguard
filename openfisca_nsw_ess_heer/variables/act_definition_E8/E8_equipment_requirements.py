# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw_base.entities import *


class new_equipment_is_window_sealing_product(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Asks whether the new product is a retail window sealing product.'


class new_equipment_is_weather_stripping_product(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Asks whether the new product is a weather stripping product.'


class E8_new_equipment_is_eligible_product(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Asks whether the product that is applied is a retail door bottom' \
            ' sealing product or door perimeter weather stripping product,' \
            ' as prescribed by Equipment Requirement 1.'

    def formula(buildings, period, parameters):
        window_sealing_product = buildings('new_equipment_is_window_sealing_product', period)
        window_weather_sealing_product = buildings('new_equipment_is_weather_stripping_product', period)
        return window_sealing_product + window_weather_sealing_product


class E8_new_equipment_is_fit_for_purpose(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Asks whether the product is fit for purpose, as prescribed by' \
            ' Equipment Requirement 2.'  # IPART to define what this means


class E8_sealing_surface_material_is_eligible(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'The product’s sealing surface must be made of a durable' \
            ' compressible material such as foam, polypropylene pile,' \
            ' flexible plastic, rubber compressible strip, fibrous' \
            ' seal or similar. As prescribed by Equipment Requirement 3.'


class new_equipment_does_not_impair_window_operation(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Asks whether the product does not impair the operation of the' \
            ' relevant window.'  # IPART to define what this means


class E8_warranty_length(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'Asks for the warranty length of the showerhead, in years.'


class E8_minimum_warranty_length(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Asks whether the sealing product has a minimum warranty length of' \
            ' 2 years, as required by Equipment Requirement 3.'

    def formula(buildings, period, parameters):
        warranty_length = buildings('E8_warranty_length', period)
        return warranty_length >= 2
