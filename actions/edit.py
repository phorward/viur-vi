import html5
from network import NetworkService
from priorityqueue import actionDelegateSelector
from widgets.edit import EditWidget
from config import conf
from pane import Pane
from i18n import translate

class SaveContinue( html5.ext.Button ):
	def __init__(self, *args, **kwargs):
		super( SaveContinue, self ).__init__( translate("Save-Continue"), *args, **kwargs )
		self["class"] = "btn btn-save-continue"

	@staticmethod
	def isSuitableFor( modul, handler, actionName ):
		return( actionName=="save.continue" )

	def onClick(self, sender=None):
		self["class"].append("is-loading")
		self.parent().parent().doSave(closeOnSuccess=False)

	def resetLoadingState(self):
		if "is-loading" in self["class"]:
			self["class"].remove("is-loading")

actionDelegateSelector.insert( 1, SaveContinue.isSuitableFor, SaveContinue )

class SaveSingleton(html5.ext.Button):
	def __init__(self, *args, **kwargs):
		super(SaveSingleton, self).__init__(translate("Save"), *args, **kwargs)
		self["class"] = "btn btn-save-close"

	@staticmethod
	def isSuitableFor(module, handler, actionName):
		return actionName == "save.singleton" and module != "_tasks"

	def onClick(self, sender=None):
		self["class"].append("is-loading")
		self.parent().parent().doSave(closeOnSuccess=False)

	def resetLoadingState(self):
		if "is-loading" in self["class"]:
			self["class"].remove("is-loading")

actionDelegateSelector.insert(1, SaveSingleton.isSuitableFor, SaveSingleton)

class ExecuteSingleton(html5.ext.Button):
	def __init__(self, *args, **kwargs):
		super(ExecuteSingleton, self).__init__(translate("Execute"), *args, **kwargs)
		self["class"] = "btn btn-save-close"

	@staticmethod
	def isSuitableFor(module, handler, actionName):
		return actionName == "save.singleton" and module == "_tasks"

	def onClick(self, sender=None):
		self["class"].append("is-loading")
		self.parent().parent().doSave(closeOnSuccess=True)

	def resetLoadingState(self):
		if "is-loading" in self["class"]:
			self["class"].remove("is-loading")

actionDelegateSelector.insert(1, ExecuteSingleton.isSuitableFor, ExecuteSingleton)

class SaveClose( html5.ext.Button ):
	def __init__(self, *args, **kwargs):
		super( SaveClose, self ).__init__( translate("Save-Close"), *args, **kwargs )
		self["class"] = "btn btn-save-close"

	@staticmethod
	def isSuitableFor( modul, handler, actionName ):
		return( actionName=="save.close" )

	def onClick(self, sender=None):
		self["class"].append("is-loading")
		self.parent().parent().doSave(closeOnSuccess=True)

	def resetLoadingState(self):
		if "is-loading" in self["class"]:
			self["class"].remove("is-loading")
		pass

actionDelegateSelector.insert( 1, SaveClose.isSuitableFor, SaveClose )

