#This file was used to analyze memory values to obtain the values listed in the Memory_addresses.txt file
from pyboy import PyBoy

game = PyBoy('_________') #Enter path to ROM File of Street Fighter Alpha: Warriors' Dream
state_file = open('_______________', 'rb') #Enter path to a previously saved state to speed up analysis of memory values
game.load_state(state_file)

while True:
    game.tick()
    print(str(game.get_memory_value(0xCB00))+'|'+str(game.get_memory_value(0xCB01))+'|'+str(game.get_memory_value(0xCB02))+'|'+str(game.get_memory_value(0xCB03))+'|'+str(game.get_memory_value(0xCB04))+'|'+str(game.get_memory_value(0xCB05))+'|'+str(game.get_memory_value(0xCB06))+'|'+str(game.get_memory_value(0xCB07))+'|'+str(game.get_memory_value(0xCB08))+'|'+str(game.get_memory_value(0xCB09))+'|'+str(game.get_memory_value(0xCB0A))+'|'+str(game.get_memory_value(0xCB0B))+'|'+str(game.get_memory_value(0xCB0C))+'|'+str(game.get_memory_value(0xCB0D))+'|'+str(game.get_memory_value(0xCB0E))+'|'+str(game.get_memory_value(0xCB0F)))
    print(str(game.get_memory_value(0xCB10))+'|'+str(game.get_memory_value(0xCB11))+'|'+str(game.get_memory_value(0xCB12))+'|'+str(game.get_memory_value(0xCB13))+'|'+str(game.get_memory_value(0xCB14))+'|'+str(game.get_memory_value(0xCB15))+'|'+str(game.get_memory_value(0xCB16))+'|'+str(game.get_memory_value(0xCB17))+'|'+str(game.get_memory_value(0xCB18))+'|'+str(game.get_memory_value(0xCB19))+'|'+str(game.get_memory_value(0xCB1A))+'|'+str(game.get_memory_value(0xCB1B))+'|'+str(game.get_memory_value(0xCB1C))+'|'+str(game.get_memory_value(0xCB1D))+'|'+str(game.get_memory_value(0xCB1E))+'|'+str(game.get_memory_value(0xCB1F)))
    print(str(game.get_memory_value(0xCB20))+'|'+str(game.get_memory_value(0xCB21))+'|'+str(game.get_memory_value(0xCB22))+'|'+str(game.get_memory_value(0xCB23))+'|'+str(game.get_memory_value(0xCB24))+'|'+str(game.get_memory_value(0xCB25))+'|'+str(game.get_memory_value(0xCB26))+'|'+str(game.get_memory_value(0xCB27))+'|'+str(game.get_memory_value(0xCB28))+'|'+str(game.get_memory_value(0xCB29))+'|'+str(game.get_memory_value(0xCB2A))+'|'+str(game.get_memory_value(0xCB2B))+'|'+str(game.get_memory_value(0xCB2C))+'|'+str(game.get_memory_value(0xCB2D))+'|'+str(game.get_memory_value(0xCB2E))+'|'+str(game.get_memory_value(0xCB2F)))
    print(str(game.get_memory_value(0xCB30))+'|'+str(game.get_memory_value(0xCB31))+'|'+str(game.get_memory_value(0xCB32))+'|'+str(game.get_memory_value(0xCB33))+'|'+str(game.get_memory_value(0xCB34))+'|'+str(game.get_memory_value(0xCB35))+'|'+str(game.get_memory_value(0xCB36))+'|'+str(game.get_memory_value(0xCB37))+'|'+str(game.get_memory_value(0xCB38))+'|'+str(game.get_memory_value(0xCB39))+'|'+str(game.get_memory_value(0xCB3A))+'|'+str(game.get_memory_value(0xCB3B))+'|'+str(game.get_memory_value(0xCB3C))+'|'+str(game.get_memory_value(0xCB3D))+'|'+str(game.get_memory_value(0xCB3E))+'|'+str(game.get_memory_value(0xCB3F)))
    print(str(game.get_memory_value(0xCB40))+'|'+str(game.get_memory_value(0xCB41))+'|'+str(game.get_memory_value(0xCB42))+'|'+str(game.get_memory_value(0xCB43))+'|'+str(game.get_memory_value(0xCB44))+'|'+str(game.get_memory_value(0xCB45))+'|'+str(game.get_memory_value(0xCB46))+'|'+str(game.get_memory_value(0xCB47))+'|'+str(game.get_memory_value(0xCB48))+'|'+str(game.get_memory_value(0xCB49))+'|'+str(game.get_memory_value(0xCB4A))+'|'+str(game.get_memory_value(0xCB4B))+'|'+str(game.get_memory_value(0xCB4C))+'|'+str(game.get_memory_value(0xCB4D))+'|'+str(game.get_memory_value(0xCB4E))+'|'+str(game.get_memory_value(0xCB4F)))
    print(str(game.get_memory_value(0xCB50))+'|'+str(game.get_memory_value(0xCB51))+'|'+str(game.get_memory_value(0xCB52))+'|'+str(game.get_memory_value(0xCB53))+'|'+str(game.get_memory_value(0xCB54))+'|'+str(game.get_memory_value(0xCB55))+'|'+str(game.get_memory_value(0xCB56))+'|'+str(game.get_memory_value(0xCB57))+'|'+str(game.get_memory_value(0xCB58))+'|'+str(game.get_memory_value(0xCB59))+'|'+str(game.get_memory_value(0xCB5A))+'|'+str(game.get_memory_value(0xCB5B))+'|'+str(game.get_memory_value(0xCB5C))+'|'+str(game.get_memory_value(0xCB5D))+'|'+str(game.get_memory_value(0xCB5E))+'|'+str(game.get_memory_value(0xCB5F)))
    print(str(game.get_memory_value(0xCB60))+'|'+str(game.get_memory_value(0xCB61))+'|'+str(game.get_memory_value(0xCB62))+'|'+str(game.get_memory_value(0xCB63))+'|'+str(game.get_memory_value(0xCB64))+'|'+str(game.get_memory_value(0xCB65))+'|'+str(game.get_memory_value(0xCB66))+'|'+str(game.get_memory_value(0xCB67))+'|'+str(game.get_memory_value(0xCB68))+'|'+str(game.get_memory_value(0xCB69))+'|'+str(game.get_memory_value(0xCB6A))+'|'+str(game.get_memory_value(0xCB6B))+'|'+str(game.get_memory_value(0xCB6C))+'|'+str(game.get_memory_value(0xCB6D))+'|'+str(game.get_memory_value(0xCB6E))+'|'+str(game.get_memory_value(0xCB6F)))
    print(str(game.get_memory_value(0xCB70))+'|'+str(game.get_memory_value(0xCB71))+'|'+str(game.get_memory_value(0xCB72))+'|'+str(game.get_memory_value(0xCB73))+'|'+str(game.get_memory_value(0xCB74))+'|'+str(game.get_memory_value(0xCB75))+'|'+str(game.get_memory_value(0xCB76))+'|'+str(game.get_memory_value(0xCB77))+'|'+str(game.get_memory_value(0xCB78))+'|'+str(game.get_memory_value(0xCB79))+'|'+str(game.get_memory_value(0xCB7A))+'|'+str(game.get_memory_value(0xCB7B))+'|'+str(game.get_memory_value(0xCB7C))+'|'+str(game.get_memory_value(0xCB7D))+'|'+str(game.get_memory_value(0xCB7E))+'|'+str(game.get_memory_value(0xCB7F)))
    print(str(game.get_memory_value(0xCB80))+'|'+str(game.get_memory_value(0xCB81))+'|'+str(game.get_memory_value(0xCB82))+'|'+str(game.get_memory_value(0xCB83))+'|'+str(game.get_memory_value(0xCB84))+'|'+str(game.get_memory_value(0xCB85))+'|'+str(game.get_memory_value(0xCB86))+'|'+str(game.get_memory_value(0xCB87))+'|'+str(game.get_memory_value(0xCB88))+'|'+str(game.get_memory_value(0xCB89))+'|'+str(game.get_memory_value(0xCB8A))+'|'+str(game.get_memory_value(0xCB8B))+'|'+str(game.get_memory_value(0xCB8C))+'|'+str(game.get_memory_value(0xCB8D))+'|'+str(game.get_memory_value(0xCB8E))+'|'+str(game.get_memory_value(0xCB8F)))
    print(str(game.get_memory_value(0xCB90))+'|'+str(game.get_memory_value(0xCB91))+'|'+str(game.get_memory_value(0xCB92))+'|'+str(game.get_memory_value(0xCB93))+'|'+str(game.get_memory_value(0xCB94))+'|'+str(game.get_memory_value(0xCB95))+'|'+str(game.get_memory_value(0xCB96))+'|'+str(game.get_memory_value(0xCB97))+'|'+str(game.get_memory_value(0xCB98))+'|'+str(game.get_memory_value(0xCB99))+'|'+str(game.get_memory_value(0xCB9A))+'|'+str(game.get_memory_value(0xCB9B))+'|'+str(game.get_memory_value(0xCB9C))+'|'+str(game.get_memory_value(0xCB9D))+'|'+str(game.get_memory_value(0xCB9E))+'|'+str(game.get_memory_value(0xCB9F)))
    print(str(game.get_memory_value(0xCBA0))+'|'+str(game.get_memory_value(0xCBA1))+'|'+str(game.get_memory_value(0xCBA2))+'|'+str(game.get_memory_value(0xCBA3))+'|'+str(game.get_memory_value(0xCBA4))+'|'+str(game.get_memory_value(0xCBA5))+'|'+str(game.get_memory_value(0xCBA6))+'|'+str(game.get_memory_value(0xCBA7))+'|'+str(game.get_memory_value(0xCBA8))+'|'+str(game.get_memory_value(0xCBA9))+'|'+str(game.get_memory_value(0xCBAA))+'|'+str(game.get_memory_value(0xCBAB))+'|'+str(game.get_memory_value(0xCBAC))+'|'+str(game.get_memory_value(0xCBAD))+'|'+str(game.get_memory_value(0xCBAE))+'|'+str(game.get_memory_value(0xCBAF)))
    print(str(game.get_memory_value(0xCBB0))+'|'+str(game.get_memory_value(0xCBB1))+'|'+str(game.get_memory_value(0xCBB2))+'|'+str(game.get_memory_value(0xCBB3))+'|'+str(game.get_memory_value(0xCBB4))+'|'+str(game.get_memory_value(0xCBB5))+'|'+str(game.get_memory_value(0xCBB6))+'|'+str(game.get_memory_value(0xCBB7))+'|'+str(game.get_memory_value(0xCBB8))+'|'+str(game.get_memory_value(0xCBB9))+'|'+str(game.get_memory_value(0xCBBA))+'|'+str(game.get_memory_value(0xCBBB))+'|'+str(game.get_memory_value(0xCBBC))+'|'+str(game.get_memory_value(0xCBBD))+'|'+str(game.get_memory_value(0xCBBE))+'|'+str(game.get_memory_value(0xCBBF)))
    print(str(game.get_memory_value(0xCBC0))+'|'+str(game.get_memory_value(0xCBC1))+'|'+str(game.get_memory_value(0xCBC2))+'|'+str(game.get_memory_value(0xCBC3))+'|'+str(game.get_memory_value(0xCBC4))+'|'+str(game.get_memory_value(0xCBC5))+'|'+str(game.get_memory_value(0xCBC6))+'|'+str(game.get_memory_value(0xCBC7))+'|'+str(game.get_memory_value(0xCBC8))+'|'+str(game.get_memory_value(0xCBC9))+'|'+str(game.get_memory_value(0xCBCA))+'|'+str(game.get_memory_value(0xCBCB))+'|'+str(game.get_memory_value(0xCBCC))+'|'+str(game.get_memory_value(0xCBCD))+'|'+str(game.get_memory_value(0xCBCE))+'|'+str(game.get_memory_value(0xCBCF)))
    print(str(game.get_memory_value(0xCBD0))+'|'+str(game.get_memory_value(0xCBD1))+'|'+str(game.get_memory_value(0xCBD2))+'|'+str(game.get_memory_value(0xCBD3))+'|'+str(game.get_memory_value(0xCBD4))+'|'+str(game.get_memory_value(0xCBD5))+'|'+str(game.get_memory_value(0xCBD6))+'|'+str(game.get_memory_value(0xCBD7))+'|'+str(game.get_memory_value(0xCBD8))+'|'+str(game.get_memory_value(0xCBD9))+'|'+str(game.get_memory_value(0xCBDA))+'|'+str(game.get_memory_value(0xCBDB))+'|'+str(game.get_memory_value(0xCBDC))+'|'+str(game.get_memory_value(0xCBDD))+'|'+str(game.get_memory_value(0xCBDE))+'|'+str(game.get_memory_value(0xCBDF)))
    print(str(game.get_memory_value(0xCBE0))+'|'+str(game.get_memory_value(0xCBE1))+'|'+str(game.get_memory_value(0xCBE2))+'|'+str(game.get_memory_value(0xCBE3))+'|'+str(game.get_memory_value(0xCBE4))+'|'+str(game.get_memory_value(0xCBE5))+'|'+str(game.get_memory_value(0xCBE6))+'|'+str(game.get_memory_value(0xCBE7))+'|'+str(game.get_memory_value(0xCBE8))+'|'+str(game.get_memory_value(0xCBE9))+'|'+str(game.get_memory_value(0xCBEA))+'|'+str(game.get_memory_value(0xCBEB))+'|'+str(game.get_memory_value(0xCBEC))+'|'+str(game.get_memory_value(0xCBED))+'|'+str(game.get_memory_value(0xCBEE))+'|'+str(game.get_memory_value(0xCBEF)))
    print(str(game.get_memory_value(0xCBF0))+'|'+str(game.get_memory_value(0xCBF1))+'|'+str(game.get_memory_value(0xCBF2))+'|'+str(game.get_memory_value(0xCBF3))+'|'+str(game.get_memory_value(0xCBF4))+'|'+str(game.get_memory_value(0xCBF5))+'|'+str(game.get_memory_value(0xCBF6))+'|'+str(game.get_memory_value(0xCBF7))+'|'+str(game.get_memory_value(0xCBF8))+'|'+str(game.get_memory_value(0xCBF9))+'|'+str(game.get_memory_value(0xCBFA))+'|'+str(game.get_memory_value(0xCBFB))+'|'+str(game.get_memory_value(0xCBFC))+'|'+str(game.get_memory_value(0xCBFD))+'|'+str(game.get_memory_value(0xCBFE))+'|'+str(game.get_memory_value(0xCBFF)))
    print('------------------------------------------------------------------------------------------------------------')