from tdc.single_pred import ADME
data = ADME(name = 'HIA_Hou')
# split into train/val/test with scaffold split methods
split = data.get_split(method = 'scaffold')
# get the entire data in the various formats
data.get_data(format = 'df')


