#!/usr/bin/python
import praw
import time
import datetime



lastID=""


def bot_login():
	print("Loggin in...")


	r = praw.Reddit(user_agent='Invest bot (by /u/username)',
                     client_id='xxxxxxxx', client_secret="xxxxxxxxxxxxxxxxxxxxxxx",
                     username='yyyyyyyy', password='yyyyyyyyyyy')
	print("Logged in!")

	return r




def run_bot(r):
	#globale variable wird verwendet
	global lastID

	#1 Kommentar von redditor wird geladen
	for comment in r.redditor('username').comments.new(limit=1):

		#Zeit wird berechnet
		now=time.time()
		age = now - comment.created_utc
		print("Zeit wurde berechnet")

		#Wenn noch nicht kommentiert und alter unter 300 sek dann
		if comment.id != lastID and age<300:
			#wenn !invest kommentiert wurde dann
			if "!invest" in comment.body:

				#Updated die CommentID
				lastID=comment.id

				#Überschreibt "comment" und setzt den Werd auf den Wert von "parent2" damit
				parent = comment.parent_id
				parent2 = parent.split('_')[1]
				comment = r.comment(parent2)

				#Antwortet dem Parentkommentar !invest 100%
				comment.reply("invest 100%")
				print("ES WURDE KOMMENTIERT")
				
				#Wenn Kommentiert wurde macht er nichts für bisschen unter 4 Stunden
				print("Sleeping für 14300 sekunden...")
				#Sleep für ein bisschen unter 4 Stunden
				time.sleep(14300)
				

	print("Sleeping für 10 sekunden...")
	#Sleep für 10
	time.sleep(10)


r = bot_login()
while True:
	run_bot(r)
