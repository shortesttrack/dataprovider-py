import st_library.dataprovider as datapv

st_lib = datapv.Library()
st_lib.set_token('Bearer token')
st_lib.set_configuration_uuid('52db99d3-edfb-44c5-b97a-f09df4402081')
print(st_lib.delete_file("d9a5b3f1-7709-485b-b7e6-91ed80e2e30b","datafile.txt"))
