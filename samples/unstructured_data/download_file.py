import st_library.dataprovider as datapv

st_lib = datapv.Library()
st_lib.set_token('Bearer token')
st_lib.set_configuration_uuid('52db99d3-edfb-44c5-b97a-f09df4402081')
print(st_lib.download_file("19a29b9b-bea2-40fb-89c4-555bba829539","image.jpg"))
