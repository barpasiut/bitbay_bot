import classes
import logging

logging.basicConfig(filename="logs.log",level=logging.DEBUG)

sec = classes.Security()
key = sec.getKeys()
con = classes.Connection(key['public'], key['private'])
bot = classes.MaxMin24(con, "ETH", True, 2.5)
bot.start()

