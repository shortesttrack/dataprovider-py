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

from st_library import Library

st_lib = Library()
st_lib.set_token('Bearer token')
st_lib.set_config_id('b11c26ec-893e-445c-a5e7-b74f99444e0c')

df = st_lib.struct_data.get_parameter()
print (df)
