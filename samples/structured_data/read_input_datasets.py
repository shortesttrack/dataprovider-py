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
st_lib.set_token('Bearer token')
st_lib.set_configuration_uuid('52db99d3-edfb-44c5-b97a-f09df4402081')

df = st_lib.read_matrix("716f0214-3b74-4937-8454-9e226643d35f", "066375bc-21dc-4d8a-90e1-92d967b40411", "MatrixA")
print (df)