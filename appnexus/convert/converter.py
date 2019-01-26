import time


class Converter(object):

    fold_position_dict = {0: 'Unknown', 1: 'Above', 2: 'Below'}
    event_type_dict = {'imp': 'Impression', 'click': 'Click', 'pc_conv': 'Post-click Conversion', 'pv_conv': 'Post-view Conversion'}
    imp_type = {1: 'Blank', 2: 'PSA', 3: 'Default Error', 4: 'Default', 5: 'Kept', 6: 'Resold', 7: 'RTB', 8: 'PSA Error', 9: 'External Impression', 10: 'External Click', 11: 'Insertion'}
    payment_type = {-1: 'No payment', 0: 'CPM', 1: 'CPC', 2: 'CPA', 3: 'Owner CPM', 4: 'Owner revshare'}
    revenue_type = { -1: 'No payment', 0: 'Flat CPM', 1: 'Cost Plus CPM', 2: 'Cost Plus Margin', 3: 'CPC', 4: 'CPA', 5: 'Revshare', 6: 'Flat Fee', 7: 'Variable CPM', 8: 'Estimated CPM'}
    is_imp = {0: False, 1: True}
    is_learn = {0: 'Base Bid', 1: 'Learn', 2: 'Optimized'}
    predict_type_rev = {-2: 'No Predict Phase', -1: 'Base Predict Phase', 0: 'Learn Giveup', 1: 'Learn', 2: 'Throttled', 3: 'Optimized', 4: 'Baised', 5: 'Optimized 1', 8: 'Optimized Giveup', 9: 'Base Bid Below Giveup'}
    buyer_member_id = {1: 'Blank', 2: 'PSA', 3: 'Default Error', 4: 'Default'}
    is_control = {0: 'Test Impression', 1: 'Control Impression', 2: 'No Cookie User'}
    is_click = {0: False, 1: True, 'NULL': 'No Information Available'}
    device_unique_id = {0: 'IDFA', 1: 'SHA1', 2: 'MD5', 3: 'ODIN', 4: 'OPENUDID', 5: 'AAID', 6: 'WINDOWSADID', 7: 'RIDA'}
    view_result = {0: 'VIEW_UNKNOWN', 1: 'VIEW_DETECTED', 2: 'VIEW_NOT_DETECTED', 3: 'VIEW_NOT_MEASURABLE', -1: 'UNKNOWN'}
    supply_type = {0: 'WEB', 1: 'MOBILE_WEB', 2: 'MOBILE_APP', 5: 'TOOLBAR'}
    view_non_measurable_reason = {0: 'N/A', 1: 'SCRIPT_NOT_SERVED', 2: 'NO_SCRIPT_CALLBACK', 3: 'TECHNICAL_LIMITATION', -1: 'UNKNOWN'}
    deal_type = {1: 'Open Auction', 2: 'Private Auction'}
    is_filtered_request = {0: True, 1: False}
    is_exclusive = {0: 'Managed and Non-managed Eligible', 1: 'Managed Eligible'}
    device_type = {0: 'Other Devices', 1: 'Desktops and Laptops', 2: 'Mobile Phones', 3: 'Tablets', 4: 'TV', 5: 'Game Consoles', 6: 'Media Players', 7: 'Set Top Box'}


    def datetime_parser(self, millis):
        date_tuple = time.localtime(millis)
        return date_tuple.tm_year, date_tuple.tm_mon, date_tuple.tm_mday, date_tuple.tm_hour, date_tuple.tm_min