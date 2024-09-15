# Copyright (c) 2024, PT Sopwer Teknologi Indonesia and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from gemini.services import GeminiService

class GeminiAccount(Document):
	def send_prompt(self, content):
		gemini_service = GeminiService(self.project_number, self.project_name, self.api_key)
		response = gemini_service.send_prompt(content)
		return response
