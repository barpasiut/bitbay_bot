import subprocess
import json
import os
import time
import logging
import sys

class Connection:
	def __init__(self, pubKey, privKey):
		self.publicKey = pubKey
		self.privateKey = privKey
		
	def pubReq(self, coinAndCurr, category="", since="", currency="PLN"):
		while(1):
			time.sleep(3)
			try:
				if since:
					res = subprocess.check_output("curl -X GET https://bitbay.net/API/Public/%s%s/%s.json?since=%s" %(coinAndCurr,currency, category,since),  shell=True, encoding="utf-8")
				else:
					res = subprocess.check_output("curl -X GET https://bitbay.net/API/Public/%s%s/%s.json" %(coinAndCurr, currency, category), shell=True, encoding="utf-8")
					logging.debug("curl -X GET https://bitbay.net/API/Public/%s%s/%s.json" %(coinAndCurr, currency, category))
					logging.debug("RES: %s" %res)
				if "code" in str(res):
					resList = json.loads(res)
					raise ValueError(resList['message'])
				if not res:
					raise ValueError("No return")
				return res
			except ValueError as e:
				logging.error("Error: %s Try Again" %e)
				time.sleep(3)
			except Exception as e:
				logging.error("Error: %s Try Again" %repr(e))
				time.sleep(3)
	
	# privReq param takes key:value parameters delimites by comma e.g. "type:bid,payment_currency:PLN"
	def privReq(self, meth, param=""):
		while(1):
			time.sleep(3)
			try:
				res = subprocess.check_output("/usr/bin/php %s/privateReq.php %s %s %s %s" %(os.getcwd(), self.publicKey, self.privateKey, meth, param), shell=True)
				logging.debug("/usr/bin/php %s/privateReq.php %s %s %s %s" %(os.getcwd(), self.publicKey, self.privateKey, meth, param))
				logging.debug("RES: %s" %res)
				if "code" in str(res):
					resList = json.loads(res)
					raise ValueError(resList['message'])
				if not res:
					raise ValueError("No return")
				return res
			except ValueError as e:
				logging.error("Error: %s Try Again" %e)
				time.sleep(3)
			except Exception as e:
				logging.error("Error: %s Try Again" %repr(e))
				time.sleep(3)

	def ticker(self, coinAndCurr="BTCPLN"):
		res = self.pubReq(coinAndCurr,"ticker")
		resList = json.loads(res)
		return resList
	
	def trades(self, coinAndCurr="BTCPLN", since=""):
		if since:
			res = self.pubReq(coinAndCurr,"trades", since)
		else:
			res = self.pubReq(coinAndCurr,"trades")
		resList = json.loads(res)
		return resList
		
	def orderbook(self, coinAndCurr="BTCPLN"):
		res = self.pubReq(coinAndCurr,"orderbook")
		resList = json.loads(res)
		return resList
		
	def market(self, coinAndCurr="BTCPLN", since=""):
		if since:
			res = self.pubReq(coinAndCurr,"market", since)
		else:
			res = self.pubReq(coinAndCurr,"market")
		resList = json.loads(res)
		return resList
		
	def all(self, coinAndCurr="BTCPLN"):
		res = self.pubReq(coinAndCurr,"all")
		resList = json.loads(res)
		return resList
	
	def info(self, params=""):
		res = self.privReq("info",params)
		resList = json.loads(res)
		return resList
	
	def trade(self, params=""):
		res = self.privReq("trade",params)
		resList = json.loads(res)
		return resList
	
	def cancel(self, params=""):
		res = self.privReq("cancel",params)
		resList = json.loads(res)
		return resList
	
	def orderbook(self, params=""):
		res = self.privReq("orderbook",params)
		resList = json.loads(res)
		return resList
	
	def orders(self, params=""):
		res = self.privReq("orders",params)
		resList = json.loads(res)
		return resList
		
	def transfer(self, params=""):
		res = self.privReq("transfer",params)
		resList = json.loads(res)
		return resList
		
	def withdraw(self, params=""):
		res = self.privReq("withdraw",params)
		resList = json.loads(res)
		return resList
		
	def history(self, params=""):
		res = self.privReq("hostory",params)
		resList = json.loads(res)
		return resList
		
	def history(self, params=""):
		res = self.privReq("history",params)
		resList = json.loads(res)
		return resList
		
	def transactions(self, params=""):
		res = self.privReq("transactions",params)
		resList = json.loads(res)
		return resList

class Security:
	def getKeys(self):
		f = open(os.getcwd()+"/keys.txt","r")
		keys = json.loads(f.read())
		f.close()
		return keys

class MaxMin24:
	def __init__(self, con, coin="BTC", n=True, pln=0, trans=-1, provi=0.43):
		self.connection = con
		self.new = n
		self.param = {}
		if self.new:
			self.param['coin'] = coin
			self.param['state'] = "buy"
			self.param['trans'] = trans
			self.param['pln'] = float(pln)
			self.param['amount'] = float(0)
			self.param['provi'] = provi
		'''
			try:
				f = open(os.getcwd()+"/classes/minMax24.txt","rw")
				self.param['coin'] = coin
				logs[self.param['coin']]['state'] = self.param['state']
				logs[self.param['coin']]['trans'] = self.param['trans']
				logs[self.param['coin']]['pln'] = self.param['pln']
				logs[self.param['coin']]['amount'] = self.param['amount']
				logs[self.param['coin']]['provi'] = self.param['provi']
				logsText = json.dumps(logs)
				f.write(logs)
				f.close()
				
			except:
				print("__init__() save to log Error")
		else:
			try:
				f = open(os.getcwd()+"/classes/minMax24.txt","r")
				logs = json.loads(f.read())
				self.param['coin'] = coin
				logs[self.param['coin']]['state'] = self.param['state']
				logs[self.param['coin']]['trans'] = self.param['trans']
				logs[self.param['coin']]['pln'] = self.param['pln']
				logs[self.param['coin']]['amount'] = self.param['amount']
				logs[self.param['coin']]['provi'] = self.param['provi']
				f.close()
			except:
				print("__init__() get from log Error")
		'''
	def getMin24AndBid(self):
		ticker = self.connection.ticker(self.param['coin'])
		return ticker['min'], ticker['bid']
		
	def getMax24AndAsk(self):
		ticker = self.connection.ticker(self.param['coin'])
		return ticker['max'], ticker['ask']
		
	def decrementTrans(self):
		self.param['trans'] = self.param['trans'] - 1
		
	def isOrder(self):
		orders = self.connection.orders()
		if len(orders):
			for value in orders:
				#logging.debug("Value of order: %s" %value)
				if 'order_currency' in value:
					if value['order_currency'] == self.param["coin"]:
						return "id:%s" %value['order_id']
					else:
						return False
				else:
					return False
		else:
			return False
			
	def buyState(self):
		min24, bid = self.getMin24AndBid()
		self.param['amount'] = float("%.8f" % (float(self.param['pln'])/bid))
		if 1.1 * min24 > bid:
			self.connection.trade("type:bid,currency:%s,amount:%.8f,payment_currency:PLN,rate:%s" %(self.param['coin'],self.param['amount'],bid+0.01))
			time.sleep(3)
			count = 5
			while(self.isOrder() and count):
				count = count -1
				time.sleep(10)
				if count == 0:
					self.connection.cancel(self.isOrder())
					return self.buyState()
			return "%.8f" % (float(self.param['amount'])*(1-self.param['provi']))
		return True
		
	def sellState(self):
		max24, ask = self.getMax24AndAsk()
		if 0.90 * max24 < ask:
			self.connection.trade("type:ask,currency:%s,amount:%.8f,payment_currency:PLN,rate:%s" %(self.param['coin'],self.param['amount'],ask))
			time.sleep(3)
			count = 5
			while(self.isOrder() and count):
				count = count -1
				time.sleep(10)
				if count == 0:
					self.connection.cancel(self.isOrder())
					return self.sellState()
			return "%.2f" % (float(self.param['amount']) * bid * (1-self.param['provi']))
		return True	
		
	
	def start(self):
		inf = 1 if self.param['trans'] == -1 else 0
		while(self.param['trans'] or inf):
			if self.param['state'] == "buy":
				while(1):
					logging.info("BuyState")
					self.param['amount'] = float(self.buyState())
					if self.param['amount'] != True:
						self.param['state'] = "sell"
						break
			elif self.param['state'] == "sell":
				while(1):
					logging.info("SellState")
					self.param['pln'] = float(self.sellState())
					if self.param['pln'] != True:
						self.param['state'] = "buy"
						break
		
	def changeErrorLogs(self, element, value):
		try:
			f = open(os.getcwd()+"/classes/minMax24.txt","rw")
			logs = json.loads(f.read())
			logs[element] = value
			f.write(json.dumps(logs))
			f.close()
		except:
			print("changeBackupLogs\(\) Error")
