#Based on 'A Desktop Review of Calculation Equations for Geothermal Volumetric Assessment' by Shinya TAKAHASHI, Satoshi YOSHIDA
#https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2018/Takahashi.pdf
import numpy as np
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

