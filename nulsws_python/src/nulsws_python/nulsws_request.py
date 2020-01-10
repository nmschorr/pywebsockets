#!/usr/bin/python3.7

import json

from .nulsws_library import NulswsLibrary
from .constants.nulsws_other_labels import *
from .user_settings.nulsws_settings_one import *
from .constants import nulsws_calls_db

# -----------prep_NEGOTIATE_data_type1--------------------------------------#


def prep_negotiate_request(msg_indx):  # return dict
    data_part = {msg_data_label: {
        proto_label: proto_ver,
        compress_type_label: compress_type_VALUE,
        compress_rate_label: compress_rate_VALUE}}
    top_sect = get_top_section(1, msg_indx)
    top_sect.update(data_part)
    return top_sect  # dict


# -----------get_REQ_MIDDLE--------------------------------------#


def get_top_section(msg_type: int, msg_indx):  # this section builds 5 items: #0
    # 0  "ProtocolVersion": "0.1",
    # 1 "MessageID": "1569897424187-1",  #2 "TimeZone": "-4",   # 3 "Timestamp": "1569897424187"
    # 4 "MessageType": "NegotiateConnection",
    # msg_type_name = type_name_dict.__getitem__(msg_type)

    msg_type_name = type_name_dict[msg_type]
    t_stamp, tzone, m_id = NulswsLibrary.get_times(msg_indx)
    top_part = {proto_label: proto_ver,
                msg_id_label: m_id,
                tmstmp_label: t_stamp,
                tmzone_label: tzone,
                msg_type_label: msg_type_name}
    return top_part


# -----------get_REQ_MIDDLE--------------------------------------#


def get_request_middle(mid_section_vals=None):  # return dict
    if not mid_section_vals:
        mid_section_vals = [1, ZERO, ZERO, ZERO, ZERO]  # 2 = ack+date
    [rtt, sec, sp, sr, rms, bottom_part] = [*mid_section_vals]

    req_middle = {
        msg_data_label: {
            request_type_label: rtt,
            subscrip_evnt_ct_label: sec,
            subscrip_period_label: sp,
            subscriptn_range_label: sr,
            response_max_size_label: rms,
            req_methods_label: bottom_part
        }}
    return req_middle  # dict


# -----------prep_REQUEST_ONESIE (request) --------------------------------------#

# class NulswsApiLabel(object):
#     AC_ADD_ADDRESS_PREFIX = ("ac_addAddressPrefix", "AC_ADD_ADDRESS_PREFIX",)
# name pairs:  ("AC_CREATE_ACCOUNT", NLab.AC_CREATE_ACCOUNT),


def prep_request(msg_indx, api_name_val):  # requesttype 2 - return ack +

    calls_list = nulsws_calls_db.NulswsParams.calls_list
    # name_list = NamePairs.name_pairs_list   ## try not to to use name_pairs_list

    # response either has a second element of a list, or not
#    api_name_tup = [i for i in name_list if i[1] == api_name_val][0]
    api_text_tp = [i[0] for i in calls_list if i[0][0] == api_name_val][0]
    api_text = api_text_tp[0]
    api_params_dict = {}
    api_text_api_params_dict = dict()
    try:
        api_params_list = [val[1] for val in calls_list if val[0][0] == api_text]
        for i in api_params_list:
            print(i)

        api_params_dict = dict(api_params_list[0])
    except Exception:
        pass

    api_text_api_params_dict.update({api_text: api_params_dict})

    request_type = "2"  # 1 or 2 for message requests
    subs_e_c = "0"  # subscription event_counter
    subs_per = "0"  # subscription period
    subs_rg = "0"  # subscription range
    resp_max = "0"  # response max size range

    newlist = [request_type, subs_e_c, subs_per, subs_rg, resp_max, api_text_api_params_dict]

    msg_section_middle = get_request_middle(newlist)
    message_section_top = get_top_section(3, msg_indx)
    message_section_top.update(msg_section_middle)
    print(json.dumps(message_section_top, indent=2))
    return message_section_top  # "'"return dict

# ----------- end library file --------------------------------------#
# ---------------- Example -------------------------------------------------------------------
#
# Example of type 3 message:
# {
#     "ProtocolVersion": "0.1.0"
#     "MessageID": m_id,
#     "TimeZone": tzone,
#     "Timestamp": t_stamp
#     "MessageType": "Request",
#     "MessageData": {
#         "RequestType": "1",
#         "SubscriptionEventCounter": "0",
#         "SubscriptionPeriod": "1",
#         "SubscriptionRange": "[100]",
#         "ResponseMaxSize": "0",
#         "RequestMethods": [
#           {
#             "GetBalance": {
#               "Address": "tNULSeBaMnrs6JKrCy6TQdzYJZkMZJDng7QAsD"
#             }
#           },
#           {
#             "GetHeight": {}
#           }
#         ]
#        }
#     }
