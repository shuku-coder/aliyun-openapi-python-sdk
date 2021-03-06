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
from aliyunsdkga.endpoint import endpoint_data

class AttachLogStoreToEndpointGroupRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Ga', '2019-11-20', 'AttachLogStoreToEndpointGroup','gaplus')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_ClientToken(self):
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self,ClientToken):
		self.add_query_param('ClientToken',ClientToken)

	def get_SlsLogStoreName(self):
		return self.get_query_params().get('SlsLogStoreName')

	def set_SlsLogStoreName(self,SlsLogStoreName):
		self.add_query_param('SlsLogStoreName',SlsLogStoreName)

	def get_ListenerId(self):
		return self.get_query_params().get('ListenerId')

	def set_ListenerId(self,ListenerId):
		self.add_query_param('ListenerId',ListenerId)

	def get_EndpointGroupIdss(self):
		return self.get_query_params().get('EndpointGroupIds')

	def set_EndpointGroupIdss(self, EndpointGroupIdss):
		for depth1 in range(len(EndpointGroupIdss)):
			if EndpointGroupIdss[depth1] is not None:
				self.add_query_param('EndpointGroupIds.' + str(depth1 + 1) , EndpointGroupIdss[depth1])

	def get_SlsProjectName(self):
		return self.get_query_params().get('SlsProjectName')

	def set_SlsProjectName(self,SlsProjectName):
		self.add_query_param('SlsProjectName',SlsProjectName)

	def get_SlsRegionId(self):
		return self.get_query_params().get('SlsRegionId')

	def set_SlsRegionId(self,SlsRegionId):
		self.add_query_param('SlsRegionId',SlsRegionId)

	def get_AcceleratorId(self):
		return self.get_query_params().get('AcceleratorId')

	def set_AcceleratorId(self,AcceleratorId):
		self.add_query_param('AcceleratorId',AcceleratorId)