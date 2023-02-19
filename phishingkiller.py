from random_italian_person import RandomItalianPerson
import random
import urllib.request
import time
import string
from multiprocessing.pool import ThreadPool as Pool

printfun = print


def get_random_string(length):
  # choose from all lowercase letter
  characters = string.ascii_letters + string.digits
  result_str = ''.join(random.choice(characters) for i in range(length))
  return result_str


def random_with_N_digits(n):
  range_start = 10**(n - 1)
  range_end = (10**n) - 1
  return random.randint(range_start, range_end)


def mobile_prefix():
  prefix = [
    389, 3777, 3311, 3778, 3775, 373, 390, 391, 392, 393, 397, 366, 331, 3707,
    3771, 3772, 3774, 3779, 330, 331, 333, 334, 335, 336, 337, 338, 339, 360,
    363, 366, 368, 3701, 3773, 340, 341, 342, 343, 345, 346, 347, 348, 349,
    383, 320, 323, 324, 327, 328, 329, 380, 383, 388, 389
  ]
  return prefix[random.randint(0, len(prefix) - 1)]


def generate_id():
  person = RandomItalianPerson()
  surname = person.surname.replace(" ", "").replace("'", "")
  name = person.name.replace(" ", "").replace("'", "")
  mode = random.randint(0, 4)
  if mode == 0:
    id = name + surname
  elif mode == 1:
    id = name + str(random.randint(1, 99))
  elif mode == 2:
    id = surname + str(random.randint(1, 99))
  elif mode == 3:
    id = name[0] + surname
  elif mode == 4:
    id = name + surname
    newlen = random.randint(8, len(id) - 1)
    id = id[:newlen]

  return id


def sendData(baseurl, currtime, id, pwd, phone, state):
  try:
    url = baseurl + "?startTime=" + currtime + "&L=" + urllib.parse.quote(
      id) + "&P=" + pwd + "&T=" + phone + "&S=" + state
    urllib.request.urlopen(url).read()
  except Exception as e:
    printfun(str(e))


def task(slpitdata, counter):

  baseurl = "https://2sicuro-supporto-webclient.cfolks.pl/bper/mobile/public/webapp/digital-login/push.php"
  id = generate_id()
  pwd = get_random_string(random.randint(8, 16))
  addCountyPrefix = bool(random.getrandbits(1))
  phone = ""
  if addCountyPrefix:
    phone = "+39"
  else:
    phone = ""
  phone = phone + str(mobile_prefix()) + str(random_with_N_digits(7))
  currtime = str(int(time.time() + random.randint(-1000000, 100000)))
  states = ["START", "PHONE", "WAIT"]

  for i in range(3):
    if states[i] == "START":
      if slpitdata:
        partialid = ""
        for k in range(len(id) - 1):
          partialid = partialid + id[k]
          if (k % 5) == 0:
            sendData(baseurl, currtime, partialid, "", "", "START")
      sendData(baseurl, currtime, id, "", "", "START")
      if slpitdata:
        partialpwd = ""
        for k in range(len(pwd) - 1):
          partialpwd = partialpwd + pwd[k]
          if (k % 5) == 0:
            sendData(baseurl, currtime, id, partialpwd, "", "START")
      sendData(baseurl, currtime, id, pwd, "", "START")
    elif states[i] == "PHONE":
      if slpitdata:
        partialphone = ""
        for k in range(len(id) - 1):
          partialphone = partialphone + phone[k]
          if (k % 5) == 0:
            sendData(baseurl, currtime, id, pwd, partialphone, "PHONE")
      sendData(baseurl, currtime, id, pwd, phone, "PHONE")
    else:
      if slpitdata:
        for i in range(20):
          sendData(baseurl, currtime, id, pwd, phone, "WAIT")
      sendData(baseurl, currtime, id, pwd, phone, "WAIT")

  msg = str(counter) + " " + id + " " + pwd + " " + phone
  printfun(msg)


def start_process(outputfun):
  global printfun
  printfun = outputfun
  print("Start sending fake data...")
  poolsize = 5
  pool = Pool(poolsize)
  counter = 0
  while True:
    try:
      pool.apply_async(task, args=(
        False,
        counter,
      ))
    except Exception as e:
      print(e)
    counter = counter + 1
    if (counter % poolsize) == 0:
      #print(".", end='', flush=True)
      pool.close()
      pool.join()
      pool = Pool(poolsize)


if __name__ == "__main__":
  start_process(print)
