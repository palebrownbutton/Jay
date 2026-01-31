import tinytuya

def toggle_lights(action):
    ip1 = "192.168.1.11"
    virtual_id1 = "bf6186839d2bd30dce8jtg"
    key1 = ":G549vkG9d2V)1QE"
    ip2 = "192.168.1.13"
    virtual_id2 = "bf759dea325d9143f9aqyu"
    key2 = "WMnk'}^4qV~!WQPg"
    ip3 = "192.168.1.129"
    virtual_id3 = "bfd2376cbad25e9653v6ei"
    key3 = "ivM98~'YW^'=ST3M"
    ip4 = "192.168.1.88"
    virtual_id4 = "bf29c77c12c7ae71a3mmw2"
    key4 = "mr>~t^o:2qNF$|k?"
    ip5 = "192.168.1.64"
    virtual_id5 = "bf670c7cd52c0e4e5fjjfp"
    key5 = "L3M5BH_O*.Fzoj1+"
    ip6 = "192.168.1.54"
    virtual_id6 = "bf5ffeab42e392f8bdzt9f"
    key6 = "lV2^Kv6Zn(Kcf+rj"
    bulb1 = tinytuya.BulbDevice(virtual_id1, ip1, key1)
    bulb2 = tinytuya.BulbDevice(virtual_id2, ip2, key2)
    bulb3 = tinytuya.BulbDevice(virtual_id3, ip3, key3)
    bulb4 = tinytuya.BulbDevice(virtual_id4, ip4, key4)
    bulb5 = tinytuya.BulbDevice(virtual_id5, ip5, key5)
    bulb6 = tinytuya.BulbDevice(virtual_id6, ip6, key6)
    if action == "on":
        bulb1.turn_on()
        bulb2.turn_on()
        bulb3.turn_on()
        bulb4.turn_on()
        bulb5.turn_on()
        bulb6.turn_on()
    elif action == "off":
        bulb1.turn_off()
        bulb2.turn_off()
        bulb3.turn_off()
        bulb4.turn_off()
        bulb5.turn_off()
        bulb6.turn_off()
toggle_lights("on")