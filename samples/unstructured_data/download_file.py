from st_library import Library

st_lib = Library()
st_lib.set_token('token')
st_lib.set_config_id('52db99d3-edfb-44c5-b97a-f09df4402081')
print(st_lib.unstruct_data.download_file("19a29b9b-bea2-40fb-89c4-555bba829539","image.jpg"))
