# Managed retreat model design

> **Earlier guide architecture.** This document preserves the original design language and illustrative values. For current Harris County definitions, evidence, and proposed equation repairs, use the [September 15 dictionary](../documentation/Model_Data_Dictionary.csv). This is not an executable or validated model.

This document records a proposed system-dynamics architecture, equations, parameterization, and validation design. Example values and tests are specifications to implement; no calibration or simulation validation is claimed.

## Model Structure Overview

### Conceptual Framework

The managed retreat system operates through seven interconnected subsystems:

Hazard & Risk Assessment Subsystem

Community & Population Dynamics Subsystem

Economic & Fiscal Subsystem

Decision-Making & Governance Subsystem

Implementation & Retreat Process Subsystem

Social Equity & Wellbeing Subsystem

Land Use & Ecosystem Management Subsystem

### Major Feedback Loops

Reinforcing Loops (R)

R1: Hazard-Migration Spiral

Hazard Exposure → Property Damage → Outmigration → Declining Tax Base → Reduced Hazard Mitigation Capacity → Hazard Exposure

R2: Community Decline Cascade

Population Decline → Service Reduction → Community Attractiveness → Population Decline

R3: Proactive Retreat Momentum

Successful Retreats → Community Trust → Retreat Participation → Successful Retreats

R4: Economic Revitalization

Retreat Land Restoration → Ecosystem Benefits → Community Attractiveness → Tax Base → Funding for Retreat → Retreat Land Restoration

Balancing Loops (B)

B1: Risk Reduction Through Retreat

Hazard Exposure → Retreat Pressure → Properties Retreated → Hazard Exposure (decreased)

B2: Funding Constraints

Retreat Demand → Funding Required → Budget Constraints → Retreat Implementation Rate

B3: Social Carrying Capacity

Relocated Population → Receiving Area Pressure → Housing Availability → Relocation Feasibility → Relocated Population (constrained)

B4: Equity Adjustment

Inequitable Outcomes → Community Opposition → Policy Adjustment → Equity Measures → Inequitable Outcomes (decreased)

## Detailed Subsystem Specifications

### Hazard & Risk Assessment Subsystem

Stock Variables

STOCK: Properties_at_RiskUNITS: propertiesINITIAL VALUE: Initial_Properties_in_Hazard_ZoneINFLOWS: New_Development_in_Risk_ZoneOUTFLOWS: Properties_Retreated, Properties_Destroyed

STOCK: Cumulative_Hazard_EventsUNITS: eventsINITIAL VALUE: 0INFLOWS: Hazard_Event_RateOUTFLOWS: None

STOCK: Climate_Change_Impact_IndexUNITS: dimensionless (0-100)INITIAL VALUE: Current_CC_ImpactINFLOWS: CC_Impact_Increase_RateOUTFLOWS: None

Flow Variables

FLOW: Hazard_Event_RateUNITS: events/yearEQUATION: Base_Hazard_Frequency * Climate_Change_Multiplier * (1 + Random_Variation)

FLOW: Properties_DestroyedUNITS: properties/yearEQUATION: Properties_at_Risk * Hazard_Event_Rate * Average_Destruction_Rate

Auxiliary Variables

AUX: Hazard_Exposure_IndexUNITS: dimensionlessEQUATION: (Properties_at_Risk / Total_Properties) * Hazard_Severity_Factor * Climate_Change_Impact_Index / 100

AUX: Climate_Change_MultiplierUNITS: dimensionlessEQUATION: 1 + (Climate_Change_Impact_Index / 100) * CC_Sensitivity_Parameter

Parameters

Base_Hazard_Frequency: 0.1-0.5 events/year (calibrate to local context)

Average_Destruction_Rate: 0.05-0.20 (fraction of properties destroyed per event)

CC_Sensitivity_Parameter: 0.5-2.0 (how much CC increases hazard frequency)

Hazard_Severity_Factor: 1-10 (relative severity: flooding=1, multiple hazards=5+)

### Community & Population Dynamics Subsystem

Stock Variables

STOCK: Community_PopulationUNITS: peopleINITIAL VALUE: Initial_PopulationINFLOWS: Births, ImmigrationOUTFLOWS: Deaths, Outmigration, Managed_Retreat_Relocations

STOCK: HomeownersUNITS: householdsINITIAL VALUE: Initial_HomeownersINFLOWS: New_HomeownershipOUTFLOWS: Homeowner_Retreat, Homeowner_Outmigration

STOCK: RentersUNITS: householdsINITIAL VALUE: Initial_RentersINFLOWS: New_RentersOUTFLOWS: Renter_Displacement, Renter_Retreat

STOCK: Community_Social_CapitalUNITS: dimensionless (0-100)INITIAL VALUE: 50INFLOWS: Social_Capital_BuildingOUTFLOWS: Social_Capital_Erosion

Flow Variables

FLOW: OutmigrationUNITS: people/yearEQUATION: Community_Population * Base_Outmigration_Rate * Hazard_Pressure_Multiplier * (1 - Community_Attachment_Factor)

FLOW: Managed_Retreat_RelocationsUNITS: people/yearEQUATION: Properties_Retreated * Average_Household_Size * Relocation_Success_Rate

FLOW: Social_Capital_ErosionUNITS: units/yearEQUATION: Community_Social_Capital * (Population_Decline_Rate + Displacement_Stress_Factor) * 0.1

Auxiliary Variables

AUX: Community_Attachment_FactorUNITS: dimensionless (0-1)EQUATION: 0.3 + 0.4 * (Social_Capital / 100) + 0.3 * Place_Attachment_Index

AUX: Hazard_Pressure_MultiplierUNITS: dimensionlessEQUATION: 1 + 2 * Hazard_Exposure_Index * (1 - Perceived_Safety)

AUX: Place_Attachment_IndexUNITS: dimensionless (0-1)EQUATION: IF THEN ELSE(First_Nations_Community = 1, 0.8 + 0.2 * Ancestral_Land_Significance,0.4 + 0.3 * Years_of_Residence / 50)

Parameters

Base_Outmigration_Rate: 0.01-0.03 per year

Average_Household_Size: 2.5 people/household

Relocation_Success_Rate: 0.6-0.95 (depends on support services)

### Economic & Fiscal Subsystem

Stock Variables

STOCK: Municipal_Tax_BaseUNITS: dollarsINITIAL VALUE: Initial_Assessment_ValueINFLOWS: New_Development_Value, Property_Value_AppreciationOUTFLOWS: Property_Value_Depreciation, Retreat_Property_Removal

STOCK: Retreat_Funding_AvailableUNITS: dollarsINITIAL VALUE: 0INFLOWS: Federal_Funding, Provincial_Funding, Municipal_Contribution, Insurance_PayoutsOUTFLOWS: Buyout_Payments, Support_Service_Costs, Land_Restoration_Costs

STOCK: Cumulative_Disaster_CostsUNITS: dollarsINITIAL VALUE: 0INFLOWS: Annual_Disaster_Damage_CostsOUTFLOWS: None

Flow Variables

FLOW: Buyout_PaymentsUNITS: dollars/yearEQUATION: Properties_Retreated * Average_Property_Value * Compensation_Rate

FLOW: Annual_Disaster_Damage_CostsUNITS: dollars/yearEQUATION: Hazard_Event_Rate * Properties_at_Risk * Average_Property_Value * Average_Damage_Fraction

FLOW: Federal_FundingUNITS: dollars/yearEQUATION: Federal_Funding_Availability * Retreat_Program_Eligibility * Political_Priority_Factor

Auxiliary Variables

AUX: Compensation_RateUNITS: dimensionlessEQUATION: Compensation_Type_Selector * Equity_Adjustment_FactorWHERE:

Market_Value_Option: 1.0

Pre_Disaster_Value_Option: 1.1

Enhanced_Compensation_Option: 1.2-1.5

AUX: Cost_Benefit_RatioUNITS: dimensionlessEQUATION: (Cumulative_Disaster_Costs + Future_Disaster_Costs_NPV) / (Total_Retreat_Costs + Retreat_Program_Admin_Costs)

AUX: Municipal_Fiscal_StressUNITS: dimensionless (0-1)EQUATION: MAX(0, MIN(1, (Budget_Gap + Service_Costs) / (Tax_Revenue + Transfer_Payments)))

Parameters

Average_Property_Value: $200,000-$800,000 (location dependent)

Average_Damage_Fraction: 0.2-0.6 per event

Federal_Funding_Availability: $0-$50M/year (program dependent)

Discount_Rate: 0.03-0.07 (for NPV calculations)

### Decision-Making & Governance Subsystem

Stock Variables

STOCK: Community_Trust_in_ProcessUNITS: dimensionless (0-100)INITIAL VALUE: 50INFLOWS: Trust_Building_ActionsOUTFLOWS: Trust_Erosion

STOCK: Retreat_Policy_Development_ProgressUNITS: dimensionless (0-100)INITIAL VALUE: 0INFLOWS: Policy_Development_RateOUTFLOWS: None

STOCK: Stakeholder_Engagement_LevelUNITS: dimensionless (0-100)INITIAL VALUE: 20INFLOWS: Engagement_ActivitiesOUTFLOWS: Engagement_Fatigue

Flow Variables

FLOW: Trust_Building_ActionsUNITS: units/yearEQUATION: Transparency_Level * Community_Engagement_Quality * Successful_Retreat_Demonstrations * 5

FLOW: Trust_ErosionUNITS: units/yearEQUATION: Community_Trust * (Perceived_Inequity + Process_Delays + Communication_Failures) * 0.1

FLOW: Policy_Development_RateUNITS: percent/yearEQUATION: Governance_Capacity * Multi_Stakeholder_Participation * (Political_Will / 100) * 10 * (1 - Retreat_Policy_Development_Progress / 100)

Auxiliary Variables

AUX: Decision_Making_ApproachUNITS: categoricalOPTIONS: Voluntary, Voluntary_with_Incentives, Persuasive, Mandatory_with_Optout, Fully_MandatoryEQUATION: Policy_Choice_Selector

AUX: Governance_Structure_EffectivenessUNITS: dimensionless (0-1)EQUATION: (Number_of_Actors_Engaged / Potential_Actors) * Coordination_Quality * Decision_Authority_Clarity

AUX: First_Nations_Engagement_QualityUNITS: dimensionless (0-1)EQUATION: Cultural_Appropriate_Process * Indigenous_Leadership_Level * Non_Market_Value_Recognition * Land_Rights_Respect

Parameters

Transparency_Level: 0-1 (policy choice)

Community_Engagement_Quality: 0-1 (based on engagement approaches)

Governance_Capacity: 0.3-1.0 (based on resources and expertise)

Political_Will: 0-100 (context dependent)

### Implementation & Retreat Process Subsystem

Stock Variables

STOCK: Properties_in_Retreat_PipelineUNITS: propertiesINITIAL VALUE: 0INFLOWS: Retreat_Applications, Proactive_Retreat_IdentificationOUTFLOWS: Properties_Retreated, Retreat_Dropouts

STOCK: Relocated_HouseholdsUNITS: householdsINITIAL VALUE: 0INFLOWS: Successful_RelocationsOUTFLOWS: None

STOCK: Support_Services_CapacityUNITS: caseworkers_equivalentINITIAL VALUE: Initial_CapacityINFLOWS: Capacity_BuildingOUTFLOWS: Capacity_Attrition

Flow Variables

FLOW: Retreat_ApplicationsUNITS: properties/yearEQUATION: Properties_at_Risk * Retreat_Willingness * Program_Awareness * Application_Ease_Factor

FLOW: Properties_RetreatedUNITS: properties/yearEQUATION: MIN(Properties_in_Pipeline / Processing_Time,Retreat_Funding_Available / (Average_Property_Value * Compensation_Rate),Support_Services_Capacity * Caseworker_Throughput)

FLOW: Successful_RelocationsUNITS: households/yearEQUATION: Properties_Retreated * Relocation_Success_RateWHERE Relocation_Success_Rate depends on:

Receiving_Area_Housing_Availability

Relocation_Support_Services

Community_Cohesion_Preservation

Auxiliary Variables

AUX: Retreat_WillingnessUNITS: dimensionless (0-1)EQUATION: Hazard_Perception * Compensation_Attractiveness * (1 - Place_Attachment_Index) * Trust_Factor - Legal_Obstacles

AUX: Processing_TimeUNITS: yearsEQUATION: Base_Processing_Time * Legal_Complexity_Factor / Administrative_Efficiency

AUX: Program_AwarenessUNITS: dimensionless (0-1)EQUATION: Communication_Effectiveness * Time_Since_Program_Launch / (Time_Since_Program_Launch + Awareness_Half_Time)

Parameters

Base_Processing_Time: 1-3 years

Caseworker_Throughput: 10-30 properties/year per caseworker

Awareness_Half_Time: 0.5-2 years

### Social Equity & Wellbeing Subsystem

Stock Variables

STOCK: Equity_IndexUNITS: dimensionless (0-100)INITIAL VALUE: 50INFLOWS: Equity_ImprovementsOUTFLOWS: Equity_Degradation

STOCK: Vulnerable_Population_WellbeingUNITS: dimensionless (0-100)INITIAL VALUE: Initial_WellbeingINFLOWS: Wellbeing_ImprovementsOUTFLOWS: Wellbeing_Decline

STOCK: Community_Psychosocial_StressUNITS: dimensionless (0-100)INITIAL VALUE: 30INFLOWS: Stress_AccumulationOUTFLOWS: Stress_Relief

Flow Variables

AUX: Equity_ImprovementsUNITS: units/yearEQUATION: Equity_Policies_Implemented * Vulnerable_Population_Support * (100 - Equity_Index) * 0.1

FLOW: Wellbeing_DeclineUNITS: units/yearEQUATION: Displacement_Rate * Displacement_Impact + Service_Access_Loss + Cultural_Heritage_Loss

FLOW: Stress_ReliefUNITS: units/yearEQUATION: Psychosocial_Support_Capacity * Support_Effectiveness * Community_Psychosocial_Stress * 0.15

Auxiliary Variables

AUX: Equity_in_CompensationUNITS: dimensionless (0-1)EQUATION: 1 - ABS(Homeowner_Compensation_Avg - Renter_Compensation_Avg) / (Homeowner_Compensation_Avg + Renter_Compensation_Avg)

AUX: Vulnerable_Population_ShareUNITS: dimensionless (0-1)EQUATION: (Low_Income_Households + Elderly_Households + Disabled_Households + Racialized_Households) / Total_Households

AUX: Historical_Inequity_FactorUNITS: dimensionless (1-3)EQUATION: IF THEN ELSE(Racialized_Community = 1 OR First_Nations_Community = 1, 1.5 + Historical_Discrimination_Index, 1.0)

AUX: Cultural_Heritage_ImpactUNITS: dimensionless (0-1)EQUATION: Heritage_Sites_Affected * Cultural_Significance * (1 - Heritage_Protection_Measures)

Parameters

Psychosocial_Support_Capacity: 0-100 (based on caseworkers, counselors)

Support_Effectiveness: 0.4-0.9

Displacement_Impact: 0.1-0.5 (wellbeing units per displaced household)

### Land Use & Ecosystem Management Subsystem

Stock Variables

STOCK: Retreat_Lands_AreaUNITS: hectaresINITIAL VALUE: 0INFLOWS: Land_Acquired_Through_RetreatOUTFLOWS: Retreat_Land_Redevelopment

STOCK: Restored_Ecosystem_AreaUNITS: hectaresINITIAL VALUE: 0INFLOWS: Ecosystem_Restoration_RateOUTFLOWS: Ecosystem_Degradation

STOCK: Ecosystem_Health_IndexUNITS: dimensionless (0-100)INITIAL VALUE: Initial_Ecosystem_HealthINFLOWS: Ecosystem_ImprovementOUTFLOWS: Ecosystem_Decline

Flow Variables

FLOW: Land_Acquired_Through_RetreatUNITS: hectares/yearEQUATION: Properties_Retreated * Average_Property_Size

FLOW: Ecosystem_Restoration_RateUNITS: hectares/yearEQUATION: MIN(Retreat_Lands_Area - Restored_Ecosystem_Area,Restoration_Funding / Cost_Per_Hectare,Restoration_Capacity)

FLOW: Ecosystem_ImprovementUNITS: units/yearEQUATION: (Restored_Ecosystem_Area / Total_Ecosystem_Area) * Natural_Recovery_Rate * 10

Auxiliary Variables

AUX: Retreat_Land_Use_StrategyUNITS: categoricalOPTIONS: Full_Natural_Restoration, Multi_Purpose, Restricted_Rebuilding, Green_InfrastructureEQUATION: Policy_Selection

AUX: Ecosystem_Service_BenefitsUNITS: dollars/yearEQUATION: Restored_Ecosystem_Area * (Flood_Protection_Value + Water_Quality_Value + Recreation_Value + Carbon_Sequestration_Value + Biodiversity_Value)

AUX: Natural_Hazard_Buffer_CapacityUNITS: dimensionless (0-1)EQUATION: (Restored_Ecosystem_Area / Total_Hazard_Zone_Area) * Ecosystem_Type_Protection_Factor

Parameters

Average_Property_Size: 0.1-2.0 hectares

Cost_Per_Hectare: $10,000-$100,000 (restoration type dependent)

Restoration_Capacity: 10-100 hectares/year

Ecosystem_Type_Protection_Factor: 0.2 (grassland) to 0.8 (wetland/mangrove)

## Key Model Equations and Relationships

### Time Constants and Delays

System dynamics models require careful specification of delays to capture realistic system behavior:

PARAMETER: Hazard_Perception_Delay = 1-3 yearsPARAMETER: Policy_Implementation_Delay = 2-5 yearsPARAMETER: Ecosystem_Restoration_Time = 5-20 yearsPARAMETER: Community_Trust_Building_Time = 3-10 yearsPARAMETER: Infrastructure_Decommissioning_Time = 1-3 years

Implementation in Vensim:Perceived_Hazard_Risk = SMOOTH3(Actual_Hazard_Risk, Hazard_Perception_Delay)Policy_Implemented = DELAY3(Policy_Adopted, Policy_Implementation_Delay)Mature_Ecosystem = DELAY3(Restored_Ecosystem_Area, Ecosystem_Restoration_Time)

### Nonlinear Relationships

Many relationships in managed retreat are nonlinear and should be represented with table functions:

Compensation Attractiveness Function:Compensation_Attractiveness = f(Compensation_Rate)Lookup Table:0.8 → 0.1 (Below market value: very unattractive)1.0 → 0.5 (Market value: moderately attractive)1.2 → 0.8 (20% above market: attractive)1.5 → 0.95 (50% bonus: very attractive)

Community Opposition Function:Community_Opposition = f(Perceived_Inequity)Lookup Table:0.0 → 0.0 (No inequity: no opposition)0.3 → 0.2 (Low inequity: mild opposition)0.6 → 0.6 (Moderate inequity: significant opposition)0.9 → 0.95 (High inequity: severe opposition blocks program)

Political Will Function:Political_Will = f(Recent_Disaster_Events, Cost_Benefit_Ratio)

Spikes after disasters (event-driven)

Sustained by favorable economics

Erodes over time without reinforcement

### Conditional Logic

Retreat Trigger Logic:Retreat_Program_Active = IF THEN ELSE(Trigger_Type = "Reactive_Disaster",IF THEN ELSE(Recent_Major_Disaster > 0, 1, 0),IF THEN ELSE(Trigger_Type = "Proactive_Policy",IF THEN ELSE(Policy_Stimulus_Present = 1 AND Funding_Available > Threshold, 1, 0),IF THEN ELSE(Trigger_Type = "Community_Request",IF THEN ELSE(Community_Petition_Threshold_Met = 1, 1, 0),0)))

First Nations Special Considerations:First_Nations_Adjustment_Factor = IF THEN ELSE(First_Nations_Community = 1,(1 + Non_Market_Values_Weight * 0.5) *(1 + Ancestral_Land_Significance * 0.3) *(1 - Historical_Forced_Relocation_Trauma * 0.4) *Cultural_Protocol_Adherence,1.0)

## Model Parameterization Guide

### Data Requirements

Parameter Category

Required Data

Typical Sources

Hazard

Historical event frequency, damage rates, climate projections

Emergency management, NOAA, IPCC

Population

Demographics, migration rates, household size

Census, municipal records

Economic

Property values, tax revenues, disaster costs

Assessment authority, insurance

Governance

Policy timelines, stakeholder involvement

Government documents, case studies

Social

Social capital indicators, equity metrics

Surveys, community assessments

Ecological

Ecosystem extent, restoration costs

Environmental agencies, NGOs

### Calibration Strategy

Step 1: Initialize Stocks

Use current actual values for all stock variables

Ensure dimensional consistency

Step 2: Set Conservative Parameters

Start with middle-range parameter values

Use literature values where available

Step 3: Validate Behavior

Run base case simulation (no retreat)

Check against historical trends for hazards, population, tax base

Step 4: Sensitivity Analysis

Identify parameters with highest leverage

Test extreme values to ensure model stability

Focus calibration effort on high-leverage parameters

Step 5: Policy Testing

Compare multiple retreat scenarios

Validate against case studies (e.g., Oakwood Beach, NY; Valmeyer, IL)

## Vensim Implementation Guide

### Model Organization

Recommended View Structure:

Main View: Overview with all 7 subsystems and major loops labeled

Hazard Risk View: Subsystem 1 detail

Community Dynamics View: Subsystem 2 detail

Economic Fiscal View: Subsystem 3 detail

Governance View: Subsystem 4 detail

Implementation View: Subsystem 5 detail

Equity Wellbeing View: Subsystem 6 detail

Land Ecosystem View: Subsystem 7 detail

Dashboard View: Key output graphs and policy controls

### Variable Naming Conventions

Follow these conventions for Vensim compatibility:

Stocks: Stock_Name (capitalize, underscores)

Flows: Flow_Name (capitalize, underscores)

Auxiliaries: Auxiliary_Name (capitalize, underscores)

Parameters: PARAMETER_NAME (all caps, underscores)

Units: Always specify in variable documentation

### Model Settings

TIME STEP = 0.125 years (quarterly)

Captures seasonal variation in hazards

Balances accuracy and computation time

INITIAL TIME = 0 yearsFINAL TIME = 50 years (adjustable to 100 for long-term scenarios)

INTEGRATION METHOD = Runge-Kutta 4

More accurate for complex nonlinear systems

Alternative: Euler for initial debugging

### Units Checking

Vensim's unit checking is critical for model validity. Define base units:

Base Units:

people

households

properties

dollars

hectares

events

dimensionless

Derived Units:

people/year

dollars/year

properties/year

hectares/year

Example Verification:Properties_Retreated [properties/year] =Properties_in_Pipeline [properties] /Processing_Time [years]

### Creating Lookup Functions

For nonlinear relationships, use Vensim's graphical lookup editor:

Click "Equation" → "With Lookup"

Define input variable range (x-axis)

Draw or enter coordinate pairs for output (y-axis)

Use interpolation: Linear or Cubic

Save as reusable function

Example:Compensation_Attractiveness_Lookup([(0.5,0)-(2,1)],(0.8,0.1),(1.0,0.5),(1.2,0.8),(1.5,0.95))

### Subscription and Array Structures

For modeling multiple land user groups or hazard types, use subscripts:

Land_User_Group: (Homeowners, Renters, Commercial, First_Nations, Government)

Properties_at_Risk[Land_User_Group] =INTEG(New_Development[Land_User_Group] -Properties_Retreated[Land_User_Group] -Properties_Destroyed[Land_User_Group],Initial_Properties[Land_User_Group])

Compensation_Rate[Land_User_Group] =Base_Compensation_Rate *Equity_Adjustment[Land_User_Group] *User_Group_Factor[Land_User_Group]

## Scenario Analysis Framework

### Base Case Scenarios

Scenario 1: Status Quo (No Managed Retreat)

No retreat program implemented

Reactive disaster response only

Measure: cumulative costs, population decline, hazard exposure

Scenario 2: Reactive Retreat (Post-Disaster)

Retreat triggered only after major disasters

Limited funding and planning

Measure: crisis-driven costs, emergency response burden

Scenario 3: Proactive Retreat (Planned)

Advance planning and voluntary programs

Adequate funding and support services

Measure: reduced long-term costs, orderly transition

Scenario 4: Hybrid Approach

Combination of proactive and reactive elements

Adaptive management with multiple triggers

### Policy Levers for Testing

These values are proposed scenario settings, not estimated effects or recommended compensation policies.

| Policy lever | Low setting | High setting |
|---|---|---|
| Compensation rate | 0.8 times market value | 1.5 times market value |
| Funding level | $5 million/year | $50 million/year |
| Support services | Minimal caseworkers | Comprehensive support |
| Equity focus | Standard approach | Enhanced support for vulnerable households |
| Engagement quality | Top-down decisions | Full participatory process |
| Retreat voluntariness | Mandatory | Completely voluntary |
| Ecosystem restoration | Minimal | Full natural restoration |
| Time horizon | Reactive, 1–5 years | Long-term, 10–100 years |

### Key Performance Indicators

Monitor these outputs across scenarios:

Economic KPIs:

Total retreat program costs (discounted)

Cumulative disaster costs avoided

Municipal tax base stability

Cost-benefit ratio

Funding sustainability

Social KPIs:

Population retained in community

Equity index trajectory

Community social capital

Psychosocial stress levels

Vulnerable population wellbeing

First Nations cultural preservation

Environmental KPIs:

Restored ecosystem area

Ecosystem health index

Ecosystem service benefits (monetized)

Natural hazard buffer capacity

Implementation KPIs:

Properties successfully retreated

Relocation success rate

Community trust in process

Stakeholder engagement level

Program completion timeline

## Model Validation and Testing

### Structural Validation Tests

Boundary Adequacy Test

Are all major feedback loops endogenous to the model?

Are exogenous drivers justified?

Structure Assessment Test

Do relationships match real-world processes?

Are delays realistic?

Are nonlinearities appropriate?

Dimensional Consistency Test

Run Vensim unit checker (Tools → Check Units)

Verify all equations are dimensionally consistent

Extreme Conditions Test

Set hazard frequency to zero → retreat demand should drop

Set funding to zero → implementation should halt

Set property values to extreme high → costs should scale appropriately

### Behavior Validation Tests

Behavior Reproduction Test

Compare model output to historical case studies

Target cases: Oakwood Beach (NY), Valmeyer (IL), Soldiers Delight (MD)

Surprise Behavior Test

Does model generate unexpected but plausible dynamics?

Example: community decline acceleration despite retreat program

Sensitivity Analysis

Use Vensim Sensitivity → Monte Carlo or Latin Hypercube

Identify critical uncertainties

Test robustness of policy recommendations

### Policy Implication Testing

Policy Effectiveness Test

Does increased compensation increase participation?

Do support services improve relocation success?

Does equity focus reduce opposition?

Unintended Consequences Test

Can too-generous compensation create moral hazard?

Can mandatory retreat destroy social capital?

Can delayed action worsen fiscal crisis?

## Advanced Model Features

### Spatial Heterogeneity

For models covering multiple communities or geographic scales:

Geographic_Scale: (Individual_Properties, Neighborhood, Community, Watershed)

Properties_at_Risk[Geographic_Scale] = ...Retreat_Strategy[Geographic_Scale] = ...

Connectivity Between Scales:Regional_Retreat_Pressure = SUM(Community_Retreat_Demand[Community])Watershed_Flooding_Benefit = f(Upstream_Retreat_Area[Neighborhood])

### Multi-Hazard Integration

For compounding hazards:

Hazard_Type: (Flooding, Coastal_Erosion, Wildfire, Sea_Level_Rise)

Total_Hazard_Exposure = SUM(Hazard_Exposure[Hazard_Type])

Compounding_Effect_Multiplier =IF THEN ELSE(Active_Hazards > 1,1 + 0.3 * (Active_Hazards - 1),1.0)

### Climate Change Scenarios

Implement IPCC scenario forcing:

CC_Scenario: (RCP2.6, RCP4.5, RCP8.5)

Climate_Change_Impact_Index =INTEG(CC_Impact_Rate[CC_Scenario], Initial_CC_Impact)

Sea_Level_Rise[Year] =LOOKUP_TABLE(Year, SLR_Projection_Table[CC_Scenario])

### Optimization and Policy Search

Use Vensim optimization to find best policy combinations:

Objective Function:Minimize: Total_Social_Cost =Retreat_Program_Costs +Disaster_Costs +Social_Disruption_Costs -Ecosystem_Benefits

Subject to:

Equity_Index > 60

Community_Trust > 50

Funding < Budget_Constraint

## Documentation and Reporting

### Model Documentation Standards

Every variable should include:

Description: What does this represent?

Units: Dimensional units

Equation: Mathematical relationship

Source: Data source or assumption basis

Sensitivity: High/Medium/Low leverage

Vensim Implementation:Use Comments field for each variable (right-click → Comment)

### Output Visualization

Recommended Graphs:

Time Series Plots

Properties at Risk vs. Properties Retreated

Municipal Tax Base trajectory

Community Population and Social Capital

Cumulative Costs (retreat vs. disaster)

Phase Plots

Community Trust vs. Equity Index

Hazard Exposure vs. Fiscal Stress

Bar Charts

Scenario comparison: Final outcomes

Policy sensitivity: Tornado diagrams

Dashboard Gauges

Current Equity Index

Cost-Benefit Ratio

Ecosystem Health

### Stakeholder Communication

Create simplified Causal Loop Diagrams for communication:

Extract from full model:

Hide auxiliary variables

Show only key stocks and major feedback loops

Add loop labels (R1, B1, etc.)

Include brief explanatory text

Use Vensim Synthesim (Professional/DSS only):

Create interactive interface

Sliders for policy levers

Real-time graph updates

Scenario comparison tools

## Limitations and Future Extensions

Current Model Limitations

Spatial Resolution: Aggregated geographic representation; doesn't capture fine-scale property-level variation

Behavioral Complexity: Simplified decision-making; doesn't fully capture psychological factors

Legal System: Simplified representation of litigation and regulatory processes

Network Effects: Limited representation of social networks and information diffusion

Economic Detail: Simplified economic multiplier effects and market dynamics

Potential Extensions

Near-term Enhancements:

Add detailed age-cohort structure for population dynamics

Incorporate housing market supply/demand dynamics

Model insurance industry feedback loops

Add detailed infrastructure network interdependencies

Advanced Capabilities:

Agent-based modeling integration for household decisions

GIS integration for spatial analysis

Real-time data feeds for hazard monitoring

Machine learning for parameter estimation from case studies

Gaming/simulation exercises for stakeholder engagement

Research Frontiers:

Climate migration at regional/national scale

Transboundary retreat coordination

Ecosystem service valuation refinement

Social tipping points and phase transitions

Intergenerational equity accounting
