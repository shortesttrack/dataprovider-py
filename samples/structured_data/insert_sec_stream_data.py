import st_library.dataprovider.structured_data as stdata
import st_library.dataprovider as datapv

st_lib = datapv.Library()
st_lib.set_token('Bearer token')
st_lib.set_configuration_uuid('98a599e9-e5b8-49fc-b5ca-0750bb0a785b')

tbl = stdata.Table(datasetsid="62a9058c_07e8_4c61_8da0_0f822952447e", name="NewTableForXing")
json_data = {
  "ignoreUnknownValues": 'true',
  "skipInvalidRows": 'true',
  "rows": [
    {
    "json": {
      "string_field_0": "333333333333333"
    }
    },
    {
    "json": {
      "string_field_0": "444444444444444"
    }
    }
  ]
}
print (tbl.insert_sec_data(json_data))
