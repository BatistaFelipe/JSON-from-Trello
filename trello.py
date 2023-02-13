#!/usr/bin/env python3

import os
import json
import csv

def get_trello_lists(lists):
	trello_lists = []
	for list_item in lists:
		trello_lists.append({ 'id': list_item['id'], 'name': list_item['name'] })
	return trello_lists

def get_trello_cards(cards):
	trello_cards = []
	for card_item in cards:
		trello_cards.append({'name': card_item['name'], 'idList': card_item['idList'] })
	return trello_cards

def format_cards_list(lists, cards):
	final_list = []
	for card_item in cards:
		for list_item in lists:
			if card_item['idList'] == list_item['id']:
				final_list.append({ 'name': card_item['name'], 'list': list_item['name']})
	return final_list

def get_data_from_file(location):
	with open(location, 'r') as f:
		data = json.loads(f.read())
	return data

def save_data_to_file(location, data):
	headers = data[0].keys()
	with open(location, 'w+') as f:
		writer = csv.DictWriter(f, fieldnames=headers)
		writer.writeheader()
		writer.writerows(data)

def main():
	DIR = os.path.abspath(os.getcwd())
	json_filename = '/trello.json'
	csv_filename = '/trello.csv'

	items = get_data_from_file(DIR + json_filename)
	lists = get_trello_lists(items['lists'])
	cards = get_trello_cards(items['cards'])
	
	final_list = format_cards_list(lists, cards)
	save_data_to_file(DIR + csv_filename, final_list)

if __name__ == '__main__':
	main()