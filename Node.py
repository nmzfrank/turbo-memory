class Node():
	def __init__(self,thershold=0,activeState=0,inlist=None):  
		self.thershold = thershold
		self.inlist = inlist
		self.activeState = activeState

	def addLink(self,link):
		self.inlist.append(link)

	def frontTrans(self):
		for link in inlist:
			value += link.weight * link.start.activeState
		if value > thershold:
			activeState = 1
		else:
			activeState = 0

