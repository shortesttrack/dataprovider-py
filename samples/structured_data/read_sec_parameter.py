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
st_lib.set_token('Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4MTIyYTNkMy1lZmQ2LTQwMjYtOGVlZi04MzMzNmJlNmFkNzciLCJhdWQiOiJ3ZWJfYXBwIiwiY29tcGFueUlkIjoidGVzdF9zaG9ydGVzdHRyYWNrX2Z1bmN0aW9uYWxpdHkiLCJzY29wZSI6WyJvcGVuaWQiXSwiaXNzIjoic2hvcnRlc3R0cmFjay11YWEiLCJleHAiOjE1MTg3ODg1MTMsImlhdCI6MTUxODQ4ODUxMywiYXV0aG9yaXRpZXMiOlsiUk9MRV9DT01QQU5ZX0FETUlOIl0sImp0aSI6IjUzYmNiNmQ5LTMwZWQtNDE2ZS04ZGFhLWE4NTA3NDE2MmJjYSIsImVtYWlsIjoicHVibGljLWFkbWluQGxvY2FsaG9zdCIsImNsaWVudF9pZCI6IndlYl9hcHAifQ.FxvCWd-D8LcEsZrRzTI5OqhyZAJbw7VQpNkOJLOebMkc9cIlkcC4Ucr5KsDAXqDfmA52I5jp6dOziXlVGOPKAv6GDZ0lFb107srdQKxbvUCaC_H31wPmQUxnuOSpLkwD6HdAClrAZriWRsOd6wxOFaRJqBavq_v3G5lP_NkA23UK_DU76clVQ80AockOdb8Xq5BPiloZl9BGH7UR_N9XPdLg0JwxrGkWzUZpjFf4Eq2lhQ2_RpJKhxLMedZt8YwPOPMDuDxe9zLIftJ12Q4p6QqXGomgDKspR4IaO309qRaHhR81DezWyHTToS0xXk3EeE4GkKqtP9qU4HVrBsjqtA')

df = st_lib.getParameter("b11c26ec-893e-445c-a5e7-b74f99444e0c")
print (df)