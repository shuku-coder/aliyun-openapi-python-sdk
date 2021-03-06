# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkscsp.endpoint import endpoint_data

class ExecuteActivityRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'scsp', '2020-07-02', 'ExecuteActivity')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ClientToken(self): # String
		return self.get_body_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_body_params('ClientToken', ClientToken)
	def get_InstanceId(self): # String
		return self.get_body_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_body_params('InstanceId', InstanceId)
	def get_TicketId(self): # Long
		return self.get_body_params().get('TicketId')

	def set_TicketId(self, TicketId):  # Long
		self.add_body_params('TicketId', TicketId)
	def get_OperatorId(self): # Long
		return self.get_body_params().get('OperatorId')

	def set_OperatorId(self, OperatorId):  # Long
		self.add_body_params('OperatorId', OperatorId)
	def get_ActivityCode(self): # String
		return self.get_body_params().get('ActivityCode')

	def set_ActivityCode(self, ActivityCode):  # String
		self.add_body_params('ActivityCode', ActivityCode)
	def get_ActivityForm(self): # String
		return self.get_body_params().get('ActivityForm')

	def set_ActivityForm(self, ActivityForm):  # String
		self.add_body_params('ActivityForm', ActivityForm)
