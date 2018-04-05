from st_library import Library

st_lib = Library()
st_lib.set_token('token')
st_lib.set_config_id('52db99d3-edfb-44c5-b97a-f09df4402081')

tbl = st_lib.struct_data.Table("edac25ec-25e3-4949-9f49-d42124c26bf2", "52db99d3-edfb-44c5-b97a-f09df4402081", "bbb")
print (tbl.upload_data(r"../data/structured_data/data.csv"))
