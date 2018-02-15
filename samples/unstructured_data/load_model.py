import st_library.dataprovider as datapv

st_lib = datapv.Library()
st_lib.set_token('Bearer token')
print(st_lib.download_file("19a29b9b-bea2-40fb-89c4-555bba829539","RandomForest_train.rds"))
