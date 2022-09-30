import json

incoming_file = open('1664302051617.txt', 'r')
# outgoing_file = open('new_stats.txt', 'w')
ready_json = open('post_processed_stats.json', 'w')

dirty_txt = incoming_file.read()
print(dirty_txt)
cleaner_txt = dirty_txt[16:]
print(cleaner_txt)
# outgoing_file.write(cleaner_txt)
ready_json.write(cleaner_txt)

# https://gf641ea24ecc468-darmok.adb.us-ashburn-1.oraclecloudapps.com/ords/admin/medium_stats/






