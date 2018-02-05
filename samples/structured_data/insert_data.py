from st_library.structured_data import Table

from st_library import Library
st_lib = Library()
st_lib.set_token('Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI4MTIyYTNkMy1lZmQ2LTQwMjYtOGVlZi04MzMzNmJlNmFkNzciLCJpc3MiOiJzaG9ydGVzdHRyYWNrLXVhYSIsImF1dGhvcml0aWVzIjpbIlJPTEVfQ09NUEFOWV9BRE1JTiJdLCJkamFuZ29Vc2VySWQiOiI5OTkiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwiYXVkIjoid2ViX2FwcCIsImNvbXBhbnlJZCI6InRlc3Rfc2hvcnRlc3R0cmFja19mdW5jdGlvbmFsaXR5IiwiZGphbmdvVG9rZW4iOiI5NjUxYmQzZGJiZWExZDQ5YjM1MzhjZjRjMDU1MWMzODhiOGVlNzZlIiwic2NvcGUiOlsib3BlbmlkIl0sImV4cCI6MTUxNzg0MDkyMSwiaWF0IjoxNTE3NTQwOTIxLCJqdGkiOiJhOGUxODM5Yi03M2JkLTRkM2YtODQzMi01NWY5NDZlNWM0ZGUiLCJlbWFpbCI6InB1YmxpYy1hZG1pbkBsb2NhbGhvc3QifQ.JAxiSYU2MsXY-S-oYGXNJCbvfLjzGgJslfv7c3NsOkCI56evluQ42asHsYqJ1uX0gXpcd1N43LVpyI3-o4rEtk6rsZnRw1fca6SY0gcwlXW2aumI7SejkllGke_obHGwfBqNJKSj-JiMvukVDcQAuI2Vuz4PxBqP1dlhzxt88cmcsLRPdicGnD8LpTkA35D8qjdzGXJPCvGFhaREVuVaHU0PZJBFWBmMNJKEZXnZRnW8vZ8W-FFLVZnofRjbQtU3Czj7KGQWKdRBoMy3uub4XTej1CQ2zFNJYijXrDIWkXOqQJRY0QNSsOZki3EwVC0e2du6NPPhTSs9mgVRjfcMUw')
st_lib.set_configuration_uuid('52db99d3-edfb-44c5-b97a-f09df4402081')

tbl = Table(datasetsid="9c6db384-93a0-467e-b767-10689e2b07f7", name="customerdsmatrix")
json_data = {
  "ignoreUnknownValues": 'true',
  "skipInvalidRows": 'true',
  "rows": [
    {
    "insertId": "1377f298-6e67-4c94-8568-69a260268ce4",
    "json": {
      "int64_field_0": "22"
    }
    },
    {"insertId": "1377f298-6e67-4c94-8568-69a260268ce5",
    "json": {
      "int64_field_0": "66"
    }
    },
    {
      "insertId": "1377f298-6e67-4c94-8568-69a260268ce4",
    "json": {
      "int64_field_0": "55"
    }
    }
  ]
}
print (tbl.insert_data(json_data))
