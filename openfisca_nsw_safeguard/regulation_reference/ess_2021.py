from openfisca_nsw_safeguard.regulation_reference.regulation_reference import Regulation, PartType as PT


ESS_2021 = Regulation("ESS 2021", "Energy Savings Scheme (Amendment No. 1) Rule 2021", "01 May 2021")

clause_8 = ESS_2021.add_part("8", PT.CLAUSE, "Metered Baseline Method")
clause_8.add_parts([("8.1", PT.CLAUSE, None),
                  ("8.2", PT.CLAUSE, None),
                  ("8.3", PT.CLAUSE, None),
                  ("8.3.A", PT.CLAUSE, None),
                  ("8.4", PT.CLAUSE, None),
                  ("8.4.A", PT.CLAUSE, "Additional Requirements for Lighting Upgrades"),
                  ("8.4.B", PT.CLAUSE, "Acceptable End-User Equipment for Lighting Upgrades"),
                  ("8.5", PT.ACTIVITY, "Baseline Per Unit of Output"),
                  ("8.6", PT.ACTIVITY, "Baseline Unaffected by Output"),
                  ("8.7", PT.ACTIVITY, "Normalised Baseline"),
                  ("8.8", PT.ACTIVITY, "NABERS Baseline"),
                  ("8.9", PT.ACTIVITY, "Aggregated Metered Baseline")])

clause_9 = ESS_2021.add_part("9", PT.CLAUSE, "Deemed Energy Savings Method")
clause_9.add_parts([("9.1", PT.CLAUSE, None),
                  ("9.2", PT.CLAUSE, None),
                  ("9.2.A", PT.CLAUSE, "Acceptable End-User Equipment"),
                  ("9.3", PT.CLAUSE, "Sale of New Appliances")
               ])

schedule_B = ESS_2021.add_part("B", PT.SCHEDULE, "Activity Definitions for the Sale of New Appliances")
schedule_B.add_parts([
                     ("B1", PT.ACTIVITY, "Sell a High Efficiency Clothes Washing Machine"),
                     ("B2", PT.ACTIVITY, "Sell a High Efficiency Clothes Dryer")
                     ])

schedule_D = ESS_2021.add_part("D", PT.SCHEDULE, "Activity Definitions for General Activities for Home Energy Efficiency Retrofits")
schedule_D.add_parts([
                     ("D1", PT.ACTIVITY, "Replace an External Single Glazed Window or Door with a Thermally Efficient Window or Door"),
                     ("D16", PT.ACTIVITY, "Install a New High Efficiency Air Conditioner or Replace an Existing Air Conditioner with a High Efficiency Air Conditioner")
                     ])