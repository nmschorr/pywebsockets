#!/usr/bin/python3.7

import json
from asyncio import sleep as a_sleep
from tornado.websocket import WebSocketClientConnection  # WebSocketClosedError
import nulsws_python.src.nulsws_python.nulsws_library as nulsws_library


class RegularRequest(object):
    def __init__(self):
        pass

    async def regular_request(self, websock_cont: WebSocketClientConnection, j_reg_dict):
        pause_time = .7
        nlib_obj = nulsws_library.NulsWsLib()

        json_reg = json.dumps(j_reg_dict)
        str_msg_out = "\n* * * REGULAR message going out: \n"
        nlib_obj.json_prt(json_reg, str_msg_out)

        await websock_cont.write_message(json_reg)  # 2 WRITE

        read_reg = await websock_cont.read_message()  # 3 READ
        await a_sleep(pause_time)

        str_msg_rec = "   -----------> ! ! ! REGULAR response received: "
        if len(read_reg) > 0:
            nlib_obj.json_prt(read_reg, str_msg_rec)

        str_msg_end = "-----------end previous / begin next request--------------------------"
        nlib_obj.myprint(str_msg_end)