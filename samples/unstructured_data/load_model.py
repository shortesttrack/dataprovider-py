from st_library import Library

st_lib = Library()
st_lib.set_token('Bearer token')
print(st_lib.unstruct_data.download_file("19a29b9b-bea2-40fb-89c4-555bba829539","RandomForest_train.rds"))
