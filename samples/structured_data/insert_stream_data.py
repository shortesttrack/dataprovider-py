import st_library.core.dataprovider.structured_data as stdata
from st_library import Library

st_lib = Library()
st_lib.set_token('Bearer token')
st_lib.set_config_id('52db99d3-edfb-44c5-b97a-f09df4402081')

tbl = stdata.Table(datasetsid="9c6db384-93a0-467e-b767-10689e2b07f7", name="customerdsmatrix")
json_data = {
  "ignoreUnknownValues": 'true',
  "skipInvalidRows": 'true',
  "rows": [
    {
    "insertId": "1377f298-6e67-4c94-8568-69a260268ce4",
    "json": {
      "int64_field_0": "1122"
    }
    },
    {"insertId": "1377f298-6e67-4c94-8568-69a260268ce5",
    "json": {
      "int64_field_0": "1166"
    }
    },
    {
      "insertId": "1377f298-6e67-4c94-8568-69a260268ce4",
    "json": {
      "int64_field_0": "00000"
    }
    }
  ]
}
print (tbl.insert_data(json_data))
