from openfisca_nsw_safeguard.regulation_reference.regulation_reference import Regulation, PartType as PT


ESS_2021 = Regulation(
    "ESS 2021", "Energy Savings Scheme (Amendment No. 1) Rule 2021", "01 May 2021")

# Identify Common Variables---------------
generic_ESS = ESS_2021.add_part("XX", PT.EQUIPMENT, "Generic")
generic_ESS_GA = generic_ESS.add_part("GA", PT.EQUIPMENT, "General Appliances")
generic_ESS_AC = generic_ESS.add_part("AC", PT.EQUIPMENT, "Air Conditioner")


#  Variables Specific to Clauses ---------------

clause_8 = ESS_2021.add_part("8", PT.CLAUSE, "Metered Baseline Method")
clause_8.add_parts([("8.1", PT.CLAUSE, None),
                    ("8.2", PT.CLAUSE, None),
                    ("8.3", PT.CLAUSE, None),
                    ("8.3.A", PT.CLAUSE, None),
                    ("8.4", PT.CLAUSE, None),
                    ("8.4.A", PT.CLAUSE, "Additional Requirements for Lighting Upgrades"),
                    ("8.4.B", PT.CLAUSE,
                     "Acceptable End-User Equipment for Lighting Upgrades"),
                    ("8.5", PT.ACTIVITY, "Baseline Per Unit of Output"),
                    ("8.6", PT.ACTIVITY, "Baseline Unaffected by Output"),
                    ("8.7", PT.ACTIVITY, "Normalised Baseline"),
                    ("8.8", PT.ACTIVITY, "NABERS Baseline"),
                    ("8.9", PT.ACTIVITY, "Aggregated Metered Baseline")])

clause_9 = ESS_2021.add_part("9", PT.CLAUSE, "Deemed Energy Savings Method")
clause_9.add_parts([("9.1", PT.CLAUSE, None),
                    ("9.2", PT.CLAUSE, None),
                    ("9.2.A", PT.CLAUSE, "Acceptable End-User Equipment"),
                    ("9.3", PT.CLAUSE, "Sale of New Appliances"),
                    ("9.4", PT.CLAUSE, "Commercial Lighting"),
                    ("9.4A", PT.CLAUSE, "Public Lighting"),
                    ("9.5", PT.CLAUSE, "High Efficiency Motor"),
                    ("9.6", PT.CLAUSE, "Power Factor Correction"),
                    ("9.7", PT.CLAUSE, "Removal of Old Appliances"),
                    ("9.8", PT.CLAUSE, "Home Energy Efficiency Retrofits"),
                    ("9.9", PT.CLAUSE,
                     "Installation of High Efficiency Appliances for Business"),
                    ])

schedule_B = ESS_2021.add_part(
    "B", PT.SCHEDULE, "Activity Definitions for the Sale of New Appliances")
schedule_B.add_parts([
                     ("B1", PT.ACTIVITY, "Sell a High Efficiency Clothes Washing Machine"),
                     ("B2", PT.ACTIVITY, "Sell a High Efficiency Clothes Dryer"),
                     ("B3", PT.ACTIVITY, "Sell a High Efficiency Clothes Dishwasher"),
                     ("B4", PT.ACTIVITY, "Sell a High Efficiency 1 Door Refrigerator"),
                     ("B5", PT.ACTIVITY, "Sell a High Efficiency 2 or More Door Refrigerator"),
                     ("B6", PT.ACTIVITY, "Sell a High Efficiency Chest Freezer or Upright Freezer"),
                     ("B7", PT.ACTIVITY, "Sell a High Efficiency Television")
                     ])

schedule_C = ESS_2021.add_part(
    "C", PT.SCHEDULE, "Activity Definitions for Removal of Old Appliances (clause 9.7)")
schedule_C.add_parts([
                     ("C1", PT.ACTIVITY, "Remove a Spare Refrigerator or Freezer"),
                     ("C2", PT.ACTIVITY, "Remove a Primary Refrigerator or Freezer")
                     ])


schedule_D = ESS_2021.add_part(
    "D", PT.SCHEDULE, "Activity Definitions for General Activities for Home Energy Efficiency Retrofits")
schedule_D.add_parts([
                     ("D1", PT.ACTIVITY, "Replace an External Single Glazed Window or Door with a Thermally Efficient Window or Door"),
                     ("D2", PT.ACTIVITY, "Modify an External Window or Glazed Door by Installing Secondary Glazing"),
                     ("D3", PT.ACTIVITY, None),
                     ("D4", PT.ACTIVITY, None),
                     ("D5", PT.ACTIVITY, "Replace an Existing Pool Pump with a High Efficiency Pool Pump"),
                     ("D6", PT.ACTIVITY, "Install Ceiling Insulation in an Uninsulated Ceiling Space"),
                     ("D7", PT.ACTIVITY, "Install Ceiling Insulation in an Under-insulated Ceiling Space"),
                     ("D8", PT.ACTIVITY, "Install Under-Floor Insulation"),
                     ("D9", PT.ACTIVITY, "Install Wall Insulation"),
                     ("D10", PT.ACTIVITY, None),
                     ("D11", PT.ACTIVITY, 
                     "Replace an Existing Gas Fired Water Heater with a High Efficiency Gas FIred Water Heater"),
                     ("D12", PT.ACTIVITY, 
                     "Install a High Efficiency Gas Space Heater, or Replace an Existing Gas Space Heater with a High Efficiency Gas Space Heater"),
                     ("D13", PT.ACTIVITY, "Install a Natural Roof Space Ventilator"),
                     ("D14", PT.ACTIVITY, 
                     "Install a Fan-Forced Roof Space Ventilator, PV-Powered Fan-Forced Roof Space Ventilator, or an Occupied Space Ventilator"),
                     ("D15", PT.ACTIVITY, "Replace an Exhaust Fan with a Self-Sealing Exhaust Fan"),
                     ("D16", PT.ACTIVITY, 
                     "Install a New High Efficiency Air Conditioner or Replace an Existing Air Conditioner with a High Efficiency Air Conditioner"),
                     ("D17", PT.ACTIVITY, 
                     "Replace an Existing Electric Water Heater with an Air Source Heat Pump Water Heater"),
                     ("D18", PT.ACTIVITY, 
                     "Replace an Existing Electric Water Heater with a Solar Electric Boosted Water Heater"),
                     ("D19", PT.ACTIVITY, 
                     "Replace an Existing Gas Water Heater with an AIr Source Heat Pump Water Heater"),
                     ("D20", PT.ACTIVITY, "Replace an Existing Gas Water Heater with a Solar Electric Boosted Water Heater"),
                     ("D21", PT.ACTIVITY, "Replace an Existing Gas Water Heater with a Solar Gas Boosted Water Heater"),
                     ])

schedule_E = ESS_2021.add_part(
    "E", PT.SCHEDULE, "Activity Definitions for Low Cost Activities for Home Energy Efficiency Retrofits")
schedule_E.add_parts([
                     ("E1", PT.ACTIVITY, "Replace Halogen Downlight with LED Luminaire and/or Lamp"),
                     ("E2", PT.ACTIVITY, "Replace a Linear Halogen Floodlight with a High Efficiency Lamp"),
                     ("E3", PT.ACTIVITY, 
                     "Replace Parabolic Aluminised Reflector (PAR) Lamp with Efficient Luminaire and/or Lamp"),
                     ("E4", PT.ACTIVITY, "Replace a T8 or T12 Luminaire with a T5 Luminaire"),
                     ("E5", PT.ACTIVITY, "Replace a T8 or T12 Luminaire with a LED Luminaire"),
                     ("E6", PT.ACTIVITY, "Replace an Existing Showerhead with an Ultra Low Flow Showerhead"),
                     ("E7", PT.ACTIVITY, "Modify an External Door with Draught-Proofing"),
                     ("E8", PT.ACTIVITY, "Modify an External Window with Draught-Proofing"),
                     ("E9", PT.ACTIVITY, "Modify a Fireplace Chimney by Sealing with a Damper"),
                     ("E10", PT.ACTIVITY, "Install an External Blind to a Window or Door"),
                     ("E11", PT.ACTIVITY, 
                     "Replace an Edison Screw or Bayonet Lamp with an LED Lamp for General Lighting Purposes"),
                     ("E12", PT.ACTIVITY, "Install an External Blind to a Window or Door"),
                     ("E13", PT.ACTIVITY, "Replace a T5 Luminaire with an LED Luminaire"),
                     ])



schedule_F = ESS_2021.add_part(
    "F", PT.SCHEDULE, "Activity Definitions for Installation of High Efficiency Appliances for Businesses (clause 9.9)")
schedule_F.add_parts([
                     ("F1.1", PT.ACTIVITY, "Install A New High Efficiency Refrigerated Cabinet"),
                     ("F1.2", PT.ACTIVITY, "Replace an Existing Refrigerated Display Cabinet"),
                     ("F2", PT.ACTIVITY, "Install A New High Efficiency Liquid Chilling Package"),
                     ("F3", PT.ACTIVITY, "Install A New High Efficiency Close Control Air Conditioner"),
                     ("F4", PT.ACTIVITY, "Install A New High Efficiency Air Conditioner"),
                     ("F5", PT.ACTIVITY, "Install An Electronically Commutated Motor to Power a Fan in an Installed Refrigerated Cabinet, Freezer or Cool Room"),
                     ("F6", PT.ACTIVITY, "Install an Electronically Commutated Motor to Power a Ventilation Fan"),
                     ("F7", PT.ACTIVITY, "Install a New High Efficiency Motor"),
                     ("F8", PT.ACTIVITY, 
                     "Replace Existing Gas Fired Steam Boiler with a New High Efficiency Gas Fired Steam Boiler"),
                     ("F9", PT.ACTIVITY, 
                     "Replace Existing Gas Fired Hot Water Boiler or Gas Fired Water Heater" \
                     "with a New High Efficiency Gas Fired Hot Water Boiler or a New Gas Fired Water Heater"),
                     ("F10", PT.ACTIVITY, 
                     "Install an Oxygen Trim System on a Gas Fired Steam Boiler, Hot Water Boiler or Water Heater"),
                     ("F11", PT.ACTIVITY, 
                     "Replace Burner on a Gas Fired Steam Boiler,. Hot Water Boiler or Water Heater"),
                     ("F12", PT.ACTIVITY, 
                     "Install an Economiser on a Gas Fired Steam Boiler, Hot Water Boiler or Water Heater"),
                     ("F13", PT.ACTIVITY, 
                     "Install a Sensor Based Blowdown Control on a Gas Fired Steam Boiler"),
                     ("F14", PT.ACTIVITY, 
                     "Install a Blowdown Flash Steam Heat Recovery System on Gas Fired Steam Boiler"),
                     ("F15", PT.ACTIVITY, 
                     "Install a Residual Blowdown Heat Exchanger on Gas Fired Steam Boiler"),
                     ("F16", PT.ACTIVITY, 
                     "Replace One or More Existing Hot Water Boilers or Water Heaters with One or More Air Source Heat Pump Water Heater Systems"),
                     ("F17", PT.ACTIVITY, 
                     "Install One or More Air Source Heat Pump Water Heater Systems")
                     ])
