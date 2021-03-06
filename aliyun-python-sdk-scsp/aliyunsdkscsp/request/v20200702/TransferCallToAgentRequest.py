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

class TransferCallToAgentRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'scsp', '2020-07-02', 'TransferCallToAgent')
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
	def get_AccountName(self): # String
		return self.get_body_params().get('AccountName')

	def set_AccountName(self, AccountName):  # String
		self.add_body_params('AccountName', AccountName)
	def get_TargetAccountName(self): # String
		return self.get_body_params().get('TargetAccountName')

	def set_TargetAccountName(self, TargetAccountName):  # String
		self.add_body_params('TargetAccountName', TargetAccountName)
	def get_CallId(self): # String
		return self.get_body_params().get('CallId')

	def set_CallId(self, CallId):  # String
		self.add_body_params('CallId', CallId)
	def get_JobId(self): # String
		return self.get_body_params().get('JobId')

	def set_JobId(self, JobId):  # String
		self.add_body_params('JobId', JobId)
	def get_ConnectionId(self): # String
		return self.get_body_params().get('ConnectionId')

	def set_ConnectionId(self, ConnectionId):  # String
		self.add_body_params('ConnectionId', ConnectionId)
	def get_HoldConnectionId(self): # String
		return self.get_body_params().get('HoldConnectionId')

	def set_HoldConnectionId(self, HoldConnectionId):  # String
		self.add_body_params('HoldConnectionId', HoldConnectionId)
	def get_Type(self): # Integer
		return self.get_body_params().get('Type')

	def set_Type(self, Type):  # Integer
		self.add_body_params('Type', Type)
	def get_IsSingleTransfer(self): # String
		return self.get_body_params().get('IsSingleTransfer')

	def set_IsSingleTransfer(self, IsSingleTransfer):  # String
		self.add_body_params('IsSingleTransfer', IsSingleTransfer)
