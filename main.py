#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweebot


TEMPLATES = [
	"@%s Are you sure you didn't mean, whether or not?",
	"@%s I think you meant, whether or not.",
	"@%s I don't think rain has anything to do with it.",
	"@%s Indecisive meteorology! My favorite.",
]

class Ithinkyoumeant(tweebot.Context):
	def __init__(self, *args, **kwargs):
		settings = {
			'app_name'       : 'ithinkyoumeant',
			'username'       : '<YOUR ACCOUNT NAME>',
			'consumer_key'   : '<YOUR CONSUMER KEY>',
			'consumer_secret': '<YOUR CONSUMER SECRET>',
			'access_key'     : '<YOUR ACCESS KEY>',
			'access_secret'  : '<YOUR ACCESS SECRET>',
			'timeout'        : 30 * 60, # 30 min
			'history_file'   : 'ithinkyoumeant.history',
			'testing'        : True
		}
		super(Complementor, self).__init__(settings)

def main():
	bot = Ithinkyoumeant()
	tweebot.enable_logging(bot)
	bot.start_forever(
		tweebot.MultiPart.Add(
			tweebot.SearchMentions(),
			tweebot.SearchQuery('"weather or not"')),
		tweebot.MultiPart.And(
			tweebot.BaseFilter),
		tweebot.ReplyTemplate(TEMPLATES))

if __name__ == '__main__':
	main()