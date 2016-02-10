import OSC

def handler(addr, tags, data, client_address):
    txt = "Mensaje OSC '%s' DE %s: " % (addr, client_address)
    txt += str(data)
    print(txt)

if __name__ == "__main__":
    s = OSC.OSCServer(('127.0.0.1', 57120))  # listen on localhost, port 57120
    s.addMsgHandler('/checkout', handler)     # call handler() for OSC messages received with the /startup address
    s.serve_forever()