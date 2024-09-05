# SwitchETH002.py - Written by Wim Bruyn
#
# Platform: python33, Windows 7
#
# Purpose:
#   Switching ETH002 or ETH008 TCP/IP relays on and off and send an
#   e-mail when done. Windows task scheduler can be used to activate
#   the relays (optional).
#
# Command line arguments required for:
#   Relays number (1-8),
#   Mode (on/off),
#   e-mail report ID (free format text).
#
# Example usage:
#
#   c:\python33\python.exe SwitchETH002.py 2 off "External WD USB disk"
#

import socket
import time
import argparse
import smtplib


def SendCommandToRelays(MESSAGE):  # Value of MESSAGE is command to be send to relays
    TCP_IP = '192.168.2.115'  # IP address of the relays
    TCP_PORT = 17494  # Port number of the relays
    BUFFER_SIZE = 80

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)  # Response from Relays
    s.close()

    # if data == b'\x00':
    #     SendMailMessage((args.Device + ' is powered ' + args.Function + ', on date: ' + time.strftime("%c")))
    # else:
    #     SendMailMessage(
    #         ('Error:' + args.Device + ' is not powered ' + args.Function + ', on date: ' + time.strftime("%c")))


# def SendMailMessage(Mtext):  # Value of Mtext is action report send to mail recipient
#     sender = 'joe.bloggs@email.com'  # mail address of the sender
#     receivers = ['joe.bloggs@email.com']  # mail address of the receiver
#
#     smtpObj = smtplib.SMTP(‘mailhost.email.com’, 25)
#     smtpObj.sendmail(sender, receivers, Mtext)
#     smtpObj.quit()


parser = argparse.ArgumentParser()
parser.add_argument("Number", help="Relays number 1 – 8", type=int, choices=[1, 2, 3, 4, 5, 6, 7, 8])
parser.add_argument("Function", help="on is relays on, off is relays off", choices=["on", "off"])
parser.add_argument("Device", help="Device id for e-mail message")

args = parser.parse_args()

if args.Number == 1:
    if args.Function == 'on':
        print('Relays 1 on'),
        SendCommandToRelays(b'\x21\x01\x00')  # Relays 1 permanent on
    elif args.Function == 'off':
        print('Relays 1 off'),
        SendCommandToRelays(b'\x20\x01\x00')  # Relays 1 permanent off

if args.Number == 2:
    if args.Function == 'on':
        print('Relays 2 on'),
        SendCommandToRelays(b'\x21\x02\x00')  # Relays 2 permanent on
    elif args.Function == 'off':
        print('Relays 2 off'),
        SendCommandToRelays(b'\x20\x02\x00')  # Relays 2 permanent off

if args.Number == 3:
    if args.Function == 'on':
        print('Relays 3 on'),
        SendCommandToRelays(b'\x21\x03\x00')  # Relays 3 permanent on
    elif args.Function == 'off':
        print('Relays 3 off'),
        SendCommandToRelays(b'\x20\x03\x00')  # Relays 3 permanent off

if args.Number == 4:
    if args.Function == 'on':
        print('Relays 4 on'),
        SendCommandToRelays(b'\x21\x04\x00')  # Relays 4 permanent on
    elif args.Function == 'off':
        print('Relays 4 off'),
        SendCommandToRelays(b'\x20\x04\x00')  # Relays 4 permanent off

if args.Number == 5:
    if args.Function == 'on':
        print('Relays 5 on'),
        SendCommandToRelays(b'\x21\x05\x00')  # Relays 5 permanent on
    elif args.Function == 'off':
        print('Relays 5 off'),
        SendCommandToRelays(b'\x20\x05\x00')  # Relays 5 permanent off

if args.Number == 6:
    if args.Function == 'on':
        print('Relays 6 on'),
        SendCommandToRelays(b'\x21\x06\x00')  # Relays 6 permanent on
    elif args.Function == 'off':
        print('Relays 6 off'),
        SendCommandToRelays(b'\x20\x06\x00')  # Relays 6 permanent off

if args.Number == 7:
    if args.Function == 'on':
        print('Relays 7 on'),
        SendCommandToRelays(b'\x21\x07\x00')  # Relays 7 permanent on
    elif args.Function == 'off':
        print('Relays 7 off'),
        SendCommandToRelays(b'\x20\x07\x00')  # Relays 7 permanent off

if args.Number == 8:
    if args.Function == 'on':
        print('Relays 8 on'),
        SendCommandToRelays(b'\x21\x08\x00')  # Relays 8 permanent on
    elif args.Function == 'off':
        print('Relays 8 off'),
        SendCommandToRelays(b'\x20\x08\x00')  # Relays 8 permanent off