# TODO:
# Chekc duplications
# auto subs from db
# full async, close, open, get notified
# Move to whatsapp


#simulate.py
from AkeyOverse import *
manager = Manager()
manager = Manager.shared
xo.asyn(Manager.manageNotifications)
t = User(name = "tami")
o = t._currentPersona
######################
d = o.delta("guitar lessons","on mondays",200,contact="wa", Global = True)
################
# >>> type(list(o.deltas.values())[0])
# offer = o.deltas.values()[0].
# offer = list(d.offers.values())[-1]
# a = mangager.getUser(offer["parent"])
offer = manager.get("G-5fjRHDuQ5XJ6daESjihC6P")
# a = manager.get(offer["parent"])
# a.recieveMsg(("MSG"*10+"\n")*3+f"\nHELLO FROM {o['name']}")
o.chat(offer=offer, msg = f"hello from {o['name']}")
# o.chat(delta=d, msg = f"hello from {o['name']}")
# o.c(o,delta=d, msg = f"hello from {o['name']}")
##################
# accepte
offer.accept()


from AkeyOverse import *
g = User(name = "Guitar Teacher 1")
a1 = g.newPersona(Alpha())
#needs redone after manager raises ? # BUG:
a1.listen("guitar lessons")
###########
# a1.giveOffer(delta, descrption = "Amazing guitar lessons - fast and furious - Pink floyd", also = "kong fu panda")
offer = a1.giveOffer(a1.notifications[-1], descrption = "Amazing guitar lessons - fast and furious - Pink floyd", also = "kong fu panda")
a1.chat(offer=offer, msg = f"yo yo yo from {a1['name']}")
###########
# msg back user
# a.msg(("MSG"*10+"\n")*3+f"\nHELLO FROM {a1['name']}")

from AkeyOverse import *
g = User(name = "Teacher 2")
a1 = g.newPersona(Alpha())
a1.listen("lessons")
###########################
# a1.giveOffer(delta, descrption = "Amazing guitar lessons - fast and furious - Pink floyd", also = "kong fu panda")
a1.giveOffer(a1.notifications[0],, "Jam like sultans of swing", jam = "like tha wind")
