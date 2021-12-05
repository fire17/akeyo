#AkeyOverse.py
from xo import *
import shortuuid
akeyo = xo.akeyo

class Entity(dict):
	empty = None
	def save(self, *args, **kwargs):
		# return self.saveAsyn(None)
		t1 = Thread(target = self.saveAsyn, kwargs= kwargs)
		t1.start()

	def saveAsyn(self, **kwargs):
		if "delay" in kwargs:
			time.sleep(kwargs["delay"])
		# print("TYPE ::: ",type(self))
		recent = self._recentSave
		self._recentSave += 1
		recent += 1

		# etype = str(type(self))
		if self["id"][0] not in akeyo.index.children():
			akeyo.index[self["id"][0]] = []
		akeyo.index[self["id"][0]] += self["id"]
		akeyo.index[self["id"]] = self
		print(f"SAVED {self['id']}")

		if False:
			# print()
			# print("self.__dir__()")
			# for key in self.__dir__():
			# 	print(key)
			# print()
			# print("type(self).__dir__()")
			# for key in type(self).__dir__(""):
			# 	print(key)
			# print()
			# print("type(self).__dir__(Entity)")
			# for key in type(self).__dir__(Entity):
			# 	print(key)
			try:
			# if True:
				for key in self.__dir__():
					# if True:
					if recent == self._recentSave:
						if key not in Entity.empty.__dir__() and "_" not in key:
							atr = self.__getattribute__(key)
							if "method" not in str(type(atr)):
								print(f"SAVING {self._recentSave} {str(type(atr))}::: akeyo.index[{self['id']}][{key}]")
								akeyo.index[self["id"]][key].set(self.__getattribute__(key))

			except:
				pass
			# 	print(f"stopping save {recent}")
			try:
			# if True:
				for key in self:
					# if True:
					if recent == self._recentSave:
						atr = self[key]
						if "method" not in str(type(atr)):
							print(f"SAVING  {self._recentSave} {str(type(atr))}::: akeyo.index[{self['id']}][{key}]")
							akeyo.index[self["id"]][key].set(self[key])
			except:
				pass
			# 	print(f"stopping save {recent}")

	def math(*args, **kwargs):
		print("got argumets:")
		for arg in args:
			print(":::",arg,":::",type(arg))
		for arg in kwargs:
			print(":::",arg,":::",kwargs[arg],":::",type(kwargs[arg]))
		print(args)

	math(1,3,"adgo", do = "multiply")

	def __init__(self,*args,**kwargs):
		self._recentSave = 0
		if Entity.empty is None:
			Entity.empty = "xxxxxxx"
			Entity.empty = Entity(__empty__ = True)
		if "__empty__" not in kwargs:
			if "_known_" in kwargs:
				known = kwargs.pop("_known_")
				firstArgs, lastArgs = args[:len(known)],args[len(known):]
				c = 0
				for a in known:
					kwargs[a] = firstArgs[c]
					c+=1
				args = lastArgs

			etype = str(type(self)).split(".")[-1].split("'")[0]
			print("Created Entity "+etype+f", {args}, {kwargs}")
			eid = etype[0] +"-"+ str(shortuuid.uuid())
			kwargs["id"] = eid
			kwargs["created"] = datetime.now() #datetime.now().timestamp() == time.time()
			c = 0
			for a in args:
				kwargs["id_"+str(c)] = a
				c+=1
			for a in kwargs:
				self[a] = kwargs[a]
			print()
			self.save()
			if etype[0] in ["D"]:
				akeyo.manager.new = eid
				# manager.trigger(eid)

class User(Entity):
	personas = dict()
	def __init__(self,*args,**kwargs):
		kwargs["type"] = type(self)
		super().__init__(*args,**kwargs)
		self.personas = dict()
		self["personas"] = []
		self["currentPersona"] = ""
		alpha  = self.newPersona(Alpha(*args,**kwargs))
		omega  = self.newPersona(Omega(*args,**kwargs))


	def msg(self, *args,**kwargs):
		print(f"<<<<<U>>>>>>>>> MSG me({type(self)},{self})",*args,**kwargs)

	def newPersona(self, entity, secret = False):
		if not secret:
			entity["parent"] = self["id"]
			for key in self:
				if key != "id":
					entity[key] = self[key]

		self.personas[entity["id"]] = entity
		self["personas"].append(entity["id"])
		self["currentPersona"] = entity["id"]
		self._currentPersona = entity
		self.save()
		return entity

# class Car():
# 	def __init__(self, owner):
# 		self.owner = owner
# 	def drive(self):
# 		print(self.owner, "is driving")


# class TelsaCar(Car):
# 	def manufacter(*args,**kwargs):
# 		print("Tesla")
#
# 	def len(self)
#
#
# 	def selfdrive(self):
# 		print(f" driving to {self.owner}'s home")


# class Honda(Car):
# 	def manufacter(*args,**kwargs):
# 		print("Honda")



class Omega(Entity):
	deltas = dict()

	# def msg(self, *args,**kwargs):
	# 	print(f"<<<<<O>>>>>>>>> MSG me({type(self)},{self})",args,kwargs)

	def recieveMsg(self, *args,**kwargs):
		# print(f"<<<<<A>>>>>>>>> MSG me({type(self)},{self})",*args,**kwargs)
		xo.notify[self["id"]] = kwargs
	def __init__(self,*args,**kwargs):
		# kwargs["known"] = ["main","description","budget"]
		kwargs["type"] = type(self)
		super().__init__(*args,**kwargs)
		self["deltas"] = []
		self.deltas = {}
		xo.subscribe(f"notify.{self['id']}", self.notify)
		self.notifications = []
		self["chats"] = []
		self.chats = []
		self["contacts"] = []
		self.contacts =  []
		self.history = {"listening":[],"offers":{},"notifications":[]}


	def negotiate(self, delta, persona, *args,**kwargs):
		pass


	def accept(self, offer, *args,**kwargs):
		print("ACCEPTING OFFER!!!!!!!!!!!!!\n"*10,offer)
		delta = offer["delta"]
		kwargs["main"] = "OFFER ACCEPTED"
		kwargs["delta"] = delta
		kwargs["offer"] = offer
		offer.accept()
		# alpha.offerAccepted(*args,**kwargs)

	def chat(self, id = None, delta=None, offer = None, persona = None, *args,**kwargs):
		if id is not None:
			persona = id
		if delta is not None:
			persona = delta["parent"]
			kwargs["delta"] = delta["id"]
		if offer is not None:
			persona = offer["parent"]
			delta = offer["delta"]
			kwargs["offer"] = offer["id"]
			if delta is not None:
				# persona = delta["parent"]
				kwargs["delta"] = delta["id"]
		if persona is not None:
			# kwargs["parent"] = self["id"]
			kwargs["sender"] = self["id"]
			# get from db
			# listening = akeyo.index[alphaid].value()["listening"]
			print("PERSONA",persona,"selfID",self["id"],)
			alpha = akeyo.index[persona].value()
			alpha.recieveMsg(*args,**kwargs)


	def delta(self, *args,**kwargs):
		return self.createDelta(*args,**kwargs)

	def createDelta(self, *args,**kwargs):
		# known = ["main","description","budget"]
		# firstArgs, lastArgs = args[:len(known)],args[len(known):]
		# c = 0
		# for a in known:
		# 	kwargs[a] = firstArgs[c]
		# 	c+=1
		kwargs["parent"] = self["id"]
		d = Delta(*args,**kwargs)
		# d = Delta(*lastArgs,**kwargs)
		self["deltas"].append(d["id"])
		self.deltas[d["id"]] = d
		self.save()
		return d

	def notify(self, data,*args,**kwargs):
		full = (data,"::::::::",args,kwargs)
		msg = f"{self['id']} ::: New Offer from Alpha!!! ::: {full}!"
		print("\n"+("@"*int(len(msg)/2)+"\n"*1))
		# print(msg)
		print(data)
		print("@"*20)
		print(args)
		print("@"*20)
		print(kwargs)
		# print(("@"*len(msg)+"\n")*4+"\n")
		print(("@"*int(len(msg)/2)+"\n")*1+"\n")
		# self["hello"]
		# self.hello
		self.notifications.append(data)
		self.history["notifications"].append(data)


class Alpha(Entity):
	def __init__(self,*args,**kwargs):
		kwargs["type"] = type(self)
		super().__init__(*args,**kwargs)
		self["listening"] = []
		xo.notify[self['id']] = None
		xo.subscribe(f"notify.{self['id']}", self.notify)
		self.history = {"listening":[],"offers":{},"notifications":[]}
		self.notifications = []

	def chat(self, id = None, delta=None, offer = None, persona = None, *args,**kwargs):
		if id is not None:
			persona = id
		if delta is not None:
			persona = delta["parent"]
			kwargs["delta"] = delta["id"]
		if offer is not None:
			delta = offer["delta"]
			persona = delta["parent"]
			kwargs["offer"] = offer["id"]
			# if delta is not None:
			# 	# persona = delta["parent"]
			# 	kwargs["delta"] = delta["id"]
		if persona is not None:
			# kwargs["parent"] = self["id"]
			kwargs["sender"] = self["id"]
			# get from db
			# listening = akeyo.index[alphaid].value()["listening"]
			# print("PERSONA",persona,"selfID",self["id"],)
			o = akeyo.index[persona].value()
			o.recieveMsg(*args,**kwargs)

	def recieveMsg(self, *args,**kwargs):
		# print(f"<<<<<A>>>>>>>>> MSG me({type(self)},{self})",*args,**kwargs)
		xo.notify[self["id"]] = kwargs

	def offerAccepted(self, *args,**kwargs):
		# print(f"<<<<<A>>>>>>>>> MSG me({type(self)},{self})",*args,**kwargs)
		xo.notify[self["id"]] = kwargs

	def giveOffer(self,delta,*args,**kwargs):
		kwargs["parent"] = self["id"]
		kwargs["delta"] = delta
		kwargs["omega"] = delta["parent"]
		offer = Gamma(*args,**kwargs)
		delta.offer(self["id"],offer)
		self.history["offers"][offer['id']] = offer
		self.save()
		return offer

	def notify(self, data,*args,**kwargs):
		full = (data,"::::::::",args,kwargs)
		# msg = f"Someone wishes for {full}!"
		msg = f"{data}"
		# print("\n"+("!"*len(msg)+"\n")*4)
		print("\n"+("!"*int(len(msg)/2)+"\n"*1))
		# print("!"*20)
		print(data)
		# if data is not None:
		# 	for d in data:
		# 		print(data[d])
		# 		print("!"*20)
		print(args)
		print("!"*20)
		print(kwargs)
		print(("!"*int(len(msg)/2)+"\n")*1+"\n")
		self.notifications.append(data)
		self.history["notifications"].append(data)

	def listen(self, keywords, *args):
		if "list" in str(type(keywords)):
			keywords += list(args)
		else:
			args = list(args)
			args.append(keywords)
			keywords = args
		for phrase in keywords:
			for word in phrase.split("\n"):
				if word not in self["listening"]:
					self.history["listening"].append(word)
					self["listening"].append(word)
					print(f"{self['id']} listening to {word}")

		# self.save(delay = 1)
		self.save()

	def silent(self, keywords, *args):
		if "list" in str(type(keywords)):
			keywords += args
		else:
			args.append(keywords)
			keywords = args
		for phrase in keywords:
			for word in phrase.split("\n"):
				if word in self["listening"]:
					self["listening"].remove(word)
					print(f"{self['id']} removed {word} from notifications")
		self.save()


class Gamma(Entity):
	# known = ["main","description","budget"]
	def __init__(self,*args,**kwargs):
		# kwargs["_known_"] = Delta.known
		kwargs["type"] = type(self)
		super().__init__(*args,**kwargs)
		self["seen"] = False
		self["accepted"] = False

	def accept(self,*args,**kwargs):
		kwargs["main"] = "OFFER ACCEPTED BY OMEGA!"
		kwargs["offer"] = self["id"]
		self["accepted"] = True, datetime.now()
		self.save()
		xo.notify[self["parent"]] = kwargs



class Delta(Entity):
	known = ["main","description","budget"]
	def __init__(self,*args,**kwargs):
		kwargs["_known_"] = Delta.known
		kwargs["type"] = type(self)
		super().__init__(*args,**kwargs)
		self["offers"] = []
		self.offers = {}
		self["open"] = True

	def offer(self,alphaid,offer,*args,**kwargs):
		if "parent" not in offer:
			offer["parent"] = alphaid
		self["offers"].append(offer["id"])
		# maybe group by alpha
		# if alphaid not in self.offers:
		# 	self.offers[alphaid] = {}
		# self.offers[alphaid][offer["id"]] = offer
		self.offers[offer["id"]] = offer
		print()
		print(f"{self['id']} ::: GOT NEW OFFER! ::: {offer}")
		print()
		xo.notify[self["parent"]] = offer
		self.save()


# class Indexer(dict):
# 	shared = None
# 	def __init__(self):
# 		if Indexer.shared is None:
# 			Indexer.shared = self
# index = Indexer()
# index = Indexer.shared

class Manager(dict):
	shared = None
	def __init__(self):
		if Manager.shared is None:
			Manager.shared = self
		self.new = []
		xo.subscribe("akeyo.manager.new", self.trigger)

	def get(self, id):
		return akeyo.index[id].value()

	def manageNotifications(*args, **kwargs):
		print("::: Managing Notifications")
		self = Manager.shared
		while True:
			current = None
			new = None
			try:
				if len(self.new) > 0:
					new = self.new.pop(0)
					print("!!!!!!!!!!!"+str(type(new)))
					if "delta" in str(type(new)).lower():
						delta = new
						print(f" Manager ::: Processing {delta}")
						for alphaid in akeyo.index["A"].value():
							if alphaid[0] == "A":
								print(" AAAAAAA ::::: ",alphaid)
								alpha = akeyo.index[alphaid].value()
								listening = alpha["listening"]
								# add listening entity to check radius and other info
								print(" LLLLLL ::::: ",listening)
								desc = str(delta["main"])+" "+delta["description"]
								notify = [False, [],None]
								for phrase in listening:
									for word in phrase.lower().split(" "):
										if word.lower() in desc:
											notify[0] = True
											notify[1].append(word)
											notify[2] = delta

							if notify[0]:
								msg = f"Sending notification to alpha {alphaid}!,{notify[1]}"
								print("\n"+("#"*len(msg)+"\n")*1)
								print(msg)
								print(("#"*len(msg)+"\n")*1+"\n")
								xo.notify[alphaid] = delta
								# index[alphaid].notify(notify)


			except:
				print()
				print(f"ERROR in manageNotifications ::: current : {current} ")
				traceback.print_exc()
				print()

	def trigger(self,eid,*args,**kwargs):
		print("TTTTTTTTTT MANAGER TRIGGER",eid,*args,**kwargs)
		entity = None
		try:
			try:
				tx = time.time()
				run = True
				while eid not in akeyo.index.children() and run:
					time.sleep(0.01)
					if time.time()-tx > 3: #timeout
						run = False
			except :
				pass
			entity = akeyo.index[eid].value()
			print("NNNNNNNNN",entity)
			if entity is not None:
				etype = entity["id"][0]
				if etype == "D":
					self.new.append(entity)
				if etype == "M":
					self.new.append(entity)
		except:
			print()
			print(f"ERROR in trigger ::: {eid} ::: {args} ::: {kwargs}")
			print(f"Entity ::: {entity}")
			traceback.print_exc()
			print()

# manager = Manager()
# manager = Manager.shared
# xo.asyn(manager.manageNotifications)

class Key(Entity):
	pass
