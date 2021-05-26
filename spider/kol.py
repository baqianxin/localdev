import gopup as gp
cookie = '''BAIDUID=520790259688E4F992CE9C85012876AA:FG=1; BIDUPSID=520790259688E4F992CE9C85012876AA; PSTM=1565922886; BDUSS=pweGxiRjJ2ZjVYNzVyQjVpa1h4a2NvVXpOZEVQSndlMjVXOEt5VTlrM2ZLfkJmRUFBQUFBJCQAAAAAAAAAAAEAAABwybYvQWN0aXZMYXVuY2hpbmcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN-eyF~fnshfb0; ZD_ENTRY=google; H_PS_PSSID=33425_33518_33580_33259_33344_31253_33595_33336_26350_22160; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; PSINO=1; delPer=1; CHKFORREG=665e9710bc428b692ad7a480a93f78ef; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1614044902,1614047132; bdshare_firstime=1614047132256; bdindexid=ubj23geqhuvjif50e2h3gs6dg6; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1614050647; __yjsv5_shitong=1.0_7_68118845e600c74d9b82672c9029ade41cb1_300_1614050647759_218.30.116.246_5e8f3a6b; RT="z=1&dm=baidu.com&si=j9w1ci5wt8a&ss=klhfz3c5&sl=5&tt=4pz&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=3wg6&ul=45mg"'''
index_df = gp.baidu_search_index(word="口罩", start_date='2020-01-01', end_date='2020-03-01', cookie=cookie)
print(index_df)

# df = gp.weibo_user(user_id="2609084213")
# print(df)

# df = gp.weibo_list(user_id="2609084213")
# print(df)

df_index = gp.realtime_artist()
print(df_index)
df_index = gp.realtime_artist_flow()
print(df_index)