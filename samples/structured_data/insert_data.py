import st_library.dataprovider.structured_data as stdata
import st_library.dataprovider as datapv

st_lib = datapv.Library()
st_lib.set_token('Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4MTIyYTNkMy1lZmQ2LTQwMjYtOGVlZi04MzMzNmJlNmFkNzciLCJhdWQiOiJ3ZWJfYXBwIiwiY29tcGFueUlkIjoidGVzdF9zaG9ydGVzdHRyYWNrX2Z1bmN0aW9uYWxpdHkiLCJzY29wZSI6WyJvcGVuaWQiXSwiaXNzIjoic2hvcnRlc3R0cmFjay11YWEiLCJleHAiOjE1MTgyMTk3OTcsImlhdCI6MTUxNzkxOTc5NywiYXV0aG9yaXRpZXMiOlsiUk9MRV9DT01QQU5ZX0FETUlOIl0sImp0aSI6IjgyZWFjN2YxLTJkOTUtNDEyZS05YTQ2LThmZjcxOGNmZWI4ZCIsImVtYWlsIjoicHVibGljLWFkbWluQGxvY2FsaG9zdCIsImNsaWVudF9pZCI6IndlYl9hcHAifQ.liY4zrdaypJHZX6786v7wrCKY8Xvx_oa8sECMkacjD4_VmU7CVMIqTnNyVhGH9tkK7THFcSl7TRk8NiAvGxPSaIBhCBT9ajlHIYYYByB25KBEQxyj7fZNng5HD8KAD7oUyjtlwz3XI3Scv_pT3_Z9g7MjbUwCIfFA2XNl1tXUZKIUadD_B_UhKtPNAyYxP4KJhePjzlPfkbjVVA-uiPEP9bhhoBbjsa_ukXzFDXOejUPproAwSsapPo6BJ1rzbsUQCxHJO5UwAK6ySaU14RuAp63KIpolzoUJllYvSHs2mhN1fzMcr7vZ3BVpBRS79g-mZ0it9zAE0oqpE_uof2txw')
st_lib.set_configuration_uuid('52db99d3-edfb-44c5-b97a-f09df4402081')

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
      "int64_field_0": "1177"
    }
    }
  ]
}
print (tbl.insert_data(json_data))
