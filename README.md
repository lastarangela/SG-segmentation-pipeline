# SG-segmentation-pipeline
This image segmentation pipeline identifies individual stress granules and cells in 16-bit tiff images and outputs total pixel intensity and count of stress granule and cell in csv files.

### SGID_pipeline_40x_051823.cppipe
Input: Images taken with Nikion Eclipse Ti spinning disc confocal microscope, 40X air objective  
Output: number of filtered SGs per filtered cell, area of each filtered SG, parent filtered cell of each SG, number of filtered cells in each image, metadata_time, metadata_position

### SGdata_analysis.py
Input: Filtered_Cell.csv, Filtered_SGs.csv, Image.csv  
Output: SG count per cell (figure), SG area per cell (figure), % of SG-positive cell (figure)  
        In each image, extract maximum value, time to maximum value, and time to disassembly  
Definitions:
SG count per cell: three replicates of mean filtered SG count per filtered cell  
SG area per cell: three replicates of total area of all filtered SGs that have a filtered cell parent divided by count of total filtered cells  
% of SG-positive cells: three replicates of the count of filtered cells with more than 5 filtered SGs divided by count of total filtered cells times 100%  
maximum value: the maximum of each quantified value in each replicate  
time to maximum value: the minimum amount of time to reach maximum of each quantified value in each replicate  
time to disassembly: the minimum amount of time to reach minimum of each quantified value beyound 1 hr - time to maximum value  

### FilteredCellArea_Time.py
Input: Image.csv  
Output: Normalized cell area (figure), Time to cell area ratio < 0.4  

Definitions:   
Normalized cell area: mean filtered cell area divided by mean filtered cell area at time 0  
Time to cell area ratio < 0: for each treatment condition, find minimum time to area ratio < 0.4  
