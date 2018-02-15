import st_library.dataprovider as datapv
import st_library.dataprovider.structured_data as stdata

st_lib = datapv.Library()
st_lib.set_token('Bearer token')
st_lib.set_configuration_uuid('52db99d3-edfb-44c5-b97a-f09df4402081')

tbl = stdata.Table("edac25ec-25e3-4949-9f49-d42124c26bf2", "52db99d3-edfb-44c5-b97a-f09df4402081", "bbb")
print (tbl.upload_data(r"data.csv"))
