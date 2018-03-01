import st_library.core.dataprovider.structured_data as stdata
from st_library import Library

st_lib = Library()
st_lib.set_token('Bearer token')
st_lib.set_config_id('98a599e9-e5b8-49fc-b5ca-0750bb0a785b')

tbl = stdata.Table(datasetsid="62a9058c_07e8_4c61_8da0_0f822952447e", name="NewTableForXing")

print (tbl.insert_batch_sec_data("../data/structured_data/","data.csv"))
