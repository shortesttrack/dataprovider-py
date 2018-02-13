# Copyright 2017 Shortest Track Company. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.

import st_library.dataprovider as datapv
st_lib = datapv.Library()
st_lib.set_token('Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4MTIyYTNkMy1lZmQ2LTQwMjYtOGVlZi04MzMzNmJlNmFkNzciLCJhdWQiOiJ3ZWJfYXBwIiwiY29tcGFueUlkIjoidGVzdF9zaG9ydGVzdHRyYWNrX2Z1bmN0aW9uYWxpdHkiLCJzY29wZSI6WyJvcGVuaWQiXSwiaXNzIjoic2hvcnRlc3R0cmFjay11YWEiLCJleHAiOjE1MTgyMTk3OTcsImlhdCI6MTUxNzkxOTc5NywiYXV0aG9yaXRpZXMiOlsiUk9MRV9DT01QQU5ZX0FETUlOIl0sImp0aSI6IjgyZWFjN2YxLTJkOTUtNDEyZS05YTQ2LThmZjcxOGNmZWI4ZCIsImVtYWlsIjoicHVibGljLWFkbWluQGxvY2FsaG9zdCIsImNsaWVudF9pZCI6IndlYl9hcHAifQ.liY4zrdaypJHZX6786v7wrCKY8Xvx_oa8sECMkacjD4_VmU7CVMIqTnNyVhGH9tkK7THFcSl7TRk8NiAvGxPSaIBhCBT9ajlHIYYYByB25KBEQxyj7fZNng5HD8KAD7oUyjtlwz3XI3Scv_pT3_Z9g7MjbUwCIfFA2XNl1tXUZKIUadD_B_UhKtPNAyYxP4KJhePjzlPfkbjVVA-uiPEP9bhhoBbjsa_ukXzFDXOejUPproAwSsapPo6BJ1rzbsUQCxHJO5UwAK6ySaU14RuAp63KIpolzoUJllYvSHs2mhN1fzMcr7vZ3BVpBRS79g-mZ0it9zAE0oqpE_uof2txw')
st_lib.set_configuration_uuid('52db99d3-edfb-44c5-b97a-f09df4402081')

df = st_lib.read_matrix("716f0214-3b74-4937-8454-9e226643d35f", "066375bc-21dc-4d8a-90e1-92d967b40411", "MatrixA")
print (df)