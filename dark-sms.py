# TUSBOL BY PDG
# uncompyle6 version 3.4.0
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jul 28 2019, 22:06:57)
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: dg
import os, sys, time, mechanize
from bs4 import BeautifulSoup as sup
import marshal, zlib, base64
br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('Connection', 'keep-alive'), ('Pragma', 'no-cache'), ('Cache-Control', 'no-cache'), ('Origin', 'http://sms.payuterus.biz'), ('Upgrade-Insecure-Requests', '1'), ('Content-Type', 'application/x-www-form-urlencoded'), ('User-Agent', 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'), ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'), ('Referer', 'http://sms.payuterus.biz/alpha/'), ('Accept-Encoding', 'gzip, deflate'), ('Accept-Language', 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7')]
z = []
merah = '\x1b[1;91m'
lime = '\x1b[1;92m'
kuning = '\x1b[1;93m'
biru = '\x1b[1;94m'
ungu = '\x1b[1;95m'
blue = '\x1b[1;96m'
putih = '\x1b[1;97m'
tutup = '\x1b[0m'
intro = blue + ' \xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97' + tutup + '\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80   ' + blue + '\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\n  \xe2\x95\x91\xe2\x95\x91' + tutup + '\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80' + blue + '\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x97\n \xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d' + tutup + '\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4 \xe2\x94\xb4   ' + blue + '\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\xa9 \xe2\x95\xa9\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d' + kuning + 'v0.2' + tutup

def only():
    os.system('clear')
    print intro
    print tutup + u'\x1b[7m     Author : MEMEK JMBUT     \x1b[0m' + tutup + '\n' + lime + '>> https://github.com/EgiRecod' + tutup
    print
    no = raw_input(tutup + '[' + lime + '+' + tutup + '] No Tujuan ex(+62) : ' + lime)
    msg = raw_input(tutup + '[' + lime + '+' + tutup + '] Pesan : ' + lime)
    if msg == '':
        only()
    else:
        bs = sup(br.open('http://sms.payuterus.biz/alpha'), features='html.parser')
        for x in bs.find_all('span'):
            z.append(x.text)

        a = str(z)[3]
        b = str(z)[7]
        by = raw_input(tutup + '[' + lime + '+' + tutup + '] ' + a + ' + ' + b + ' = ' + lime)
        br.select_form(nr=0)
        br.form['nohp'] = str(no)
        br.form['pesan'] = str(msg)
        br.form['captcha'] = str(by)
        print tutup + '[' + lime + '+' + tutup + '] Mengirim ...'
        get = br.submit().read()
        if 'SMS Gratis Telah Dikirim' in str(get):
            print tutup + '[' + lime + '+' + tutup + '] Terkirim : ' + lime + str(no)
            p = raw_input(tutup + '[' + lime + '?' + tutup + '] Send again? [y/n] : ' + lime)
            if p == 'y':
                os.system('python2 sms.py')
            else:
                exit(tutup + '[' + merah + '!' + tutup + '] Exit')

if __name__ == '__main__':
     only()