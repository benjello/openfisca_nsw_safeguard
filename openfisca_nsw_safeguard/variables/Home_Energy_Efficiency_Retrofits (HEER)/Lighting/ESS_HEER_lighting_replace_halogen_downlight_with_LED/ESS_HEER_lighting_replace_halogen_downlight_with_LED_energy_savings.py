from openfisca_core.variables import Variable
from openfisca_core.periods import ETERNITY
from openfisca_core.indexed_enums import Enum
from openfisca_nsw_base.entities import Building

import numpy as np


class ESS_HEER_lighting_replace_halogen_downlight_with_LED_electricity_savings(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'Returns the electricity savings for activity definition E1.'

    def formula(buildings, period, parameters):
        site_type = buildings('ESS_site_type', period)
        ESS_SiteType = site_type.possible_values

        is_residential = (site_type == ESS_SiteType.residential)
        is_small_business = (site_type == ESS_SiteType.small_business)

        electricity_savings = np.select(
                [is_residential,
                is_small_business,
                np.logical_not(is_residential + is_small_business)
                ],
                [
                        buildings('ESS_HEER_lighting_replace_halogen_downlight_with_LED_residential_savings_factor', period),
                        buildings('ESS_HEER_lighting_replace_halogen_downlight_with_LED_small_business_savings_factor', period),
                        0
                ]
                )

        return electricity_savings


class ESS_HEER_lighting_replace_halogen_downlight_with_LED_residential_savings_factor(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'Returns the relevant savings factor for the existing and new lamp' \
            ' for residential replacements.'

    def formula(buildings, period, parameters):
        existing_lamp_type = buildings('ESS_HEER_lighting_existing_lamp_type', period)
        new_lamp_type = buildings('ESS_HEER_lighting_new_lamp_type', period)

        from openfisca_nsw_safeguard.variables.ESS_lighting_common_variables import LightingEquipmentClass

        # ExistingLighting_EquipmentClass = existing_lamp_type.possible_values
        # NewLighting_EquipmentClass = new_lamp_type.possible_values

        is_eligible_existing_lamp = (
                (existing_lamp_type == LightingEquipmentClass.tungsten_halogen_ELV) +
                (existing_lamp_type == LightingEquipmentClass.infrared_coated_ELV) +
                (existing_lamp_type == LightingEquipmentClass.tungsten_halogen_240V)
                )

        existing_lamp_type = np.where(is_eligible_existing_lamp,
                existing_lamp_type,
                (EquipmentClass.is_not_eligible)
                )

        # above code a. checks if the existing lamp type is one of the eligible lamp classes (as defined in the equipment requirements)
        # and b. if it's not eligible, assigns the Enum to a not_eligible product class
        # Table E1.1 now has an appended is_not_eligible index section, with all values set to 0
        # this is kind of hacky but means a. you can use the single list of lighting types and
        # b. you don't have to write out every table with every single class - you can just write what's explicitly written
        # in the rules

        is_eligible_new_lamp = (
                (new_lamp_type == LightingEquipmentClass.LED_lamp_only_ELV) +
                (new_lamp_type == LightingEquipmentClass.LED_lamp_and_driver) +
                (new_lamp_type == LightingEquipmentClass.LED_luminaire_recessed) +
                (new_lamp_type == LightingEquipmentClass.LED_lamp_only_240V_self_ballasted)
        )

        new_lamp_type = np.where(is_eligible_new_lamp,
                new_lamp_type,
                (EquipmentClass.is_not_eligible)
                )

        # as above but for new product class


        new_lamp_circuit_power = buildings('ESS_HEER_lighting_new_lamp_circuit_power', period)
        lamp_rating_power = np.select(
                [
                        new_lamp_circuit_power <= 5,
                        ((new_lamp_circuit_power > 5) * (new_lamp_circuit_power <= 10)),
                        ((new_lamp_circuit_power > 10) * (new_lamp_circuit_power <= 15)),
                        new_lamp_circuit_power > 15],
                [
                "under_or_equal_to_five_watts",
                "under_or_equal_to_ten_watts",
                "under_or_equal_to_fifteen_watts",
                "over_fifteen_watts"
                ]
                )

        residential_building_savings_factor = (
                parameters(period).ESS.HEER.table_E1_1.residential_savings_factor
                [existing_lamp_type]
                [new_lamp_type]
                [lamp_rating_power]
                )
        return residential_building_savings_factor


class ESS_HEER_lighting_replace_halogen_downlight_with_LED_small_business_savings_factor(Variable):
    value_type = float
    entity = Building
    definition_period = ETERNITY
    label = 'Returns the relevant savings factor for the existing and new lamp' \
            ' for residential replacements.'

    def formula(buildings, period, parameters):
        existing_lamp_type = buildings('ESS_HEER_lighting_existing_lamp_type', period)
        new_lamp_type = buildings('ESS_HEER_lighting_new_lamp_type', period)
        EquipmentClass = existing_lamp_type.possible_values
        NewLighting_EquipmentClass = new_lamp_type.possible_values

        is_eligible_existing_lamp = (
                (existing_lamp_type == EquipmentClass.tungsten_halogen_ELV) +
                (existing_lamp_type == EquipmentClass.infrared_coated_ELV) +
                (existing_lamp_type == EquipmentClass.tungsten_halogen_240V)
                                )

        existing_lamp_type = np.where(is_eligible_existing_lamp,
                existing_lamp_type,
                (EquipmentClass.is_not_eligible)
                )

        # above code a. checks if the existing lamp type is one of the eligible lamp classes (as defined in the equipment requirements)
        # and b. if it's not eligible, assigns the Enum to a not_eligible product class
        # Table E1.1 now has an appended is_not_eligible index section, with all values set to 0
        # this is kind of hacky but means a. you can use the single list of lighting types and
        # b. you don't have to write out every table with every single class - you can just write what's explicitly written
        # in the rules

        is_eligible_new_lamp = (
                (new_lamp_type == NewLighting_EquipmentClass.LED_lamp_only_ELV) +
                (new_lamp_type == NewLighting_EquipmentClass.LED_lamp_and_driver) +
                (new_lamp_type == NewLighting_EquipmentClass.LED_luminaire_recessed) +
                (new_lamp_type == NewLighting_EquipmentClass.LED_lamp_only_240V_self_ballasted)
        )

        new_lamp_type = np.where(is_eligible_new_lamp,
                new_lamp_type,
                (EquipmentClass.is_not_eligible)
                )

        # as above but for new product class


        new_lamp_circuit_power = buildings('ESS_HEER_lighting_new_lamp_circuit_power', period)
        lamp_rating_power = np.select(
                [
                        new_lamp_circuit_power <= 5,
                        ((new_lamp_circuit_power > 5) * (new_lamp_circuit_power <= 10)),
                        ((new_lamp_circuit_power > 10) * (new_lamp_circuit_power <= 15)),
                        new_lamp_circuit_power > 15],
                [
                "under_or_equal_to_five_watts",
                "under_or_equal_to_ten_watts",
                "under_or_equal_to_fifteen_watts",
                "over_fifteen_watts"
                ]
                )

        small_business_building_savings_factor = (parameters(period).
        ESS.HEER.table_E1_2.small_business_savings_factor
        [existing_lamp_type][new_lamp_type][lamp_rating_power])
        return small_business_building_savings_factor
