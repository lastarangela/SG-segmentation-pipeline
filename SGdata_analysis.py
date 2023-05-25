#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 11:12:10 2022

@author: angela_gao
"""

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt

##################################################################################################
####################################### DATA INPUT ###############################################
##################################################################################################

# Replicate 1 data input
CellInfo1 = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/Pipeline_04_29_22/GranuleInfo/Replicate1/Filtered_Cells.csv')
CellInfo_short1 = CellInfo1[['ImageNumber', 'ObjectNumber', 'Children_Filtered_SGs_Count']]
SGInfo1 = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/Pipeline_04_29_22/GranuleInfo/Replicate1/Filtered_SGs.csv')
SGInfo_short1 = SGInfo1[['ImageNumber', 'ObjectNumber', 'AreaShape_Area', 'Parent_Filtered_Cells']]
Image_Info1 = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/Pipeline_04_29_22/GranuleInfo/Replicate1/Image.csv')
ImageInfo_short1 = Image_Info1[['ImageNumber','Metadata_time','Metadata_Position', 'Count_Filtered_Cells']]

CellInfo_short_Time1 = CellInfo_short1.merge(ImageInfo_short1, how="left", on= ["ImageNumber"])
SGInfo_short_Time1 = SGInfo_short1.merge(ImageInfo_short1, how="left", on= ["ImageNumber"])

CellInfo_short_Time1 = CellInfo_short_Time1[CellInfo_short_Time1['Metadata_Position'].isin([17,18])]
SGInfo_short_Time1 = SGInfo_short_Time1[SGInfo_short_Time1['Metadata_Position'].isin([17,18])]
ImageInfo_short1 = ImageInfo_short1[ImageInfo_short1['Metadata_Position'].isin([17,18])]

CellCount1 = ImageInfo_short1[['Count_Filtered_Cells', 'Metadata_time']].groupby(['Metadata_time']).sum()
CellCount1 = CellCount1.reset_index()

# Replicate 2 data input
CellInfo2 = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/Pipeline_04_29_22/GranuleInfo/Replicate2/Filtered_Cells.csv')
CellInfo_short2 = CellInfo2[['ImageNumber', 'ObjectNumber', 'Children_Filtered_SGs_Count']]
SGInfo2 = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/Pipeline_04_29_22/GranuleInfo/Replicate2/Filtered_SGs.csv')
SGInfo_short2 = SGInfo2[['ImageNumber', 'ObjectNumber', 'AreaShape_Area', 'Parent_Filtered_Cells']]
Image_Info2 = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/Pipeline_04_29_22/GranuleInfo/Replicate2/Image.csv')
ImageInfo_short2 = Image_Info2[['ImageNumber','Metadata_time','Metadata_Position', 'Count_Filtered_Cells']]

CellInfo_short_Time2 = CellInfo_short2.merge(ImageInfo_short2, how="left", on= ["ImageNumber"])
SGInfo_short_Time2 = SGInfo_short2.merge(ImageInfo_short2, how="left", on= ["ImageNumber"])

CellInfo_short_Time2 = CellInfo_short_Time2[CellInfo_short_Time2['Metadata_Position'].isin([35,36])]
SGInfo_short_Time2 = SGInfo_short_Time2[SGInfo_short_Time2['Metadata_Position'].isin([35,36])]
ImageInfo_short2 = ImageInfo_short2[ImageInfo_short2['Metadata_Position'].isin([35,36])]

CellCount2 = ImageInfo_short2[['Count_Filtered_Cells', 'Metadata_time']].groupby(['Metadata_time']).sum()
CellCount2 = CellCount2.reset_index()

# Replicate 3 data input
CellInfo3 = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/Pipeline_04_29_22/GranuleInfo/Replicate3/Filtered_Cells.csv')
CellInfo_short3 = CellInfo3[['ImageNumber', 'ObjectNumber', 'Children_Filtered_SGs_Count']]
SGInfo3 = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/Pipeline_04_29_22/GranuleInfo/Replicate3/Filtered_SGs.csv')
SGInfo_short3 = SGInfo3[['ImageNumber', 'ObjectNumber', 'AreaShape_Area', 'Parent_Filtered_Cells']]
Image_Info3 = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/Pipeline_04_29_22/GranuleInfo/Replicate3/Image.csv')
ImageInfo_short3 = Image_Info3[['ImageNumber','Metadata_time','Metadata_Position', 'Count_Filtered_Cells']]

CellInfo_short_Time3 = CellInfo_short3.merge(ImageInfo_short3, how="left", on= ["ImageNumber"])
SGInfo_short_Time3 = SGInfo_short3.merge(ImageInfo_short3, how="left", on= ["ImageNumber"])

CellInfo_short_Time3 = CellInfo_short_Time3[CellInfo_short_Time3['Metadata_Position'].isin([53,54])]
SGInfo_short_Time3 = SGInfo_short_Time3[SGInfo_short_Time3['Metadata_Position'].isin([53,54])]
ImageInfo_short3 = ImageInfo_short3[ImageInfo_short3['Metadata_Position'].isin([53,54])]

CellCount3 = ImageInfo_short3[['Count_Filtered_Cells', 'Metadata_time']].groupby(['Metadata_time']).sum()
CellCount3 = CellCount3.reset_index()

# ##################################################################################################
# ################################ DATA INPUT (alternative) ########################################
# ##################################################################################################
# # Replicate 1-3 data input
# CellInfo = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/Jess_Microscope/072222/ImageAnalysis/Pipeline_07_26_22IF/GranuleInfo/All/Filtered_Cells.csv')
# CellInfo_short = CellInfo[['ImageNumber', 'ObjectNumber', 'Children_Filtered_SGs_Count']]
# SGInfo = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/Jess_Microscope/072222/ImageAnalysis/Pipeline_07_26_22IF/GranuleInfo/All/Filtered_SGs.csv')
# SGInfo_short = SGInfo[['ImageNumber', 'ObjectNumber', 'AreaShape_Area', 'Parent_Filtered_Cells']]
# ImageInfo = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/Jess_Microscope/072222/ImageAnalysis/Pipeline_07_26_22IF/GranuleInfo/All/Image.csv')
# ImageInfo_short = ImageInfo[['ImageNumber','Metadata_Well', 'Count_Filtered_Cells']]
# # Update time according to imaging
# Time = [0,1,2,3,4,5,6]*25
# Time.sort()
# Time = Time*6
# ImageInfo_short['Metadata_time'] = Time

# CellInfo_short_Time = CellInfo_short.merge(ImageInfo_short, how="left", on= ["ImageNumber"])
# SGInfo_short_Time = SGInfo_short.merge(ImageInfo_short, how="left", on= ["ImageNumber"])

# #'E2','E3','E4','E5','E6','E7','E8'
# CellInfo_short_Time1 = CellInfo_short_Time[CellInfo_short_Time['Metadata_Well'].isin(['B2','B3','B4','B5','B6','B7','B8'])]
# SGInfo_short_Time1 = SGInfo_short_Time[SGInfo_short_Time['Metadata_Well'].isin(['B2','B3','B4','B5','B6','B7','B8'])]
# ImageInfo_short1 = ImageInfo_short[ImageInfo_short['Metadata_Well'].isin(['B2','B3','B4','B5','B6','B7','B8'])]

# CellCount1 = ImageInfo_short1[['Count_Filtered_Cells', 'Metadata_time']].groupby(['Metadata_time']).sum()
# CellCount1 = CellCount1.reset_index()

# #'F2','F3','F4','F5','F6','F7','F8'
# CellInfo_short_Time2 = CellInfo_short_Time[CellInfo_short_Time['Metadata_Well'].isin(['C2','C3','C4','C5','C6','C7','C8'])]
# SGInfo_short_Time2 = SGInfo_short_Time[SGInfo_short_Time['Metadata_Well'].isin(['C2','C3','C4','C5','C6','C7','C8'])]
# ImageInfo_short2 = ImageInfo_short[ImageInfo_short['Metadata_Well'].isin(['C2','C3','C4','C5','C6','C7','C8'])]

# CellCount2 = ImageInfo_short2[['Count_Filtered_Cells', 'Metadata_time']].groupby(['Metadata_time']).sum()
# CellCount2 = CellCount2.reset_index()

# #'G2','G3','G4','G5','G6','G7','G8'
# CellInfo_short_Time3 = CellInfo_short_Time[CellInfo_short_Time['Metadata_Well'].isin(['D2','D3','D4','D5','D6','D7','D8'])]
# SGInfo_short_Time3 = SGInfo_short_Time[SGInfo_short_Time['Metadata_Well'].isin(['D2','D3','D4','D5','D6','D7','D8'])]
# ImageInfo_short3 = ImageInfo_short[ImageInfo_short['Metadata_Well'].isin(['D2','D3','D4','D5','D6','D7','D8'])]

# CellCount3 = ImageInfo_short3[['Count_Filtered_Cells', 'Metadata_time']].groupby(['Metadata_time']).sum()
# CellCount3 = CellCount3.reset_index()

##################################################################################################
####################################### Global Values ############################################
##################################################################################################
Metadata_Time_multiplier = 10/60 #10/60 for acquisition by 10 min
plt.rcParams['font.size'] = '30'
plt.rcParams.update({'font.family':'Helvetica'})

##################################################################################################
################## Calculate mean granule count per cell in all fields of view ###################
##################################################################################################

SGcount1_df = CellInfo_short_Time1[['Children_Filtered_SGs_Count', 'Metadata_time']].groupby(['Metadata_time']).mean()
SGcount2_df = CellInfo_short_Time2[['Children_Filtered_SGs_Count', 'Metadata_time']].groupby(['Metadata_time']).mean()
SGcount3_df = CellInfo_short_Time3[['Children_Filtered_SGs_Count', 'Metadata_time']].groupby(['Metadata_time']).mean()

SGcount_df = pd.concat([SGcount1_df, SGcount2_df, SGcount3_df])
SGcount_df = SGcount_df.reset_index()

################################## Extract values from graph ###################################
Rep = [1]*25 + [2]*25 + [3]*25
SGcount_df['Replicate'] = Rep
# Find maximum
SGcountMAX = SGcount_df.groupby(['Replicate']).max()
SGcountMAX = SGcountMAX.reset_index()
SGcountMAX = SGcountMAX[['Replicate', 'Children_Filtered_SGs_Count']]
# Find time to maximum
SGcount_df['Time (hr)'] = (SGcount_df['Metadata_time']) * Metadata_Time_multiplier
SGcount_df['Time (min)'] = (SGcount_df['Time (hr)']) * 60
SGcount_Time2MAX = SGcountMAX.merge(SGcount_df, how="left", on= ['Replicate', 'Children_Filtered_SGs_Count'])
# Find time to minimum
SGcount_disassembly = SGcount_df[SGcount_df['Metadata_time'] > 6]
SGcountMIN = SGcount_disassembly[['Children_Filtered_SGs_Count','Replicate']].groupby(['Replicate']).min()
SGcountMIN = SGcountMIN.reset_index()
SGcount_Time2MIN = SGcountMIN.merge(SGcount_disassembly, how='left', on= ['Replicate', 'Children_Filtered_SGs_Count'])
SGcount_Time2MIN = SGcount_Time2MIN[['Replicate', 'Time (min)']].groupby(['Replicate']).min()
SGcount_Time2MIN = SGcount_Time2MIN.reset_index()
# Find difference between time to max and time to min
SGcount_Time2Disassembly = SGcount_Time2MIN['Time (min)'].subtract(SGcount_Time2MAX['Time (min)'])
#################################################################################################

SGcountMean = SGcount_df.groupby(['Metadata_time']).mean()
SGcountMean.rename(columns={'Children_Filtered_SGs_Count': 'Mean Granule Count per Cell'}, inplace=True)
SGcountMean = SGcountMean.reset_index()
SGcountMean['Time (hr)'] = (SGcountMean['Metadata_time']) * Metadata_Time_multiplier

SGcountSEM = SGcount_df.groupby(['Metadata_time']).sem()
SGcountSEM = SGcountSEM.reset_index()
SGcountSEM.rename(columns={'Children_Filtered_SGs_Count': 'SEM'}, inplace=True)

# plt.figure(figsize=(6.4, 4.8))
plt.figure(1, figsize=(6.4, 4.8))
# plt.plot(SGcount_df['Time (hr)'], SGcount_df['Children_Filtered_SGs_Count'], 'Xg') #Plots individual replicates
# plt.figure(figsize=(10, 6))
plt.errorbar(SGcountMean['Time (hr)'], SGcountMean['Mean Granule Count per Cell'], yerr=SGcountSEM['SEM'], fmt='o--g', capsize=4, capthick=2, linewidth=2, markersize=7)
plt.xlabel('Time (hr)')
plt.ylabel('SG Count per Cell')
plt.ylim(-0.5, 23)
plt.xticks(range(0, 5))

# Save plots and data
SGcount_df.to_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/500/SGcount.csv')
SGcount_Time2MAX.to_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/500/SGcount_Time2MAX.csv')
# SGcount_Time2Disassembly.to_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/500/SGcount_Time2Disassembly.csv')
plt.savefig('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/500/SGCount.pdf', format='pdf', bbox_inches='tight', transparent=True)

##################################################################################################
#################### Calculate granule area per cell in all fields of view #######################
##################################################################################################
# Replicate 1
SGInfo_short_Time1.loc[SGInfo_short_Time1.Parent_Filtered_Cells==0, 'AreaShape_Area'] = 0 # Don't count granules that don't have a cell parent
SGarea1_df = SGInfo_short_Time1[['AreaShape_Area', 'Metadata_time']].groupby(['Metadata_time']).sum()
SGarea1_df = SGarea1_df.reset_index()
SG_AreaCell1 = CellCount1.merge(SGarea1_df, how="left", on= ["Metadata_time"])
SG_AreaCell1['SG_Area_per_Cell'] = SG_AreaCell1['AreaShape_Area']/SG_AreaCell1['Count_Filtered_Cells']
# Replicate 2
SGInfo_short_Time2.loc[SGInfo_short_Time2.Parent_Filtered_Cells==0, 'AreaShape_Area'] = 0 # Don't count granules that don't have a cell parent
SGarea2_df = SGInfo_short_Time2[['AreaShape_Area', 'Metadata_time']].groupby(['Metadata_time']).sum()
SGarea2_df = SGarea2_df.reset_index()
SG_AreaCell2 = CellCount2.merge(SGarea2_df, how="left", on= ["Metadata_time"])
SG_AreaCell2['SG_Area_per_Cell'] = SG_AreaCell2['AreaShape_Area']/SG_AreaCell2['Count_Filtered_Cells']
# Replicate 3
SGInfo_short_Time3.loc[SGInfo_short_Time3.Parent_Filtered_Cells==0, 'AreaShape_Area'] = 0 # Don't count granules that don't have a cell parent
SGarea3_df = SGInfo_short_Time3[['AreaShape_Area', 'Metadata_time']].groupby(['Metadata_time']).sum()
SGarea3_df = SGarea3_df.reset_index()
SG_AreaCell3 = CellCount3.merge(SGarea3_df, how="left", on= ["Metadata_time"])
SG_AreaCell3['SG_Area_per_Cell'] = SG_AreaCell3['AreaShape_Area']/SG_AreaCell3['Count_Filtered_Cells']

SG_AreaCell = pd.concat([SG_AreaCell1[['Metadata_time', 'SG_Area_per_Cell']], SG_AreaCell2[['Metadata_time', 'SG_Area_per_Cell']], SG_AreaCell3[['Metadata_time', 'SG_Area_per_Cell']]])
SG_AreaCell.loc[pd.isna(SG_AreaCell.SG_Area_per_Cell), 'SG_Area_per_Cell'] = 0 # Set all NaN values to 0

################################## Extract values from graph ###################################
Rep = [1]*25 + [2]*25 + [3]*25
SG_AreaCell['Replicate'] = Rep
SGareaMAX = SG_AreaCell.groupby(['Replicate']).max()
SGareaMAX = SGareaMAX.reset_index()
SGareaMAX = SGareaMAX[['Replicate', 'SG_Area_per_Cell']]
SG_AreaCell['Time (hr)'] = (SG_AreaCell['Metadata_time']) * Metadata_Time_multiplier
SG_AreaCell['Time (min)'] = (SG_AreaCell['Time (hr)']) * 60
SGarea_Time2MAX = SGareaMAX.merge(SG_AreaCell, how="left", on= ['Replicate', 'SG_Area_per_Cell'])
# Find time to minimum
SGarea_disassembly = SG_AreaCell[SG_AreaCell['Metadata_time'] > 6]
SGareaMIN = SGarea_disassembly[['SG_Area_per_Cell','Replicate']].groupby(['Replicate']).min()
SGareaMIN = SGareaMIN.reset_index()
SGarea_Time2MIN = SGareaMIN.merge(SGarea_disassembly, how='left', on= ['Replicate', 'SG_Area_per_Cell'])
SGarea_Time2MIN = SGarea_Time2MIN[['Replicate', 'Time (min)']].groupby(['Replicate']).min()
SGarea_Time2MIN = SGarea_Time2MIN.reset_index()
# Find difference between time to max and time to min
SGarea_Time2Disassembly = SGarea_Time2MIN['Time (min)'].subtract(SGarea_Time2MAX['Time (min)'])
#################################################################################################

SG_AreaCell_Mean = SG_AreaCell.groupby(['Metadata_time']).mean()
SG_AreaCell_Mean = SG_AreaCell_Mean.reset_index()
SG_AreaCell_Mean['Time (hr)'] = (SG_AreaCell_Mean['Metadata_time']) * Metadata_Time_multiplier

SG_AreaCell_SEM = SG_AreaCell.groupby(['Metadata_time']).sem()
SG_AreaCell_SEM = SG_AreaCell_SEM .reset_index()
SG_AreaCell_SEM.rename(columns={'SG_Area_per_Cell': 'SEM'}, inplace=True)

# plt.figure(figsize=(6.4, 4.8))
plt.figure(2, figsize=(6.4, 4.8))
plt.errorbar(SG_AreaCell_Mean['Time (hr)'], SG_AreaCell_Mean['SG_Area_per_Cell'], yerr=SG_AreaCell_SEM['SEM'], fmt='o--g', capsize=4, capthick=2, linewidth=2, markersize=7)
plt.xlabel('Time (hr)')
plt.ylabel('SG Area per Cell')
plt.ylim(-30, 800)
plt.xticks(range(0, 5))

# Save plots and data
SG_AreaCell.to_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/500/SGarea.csv')
SGarea_Time2MAX.to_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/500/SGarea_Time2MAX.csv')
# SGarea_Time2Disassembly.to_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/500/SGarea_Time2Disassembly.csv')
plt.savefig('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/500/SGarea.pdf', format='pdf', bbox_inches='tight', transparent=True)

##################################################################################################
################### Calculate % of SG positive cells in all fields of view #######################
##################################################################################################
# Replicate 1
CellInfo_short_Time1['Children_Filtered_SGs_Count > 5'] = CellInfo_short_Time1.Children_Filtered_SGs_Count > 5
SG_CellCount1 = CellInfo_short_Time1[['Children_Filtered_SGs_Count > 5', 'Metadata_time']].groupby(['Metadata_time']).sum()
SG_CellCount1 = SG_CellCount1.reset_index()
SG_Cell1 = CellCount1.merge(SG_CellCount1, how="left", on= ["Metadata_time"])
SG_Cell1['% SG Positive Cells'] = SG_Cell1['Children_Filtered_SGs_Count > 5']/SG_Cell1['Count_Filtered_Cells'] * 100
# Replicate 2
CellInfo_short_Time2['Children_Filtered_SGs_Count > 5'] = CellInfo_short_Time2.Children_Filtered_SGs_Count > 5
SG_CellCount2 = CellInfo_short_Time2[['Children_Filtered_SGs_Count > 5', 'Metadata_time']].groupby(['Metadata_time']).sum()
SG_CellCount2 = SG_CellCount2.reset_index()
SG_Cell2 = CellCount2.merge(SG_CellCount2, how="left", on= ["Metadata_time"])
SG_Cell2['% SG Positive Cells'] = SG_Cell2['Children_Filtered_SGs_Count > 5']/SG_Cell2['Count_Filtered_Cells'] * 100
# Replicate 3
CellInfo_short_Time3['Children_Filtered_SGs_Count > 5'] = CellInfo_short_Time3.Children_Filtered_SGs_Count > 5
SG_CellCount3 = CellInfo_short_Time3[['Children_Filtered_SGs_Count > 5', 'Metadata_time']].groupby(['Metadata_time']).sum()
SG_CellCount3 = SG_CellCount3.reset_index()
SG_Cell3 = CellCount3.merge(SG_CellCount3, how="left", on= ["Metadata_time"])
SG_Cell3['% SG Positive Cells'] = SG_Cell3['Children_Filtered_SGs_Count > 5']/SG_Cell3['Count_Filtered_Cells'] * 100
SG_Cell = pd.concat([SG_Cell1[['Metadata_time', '% SG Positive Cells']], SG_Cell2[['Metadata_time', '% SG Positive Cells']], SG_Cell3[['Metadata_time', '% SG Positive Cells']]])

################################## Extract values from graph ###################################
Rep = [1]*25 + [2]*25 + [3]*25
SG_Cell['Replicate'] = Rep
SG_CellMAX = SG_Cell.groupby(['Replicate']).max()
SG_CellMAX = SG_CellMAX.reset_index()
SG_CellMAX = SG_CellMAX[['Replicate', '% SG Positive Cells']]
SG_Cell['Time (hr)'] = (SG_Cell['Metadata_time']) * Metadata_Time_multiplier
SG_Cell['Time (min)'] = (SG_Cell['Time (hr)']) * 60
SGcell_Time2MAX = SG_CellMAX.merge(SG_Cell, how="left", on= ['Replicate', '% SG Positive Cells'])
# Find time to minimum
SGcell_disassembly = SG_Cell[SG_Cell['Metadata_time'] > 6]
SGcellMIN = SGcell_disassembly[['% SG Positive Cells','Replicate']].groupby(['Replicate']).min()
SGcellMIN = SGcellMIN.reset_index()
SGcell_Time2MIN = SGcellMIN.merge(SGcell_disassembly, how='left', on= ['Replicate', '% SG Positive Cells'])
SGcell_Time2MIN = SGcell_Time2MIN[['Replicate', 'Time (min)']].groupby(['Replicate']).min()
SGcell_Time2MIN = SGcell_Time2MIN.reset_index()
# Find difference between time to max and time to min
SGcell_Time2Disassembly = SGcell_Time2MIN['Time (min)'].subtract(SGcell_Time2MAX['Time (min)'])
#################################################################################################

SG_Cell_Mean = SG_Cell.groupby(['Metadata_time']).mean()
SG_Cell_Mean = SG_Cell_Mean.reset_index()
SG_Cell_Mean['Time (hr)'] = (SG_Cell_Mean['Metadata_time']) * Metadata_Time_multiplier

SG_Cell_SEM = SG_Cell.groupby(['Metadata_time']).sem()
SG_Cell_SEM = SG_Cell_SEM .reset_index()
SG_Cell_SEM.rename(columns={'% SG Positive Cells': 'SEM'}, inplace=True)

# plt.figure(figsize=(6.4, 4.8))
plt.figure(3, figsize=(6.4, 5.2))
plt.errorbar(SG_Cell_Mean['Time (hr)'], SG_Cell_Mean['% SG Positive Cells'], yerr=SG_Cell_SEM['SEM'], fmt='o--g', capsize=4, capthick=2, linewidth=2, markersize=7)
plt.xlabel('Time (hr)')
plt.ylabel('% of SG Positive Cells')
plt.ylim(-3, 95)
plt.xticks(range(0, 5))


# Save plots and data
SG_Cell.to_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/500/SGcell.csv')
SGcell_Time2MAX.to_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/500/SGcell_Time2MAX.csv')
# SGcell_Time2Disassembly.to_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/500/SGcell_Time2Disassembly.csv')
plt.savefig('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/042523/ImageAnalysis/500/SGcell.pdf', format='pdf', bbox_inches='tight', transparent=True)