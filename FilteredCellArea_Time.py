#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 11:37:40 2023

@author: angela_gao
"""

import pandas as pd
import matplotlib.pyplot as plt

##################################################################################################
####################################### DATA INPUT ###############################################
##################################################################################################

# Replicate 1 data input
Image_Info1 = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/050622/ImageAnalysis/Pipeline_04_29_22/GranuleInfo/Replicate1/Image.csv')
ImageInfo_short1 = Image_Info1[['Metadata_time','Metadata_Position', 'Mean_Filtered_Cells_AreaShape_Area']]
ImageInfo_short1 = ImageInfo_short1[ImageInfo_short1['Metadata_Position'].isin([7,8])]

# Replicate 2 data input
Image_Info2 = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/050622/ImageAnalysis/Pipeline_04_29_22/GranuleInfo/Replicate2/Image.csv')
ImageInfo_short2 = Image_Info2[['Metadata_time','Metadata_Position', 'Mean_Filtered_Cells_AreaShape_Area']]
ImageInfo_short2 = ImageInfo_short2[ImageInfo_short2['Metadata_Position'].isin([25,26])]

# Replicate 3 data input
Image_Info3 = pd.read_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/050622/ImageAnalysis/Pipeline_04_29_22/GranuleInfo/Replicate3/Image.csv')
ImageInfo_short3 = Image_Info3[['Metadata_time','Metadata_Position', 'Mean_Filtered_Cells_AreaShape_Area']]
ImageInfo_short3 = ImageInfo_short3[ImageInfo_short3['Metadata_Position'].isin([43,44])]


##################################################################################################
####################################### Global Values ############################################
##################################################################################################
Metadata_Time_multiplier = 10/60 #10/60 for acquisition by 10 min
plt.rcParams['font.size'] = '30'
plt.rcParams.update({'font.family':'Helvetica'})
# plt.rcParams["figure.figsize"] = (8,4.8)

# plt.rcParams.update({'figure.autolayout': True})

##################################################################################################
###################### Plot cell area wrp to the initial cell area ###############################
##################################################################################################

# Get initial cell area
InitCellArea1 = ImageInfo_short1.loc[ImageInfo_short1.Metadata_time==0, ['Mean_Filtered_Cells_AreaShape_Area','Metadata_Position']]
InitCellArea1.rename(columns = {'Mean_Filtered_Cells_AreaShape_Area':'Initial_FilteredCellArea'}, inplace = True)
InitCellArea2 = ImageInfo_short2.loc[ImageInfo_short2.Metadata_time==0, ['Mean_Filtered_Cells_AreaShape_Area','Metadata_Position']]
InitCellArea2.rename(columns = {'Mean_Filtered_Cells_AreaShape_Area':'Initial_FilteredCellArea'}, inplace = True)
InitCellArea3 = ImageInfo_short3.loc[ImageInfo_short3.Metadata_time==0, ['Mean_Filtered_Cells_AreaShape_Area','Metadata_Position']]
InitCellArea3.rename(columns = {'Mean_Filtered_Cells_AreaShape_Area':'Initial_FilteredCellArea'}, inplace = True)

# Find the mean of all initial cell area
InitCellArea = pd.concat([InitCellArea1[['Initial_FilteredCellArea']], InitCellArea2[['Initial_FilteredCellArea']], InitCellArea3[['Initial_FilteredCellArea']]])
InitCellArea = InitCellArea['Initial_FilteredCellArea'].mean()

# Merge inital cell area with other area data
CellArea1 = ImageInfo_short1.merge(InitCellArea1, how="left", on= ["Metadata_Position"])
CellArea2 = ImageInfo_short2.merge(InitCellArea2, how="left", on= ["Metadata_Position"])
CellArea3 = ImageInfo_short3.merge(InitCellArea3, how="left", on= ["Metadata_Position"])

# Calculate ratio of cell area and initial cell area
CellArea1['Area_Ratio'] = CellArea1.Mean_Filtered_Cells_AreaShape_Area/CellArea1.Initial_FilteredCellArea
CellArea2['Area_Ratio'] = CellArea2.Mean_Filtered_Cells_AreaShape_Area/CellArea2.Initial_FilteredCellArea
CellArea3['Area_Ratio'] = CellArea3.Mean_Filtered_Cells_AreaShape_Area/CellArea3.Initial_FilteredCellArea

# CellArea1 = ImageInfo_short1
# CellArea2 = ImageInfo_short2
# CellArea3 = ImageInfo_short3
# CellArea1['Area_Ratio'] = CellArea1.Mean_Filtered_Cells_AreaShape_Area/InitCellArea
# CellArea2['Area_Ratio'] = CellArea2.Mean_Filtered_Cells_AreaShape_Area/InitCellArea
# CellArea3['Area_Ratio'] = CellArea3.Mean_Filtered_Cells_AreaShape_Area/InitCellArea

# Calculate mean of all fields of view within each replicate
CellAreaRatio1 = CellArea1[['Area_Ratio', 'Metadata_time']].groupby(['Metadata_time']).mean()
CellAreaRatio1 = CellAreaRatio1.reset_index()
CellAreaRatio2 = CellArea2[['Area_Ratio', 'Metadata_time']].groupby(['Metadata_time']).mean()
CellAreaRatio2 = CellAreaRatio2.reset_index()
CellAreaRatio3 = CellArea3[['Area_Ratio', 'Metadata_time']].groupby(['Metadata_time']).mean()
CellAreaRatio3 = CellAreaRatio3.reset_index()

CellAreaRatio = pd.concat([CellAreaRatio1[['Metadata_time', 'Area_Ratio']], CellAreaRatio2[['Metadata_time', 'Area_Ratio']], CellAreaRatio3[['Metadata_time', 'Area_Ratio']]])
CellAreaRatio_Mean = CellAreaRatio.groupby(['Metadata_time']).mean()
CellAreaRatio_Mean = CellAreaRatio_Mean.reset_index()
CellAreaRatio_Mean['Time (hr)'] = (CellAreaRatio_Mean['Metadata_time']) * Metadata_Time_multiplier

CellAreaRatio_SEM = CellAreaRatio.groupby(['Metadata_time']).sem()
CellAreaRatio_SEM = CellAreaRatio_SEM .reset_index()
CellAreaRatio_SEM.rename(columns={'Area_Ratio': 'SEM'}, inplace=True)

plt.figure(1, figsize=(6.4,4.8)) # Default: 6.4 by 4.8
plt.errorbar(CellAreaRatio_Mean['Time (hr)'], CellAreaRatio_Mean['Area_Ratio'], yerr=CellAreaRatio_SEM['SEM'], fmt='o--y', capsize=4, capthick=2, linewidth=2, markersize=7)
'''set color to dark grey'''
plt.xlabel('Time (hr)')
plt.ylabel('Normalized Cell Area')
plt.ylim(0, 1.5)
plt.xticks(range(0, 6))
# plt.tight_layout()
# plt.show()


# Find time when ratio is less than 0.4
Runtime = 5 # hr
TimePerImage = 10 # min
NumberofImagesPerRep = Runtime * 60 / TimePerImage + 1 # 31
'''change numberofimagesperrep to integer'''
NumberofImagesPerRep = int(NumberofImagesPerRep)
Rep = [1]*NumberofImagesPerRep + [2]*NumberofImagesPerRep + [3]*NumberofImagesPerRep
CellAreaRatio['Replicate'] = Rep
CellAreaRatioLOW = CellAreaRatio.loc[CellAreaRatio.Area_Ratio < 0.4, ['Metadata_time', 'Area_Ratio', 'Replicate']]
Time2CellAreaRatioLOW = CellAreaRatioLOW[['Metadata_time', 'Replicate']].groupby(['Replicate']).min()
Time2CellAreaRatioLOW = Time2CellAreaRatioLOW.reset_index()
Time2CellAreaRatioLOW['Time (min)'] = Time2CellAreaRatioLOW['Metadata_time'] * Metadata_Time_multiplier * 60

# Save plots and data
CellAreaRatio.to_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/050622/ImageAnalysis/150/CellAreaRatio.csv')
Time2CellAreaRatioLOW.to_csv('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/050622/ImageAnalysis/150/Time2CellAreaRatioLOW.csv')
plt.savefig('/Volumes/AGHardDrive/Angela Gao - Floor Lab/Stress Granule Project/TorstenConfocalMicroscopy/050622/ImageAnalysis/150/CellAreaRatio.pdf', format='pdf', bbox_inches='tight', transparent=True)