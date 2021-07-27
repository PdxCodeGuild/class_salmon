#Based on 'A Desktop Review of Calculation Equations for Geothermal Volumetric Assessment' by Shinya TAKAHASHI, Satoshi YOSHIDA
#https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2018/Takahashi.pdf
import numpy as np
#these equations need to be adjusted according to thermodynamic law, follow to the corrected equations below
q_rsv = c_v*v*(t_rsv-t_ref) #estimate of thermal energy originally stored in reservoir (Muffler, 1978); in kJ or  reservoir thermal energy available under reference temperature condition, according to TAKAHASHI and YOSHIDA
c_v = int(input('What is the average specific heat of the reservoir [kJ/m3/K] at the reservoir temperature')) #average volumetric specific heat of the reservoir at temperature t_res [kJ/m3/K], c_v = den_rock*c_r*(1-res_por)+den_fluid*cf_rsv
c_r = int(input('What is the specific heat [kJ/kg/K] of the rock in the reservoir?' ))#specific heat of rock [kJ/kg/K]
cf_rsv = int(input('What is the specific heat of fluid at reservoir temperature in [kJ/kg/K]? '))#specific heat of fluid at reservoir temperature [kJ/kg/K]
res_por = float(input('What is the reservoir porosity from 0-1? '))#reservoir porosity
den_rock = float(input('What is the density of the reservoir rock in kg/m3? ')) #density of rock [kg/m3]
den_fluid = float(input('What is the density of the fluid [kg/m3] in the reservoir at the reference temperature? '))#density of fluid at reservoir temperature[kg/m3]
v = int(input('What is the volume of the reservoir in cubic meters [m3]? ')) #volume of the reservoir [m3]
t_rsv = float(input('What is the temperature of the reservoir in degrees celcius? '))#temperature of the reservoir [C]
t_ref #reference temperature [C], temporary starting point or datum point aka ambient temperature


#calculating the mass of fluid at the wellhead
rg_amb #Recovery factor defined by the USGS method (t_amb = 15°C), equal to 𝐑𝐠
q_wh #Thermal energy available at wellhead, that sent into power cycle [kJ]
#q_rsv #Thermal energy originally in reservoir defined by Eq. 1; the right-side term of Eq. 1 is re-defined by this paper to be reservoir thermal energy available under reference temperature condition [kJ]
mass_wh_l #q_wh/(h_wh_l - h_amb_l)# Mass of fluid in liquid phase at wellhead [kg]

h_wh_l #Specific enthalpy of fluid in liquid phase at wellhead [kJ/kg]; assumes isenthalpic flow in wellbore; that is, no heat is lost by conduction as the water comes to the surface (Muffler, 1978)
r_g #recovery factor; "the ratio of geothermal energy recovered at the wellhead, to the geothermal energy originally in the reservoir" - reflects the physical and technological constraints of recovering all energy above the reference temperature
#with these USGS assumptions:
t_rsv = t_wh
t_wh #the temperature at the wellhead [C]
h_wh_l = h_rsv_l
h_rsv_l #specific enthalpy of the fluid in liquid phase, in the reservoir

#USGS method describing available work (exergy):
w_a = mass_wh_l*((h_wh_l - h_0_l)-t_0*(s_wh_l-s_0_l)) #in kJ or kW
w_a #Available work (exergy) [kJ] or [kW]
mass_wh_l #mass of liquid at the wellhead
h_wh_l #enthalpy of liquid at the wellhead
h_0_l #Specific enthalpy of fluid in liquid phase at final state [kJ/kg]
t_0 #It describes that two likely choices are 𝐓𝟎 equal to ambient (15℃; 288.15 K) in the USA or to condenser temperature (say, 40℃; 313.15 K), and that it prefers to use 𝟏𝟓℃ in order to keep 𝐖𝐀 a maximum value and thus the most appropriate reference value (Muffler, 1978).
s_wh_l #Specific entropy of fluid in liquid phase at wellhead [kJ/ (kg K)]
s_0_l #Specific entropy of fluid in liquid phase at final state [kJ/ (kg K)]

#combined equation for mass at the wellhead
mass_wh_l = r_g*c_v*v*(t_wh-t_amb)/(h_wh_l - h_amb_l)
#This is not in greement with definition of specific enthalpy; the mass sent into power cycle should be of the initial temperature 𝐭𝐫𝐬𝐯 = 𝐭𝐖𝐇 and specific enthalpy 𝐡𝐫𝐬𝐯_𝐋=𝐡𝐖𝐇_l
#Introducing the triple point temperature to the geothermal volumetric assessment method

#corrected equations below this comment, abiding by thermodynamic law
#formally known as the modified USGS method (2018)
q_rsv_trp = c_v*v*(t_rsv-t_trp) #[kJ]represents thermal energy inherently stored in reservoir; which shall be estimated before consideration of ambient temperature at which thermo-utilization system is to be used
r_g_trp = q_wh/q_rsv_trp #recovery factor at the triple point “the ratio of geothermal energy recovered at wellhead, to the geothermal energy originally (inherently) in the reservoir”
m_wh_l = q_wh/(h_wh_l - h_trp_l) = q_wh/h_wh_l #[kJ]




