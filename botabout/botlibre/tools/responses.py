# -*- coding: utf-8 -*-
# File:         responses.py
# Description:  Responses module for processing Botlibre response-lists
# Author:       ValV

import re, errno, json
from os import makedirs
from os.path import join
from math import log10, floor
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode, quote_plus

from memkalkul import total_size

# Response dictionary key names (not defined by response-lists)
question_key = "question"
response_key = "response"
# Global token variable
token = None
# Regex patterns for response-lists processing
xt_html = re.compile(r"<[^>]+>")
xpuncts = re.compile(r"[^-\w\s]|\s+[^\w]+\s+")
xspaces = re.compile(r"\s+")
xextens = re.compile(r"\.res$|\.$|$")

# Function: parse_responses
def parse_responses(list_file):
  # Regex patterns for BotLibre response lists (simplified)
  xdivide = re.compile(r"^$")
  xmeta_key = re.compile(r"^[a-z ]+: ")
  xmeta_value = re.compile(r": .+$")
  # Responses are a list of disctionaries
  responses = []
  the_response = {}
  for line in list_file:
    if xdivide.match(line):
      responses.append(the_response)
      the_response = {}
    if not the_response.get(question_key):
      the_response[question_key] = line.strip()
    elif not xmeta_key.search(line):
      if the_response.get(response_key):
        the_response[response_key] += line.strip()
      else:
        the_response[response_key] = line.strip()
    else:
      the_response[xmeta_value.sub('', line).strip()] =\
          xmeta_key.sub('', line.strip())
  return responses
# Function: parse_responses

# Function: show_responses
def show_responses(responses=None, field=question_key):
  # Check responses
  if responses:
    counter = 0
    pad = floor(log10(len(responses))) + 1
    for the_response in responses:
      counter += 1
      print(str(counter).zfill(pad), the_response.get(field))
    # Display total
    print("Total number of entries:", counter)
    print("Memory consumption:", total_size(responses))
  return None
# Function: show_responses

# Function: dump_responses
def dump_responses(responses, path="./dump_responses"):
  try:
    makedirs(path, 0o755)
  except OSError as e:
    if e.errno != errno.EEXIST:
      raise
  if responses:
    counter = 0
    pad = floor(log10(len(responses))) + 1
    for the_response in responses:
      counter += 1
      file_name = str(counter).zfill(pad)
      file_name += " - " + the_response[question_key]
      try:
        with open(join(path, file_name), "w+") as response_file:
          #response_file.write(strip_tags(the_response[response_key]))
          response_file.write(normalize(the_response[response_key]))
          response_file.close()
      except IOError:
        print("Error writing to:", file_name)
  return None
# Function: dump_responses

# Function: strip_tags
def strip_tags(text=None):
  if text:
    return xt_html.sub("", text)
  return None
# Function: strip_tags

# Function: normalize
def normalize(text=None):
  if text:
    return (xspaces.sub(" ", (xpuncts.sub(" ", strip_tags(text))))
        ).lower().strip()
  return None
# Function: normalize

# Function: fetch_token
def fetch_token(login=None, password=None):
  """ ParaPhraser server requires login and password to be supplied
      in order to get an API token.
      This function also reads login and password from file in the
      working directory called "authentication". This file must be
      of json format: {"login": "User", "password": "Password"}
  """
  payload = ""
  if login and password:
    payload = json.loads({"login": login, "password": password})
  else:
    with open("authentication", "r") as authfile:
      payload = json.load(authfile)
  print("fetch_token.payload:", payload)
  payload = urlencode(payload).encode("utf-8")
  print("fetch_token.payload:", payload)
  request = Request("https://paraphraser.ru/token/", data=payload)
  try:
    response = json.loads(urlopen(request).read().decode("utf-8"))
    print("fetch_token.response:", response)
    return response["token"]
  except (URLError, HTTPError) as e:
    print(e.reason)
    if type (e) is HTTPError:
      print(json.loads(e.read().decode("utf-8")))
  except Exception as e:
    print(e)
  return None
# Function: fetch_token

# Function: submit_query
def submit_query(payload):
  payload = urlencode(payload).encode()
  print("submit_query.params:", payload)
  request = Request("http://paraphraser.ru/api/", data=payload,)
      #headers={"Content-Type": "application/json"}, method="POST")
  try:
    return json.loads(urlopen(request).read().decode("utf-8"))
  except (URLError, HTTPError) as e:
    print(e.reason)
    if type(e) is HTTPError:
      return json.loads(e.read().decode("utf-8"))
  except Exception as e:
    print(e)
  return dict()
# Function: submit_query

# Function: get_keywords
def get_keywords(text=""):
  print("get_keywords.text:", text)
  global token
  if not token:
    token = fetch_token()
  if token is not None:
    result = submit_query({
        "c": "keywords",
        "query": "по отношению к виртуальным собеседникам также употребляется термин программа-собеседник",
        "top": 3,
        "pos": "NOUN",
        "clusters": 0,
        "vecth": 0.68,
        "synth": 0.1,
        "expand": 0,
        "mwe": 1,
        "forms": 0,
        "lang": "ru",
        "format": "json",
        "token": token,
      })
    # Display Paraphraser response
    if result.get("code") == 0:
      response = result.get("response")
      for item in response:
        for value in response[item].get("keywords"):
          print(value)
      return response
    else:
      print("Error executing query.\nRESPONSE:", result.get("msg"))
  else:
    print("No API token. Perhaps, wrong login or password...")
  return None
# Function: get_keywords

# vim: se et ts=2 sw=2 number syntax=python:
